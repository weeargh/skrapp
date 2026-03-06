-- Add retry tracking fields to jobs table

-- Retry relationship tracking
ALTER TABLE jobs ADD COLUMN retry_of_job_id TEXT DEFAULT NULL;
ALTER TABLE jobs ADD COLUMN retry_attempt INTEGER DEFAULT 0;
ALTER TABLE jobs ADD COLUMN retry_reason TEXT DEFAULT NULL;
ALTER TABLE jobs ADD COLUMN retry_mode TEXT DEFAULT NULL; -- 'slower', 'playwright'

-- Index for finding retry chains
CREATE INDEX IF NOT EXISTS jobs_retry_of_idx ON jobs(retry_of_job_id);
