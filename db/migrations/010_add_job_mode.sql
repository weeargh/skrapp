-- Add job mode to support non-crawl acquisition strategies (e.g. zendesk_rag).
ALTER TABLE jobs ADD COLUMN mode TEXT NOT NULL DEFAULT 'crawl';
