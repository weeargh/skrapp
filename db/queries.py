"""Database query functions for jobs and related tables."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, List

from config.constants import JobState, EventLevel, EventType
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
        WHERE state IN (?, ?)
        AND runner_heartbeat_at IS NOT NULL
        AND runner_heartbeat_at < ?
        """,
        (JobState.RUNNING, JobState.FINALIZING, threshold_time)
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
