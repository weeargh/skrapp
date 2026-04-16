"""Helpers for building downloadable job artifacts."""
from __future__ import annotations

import hashlib
import json
import os
import re
import zipfile
from datetime import datetime, timezone
from typing import Any, Mapping

from config import settings
from config.constants import ArtifactKind
from db import database, queries


def build_page_json_record(page: Mapping[str, Any]) -> dict:
    """Build the canonical per-page JSON export record."""
    plain_text = page.get("plain_text") or page.get("raw_text") or ""
    removed_blocks = page.get("removed_blocks_json")
    if removed_blocks is None:
        removed_blocks = page.get("removed_blocks") or []

    return {
        "job_id": page.get("job_id"),
        "page_id": _page_identifier(page),
        "title": page.get("title"),
        "status": page.get("status"),
        "page_type": page.get("page_type"),
        "url": page.get("url"),
        "canonical_url": page.get("canonical_url"),
        "parent_page_id": page.get("parent_page_id"),
        "depth": page.get("depth"),
        "text_length": len(plain_text),
        "cleanup_score": page.get("cleanup_score"),
        "cleanup_confidence": page.get("cleanup_confidence"),
        "main_content_selector": page.get("main_content_selector"),
        "error_message": page.get("error_message"),
        "removed_blocks": removed_blocks,
        "content": {
            "clean_markdown": page.get("clean_markdown") or "",
            "raw_markdown": page.get("raw_markdown") or "",
            "plain_text": plain_text,
        },
    }


def build_content_jsonl_record(
    job_id: str,
    page: Mapping[str, Any],
    content_field: str,
    content_format: str,
) -> dict:
    """Build a JSONL record for one content projection."""
    return {
        "job_id": job_id,
        "page_id": _page_identifier(page),
        "url": page.get("url"),
        "canonical_url": page.get("canonical_url"),
        "parent_page_id": page.get("parent_page_id"),
        "depth": page.get("depth"),
        "title": page.get("title"),
        "status": page.get("status"),
        "page_type": page.get("page_type"),
        "cleanup_confidence": page.get("cleanup_confidence"),
        "content_format": content_format,
        "content": page.get(content_field) or "",
    }


def generate_artifact(
    job_id: str,
    kind: str,
    *,
    job_dir: str | None = None,
    pages: list[dict] | None = None,
) -> str:
    """Generate a single downloadable artifact on disk."""
    job_dir = job_dir or os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)

    if kind == ArtifactKind.PAGE_JSON_ZIP:
        return _write_page_json_zip(job_id, job_dir, pages=pages)
    if kind == ArtifactKind.LLM_READY_JSONL:
        return _write_content_jsonl(
            job_id,
            job_dir,
            "llm-ready.jsonl",
            "clean_markdown",
            "markdown",
            pages=pages,
        )
    if kind == ArtifactKind.RAW_MARKDOWN_JSONL:
        return _write_content_jsonl(
            job_id,
            job_dir,
            "raw-markdown.jsonl",
            "raw_markdown",
            "markdown",
            pages=pages,
        )
    if kind == ArtifactKind.PLAIN_TEXT_JSONL:
        return _write_content_jsonl(
            job_id,
            job_dir,
            "plain-text.jsonl",
            "plain_text",
            "text",
            pages=pages,
        )
    if kind == ArtifactKind.TREE_JSON:
        return _write_tree_json(job_id, job_dir)
    raise ValueError(f"Unsupported artifact kind: {kind}")


def ensure_artifact(job_id: str, kind: str) -> str:
    """Return an artifact path, generating and registering it when needed."""
    artifact = queries.get_artifact_by_kind(job_id, kind)
    if artifact and os.path.exists(artifact["path"]):
        return artifact["path"]

    path = generate_artifact(job_id, kind)
    upsert_artifact(job_id, kind, path)
    return path


def upsert_artifact(job_id: str, kind: str, path: str) -> None:
    """Create or replace an artifact record."""
    size_bytes = os.path.getsize(path)
    sha256 = _sha256_file(path)

    existing = queries.get_artifact_by_kind(job_id, kind)
    if existing:
        queries.update_job(job_id)
        database.execute_query(
            """
            UPDATE job_artifacts
            SET path = ?, byte_size = ?, sha256 = ?, created_at = ?
            WHERE id = ?
            """,
            (path, size_bytes, sha256, datetime.now(timezone.utc).isoformat(), existing["id"]),
        )
        database.commit()
        return

    queries.create_artifact(job_id, kind, path, size_bytes, sha256=sha256)


def _write_content_jsonl(
    job_id: str,
    job_dir: str,
    filename: str,
    content_field: str,
    content_format: str,
    *,
    pages: list[dict] | None = None,
) -> str:
    """Write a job-wide JSONL export for one content format."""
    path = os.path.join(job_dir, filename)
    pages = pages if pages is not None else _list_job_pages(job_id)
    with open(path, "w", encoding="utf-8") as handle:
        for page in pages:
            record = build_content_jsonl_record(job_id, page, content_field, content_format)
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return path


def _write_page_json_zip(
    job_id: str,
    job_dir: str,
    *,
    pages: list[dict] | None = None,
) -> str:
    """Write a zip archive with one JSON file per page."""
    path = os.path.join(job_dir, "pages-json.zip")
    pages = pages if pages is not None else _list_job_pages(job_id)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for index, page in enumerate(pages, start=1):
            archive.writestr(
                _page_json_filename(page, index),
                json.dumps(build_page_json_record(page), indent=2, ensure_ascii=False),
            )
    return path


def _write_tree_json(job_id: str, job_dir: str) -> str:
    """Write tree.json from the DB tree payload."""
    path = os.path.join(job_dir, "tree.json")
    tree = queries.get_job_tree(job_id)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(tree, handle, indent=2, ensure_ascii=False)
    return path


def _list_job_pages(job_id: str) -> list[dict]:
    """Load all pages for a job in export order."""
    return queries.list_pages_for_job(job_id, limit=100000, offset=0)


def _page_json_filename(page: Mapping[str, Any], index: int) -> str:
    """Build a stable per-page filename inside the zip."""
    page_id = _page_identifier(page)
    label = _slugify_fragment(page.get("title") or page.get("canonical_url") or page.get("url") or page_id)
    label = label[:72] if label else page_id
    return f"{index:04d}-{label}-{page_id}.json"


def _page_identifier(page: Mapping[str, Any]) -> str:
    """Return the best available page identifier across DB and API shapes."""
    return str(page.get("page_id") or page.get("id") or "page")


def _slugify_fragment(value: Any) -> str:
    """Normalize a label for use in filenames."""
    text = re.sub(r"https?://", "", str(value or ""))
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "page"


def _sha256_file(path: str) -> str:
    """Hash a file on disk."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
