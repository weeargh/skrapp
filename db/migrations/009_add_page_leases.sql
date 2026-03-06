ALTER TABLE pages ADD COLUMN claimed_by TEXT;
ALTER TABLE pages ADD COLUMN claimed_at TEXT;
ALTER TABLE pages ADD COLUMN lease_expires_at TEXT;

CREATE INDEX IF NOT EXISTS pages_job_claim_idx
ON pages(job_id, status, lease_expires_at, discovery_order);
