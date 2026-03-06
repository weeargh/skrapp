"""MVP finalizer - clean page content and generate export artifacts."""
from __future__ import annotations

import hashlib
import json
import logging
import os
from datetime import datetime, timezone

from config import settings
from config.constants import ArtifactKind, JobState, PageState
from crawler.markdown_cleaner import clean_pages
from db import queries


logger = logging.getLogger(__name__)


def finalize_job(job_id: str) -> bool:
    """Finalize a crawl job from DB-backed pages."""
    job = queries.get_crawl_job(job_id)
    if not job:
        logger.error("Cannot finalize missing job %s", job_id)
        return False

    was_cancelled = job["status"] == JobState.CANCELLED
    queries.update_crawl_job(job_id, cleanup_status="running")
    if not was_cancelled and job["status"] != JobState.FINALIZING:
        queries.update_crawl_job_status(job_id, JobState.FINALIZING)

    pages = queries.list_pages_for_job(job_id, limit=100000, offset=0)
    successful_pages = [page for page in pages if page["status"] == PageState.DONE]
    cleaned_pages = clean_pages(successful_pages)

    for page in cleaned_pages:
        page_meta = dict(page.get("meta_json") or {})
        page_meta.update({
            "page_type": page.get("page_type"),
            "cleanup_confidence": page.get("cleanup_confidence"),
        })
        queries.update_page(
            page["id"],
            status=PageState.DONE,
            clean_markdown=page.get("clean_markdown") or "",
            plain_text=page.get("plain_text") or "",
            cleanup_score=page.get("cleanup_score"),
            cleanup_confidence=page.get("cleanup_confidence"),
            page_type=page.get("page_type"),
            removed_blocks_json=page.get("removed_blocks") or [],
            meta_json=page_meta,
        )

    job_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    llm_ready_path = _write_content_jsonl(job_id, job_dir, "llm-ready.jsonl", "clean_markdown", "markdown")
    raw_markdown_path = _write_content_jsonl(job_id, job_dir, "raw-markdown.jsonl", "raw_markdown", "markdown")
    plain_text_path = _write_content_jsonl(job_id, job_dir, "plain-text.jsonl", "plain_text", "text")
    tree_path = _write_tree_json(job_id, job_dir)

    _register_artifact(job_id, ArtifactKind.LLM_READY_JSONL, llm_ready_path)
    _register_artifact(job_id, ArtifactKind.RAW_MARKDOWN_JSONL, raw_markdown_path)
    _register_artifact(job_id, ArtifactKind.PLAIN_TEXT_JSONL, plain_text_path)
    _register_artifact(job_id, ArtifactKind.TREE_JSON, tree_path)

    queries.recalculate_job_counts(job_id)
    final_status = JobState.CANCELLED if was_cancelled else JobState.DONE
    queries.update_crawl_job_status(job_id, final_status, cleanup_status="done")
    queries.insert_job_event(job_id, "info", "finalized", {
        "llm_ready_jsonl": os.path.basename(llm_ready_path),
        "raw_markdown_jsonl": os.path.basename(raw_markdown_path),
        "plain_text_jsonl": os.path.basename(plain_text_path),
        "tree_json": os.path.basename(tree_path),
    })
    logger.info("Finalized job %s", job_id)
    return True


def _write_content_jsonl(
    job_id: str,
    job_dir: str,
    filename: str,
    content_field: str,
    content_format: str,
) -> str:
    """Write a job-wide JSONL export for one content format."""
    path = os.path.join(job_dir, filename)
    pages = queries.list_pages_for_job(job_id, limit=100000, offset=0)
    with open(path, "w", encoding="utf-8") as handle:
        for page in pages:
            record = {
                "job_id": job_id,
                "page_id": page["id"],
                "url": page["url"],
                "canonical_url": page["canonical_url"],
                "parent_page_id": page.get("parent_page_id"),
                "depth": page["depth"],
                "title": page.get("title"),
                "status": page["status"],
                "page_type": page.get("page_type"),
                "cleanup_confidence": page.get("cleanup_confidence"),
                "content_format": content_format,
                "content": page.get(content_field) or "",
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return path


def _write_tree_json(job_id: str, job_dir: str) -> str:
    """Write tree.json from the DB tree payload."""
    path = os.path.join(job_dir, "tree.json")
    tree = queries.get_job_tree(job_id)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(tree, handle, indent=2, ensure_ascii=False)
    return path


def _register_artifact(job_id: str, kind: str, path: str):
    """Create or replace an artifact record."""
    size_bytes = os.path.getsize(path)
    sha256 = _sha256_file(path)

    existing = queries.get_artifact_by_kind(job_id, kind)
    if existing:
        queries.update_job(job_id)  # Touch updated_at for visibility.
        from db import database
        database.execute_query(
            """
            UPDATE job_artifacts
            SET path = ?, byte_size = ?, sha256 = ?, created_at = ?
            WHERE id = ?
            """,
            (path, size_bytes, sha256, datetime.now(timezone.utc).isoformat(), existing["id"])
        )
        database.commit()
        return
    queries.create_artifact(job_id, kind, path, size_bytes, sha256=sha256)


def _sha256_file(path: str) -> str:
    """Hash a file on disk."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
