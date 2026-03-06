"""Database query functions for jobs and related tables."""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, List

from config.constants import JobState, PageState, EventLevel, EventType
from db import database


def _now_iso() -> str:
    """Get current UTC timestamp in ISO format."""
    return datetime.now(timezone.utc).isoformat()


def _row_to_dict(row) -> dict | None:
    """Convert a sqlite3.Row to a dictionary."""
    if row is None:
        return None
    return dict(row)


def _parse_json_field(value: Any, default):
    """Parse a JSON string field if present."""
    if value is None:
        return default
    if isinstance(value, (list, dict)):
        return value
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return default


def _normalize_job_row(job: dict | None) -> dict | None:
    """Map the database job row to the MVP-facing shape."""
    if not job:
        return None
    normalized = dict(job)
    normalized['status'] = job.get('state')
    normalized['ignore_path_prefixes'] = _parse_json_field(
        job.get('ignore_path_prefixes'),
        []
    )
    return normalized


def _normalize_page_row(page: dict | None) -> dict | None:
    """Parse JSON-ish page fields into Python objects."""
    if not page:
        return None
    normalized = dict(page)
    normalized['removed_blocks_json'] = _parse_json_field(
        page.get('removed_blocks_json'),
        []
    )
    normalized['meta_json'] = _parse_json_field(
        page.get('meta_json'),
        {}
    )
    return normalized


def generate_page_id() -> str:
    """Generate a unique page ID."""
    return f"page_{uuid.uuid4().hex[:16]}"


# ============================================================================
# Jobs
# ============================================================================

def create_job(
    job_id: str,
    token_hash: str,
    start_url: str,
    allowed_host: str,
    max_pages: int,
    timeout_seconds: int,
    ignore_path_prefixes: list[str],
    requester_ip_hash: str,
    expiry_hours: int = 24,
    use_js: bool = False
) -> dict:
    """Create a new job record."""
    now = _now_iso()
    expires_at = (datetime.now(timezone.utc) + timedelta(hours=expiry_hours)).isoformat()
    
    database.execute_query(
        """
        INSERT INTO jobs (
            id, token_hash, start_url, allowed_host, max_pages, timeout_seconds,
            ignore_path_prefixes, state, created_at, updated_at,
            requester_ip_hash, expires_at, use_js
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            job_id, token_hash, start_url, allowed_host, max_pages, timeout_seconds,
            json.dumps(ignore_path_prefixes), JobState.QUEUED, now, now,
            requester_ip_hash, expires_at, 1 if use_js else 0
        )
    )
    database.commit()
    
    insert_job_event(job_id, EventLevel.INFO, EventType.STATE_CHANGE, {
        "from": None, "to": JobState.QUEUED
    })
    
    return get_job_by_id(job_id)


def get_job_by_id(job_id: str) -> dict | None:
    """Get a job by its ID."""
    row = database.fetchone("SELECT * FROM jobs WHERE id = ?", (job_id,))
    return _row_to_dict(row)


def get_job_for_auth(job_id: str, token_hash: str) -> dict | None:
    """Get a job by ID and token hash for authentication."""
    row = database.fetchone(
        "SELECT * FROM jobs WHERE id = ? AND token_hash = ?",
        (job_id, token_hash)
    )
    return _row_to_dict(row)


def update_job(job_id: str, **kwargs) -> dict | None:
    """Update job fields."""
    if not kwargs:
        return get_job_by_id(job_id)
    
    kwargs['updated_at'] = _now_iso()
    
    set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
    values = list(kwargs.values()) + [job_id]
    
    database.execute_query(
        f"UPDATE jobs SET {set_clause} WHERE id = ?",
        tuple(values)
    )
    database.commit()
    
    return get_job_by_id(job_id)


def update_job_state(job_id: str, new_state: str, **kwargs) -> dict | None:
    """Update job state and log the transition."""
    job = get_job_by_id(job_id)
    if not job:
        return None
    
    old_state = job['state']
    kwargs['state'] = new_state
    
    if new_state == JobState.RUNNING and not job.get('started_at'):
        kwargs['started_at'] = _now_iso()
    
    if new_state in JobState.TERMINAL and not job.get('finished_at'):
        kwargs['finished_at'] = _now_iso()
    
    result = update_job(job_id, **kwargs)
    
    insert_job_event(job_id, EventLevel.INFO, EventType.STATE_CHANGE, {
        "from": old_state, "to": new_state
    })
    
    return result


def touch_job_heartbeat(job_id: str) -> dict | None:
    """Update only the worker heartbeat timestamp for a job."""
    return update_job(job_id, runner_heartbeat_at=_now_iso())


def get_next_queued_job() -> dict | None:
    """Get the oldest queued job for processing."""
    row = database.fetchone(
        """
        SELECT * FROM jobs 
        WHERE state = ? 
        ORDER BY created_at ASC 
        LIMIT 1
        """,
        (JobState.QUEUED,)
    )
    return _row_to_dict(row)


def get_running_jobs() -> list[dict]:
    """Get all running jobs."""
    rows = database.fetchall(
        "SELECT * FROM jobs WHERE state = ?",
        (JobState.RUNNING,)
    )
    return [_row_to_dict(row) for row in rows]


def get_jobs_by_state(state: str) -> list[dict]:
    """Get all jobs in a specific state."""
    rows = database.fetchall(
        "SELECT * FROM jobs WHERE state = ?",
        (state,)
    )
    return [_row_to_dict(row) for row in rows]


def update_heartbeat(job_id: str, pages_fetched: int | None = None):
    """Update the runner heartbeat timestamp."""
    kwargs = {
        'runner_heartbeat_at': _now_iso(),
    }
    if pages_fetched is not None:
        kwargs['pages_fetched'] = pages_fetched
        kwargs['last_progress_at'] = _now_iso()
    
    update_job(job_id, **kwargs)


def increment_restart_count(job_id: str) -> int:
    """Increment and return the restart count for a job."""
    job = get_job_by_id(job_id)
    if not job:
        return 0
    
    new_count = job['restart_count'] + 1
    update_job(job_id, restart_count=new_count)
    
    insert_job_event(job_id, EventLevel.WARN, EventType.RESTART, {
        "restart_count": new_count
    })
    
    return new_count


def find_orphaned_jobs(threshold_seconds: int) -> list[dict]:
    """Find jobs that appear to be orphaned (worker died)."""
    threshold_time = (
        datetime.now(timezone.utc) - timedelta(seconds=threshold_seconds)
    ).isoformat()
    
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE state IN (?, ?, ?)
        AND runner_heartbeat_at IS NOT NULL
        AND runner_heartbeat_at < ?
        """,
        (JobState.STARTING, JobState.RUNNING, JobState.FINALIZING, threshold_time)
    )
    return [_row_to_dict(row) for row in rows]


