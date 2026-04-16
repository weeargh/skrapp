"""MVP finalizer - clean page content and generate export artifacts."""
from __future__ import annotations

import logging
import os

from config import settings
from config.constants import ArtifactKind, JobState, PageState
from crawler.markdown_cleaner import clean_pages
from db import queries
from worker.job_artifacts import generate_artifact, upsert_artifact


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

    pages = queries.list_pages_for_job(job_id, limit=100000, offset=0)
    artifact_paths = {
        ArtifactKind.PAGE_JSON_ZIP: generate_artifact(job_id, ArtifactKind.PAGE_JSON_ZIP, job_dir=job_dir, pages=pages),
        ArtifactKind.LLM_READY_JSONL: generate_artifact(job_id, ArtifactKind.LLM_READY_JSONL, job_dir=job_dir, pages=pages),
        ArtifactKind.RAW_MARKDOWN_JSONL: generate_artifact(job_id, ArtifactKind.RAW_MARKDOWN_JSONL, job_dir=job_dir, pages=pages),
        ArtifactKind.PLAIN_TEXT_JSONL: generate_artifact(job_id, ArtifactKind.PLAIN_TEXT_JSONL, job_dir=job_dir, pages=pages),
        ArtifactKind.TREE_JSON: generate_artifact(job_id, ArtifactKind.TREE_JSON, job_dir=job_dir),
    }

    for kind, path in artifact_paths.items():
        upsert_artifact(job_id, kind, path)

    queries.recalculate_job_counts(job_id)
    final_status = JobState.CANCELLED if was_cancelled else JobState.DONE
    queries.update_crawl_job_status(job_id, final_status, cleanup_status="done")
    queries.insert_job_event(job_id, "info", "finalized", {
        "page_json_zip": os.path.basename(artifact_paths[ArtifactKind.PAGE_JSON_ZIP]),
        "llm_ready_jsonl": os.path.basename(artifact_paths[ArtifactKind.LLM_READY_JSONL]),
        "raw_markdown_jsonl": os.path.basename(artifact_paths[ArtifactKind.RAW_MARKDOWN_JSONL]),
        "plain_text_jsonl": os.path.basename(artifact_paths[ArtifactKind.PLAIN_TEXT_JSONL]),
        "tree_json": os.path.basename(artifact_paths[ArtifactKind.TREE_JSON]),
    })
    logger.info("Finalized job %s", job_id)
    return True
