"""SQLite database connection management."""
from __future__ import annotations

import os
import sqlite3
import threading
from contextlib import contextmanager
from typing import Optional, List

from config import settings

_local = threading.local()


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
    except Exception:
        conn.rollback()
        raise


def init_db():
    """Initialize the database with the schema."""
    migrations_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "migrations"
    )
    
    conn = get_connection()
    
    migration_file = os.path.join(migrations_dir, "001_initial.sql")
    if os.path.exists(migration_file):
        with open(migration_file, 'r') as f:
            conn.executescript(f.read())
        conn.commit()
    
    # Run additional migrations
    migration_002 = os.path.join(migrations_dir, "002_add_use_js.sql")
    if os.path.exists(migration_002):
        try:
            with open(migration_002, 'r') as f:
                conn.executescript(f.read())
            conn.commit()
        except sqlite3.OperationalError:
            # Column already exists
            pass
    
    migration_003 = os.path.join(migrations_dir, "003_add_crawler_strategy.sql")
    if os.path.exists(migration_003):
        try:
            with open(migration_003, 'r') as f:
                conn.executescript(f.read())
            conn.commit()
        except sqlite3.OperationalError:
            # Columns already exist
            pass


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
