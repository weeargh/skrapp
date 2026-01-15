"""Frontier (URL queue) query functions for persistent crawl state."""
from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import List, Optional

from db import database


def _now_iso() -> str:
    """Get current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).isoformat()


def _row_to_dict(row) -> dict | None:
    """Convert a sqlite3.Row to a dictionary."""
    if row is None:
        return None
    return dict(row)


# ============================================================================
# URL Queue (Frontier)
# ============================================================================

def enqueue_url(
    job_id: str,
    url: str,
    canonical_url: str,
    depth: int = 0,
    priority: int = 0,
) -> dict | None:
    """
    Add a URL to the queue if not already present.
    Returns the queue entry or None if duplicate.
    """
    now = _now_iso()
    
    # Check if already in queue
    existing = database.fetchone(
        "SELECT id FROM url_queue WHERE job_id = ? AND canonical_url = ?",
        (job_id, canonical_url)
    )
    if existing:
        return None
    
    database.execute_query(
        """
        INSERT INTO url_queue (
            job_id, url, canonical_url, state, depth, priority, discovered_at
        ) VALUES (?, ?, ?, 'queued', ?, ?, ?)
        """,
        (job_id, url, canonical_url, depth, priority, now)
    )
    database.commit()
    
    row = database.fetchone(
        "SELECT * FROM url_queue WHERE job_id = ? AND canonical_url = ?",
        (job_id, canonical_url)
    )
    return _row_to_dict(row)


def enqueue_urls_batch(
    job_id: str,
    urls: List[tuple],  # [(url, canonical_url, depth, priority), ...]
) -> int:
    """
    Batch enqueue URLs. Returns count of newly added URLs.
    """
    now = _now_iso()
    added = 0
    
    for url, canonical_url, depth, priority in urls:
        # Check if already exists
        existing = database.fetchone(
            "SELECT id FROM url_queue WHERE job_id = ? AND canonical_url = ?",
            (job_id, canonical_url)
        )
        if not existing:
            database.execute_query(
                """
                INSERT INTO url_queue (
                    job_id, url, canonical_url, state, depth, priority, discovered_at
                ) VALUES (?, ?, ?, 'queued', ?, ?, ?)
                """,
                (job_id, url, canonical_url, depth, priority, now)
            )
            added += 1
    
    database.commit()
    return added


def lease_urls(
    job_id: str,
    worker_id: str,
    batch_size: int = 10,
    lease_seconds: int = 300,
) -> List[dict]:
    """
    Lease a batch of URLs for processing.
    Uses visibility timeout pattern for crash safety.
    """
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    expires_at = (now + timedelta(seconds=lease_seconds)).isoformat()
    
    # First, release expired leases
    database.execute_query(
        """
        UPDATE url_queue 
        SET state = 'queued', leased_at = NULL, leased_by = NULL, lease_expires_at = NULL
        WHERE job_id = ? AND state = 'fetching' AND lease_expires_at < ?
        """,
        (job_id, now_iso)
    )
    
    # Get URLs to lease (priority order, then discovery order)
    rows = database.fetchall(
        """
        SELECT * FROM url_queue 
        WHERE job_id = ? AND state = 'queued'
        ORDER BY priority DESC, depth ASC, discovered_at ASC
        LIMIT ?
        """,
        (job_id, batch_size)
    )
    
    leased = []
    for row in rows:
        database.execute_query(
            """
            UPDATE url_queue 
            SET state = 'fetching', leased_at = ?, leased_by = ?, lease_expires_at = ?
            WHERE id = ?
            """,
            (now_iso, worker_id, expires_at, row['id'])
        )
        leased.append(_row_to_dict(row))
    
    database.commit()
    return leased


def complete_url(
    queue_id: int,
    status_code: int = None,
    error: str = None,
) -> dict | None:
    """Mark a URL as fetched (success or error)."""
    now = _now_iso()
    
    if error:
        # Increment retry count
        database.execute_query(
            """
            UPDATE url_queue 
            SET state = 'queued', 
                retry_count = retry_count + 1,
                last_error = ?,
                last_status_code = ?,
                leased_at = NULL, leased_by = NULL, lease_expires_at = NULL
            WHERE id = ?
            """,
            (error, status_code, queue_id)
        )
    else:
        database.execute_query(
            """
            UPDATE url_queue 
            SET state = 'fetched', 
                fetched_at = ?,
                last_status_code = ?,
                leased_at = NULL, leased_by = NULL, lease_expires_at = NULL
            WHERE id = ?
            """,
            (now, status_code, queue_id)
        )
    
    database.commit()
    
    row = database.fetchone("SELECT * FROM url_queue WHERE id = ?", (queue_id,))
    return _row_to_dict(row)


def mark_url_stored(queue_id: int) -> dict | None:
    """Mark a URL as fully processed and stored."""
    now = _now_iso()
    
    database.execute_query(
        "UPDATE url_queue SET state = 'stored', stored_at = ? WHERE id = ?",
        (now, queue_id)
    )
    database.commit()
    
    row = database.fetchone("SELECT * FROM url_queue WHERE id = ?", (queue_id,))
    return _row_to_dict(row)


def get_queue_stats(job_id: str) -> dict:
    """Get queue statistics for a job."""
    rows = database.fetchall(
        """
        SELECT state, COUNT(*) as count 
        FROM url_queue WHERE job_id = ? 
        GROUP BY state
        """,
        (job_id,)
    )
    
    stats = {row['state']: row['count'] for row in rows}
    stats['total'] = sum(stats.values())
    
    return stats


def is_url_seen(job_id: str, canonical_url: str) -> bool:
    """Check if a URL has already been queued."""
    row = database.fetchone(
        "SELECT id FROM url_queue WHERE job_id = ? AND canonical_url = ?",
        (job_id, canonical_url)
    )
    return row is not None


def get_expired_leases(job_id: str) -> List[dict]:
    """Get URLs with expired leases (stuck in fetching)."""
    now = _now_iso()
    
    rows = database.fetchall(
        """
        SELECT * FROM url_queue 
        WHERE job_id = ? AND state = 'fetching' AND lease_expires_at < ?
        """,
        (job_id, now)
    )
    
    return [_row_to_dict(row) for row in rows]


# ============================================================================
# Documents
# ============================================================================

def generate_doc_id() -> str:
    """Generate a unique document ID."""
    return f"doc_{uuid.uuid4().hex[:16]}"


def create_document(
    job_id: str,
    url: str,
    canonical_url: str,
    title: str = None,
    content_hash: str = None,
    language: str = None,
    doc_type: str = 'article',
    quality_score: float = None,
    quality_passed: bool = True,
) -> dict:
    """Create a new document record."""
    doc_id = generate_doc_id()
    now = _now_iso()
    
    # Generate title hash for matching
    title_hash = None
    if title:
        normalized_title = ' '.join(title.lower().split())
        title_hash = hashlib.sha256(normalized_title.encode()).hexdigest()[:16]
    
    database.execute_query(
        """
        INSERT INTO documents (
            id, job_id, content_hash, title_hash, primary_url, primary_canonical,
            title, language, doc_type, quality_score, quality_passed,
            first_seen_at, last_seen_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            doc_id, job_id, content_hash, title_hash, url, canonical_url,
            title, language, doc_type, quality_score, 1 if quality_passed else 0,
            now, now
        )
    )
    database.commit()
    
    # Add primary URL alias
    add_document_url(doc_id, job_id, url, canonical_url, 'canonical', language, is_primary=True)
    
    row = database.fetchone("SELECT * FROM documents WHERE id = ?", (doc_id,))
    return _row_to_dict(row)


