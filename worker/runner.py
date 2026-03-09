"""Page-centric job runner helpers for discovery and extraction."""
from __future__ import annotations

import logging
import os
from urllib.parse import urlparse, urlunparse

from config import settings
from config.constants import JobState, PageState
from crawler.crawl4ai_session import Crawl4AIPageSession
from crawler.openapi_extractor import convert_spec_to_markdown, detect_openapi_spec_url, fetch_openapi_spec
from crawler.sitemap import discover_sitemap_urls
from crawler.text_utils import markdown_to_text
from crawler.url_utils import canonicalize_url, get_path
from db import queries
from worker.finalizer import finalize_job


logger = logging.getLogger(__name__)


def start_job(job_id: str) -> dict | None:
    """Prepare a running job so pages are ready to be claimed."""
    job = queries.get_crawl_job(job_id)
    if not job:
        logger.error("Job %s not found", job_id)
        return None

    os.makedirs(os.path.join(settings.JOBS_OUTPUT_DIR, job_id), exist_ok=True)
    job = _prepare_job(job)
    if job["status"] != JobState.RUNNING:
        job = queries.update_crawl_job_status(
            job_id,
            JobState.RUNNING,
            cleanup_status="pending",
            error_message=None,
        )
    queries.touch_job_heartbeat(job_id)
    return job


def start_next_queued_job() -> dict | None:
    """Atomically activate the next queued job."""
    job = queries.claim_next_queued_crawl_job()
    if not job:
        return None
    try:
        return start_job(job["id"])
    except Exception as e:
        logger.error("Failed to prepare job %s: %s", job["id"], e, exc_info=True)
        queries.update_crawl_job_status(
            job["id"],
            JobState.FAILED,
            cleanup_status="failed",
            error_message=f"{type(e).__name__}: {e}",
        )
        return None


def process_page(job: dict, page: dict, worker_id: str, crawler_session: Crawl4AIPageSession):
    """Process one leased page."""
    queries.touch_job_heartbeat(job["id"])
    queries.renew_page_lease(page["id"], worker_id, settings.PAGE_LEASE_SECONDS)
    _process_page(job, page, worker_id, crawler_session)
    queries.touch_job_heartbeat(job["id"])


def finalize_ready_job() -> bool:
    """Claim and finalize one job that has no remaining work."""
    job = queries.claim_job_ready_for_finalization()
    if not job:
        return False

    try:
        return finalize_job(job["id"])
    except Exception as e:
        logger.error("Failed to finalize job %s: %s", job["id"], e, exc_info=True)
        queries.update_crawl_job(
            job["id"],
            cleanup_status="failed",
            error_message=f"{type(e).__name__}: {e}",
        )
        if job["status"] == JobState.FINALIZING:
            queries.update_crawl_job_status(job["id"], JobState.FAILED, cleanup_status="failed")
        return False


def _prepare_job(job: dict) -> dict:
    """Ensure the job has a root page and resolved path prefix."""
    allowed_path_prefix = job.get("allowed_path_prefix") or _derive_allowed_path_prefix(job["start_url"])
    if allowed_path_prefix != job.get("allowed_path_prefix"):
        job = queries.update_crawl_job(job["id"], allowed_path_prefix=allowed_path_prefix)

    if queries.count_pages_for_job(job["id"]) == 0:
        root_url = canonicalize_url(job["start_url"])
        root_page = queries.create_page(
            job_id=job["id"],
            url=job["start_url"],
            canonical_url=root_url,
            parent_page_id=None,
            depth=0,
            discovery_order=0,
            status=PageState.QUEUED,
            title=None,
            meta_json={"root": True},
        )
        queries.insert_job_event(job["id"], "info", "root_page_created", {
            "url": job["start_url"],
            "allowed_path_prefix": allowed_path_prefix,
        })
        if root_page:
            _seed_pages_from_sitemap(job, root_page)

    return queries.get_crawl_job(job["id"])