def find_stalled_jobs(threshold_seconds: int) -> list[dict]:
    """Find jobs that haven't made progress."""
    threshold_time = (
        datetime.now(timezone.utc) - timedelta(seconds=threshold_seconds)
    ).isoformat()
    
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE state = ?
        AND last_progress_at IS NOT NULL
        AND last_progress_at < ?
        AND pages_fetched > 0
        """,
        (JobState.RUNNING, threshold_time)
    )
    return [_row_to_dict(row) for row in rows]


def find_hard_stalled_jobs(threshold_seconds: int) -> list[dict]:
    """Find jobs that never fetched any pages."""
    threshold_time = (
        datetime.now(timezone.utc) - timedelta(seconds=threshold_seconds)
    ).isoformat()
    
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE state = ?
        AND started_at IS NOT NULL
        AND started_at < ?
        AND pages_fetched = 0
        """,
        (JobState.RUNNING, threshold_time)
    )
    return [_row_to_dict(row) for row in rows]


def find_expired_jobs() -> list[dict]:
    """Find jobs that have passed their expiry time."""
    now = _now_iso()
    
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE state NOT IN (?, ?)
        AND expires_at < ?
        """,
        (JobState.EXPIRED, JobState.QUEUED, now)
    )
    return [_row_to_dict(row) for row in rows]


# ============================================================================
# MVP Job + Page Model
# ============================================================================

def create_crawl_job(
    job_id: str,
    start_url: str,
    allowed_host: str,
    allowed_path_prefix: str | None,
    max_depth: int,
    max_pages: int,
    ignore_path_prefixes: list[str] | None = None,
    timeout_seconds: int = 1800,
) -> dict:
    """Create an MVP crawl job without auth concerns."""
    now = _now_iso()
    expires_at = (datetime.now(timezone.utc) + timedelta(days=30)).isoformat()
    ignore_prefixes = ignore_path_prefixes or []

    database.execute_query(
        """
        INSERT INTO jobs (
            id, token_hash, start_url, allowed_host, allowed_path_prefix,
            max_pages, max_depth, timeout_seconds, ignore_path_prefixes,
            state, cleanup_status, created_at, updated_at,
            requester_ip_hash, expires_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            job_id,
            '',
            start_url,
            allowed_host,
            allowed_path_prefix,
            max_pages,
            max_depth,
            timeout_seconds,
            json.dumps(ignore_prefixes),
            JobState.QUEUED,
            'pending',
            now,
            now,
            '',
            expires_at,
        )
    )
    database.commit()

    insert_job_event(job_id, EventLevel.INFO, 'job_created', {
        'start_url': start_url,
        'allowed_path_prefix': allowed_path_prefix,
        'max_depth': max_depth,
        'max_pages': max_pages,
    })
    return get_crawl_job(job_id)