def find_document_by_content(job_id: str, content_hash: str) -> dict | None:
    """Find a document by content hash (for deduplication)."""
    row = database.fetchone(
        "SELECT * FROM documents WHERE job_id = ? AND content_hash = ?",
        (job_id, content_hash)
    )
    return _row_to_dict(row)


def find_document_by_url(job_id: str, canonical_url: str) -> dict | None:
    """Find a document by canonical URL."""
    row = database.fetchone(
        """
        SELECT d.* FROM documents d
        JOIN document_urls du ON d.id = du.document_id
        WHERE du.job_id = ? AND du.canonical_url = ?
        """,
        (job_id, canonical_url)
    )
    return _row_to_dict(row)


def add_document_url(
    document_id: str,
    job_id: str,
    url: str,
    canonical_url: str,
    match_reason: str,
    language: str = None,
    is_primary: bool = False,
) -> dict:
    """Add a URL alias to a document."""
    now = _now_iso()
    
    database.execute_query(
        """
        INSERT INTO document_urls (
            document_id, job_id, url, canonical_url, match_reason,
            language, is_primary, discovered_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            document_id, job_id, url, canonical_url, match_reason,
            language, 1 if is_primary else 0, now
        )
    )
    database.commit()
    
    row = database.fetchone(
        "SELECT * FROM document_urls WHERE document_id = ? AND canonical_url = ?",
        (document_id, canonical_url)
    )
    return _row_to_dict(row)


def get_document_urls(document_id: str) -> List[dict]:
    """Get all URL aliases for a document."""
    rows = database.fetchall(
        "SELECT * FROM document_urls WHERE document_id = ?",
        (document_id,)
    )
    return [_row_to_dict(row) for row in rows]


# ============================================================================
# Structured Logs
# ============================================================================

def log_crawl_event(
    job_id: str,
    url: str,
    canonical_url: str = None,
    status_code: int = None,
    latency_ms: int = None,
    content_type: str = None,
    content_length: int = None,
    stage: str = None,
    extraction_mode: str = None,
    quality_score: float = None,
    error_type: str = None,
    error_message: str = None,
    depth: int = None,
    retry_count: int = None,
):
    """Log a crawl event to the database."""
    now = _now_iso()
    
    database.execute_query(
        """
        INSERT INTO crawl_logs (
            job_id, url, canonical_url, timestamp, latency_ms,
            status_code, content_type, content_length,
            stage, extraction_mode, quality_score,
            error_type, error_message, depth, retry_count
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            job_id, url, canonical_url, now, latency_ms,
            status_code, content_type, content_length,
            stage, extraction_mode, quality_score,
            error_type, error_message, depth, retry_count
        )
    )
    database.commit()


def get_crawl_logs(
    job_id: str,
    limit: int = 100,
    error_only: bool = False,
) -> List[dict]:
    """Get crawl logs for a job."""
    if error_only:
        rows = database.fetchall(
            """
            SELECT * FROM crawl_logs 
            WHERE job_id = ? AND error_type IS NOT NULL
            ORDER BY timestamp DESC LIMIT ?
            """,
            (job_id, limit)
        )
    else:
        rows = database.fetchall(
            """
            SELECT * FROM crawl_logs 
            WHERE job_id = ? 
            ORDER BY timestamp DESC LIMIT ?
            """,
            (job_id, limit)
        )
    
    return [_row_to_dict(row) for row in rows]


def get_error_summary(job_id: str) -> dict:
    """Get error summary for a job."""
    rows = database.fetchall(
        """
        SELECT error_type, COUNT(*) as count 
        FROM crawl_logs 
        WHERE job_id = ? AND error_type IS NOT NULL
        GROUP BY error_type
        ORDER BY count DESC
        """,
        (job_id,)
    )
    
    return {row['error_type']: row['count'] for row in rows}
