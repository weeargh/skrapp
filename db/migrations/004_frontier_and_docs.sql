-- Persistent frontier (URL queue) for crash-safe resumability
CREATE TABLE IF NOT EXISTS url_queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    
    -- Queue state: discovered -> queued -> fetching -> fetched -> parsed -> stored
    state TEXT NOT NULL DEFAULT 'queued',
    
    -- Metadata
    depth INTEGER NOT NULL DEFAULT 0,
    priority INTEGER NOT NULL DEFAULT 0,  -- Higher = more important
    discovered_at TEXT NOT NULL,
    
    -- Lease for crash safety (visibility timeout pattern)
    leased_at TEXT,
    leased_by TEXT,  -- worker_id
    lease_expires_at TEXT,
    
    -- Retry tracking
    retry_count INTEGER NOT NULL DEFAULT 0,
    last_error TEXT,
    last_status_code INTEGER,
    
    -- Timestamps
    fetched_at TEXT,
    parsed_at TEXT,
    stored_at TEXT
);

CREATE INDEX IF NOT EXISTS url_queue_job_state_idx ON url_queue(job_id, state);
CREATE INDEX IF NOT EXISTS url_queue_job_canonical_idx ON url_queue(job_id, canonical_url);
CREATE INDEX IF NOT EXISTS url_queue_lease_idx ON url_queue(state, lease_expires_at);

-- Document identity: separate doc_id from URL
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,  -- UUID or content-based hash
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    
    -- Stable identity
    content_hash TEXT,  -- SHA256 of normalized text
    title_hash TEXT,    -- Hash of title for matching
    
    -- Primary URL (first seen)
    primary_url TEXT NOT NULL,
    primary_canonical TEXT NOT NULL,
    
    -- Metadata
    title TEXT,
    language TEXT,
    doc_type TEXT,  -- article, category, index, etc.
    
    -- Quality
    quality_score REAL,
    quality_passed INTEGER DEFAULT 1,
    
    -- Timestamps
    first_seen_at TEXT NOT NULL,
    last_seen_at TEXT NOT NULL,
    
    -- Content versioning (optional)
    version INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX IF NOT EXISTS documents_job_idx ON documents(job_id);
CREATE INDEX IF NOT EXISTS documents_content_hash_idx ON documents(content_hash);

-- URL aliases for a document (multiple URLs -> same content)
CREATE TABLE IF NOT EXISTS document_urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    
    url TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    
    -- Why this URL maps to this document
    match_reason TEXT,  -- 'canonical', 'content_hash', 'redirect', 'language_variant'
    
    -- Metadata
    language TEXT,
    is_primary INTEGER NOT NULL DEFAULT 0,
    
    discovered_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS document_urls_doc_idx ON document_urls(document_id);
CREATE INDEX IF NOT EXISTS document_urls_job_canonical_idx ON document_urls(job_id, canonical_url);

-- Structured crawl logs for debugging and analytics
CREATE TABLE IF NOT EXISTS crawl_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    
    -- Request info
    url TEXT NOT NULL,
    canonical_url TEXT,
    
    -- Timing
    timestamp TEXT NOT NULL,
    latency_ms INTEGER,
    
    -- Response
    status_code INTEGER,
    content_type TEXT,
    content_length INTEGER,
    
    -- Processing
    stage TEXT,  -- fetch, parse, extract, store
    extraction_mode TEXT,
    quality_score REAL,
    
    -- Errors
    error_type TEXT,
    error_message TEXT,
    
    -- Context
    depth INTEGER,
    retry_count INTEGER
);

CREATE INDEX IF NOT EXISTS crawl_logs_job_idx ON crawl_logs(job_id);
CREATE INDEX IF NOT EXISTS crawl_logs_job_timestamp_idx ON crawl_logs(job_id, timestamp);
CREATE INDEX IF NOT EXISTS crawl_logs_error_idx ON crawl_logs(job_id, error_type);
