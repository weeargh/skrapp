-- Initial database schema for the docs crawler

-- Jobs table: stores job configuration and lifecycle state
CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,
    token_hash TEXT NOT NULL,
    
    start_url TEXT NOT NULL,
    allowed_host TEXT NOT NULL,
    max_pages INTEGER NOT NULL DEFAULT 1000,
    timeout_seconds INTEGER NOT NULL DEFAULT 1800,
    ignore_path_prefixes TEXT NOT NULL DEFAULT '[]',
    
    state TEXT NOT NULL DEFAULT 'queued',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    started_at TEXT,
    finished_at TEXT,
    
    pages_fetched INTEGER NOT NULL DEFAULT 0,
    pages_exported INTEGER NOT NULL DEFAULT 0,
    errors_count INTEGER NOT NULL DEFAULT 0,
    
    runner_heartbeat_at TEXT,
    last_progress_at TEXT,
    restart_count INTEGER NOT NULL DEFAULT 0,
    
    site_status TEXT,
    block_evidence TEXT,
    last_error TEXT,
    
    requester_ip_hash TEXT NOT NULL,
    expires_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS jobs_state_idx ON jobs(state);
CREATE INDEX IF NOT EXISTS jobs_expires_idx ON jobs(expires_at);
CREATE INDEX IF NOT EXISTS jobs_host_idx ON jobs(allowed_host);

-- Job artifacts table: tracks output files
CREATE TABLE IF NOT EXISTS job_artifacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    kind TEXT NOT NULL,
    path TEXT NOT NULL,
    byte_size INTEGER NOT NULL,
    sha256 TEXT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS job_artifacts_job_id_idx ON job_artifacts(job_id);

-- IP usage table: tracks concurrent jobs per IP for rate limiting
CREATE TABLE IF NOT EXISTS ip_usage (
    ip_hash TEXT PRIMARY KEY,
    concurrent_count INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL
);

-- Job events table: logs state transitions and notable events
CREATE TABLE IF NOT EXISTS job_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    at TEXT NOT NULL,
    level TEXT NOT NULL,
    event TEXT NOT NULL,
    data TEXT
);

CREATE INDEX IF NOT EXISTS job_events_job_id_idx ON job_events(job_id);