def get_crawl_job(job_id: str) -> dict | None:
    """Get a crawl job in MVP-facing shape."""
    return _normalize_job_row(get_job_by_id(job_id))


def list_crawl_jobs(
    status: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[dict]:
    """List crawl jobs ordered by newest first."""
    params: list[Any] = []
    query = "SELECT * FROM jobs"
    if status:
        query += " WHERE state = ?"
        params.append(status)
    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    rows = database.fetchall(query, tuple(params))
    return [_normalize_job_row(_row_to_dict(row)) for row in rows]


def get_next_queued_crawl_job() -> dict | None:
    """Get the next queued crawl job in MVP-facing shape."""
    return _normalize_job_row(get_next_queued_job())


def claim_next_queued_crawl_job() -> dict | None:
    """Atomically claim the oldest queued crawl job for preparation."""
    conn = database.get_connection()
    now = _now_iso()
    conn.execute("BEGIN IMMEDIATE")
    try:
        row = conn.execute(
            """
            SELECT id FROM jobs
            WHERE state = ?
            ORDER BY created_at ASC
            LIMIT 1
            """,
            (JobState.QUEUED,),
        ).fetchone()
        if row is None:
            conn.commit()
            return None

        updated = conn.execute(
            """
            UPDATE jobs
            SET state = ?, cleanup_status = ?, error_message = NULL,
                started_at = COALESCE(started_at, ?),
                runner_heartbeat_at = ?, last_progress_at = ?,
                updated_at = ?
            WHERE id = ? AND state = ?
            """,
            (
                JobState.STARTING,
                "pending",
                now,
                now,
                now,
                now,
                row["id"],
                JobState.QUEUED,
            ),
        )
        if updated.rowcount != 1:
            conn.rollback()
            return None
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    insert_job_event(row["id"], EventLevel.INFO, EventType.STATE_CHANGE, {
        "from": JobState.QUEUED,
        "to": JobState.STARTING,
    })
    return get_crawl_job(row["id"])


def update_crawl_job(job_id: str, **kwargs) -> dict | None:
    """Update crawl job fields and return normalized job."""
    if 'status' in kwargs:
        kwargs['state'] = kwargs.pop('status')
    if 'ignore_path_prefixes' in kwargs and isinstance(kwargs['ignore_path_prefixes'], list):
        kwargs['ignore_path_prefixes'] = json.dumps(kwargs['ignore_path_prefixes'])
    return _normalize_job_row(update_job(job_id, **kwargs))


def update_crawl_job_status(job_id: str, status: str, **kwargs) -> dict | None:
    """Update crawl job state and return normalized job."""
    return _normalize_job_row(update_job_state(job_id, status, **kwargs))


def recalculate_job_counts(job_id: str) -> dict | None:
    """Recalculate page-derived counters for a job."""
    row = database.fetchone(
        """
        SELECT
            COUNT(*) AS pages_discovered,
            SUM(CASE WHEN status != ? THEN 1 ELSE 0 END) AS pages_processed,
            SUM(CASE WHEN status = ? THEN 1 ELSE 0 END) AS pages_succeeded,
            SUM(CASE WHEN status = ? THEN 1 ELSE 0 END) AS pages_failed
        FROM pages
        WHERE job_id = ?
        """,
        (PageState.QUEUED, PageState.DONE, PageState.FAILED, job_id)
    )
    counts = dict(row) if row else {}
    pages_discovered = counts.get('pages_discovered') or 0
    pages_processed = counts.get('pages_processed') or 0
    pages_succeeded = counts.get('pages_succeeded') or 0
    pages_failed = counts.get('pages_failed') or 0

    update_job(
        job_id,
        pages_discovered=pages_discovered,
        pages_processed=pages_processed,
        pages_succeeded=pages_succeeded,
        pages_failed=pages_failed,
        pages_fetched=pages_discovered,
        pages_exported=pages_succeeded,
        last_progress_at=_now_iso(),
    )
    return get_crawl_job(job_id)


def create_page(
    job_id: str,
    url: str,
    canonical_url: str,
    parent_page_id: str | None,
    depth: int,
    discovery_order: int | None,
    status: str = PageState.QUEUED,
    title: str | None = None,
    meta_json: dict | None = None,
    max_pages: int | None = None,
) -> dict | None:
    """Create a page if it has not already been seen for the job."""
    conn = database.get_connection()
    conn.execute("BEGIN IMMEDIATE")
    try:
        existing = conn.execute(
            "SELECT * FROM pages WHERE job_id = ? AND canonical_url = ?",
            (job_id, canonical_url),
        ).fetchone()
        if existing:
            conn.commit()
            return _normalize_page_row(_row_to_dict(existing))

        if max_pages is not None:
            count_row = conn.execute(
                "SELECT COUNT(*) AS count FROM pages WHERE job_id = ?",
                (job_id,),
            ).fetchone()
            if (count_row["count"] if count_row else 0) >= max_pages:
                conn.commit()
                return None

        if discovery_order is None:
            order_row = conn.execute(
                "SELECT COALESCE(MAX(discovery_order), -1) + 1 AS next_order FROM pages WHERE job_id = ?",
                (job_id,),
            ).fetchone()
            discovery_order = order_row["next_order"] if order_row else 0

        page_id = generate_page_id()
        now = _now_iso()
        conn.execute(
            """
            INSERT INTO pages (
                id, job_id, url, canonical_url, parent_page_id, depth, title,
                status, discovery_order, meta_json, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                page_id,
                job_id,
                url,
                canonical_url,
                parent_page_id,
                depth,
                title,
                status,
                discovery_order,
                json.dumps(meta_json or {}),
                now,
                now,
            ),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    recalculate_job_counts(job_id)
    return get_page_by_id(page_id)


def get_page_by_id(page_id: str) -> dict | None:
    """Get a page by ID."""
    row = database.fetchone("SELECT * FROM pages WHERE id = ?", (page_id,))
    return _normalize_page_row(_row_to_dict(row))


def get_page_by_canonical_url(job_id: str, canonical_url: str) -> dict | None:
    """Get a page by canonical URL within a job."""
    row = database.fetchone(
        "SELECT * FROM pages WHERE job_id = ? AND canonical_url = ?",
        (job_id, canonical_url)
    )
    return _normalize_page_row(_row_to_dict(row))


def update_page(page_id: str, **kwargs) -> dict | None:
    """Update page fields."""
    if not kwargs:
        return get_page_by_id(page_id)

    if 'removed_blocks_json' in kwargs and not isinstance(kwargs['removed_blocks_json'], str):
        kwargs['removed_blocks_json'] = json.dumps(kwargs['removed_blocks_json'])
    if 'meta_json' in kwargs and not isinstance(kwargs['meta_json'], str):
        kwargs['meta_json'] = json.dumps(kwargs['meta_json'])
    kwargs['updated_at'] = _now_iso()

    set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
    values = list(kwargs.values()) + [page_id]
    database.execute_query(
        f"UPDATE pages SET {set_clause} WHERE id = ?",
        tuple(values)
    )
    database.commit()
    return get_page_by_id(page_id)


def update_page_status(page_id: str, status: str, **kwargs) -> dict | None:
    """Update page status, then refresh job counters."""
    page = get_page_by_id(page_id)
    if not page:
        return None
    result = update_page(page_id, status=status, **kwargs)
    recalculate_job_counts(page['job_id'])
    return result


def get_next_queued_page(job_id: str) -> dict | None:
    """Get the next queued page for BFS processing."""
    row = database.fetchone(
        """
        SELECT * FROM pages
        WHERE job_id = ? AND status = ?
        ORDER BY depth ASC, discovery_order ASC
        LIMIT 1
        """,
        (job_id, PageState.QUEUED)
    )
    return _normalize_page_row(_row_to_dict(row))


def claim_next_page_for_processing(worker_id: str, lease_seconds: int) -> dict | None:
    """Lease the next queued page across running jobs."""
    conn = database.get_connection()
    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    expires_at = (now + timedelta(seconds=lease_seconds)).isoformat()

    conn.execute("BEGIN IMMEDIATE")
    try:
        conn.execute(
            """
            UPDATE pages
            SET status = ?, claimed_by = NULL, claimed_at = NULL, lease_expires_at = NULL, updated_at = ?
            WHERE status IN (?, ?, ?)
              AND lease_expires_at IS NOT NULL
              AND lease_expires_at < ?
            """,
            (
                PageState.QUEUED,
                now_iso,
                PageState.QUEUED,
                PageState.DISCOVERING,
                PageState.EXTRACTING,
                now_iso,
            ),
        )

        row = conn.execute(
            """
            SELECT p.id
            FROM pages p
            JOIN jobs j ON j.id = p.job_id
            WHERE j.state = ?
              AND p.status = ?
            ORDER BY j.created_at ASC, p.depth ASC, p.discovery_order ASC
            LIMIT 1
            """,
            (JobState.RUNNING, PageState.QUEUED),
        ).fetchone()
        if row is None:
            conn.commit()
            return None

        updated = conn.execute(
            """
            UPDATE pages
            SET status = ?, claimed_by = ?, claimed_at = ?, lease_expires_at = ?, updated_at = ?
            WHERE id = ? AND status = ?
            """,
            (
                PageState.DISCOVERING,
                worker_id,
                now_iso,
                expires_at,
                now_iso,
                row["id"],
                PageState.QUEUED,
            ),
        )
        if updated.rowcount != 1:
            conn.rollback()
            return None
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    page = get_page_by_id(row["id"])
    if page:
        recalculate_job_counts(page["job_id"])
    return page


def renew_page_lease(page_id: str, worker_id: str, lease_seconds: int) -> dict | None:
    """Extend the lease for an in-flight page."""
    expires_at = (datetime.now(timezone.utc) + timedelta(seconds=lease_seconds)).isoformat()
    page = update_page(
        page_id,
        claimed_by=worker_id,
        lease_expires_at=expires_at,
    )
    return page


def claim_job_ready_for_finalization() -> dict | None:
    """Atomically claim the next finished job for finalization."""
    conn = database.get_connection()
    now = _now_iso()
    conn.execute("BEGIN IMMEDIATE")
    try:
        row = conn.execute(
            """
            SELECT id, state
            FROM jobs j
            WHERE (
                j.state = ?
                AND NOT EXISTS (
                    SELECT 1 FROM pages p
                    WHERE p.job_id = j.id
                      AND p.status IN (?, ?, ?, ?)
                )
            ) OR (
                j.state = ?
                AND COALESCE(j.cleanup_status, 'pending') NOT IN ('running', 'done')
                AND NOT EXISTS (
                    SELECT 1 FROM pages p
                    WHERE p.job_id = j.id
                      AND p.status IN (?, ?, ?)
                )
            )
            ORDER BY j.created_at ASC
            LIMIT 1
            """,
            (
                JobState.RUNNING,
                PageState.QUEUED,
                PageState.DISCOVERING,
                PageState.EXTRACTING,
                PageState.CLEANING,
                JobState.CANCELLED,
                PageState.DISCOVERING,
                PageState.EXTRACTING,
                PageState.CLEANING,
            ),
        ).fetchone()
        if row is None:
            conn.commit()
            return None

        if row["state"] == JobState.RUNNING:
            updated = conn.execute(
                """
                UPDATE jobs
                SET state = ?, cleanup_status = ?, runner_heartbeat_at = ?, updated_at = ?
                WHERE id = ? AND state = ?
                """,
                (JobState.FINALIZING, "running", now, now, row["id"], JobState.RUNNING),
            )
        else:
            updated = conn.execute(
                """
                UPDATE jobs
                SET cleanup_status = ?, runner_heartbeat_at = ?, updated_at = ?
                WHERE id = ? AND state = ? AND COALESCE(cleanup_status, 'pending') NOT IN ('running', 'done')
                """,
                ("running", now, now, row["id"], JobState.CANCELLED),
            )
        if updated.rowcount != 1:
            conn.rollback()
            return None
        conn.commit()
    except Exception:
        conn.rollback()
        raise

    if row["state"] == JobState.RUNNING:
        insert_job_event(row["id"], EventLevel.INFO, EventType.STATE_CHANGE, {
            "from": JobState.RUNNING,
            "to": JobState.FINALIZING,
        })
    return get_crawl_job(row["id"])


def reset_inflight_pages(job_id: str) -> None:
    """Release any leased or in-flight pages back to the queue."""
    database.execute_query(
        """
        UPDATE pages
        SET status = ?, claimed_by = NULL, claimed_at = NULL, lease_expires_at = NULL, updated_at = ?
        WHERE job_id = ?
          AND status IN (?, ?, ?)
        """,
        (
            PageState.QUEUED,
            _now_iso(),
            job_id,
            PageState.DISCOVERING,
            PageState.EXTRACTING,
            PageState.CLEANING,
        ),
    )
    database.commit()
    recalculate_job_counts(job_id)


def list_pages_for_job(
    job_id: str,
    depth: int | None = None,
    parent_page_id: str | None = None,
    status: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[dict]:
    """List pages for a job with optional filters."""
    where = ["job_id = ?"]
    params: list[Any] = [job_id]

    if depth is not None:
        where.append("depth = ?")
        params.append(depth)
    if parent_page_id is not None:
        where.append("parent_page_id = ?")
        params.append(parent_page_id)
    if status:
        where.append("status = ?")
        params.append(status)

    query = f"""
        SELECT * FROM pages
        WHERE {" AND ".join(where)}
        ORDER BY depth ASC, discovery_order ASC
        LIMIT ? OFFSET ?
    """
    params.extend([limit, offset])
    rows = database.fetchall(query, tuple(params))
    return [_normalize_page_row(_row_to_dict(row)) for row in rows]


def count_pages_for_job(
    job_id: str,
    depth: int | None = None,
    parent_page_id: str | None = None,
    status: str | None = None,
) -> int:
    """Count pages for a job with optional filters."""
    where = ["job_id = ?"]
    params: list[Any] = [job_id]

    if depth is not None:
        where.append("depth = ?")
        params.append(depth)
    if parent_page_id is not None:
        where.append("parent_page_id = ?")
        params.append(parent_page_id)
    if status:
        where.append("status = ?")
        params.append(status)

    row = database.fetchone(
        f"SELECT COUNT(*) AS count FROM pages WHERE {' AND '.join(where)}",
        tuple(params)
    )
    return row['count'] if row else 0


def record_page_link(
    job_id: str,
    from_page_id: str | None,
    to_url: str,
    to_canonical_url: str,
    accepted: bool,
    reject_reason: str | None = None,
) -> dict:
    """Record a discovered page link for debugging and tree analysis."""
    now = _now_iso()
    cursor = database.execute_query(
        """
        INSERT INTO page_links (
            job_id, from_page_id, to_url, to_canonical_url, accepted, reject_reason, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            job_id,
            from_page_id,
            to_url,
            to_canonical_url,
            1 if accepted else 0,
            reject_reason,
            now,
        )
    )
    database.commit()
    row = database.fetchone("SELECT * FROM page_links WHERE id = ?", (cursor.lastrowid,))
    return _row_to_dict(row)


def get_job_tree(job_id: str) -> dict:
    """Build a tree payload from job pages."""
    pages = list_pages_for_job(job_id, limit=100000, offset=0)
    nodes = []
    child_map: dict[str, list[str]] = {}
    root_page_id = None

    for page in pages:
        parent_page_id = page.get('parent_page_id')
        if parent_page_id:
            child_map.setdefault(parent_page_id, []).append(page['id'])
        elif root_page_id is None:
            root_page_id = page['id']

    for page in pages:
        nodes.append({
            'page_id': page['id'],
            'parent_page_id': page.get('parent_page_id'),
            'url': page['url'],
            'title': page.get('title'),
            'depth': page['depth'],
            'status': page['status'],
            'child_page_ids': child_map.get(page['id'], []),
        })

    return {
        'job_id': job_id,
        'root_page_id': root_page_id,
        'nodes': nodes,
    }


# ============================================================================
# IP Usage (Rate Limiting)
# ============================================================================

def get_ip_concurrent_count(ip_hash: str) -> int:
    """Get the current concurrent job count for an IP."""
    row = database.fetchone(
        "SELECT concurrent_count FROM ip_usage WHERE ip_hash = ?",
        (ip_hash,)
    )
    return row['concurrent_count'] if row else 0


def increment_ip_concurrent(ip_hash: str) -> int:
    """Increment and return the concurrent job count for an IP."""
    now = _now_iso()
    
    database.execute_query(
        """
        INSERT INTO ip_usage (ip_hash, concurrent_count, updated_at)
        VALUES (?, 1, ?)
        ON CONFLICT(ip_hash) DO UPDATE SET
            concurrent_count = concurrent_count + 1,
            updated_at = ?
        """,
        (ip_hash, now, now)
    )
    database.commit()
    
    return get_ip_concurrent_count(ip_hash)


def decrement_ip_concurrent(ip_hash: str) -> int:
    """Decrement and return the concurrent job count for an IP."""
    now = _now_iso()
    
    database.execute_query(
        """
        UPDATE ip_usage 
        SET concurrent_count = MAX(0, concurrent_count - 1),
            updated_at = ?
        WHERE ip_hash = ?
        """,
        (now, ip_hash)
    )
    database.commit()
    
    return get_ip_concurrent_count(ip_hash)


# ============================================================================
# Job Artifacts
# ============================================================================

def create_artifact(
    job_id: str,
    kind: str,
    path: str,
    byte_size: int,
    sha256: str | None = None
) -> dict:
    """Create a job artifact record."""
    now = _now_iso()
    
    cursor = database.execute_query(
        """
        INSERT INTO job_artifacts (job_id, kind, path, byte_size, sha256, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (job_id, kind, path, byte_size, sha256, now)
    )
    database.commit()
    
    artifact_id = cursor.lastrowid
    row = database.fetchone("SELECT * FROM job_artifacts WHERE id = ?", (artifact_id,))
    return _row_to_dict(row)


def get_artifacts_for_job(job_id: str) -> list[dict]:
    """Get all artifacts for a job."""
    rows = database.fetchall(
        "SELECT * FROM job_artifacts WHERE job_id = ?",
        (job_id,)
    )
    return [_row_to_dict(row) for row in rows]


def get_artifact_by_kind(job_id: str, kind: str) -> dict | None:
    """Get a specific artifact for a job by kind."""
    row = database.fetchone(
        "SELECT * FROM job_artifacts WHERE job_id = ? AND kind = ?",
        (job_id, kind)
    )
    return _row_to_dict(row)


# ============================================================================
# Job Events
# ============================================================================

def insert_job_event(
    job_id: str,
    level: str,
    event: str,
    data: dict | None = None
):
    """Insert a job event record."""
    now = _now_iso()
    
    database.execute_query(
        """
        INSERT INTO job_events (job_id, at, level, event, data)
        VALUES (?, ?, ?, ?, ?)
        """,
        (job_id, now, level, event, json.dumps(data) if data else None)
    )
    database.commit()


def get_recent_events(job_id: str, limit: int = 10) -> list[dict]:
    """Get recent events for a job."""
    rows = database.fetchall(
        """
        SELECT * FROM job_events 
        WHERE job_id = ? 
        ORDER BY at DESC 
        LIMIT ?
        """,
        (job_id, limit)
    )
    return [_row_to_dict(row) for row in rows]


# ============================================================================
# Retry Job Management
# ============================================================================

def get_retry_chain(job_id: str) -> list[dict]:
    """Get the full retry chain for a job (original + all retries)."""
    # First, find the original job
    job = get_job_by_id(job_id)
    if not job:
        return []
    
    # If this is a retry, find the original
    original_id = job.get('retry_of_job_id') or job_id
    
    # Get all jobs in the retry chain
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE id = ? OR retry_of_job_id = ?
        ORDER BY retry_attempt ASC
        """,
        (original_id, original_id)
    )
    return [_row_to_dict(row) for row in rows]


def get_latest_retry(job_id: str) -> dict | None:
    """Get the latest retry job for a given job."""
    rows = database.fetchall(
        """
        SELECT * FROM jobs 
        WHERE retry_of_job_id = ?
        ORDER BY retry_attempt DESC
        LIMIT 1
        """,
        (job_id,)
    )
    return _row_to_dict(rows[0]) if rows else None