def _process_page(job: dict, page: dict, worker_id: str, crawler_session: Crawl4AIPageSession):
    """Discover links and extract content for one page."""
    page_id = page["id"]
    job_id = job["id"]
    queries.insert_job_event(job_id, "info", "page_discovering", {
        "page_id": page_id,
        "url": page["url"],
        "depth": page["depth"],
        "worker_id": worker_id,
    })

    try:
        extracted = crawler_session.fetch_page(page["url"])
        if extracted.status_code == 404 and not _is_soft_404_success(page["url"], extracted):
            queries.insert_job_event(job_id, "warn", "page_404_retrying", {
                "page_id": page_id,
                "url": page["url"],
                "final_url": extracted.final_url,
                "title": extracted.title,
            })
            retry_extracted = crawler_session.fetch_page(page["url"])
            if _is_soft_404_success(page["url"], retry_extracted):
                extracted = retry_extracted
        if extracted.status_code and extracted.status_code >= 400 and not _is_soft_404_success(page["url"], extracted):
            raise RuntimeError(f"Page returned HTTP {extracted.status_code}")
        if extracted.status_code == 404:
            queries.insert_job_event(job_id, "warn", "page_soft_404_accepted", {
                "page_id": page_id,
                "url": page["url"],
                "final_url": extracted.final_url,
                "title": extracted.title,
            })

        # OpenAPI / Swagger detection: replace markdown with spec-derived content
        extractor_name = "crawl4ai"
        raw_markdown = extracted.raw_markdown
        raw_text = extracted.raw_text
        spec_url = detect_openapi_spec_url(extracted.html, extracted.final_url)
        if spec_url:
            queries.insert_job_event(job_id, "info", "openapi_spec_detected", {
                "page_id": page_id,
                "page_url": extracted.final_url,
                "spec_url": spec_url,
            })
            spec = fetch_openapi_spec(spec_url, page_url=extracted.final_url)
            if spec:
                raw_markdown = convert_spec_to_markdown(spec)
                raw_text = markdown_to_text(raw_markdown)
                extractor_name = "openapi"

        queries.update_page(
            page_id,
            url=extracted.final_url,
            canonical_url=extracted.canonical_url,
            title=extracted.title,
            raw_html=extracted.html,
            meta_json={
                "status_code": extracted.status_code,
                "outlinks_count": len(extracted.outlinks),
                "extractor": extractor_name,
                "extractor_meta": extracted.meta,
                "worker_id": worker_id,
            },
        )

        _enqueue_child_pages(job, page_id, page["depth"], extracted.outlinks)

        queries.update_page_status(page_id, PageState.EXTRACTING, claimed_by=worker_id)
        queries.renew_page_lease(page_id, worker_id, settings.PAGE_LEASE_SECONDS)
        queries.update_page_status(
            page_id,
            PageState.DONE,
            title=extracted.title or page.get("title"),
            raw_markdown=raw_markdown,
            raw_text=raw_text,
            meta_json={
                "status_code": extracted.status_code,
                "outlinks_count": len(extracted.outlinks),
                "extractor": extractor_name,
                "extractor_meta": extracted.meta,
                "cleaned_html_length": len(extracted.cleaned_html or ""),
                "worker_id": worker_id,
                **({"spec_url": spec_url} if spec_url else {}),
            },
            claimed_by=None,
            claimed_at=None,
            lease_expires_at=None,
        )
        queries.insert_job_event(job_id, "info", "page_done", {
            "page_id": page_id,
            "url": extracted.final_url,
            "depth": page["depth"],
            "outlinks_count": len(extracted.outlinks),
            "worker_id": worker_id,
        })
    except Exception as e:
        queries.update_page_status(
            page_id,
            PageState.FAILED,
            error_message=str(e),
            claimed_by=None,
            claimed_at=None,
            lease_expires_at=None,
        )
        queries.insert_job_event(job_id, "error", "page_failed", {
            "page_id": page_id,
            "url": page["url"],
            "depth": page["depth"],
            "message": str(e),
            "worker_id": worker_id,
        })


def _is_soft_404_success(requested_url: str, extracted: Crawl4AIPageResult) -> bool:
    """Allow rendered deep-link docs pages that incorrectly return HTTP 404."""
    if extracted.status_code != 404:
        return False

    requested_path = get_path(requested_url)
    final_path = get_path(extracted.final_url)
    if requested_path in ("", "/") or requested_path != final_path:
        return False

    title = (extracted.title or "").strip()
    raw_text = (extracted.raw_text or "").strip()
    raw_markdown = (extracted.raw_markdown or "").strip()
    if not title or len(raw_text) < settings.MIN_TEXT_LENGTH_SUCCESS or not raw_markdown:
        return False

    first_heading = ""
    for line in raw_markdown.splitlines():
        line = line.strip()
        if line.startswith("#"):
            first_heading = line.lstrip("#").strip()
            break

    error_markers = (
        "404",
        "not found",
        "page not found",
        "cannot be found",
    )
    preview = "\n".join(part for part in (title, first_heading, raw_text[:500]) if part).lower()
    if any(marker in preview for marker in error_markers):
        return False

    # Reject the common docs fallback where every missing route renders the overview page.
    if requested_path != "/" and title.lower().startswith("overview"):
        return False
    if requested_path != "/" and first_heading.lower() == "overview":
        return False

    return True


