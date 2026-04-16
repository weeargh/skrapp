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

GENERIC_TITLE_PATTERNS = (
    re.compile(r"\bonline help center\b", re.IGNORECASE),
    re.compile(r"\blayanan bantuan\b", re.IGNORECASE),
    re.compile(r"\bhelp center\b", re.IGNORECASE),
    re.compile(r"\bpanduan pengguna\b", re.IGNORECASE),
    re.compile(r"\btemukan artikel panduan\b", re.IGNORECASE),
)

GENERIC_HEADING_PATTERNS = (
    *GENERIC_TITLE_PATTERNS,
    re.compile(r"\bpilih topik sesuai kebutuhan anda\b", re.IGNORECASE),
    re.compile(r"\btopik terpopuler\b", re.IGNORECASE),
    re.compile(r"\ball topics\b", re.IGNORECASE),
)


def build_page_json_record(page: Mapping[str, Any]) -> dict:
    """Build the canonical per-page JSON export record."""
    plain_text = page.get("plain_text") or page.get("raw_text") or ""
    removed_blocks = page.get("removed_blocks_json")
    if removed_blocks is None:
        removed_blocks = page.get("removed_blocks") or []
    export_title = _export_title(page)

    return {
        "job_id": page.get("job_id"),
        "page_id": _page_identifier(page),
        "title": export_title,
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
        "title": _export_title(page),
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


def ensure_artifact(job_id: str, kind: str, *, force_refresh: bool = False) -> str:
    """Return an artifact path, generating and registering it when needed."""
    artifact = queries.get_artifact_by_kind(job_id, kind)
    if artifact and os.path.exists(artifact["path"]) and not force_refresh:
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
    label = _slugify_fragment(_export_title(page) or page.get("canonical_url") or page.get("url") or page_id)
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


def _export_title(page: Mapping[str, Any]) -> str | None:
    """Return a user-meaningful title for exports."""
    stored_title = _normalize_title(page.get("title"))
    heading_title = _extract_heading_title(page)

    if heading_title and (
        not stored_title
        or _looks_generic_title(stored_title)
        or _title_token_overlap(stored_title, heading_title) == 0
    ):
        return heading_title

    if stored_title and not _looks_generic_title(stored_title):
        return stored_title

    return heading_title or stored_title or None


def _extract_heading_title(page: Mapping[str, Any]) -> str:
    """Find the first meaningful heading from cleaned or raw markdown."""
    markdown = f"{page.get('clean_markdown') or ''}\n{page.get('raw_markdown') or ''}"
    seen: set[str] = set()

    for line in markdown.splitlines()[:80]:
        stripped = line.strip()
        match = re.match(r"^#{1,3}\s+(.*)$", stripped)
        if not match:
            continue
        text = _normalize_title(_strip_markdown_formatting(match.group(1)))
        if not text or text in seen or _looks_generic_heading(text):
            continue
        seen.add(text)
        return text

    return ""


def _normalize_title(value: Any) -> str:
    """Normalize spacing and wrapper punctuation in titles."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text.strip(" -|")


def _strip_markdown_formatting(value: str) -> str:
    """Remove lightweight markdown syntax from a heading."""
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r"\1", value or "")
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r"\1", text)
    text = re.sub(r"[*_`>#]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _looks_generic_title(value: str) -> bool:
    """Check whether a title looks like site shell boilerplate."""
    return any(pattern.search(value or "") for pattern in GENERIC_TITLE_PATTERNS)


def _looks_generic_heading(value: str) -> bool:
    """Check whether a heading looks like navigation or shell content."""
    return any(pattern.search(value or "") for pattern in GENERIC_HEADING_PATTERNS)


def _title_token_overlap(left: str, right: str) -> int:
    """Compare title similarity while ignoring common shell words."""
    return len(_significant_tokens(left) & _significant_tokens(right))


def _significant_tokens(value: str) -> set[str]:
    """Tokenize a title while dropping generic help-center words."""
    ignored_tokens = {
        "help",
        "center",
        "online",
        "panduan",
        "pengguna",
        "mekari",
        "layanan",
        "bantuan",
        "artikel",
        "topik",
    }
    return {
        token
        for token in re.findall(r"[a-zA-Z0-9]{4,}", (value or "").lower())
        if token not in ignored_tokens
    }


def _sha256_file(path: str) -> str:
    """Hash a file on disk."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()
