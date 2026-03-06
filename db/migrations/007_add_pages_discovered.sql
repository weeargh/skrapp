-- Add the missing pages_discovered counter used by the MVP job model.
ALTER TABLE jobs ADD COLUMN pages_discovered INTEGER NOT NULL DEFAULT 0;
