-- Add crawler strategy tracking fields
ALTER TABLE jobs ADD COLUMN crawler_strategy TEXT;
ALTER TABLE jobs ADD COLUMN fallback_retry_count INTEGER NOT NULL DEFAULT 0;
