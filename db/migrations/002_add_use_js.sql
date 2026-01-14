-- Add use_js column for Playwright support
ALTER TABLE jobs ADD COLUMN use_js INTEGER NOT NULL DEFAULT 0;
