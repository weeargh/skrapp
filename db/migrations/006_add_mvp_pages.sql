-- Extend the existing schema toward the MVP page/tree model.

-- Jobs: add page-tree oriented metadata on top of the existing job table.
ALTER TABLE jobs ADD COLUMN allowed_path_prefix TEXT;
ALTER TABLE jobs ADD COLUMN max_depth INTEGER NOT NULL DEFAULT 2;
ALTER TABLE jobs ADD COLUMN pages_processed INTEGER NOT NULL DEFAULT 0;
ALTER TABLE jobs ADD COLUMN pages_succeeded INTEGER NOT NULL DEFAULT 0;
ALTER TABLE jobs ADD COLUMN pages_failed INTEGER NOT NULL DEFAULT 0;
ALTER TABLE jobs ADD COLUMN cleanup_status TEXT NOT NULL DEFAULT 'pending';
ALTER TABLE jobs ADD COLUMN error_message TEXT;

CREATE INDEX IF NOT EXISTS jobs_created_at_idx ON jobs(created_at);

-- Pages: first-class page records for the crawl tree.
CREATE TABLE IF NOT EXISTS pages (
    id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    parent_page_id TEXT REFERENCES pages(id) ON DELETE SET NULL,
    depth INTEGER NOT NULL DEFAULT 0,
    title TEXT,
    status TEXT NOT NULL DEFAULT 'queued',
    discovery_order INTEGER NOT NULL DEFAULT 0,
    raw_html TEXT,
    raw_markdown TEXT,
    raw_text TEXT,
    clean_markdown TEXT,
    plain_text TEXT,
    main_content_selector TEXT,
    cleanup_score REAL,
    removed_blocks_json TEXT,
    meta_json TEXT,
    error_message TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(job_id, canonical_url)
);

CREATE INDEX IF NOT EXISTS pages_job_status_idx ON pages(job_id, status);
CREATE INDEX IF NOT EXISTS pages_job_depth_idx ON pages(job_id, depth, discovery_order);
CREATE INDEX IF NOT EXISTS pages_parent_idx ON pages(parent_page_id);
CREATE INDEX IF NOT EXISTS pages_job_canonical_idx ON pages(job_id, canonical_url);

-- Page links: track discovered edges and rejection reasons.
CREATE TABLE IF NOT EXISTS page_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    from_page_id TEXT REFERENCES pages(id) ON DELETE SET NULL,
    to_url TEXT NOT NULL,
    to_canonical_url TEXT NOT NULL,
    accepted INTEGER NOT NULL DEFAULT 0,
    reject_reason TEXT,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS page_links_job_from_idx ON page_links(job_id, from_page_id);
CREATE INDEX IF NOT EXISTS page_links_job_target_idx ON page_links(job_id, to_canonical_url);