def _enqueue_child_pages(job: dict, parent_page_id: str, parent_depth: int, outlinks: list[str]):
    """Insert accepted child pages in BFS order."""
    if parent_depth >= job["max_depth"]:
        for link in outlinks:
            queries.record_page_link(job["id"], parent_page_id, link, canonicalize_url(link), False, "depth_limit")
        return

    existing_pages = queries.list_pages_for_job(job["id"], limit=100000, offset=0)
    page_by_canonical = {
        page["canonical_url"]: page
        for page in existing_pages
        if page.get("canonical_url")
    }
    root_page = next((page for page in existing_pages if page.get("depth") == 0), None)

    for link in outlinks:
        canonical = canonicalize_url(link)
        existing = queries.get_page_by_canonical_url(job["id"], canonical)
        if existing:
            queries.record_page_link(job["id"], parent_page_id, link, canonical, False, "duplicate")
            continue

        resolved_parent_page_id, resolved_depth = _resolve_page_position(
            link,
            page_by_canonical,
            root_page,
            job.get("allowed_path_prefix"),
        )
        if resolved_depth > job["max_depth"]:
            queries.record_page_link(job["id"], parent_page_id, link, canonical, False, "depth_limit")
            continue

        child = queries.create_page(
            job_id=job["id"],
            url=link,
            canonical_url=canonical,
            parent_page_id=resolved_parent_page_id,
            depth=resolved_depth,
            discovery_order=None,
            status=PageState.QUEUED,
            title=None,
            max_pages=job["max_pages"],
        )
        if child:
            page_by_canonical[child["canonical_url"]] = child
            queries.record_page_link(job["id"], parent_page_id, link, canonical, True, None)
            continue

        existing = queries.get_page_by_canonical_url(job["id"], canonical)
        reject_reason = "duplicate" if existing else "max_pages"
        queries.record_page_link(job["id"], parent_page_id, link, canonical, False, reject_reason)


def _derive_allowed_path_prefix(start_url: str) -> str | None:
    """Default the crawl scope to the root page's path subtree."""
    path = get_path(start_url)
    if not path or path == "/":
        return None
    if path.endswith((".html", ".htm", ".php", ".jsp", ".asp")):
        return path.rsplit("/", 1)[0] or "/"
    return path.rstrip("/") or "/"


def _seed_pages_from_sitemap(job: dict, root_page: dict):
    """Pre-seed pages from the sitemap so hierarchy does not depend on random first discovery."""
    sitemap_urls = discover_sitemap_urls(
        job["start_url"],
        job["allowed_host"],
        job.get("allowed_path_prefix"),
        job.get("ignore_path_prefixes"),
    )
    if not sitemap_urls:
        queries.insert_job_event(job["id"], "info", "sitemap_not_found", {
            "start_url": job["start_url"],
        })
        return

    page_by_canonical = {root_page["canonical_url"]: root_page}
    discovery_order = queries.count_pages_for_job(job["id"])
    ordered_urls = sorted(
        {canonicalize_url(url): url for url in sitemap_urls}.values(),
        key=lambda value: (_path_segment_count(value), canonicalize_url(value)),
    )

    created_count = 0
    for url in ordered_urls:
        if queries.count_pages_for_job(job["id"]) >= job["max_pages"]:
            break
        canonical = canonicalize_url(url)
        if canonical == root_page["canonical_url"]:
            continue
        if canonical in page_by_canonical:
            continue

        parent_page_id, depth = _resolve_page_position(
            url,
            page_by_canonical,
            root_page,
            job.get("allowed_path_prefix"),
        )
        if depth > job["max_depth"]:
            continue
        page = queries.create_page(
            job_id=job["id"],
            url=url,
            canonical_url=canonical,
            parent_page_id=parent_page_id,
            depth=depth,
            discovery_order=discovery_order + 1,
            status=PageState.QUEUED,
            title=None,
            meta_json={"seeded_from_sitemap": True},
            max_pages=job["max_pages"],
        )
        discovery_order += 1
        if page:
            page_by_canonical[canonical] = page
            created_count += 1

    queries.insert_job_event(job["id"], "info", "sitemap_seeded", {
        "pages_seeded": created_count,
    })


def _resolve_page_position(
    url: str,
    page_by_canonical: dict[str, dict],
    root_page: dict | None,
    allowed_path_prefix: str | None,
) -> tuple[str | None, int]:
    """Place a page in the hierarchy using URL path ancestry instead of discoverer order."""
    if not root_page:
        return None, 0

    canonical = canonicalize_url(url)
    if canonical == root_page["canonical_url"]:
        return None, 0

    parsed = urlparse(canonical)
    path = parsed.path or "/"
    base_path = _normalized_path(allowed_path_prefix or get_path(root_page["canonical_url"]))
    segments = [segment for segment in path.strip("/").split("/") if segment]
    base_segments = [segment for segment in base_path.strip("/").split("/") if segment]

    for cut in range(len(segments) - 1, len(base_segments) - 1, -1):
        candidate_path = "/" + "/".join(segments[:cut]) if cut else "/"
        candidate_url = urlunparse((parsed.scheme, parsed.netloc, candidate_path, "", "", ""))
        candidate_canonical = canonicalize_url(candidate_url)
        candidate = page_by_canonical.get(candidate_canonical)
        if not candidate:
            candidate = queries.get_page_by_canonical_url(root_page["job_id"], candidate_canonical)
            if candidate:
                page_by_canonical[candidate_canonical] = candidate
        if candidate:
            return candidate["id"], candidate["depth"] + 1

    return root_page["id"], 1


def _path_segment_count(url: str) -> int:
    """Count path segments for stable sitemap seeding order."""
    path = get_path(url)
    return len([segment for segment in path.strip("/").split("/") if segment])


def _normalized_path(path: str | None) -> str:
    """Normalize a path for prefix comparisons."""
    if not path or path == "/":
        return "/"
    return path.rstrip("/")
