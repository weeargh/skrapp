"""SQLite database connection management."""
from __future__ import annotations

import os
import sqlite3
import threading
import logging
from contextlib import contextmanager
from typing import Optional, List

from config import settings

logger = logging.getLogger(__name__)
_local = threading.local()


def _is_expected_migration_error(error: sqlite3.OperationalError) -> bool:
    """Best-effort filter for idempotent migration errors."""
    message = str(error).lower()
    expected_fragments = (
        "duplicate column name",
        "already exists",
        "duplicate table name",
        "index ",
    )
    return any(fragment in message for fragment in expected_fragments)


def get_connection() -> sqlite3.Connection:
    """Get a thread-local database connection."""
    if not hasattr(_local, 'connection') or _local.connection is None:
        os.makedirs(os.path.dirname(settings.DATABASE_PATH), exist_ok=True)
        conn = sqlite3.connect(
            settings.DATABASE_PATH,
            check_same_thread=False,
            timeout=30.0
        )
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=5000")
        conn.execute("PRAGMA foreign_keys=ON")
        _local.connection = conn
    return _local.connection


def close_connection():
    """Close the thread-local database connection."""
    if hasattr(_local, 'connection') and _local.connection is not None:
        _local.connection.close()
        _local.connection = None


@contextmanager
def transaction():
    """Context manager for database transactions."""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        logger.error(f"Transaction failed, rolling back: {e}")
        raise


def init_db():
    """Initialize the database with the schema."""
    migrations_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "migrations"
    )
    
    conn = get_connection()
    migration_files = sorted(
        filename for filename in os.listdir(migrations_dir)
        if filename.endswith(".sql")
    )
    
    for filename in migration_files:
        migration_path = os.path.join(migrations_dir, filename)
        try:
            with open(migration_path, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
            conn.commit()
        except sqlite3.OperationalError as e:
            if _is_expected_migration_error(e):
                logger.debug("Skipping idempotent migration error for %s: %s", filename, e)
                continue
            raise


def execute_query(query: str, params: tuple = ()) -> sqlite3.Cursor:
    """Execute a query and return the cursor."""
    conn = get_connection()
    return conn.execute(query, params)


def execute_many(query: str, params_list: list) -> sqlite3.Cursor:
    """Execute a query with multiple parameter sets."""
    conn = get_connection()
    return conn.executemany(query, params_list)


def fetchone(query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
    """Execute a query and fetch one result."""
    cursor = execute_query(query, params)
    return cursor.fetchone()


def fetchall(query: str, params: tuple = ()) -> List[sqlite3.Row]:
    """Execute a query and fetch all results."""
    cursor = execute_query(query, params)
    return cursor.fetchall()


def commit():
    """Commit the current transaction."""
    get_connection().commit()
