# Skrapp MVP Spec

## Goal

Skrapp is an internal crawling tool for personal or team use.

The product goal is simple:

- start from a root URL
- discover that page and its child pages
- preserve the parent -> child tree
- limit crawl depth and page count
- extract readable markdown/plain text for each page
- clean repetitive help-center boilerplate such as headers, footers, sidebars, related links, and repeated FAQ modules

This is an MVP, not a general-purpose internet crawler.

## Core User Outcome

A user should always be able to:

- enter a docs/help-center URL
- set `max_depth`
- set `max_pages`
- optionally scope the crawl to a path prefix
- watch pages being discovered level by level
- open any page in the crawl and see:
  - raw extracted markdown
  - cleaned markdown
  - plain text
- download the crawl as:
  - `pages.jsonl`
  - `tree.json`
  - `markdown.zip`

## MVP Principles

- Ignore auth for now.
- Optimize for clarity and reliability, not high scale.
- Use a single API service and a single worker service.
- Use BFS so the tree fills level by level.
- Keep one canonical parent per page for a clean tree.
- Use Playwright for page discovery.
- Use Jina Reader for markdown/text extraction.
- Run cleanup after extraction, with both page-level and crawl-level rules.

## Non-Goals

- Public multi-tenant SaaS
- Large-scale distributed crawling
- Complex scheduling
- Full graph traversal across many domains
- Fine-grained user permissions
- Search, embeddings, reranking, or chat over content

## Product Architecture

### High-Level Components

```text
Web UI
  ->
Flask API
  ->
Postgres
  ->
Background Worker
  ->
Playwright (discovery)
  ->
Jina Reader (extraction)
  ->
Postgres + artifact storage
```

### Responsibilities

#### 1. Web UI

- create crawl jobs
- show job progress
- show page tree
- show page detail
- expose exports

#### 2. API Service

- validate input
- create jobs
- expose job and page status
- expose tree and page detail
- expose downloads
- mark jobs cancelled

#### 3. Worker Service

- poll queued jobs
- crawl pages with BFS
- extract links with Playwright
- call Jina Reader per page
- store raw content
- run cleanup/finalization
- write export artifacts

#### 4. Postgres

- jobs
- pages
- job events
- page links
- artifact metadata

#### 5. Artifact Storage

MVP:

- local disk or mounted volume

Later:

- S3 or Cloudflare R2

## Crawl Model

### Scope Rules

A crawl job is restricted by:

- `start_url`
- `allowed_host`
- `allowed_path_prefix`
- `max_depth`
- `max_pages`

Only URLs that satisfy all of the following are accepted:

- same hostname as the root URL
- path begins with the allowed prefix
- not excluded by extension or ignore rules
- not already seen in canonical form

### Traversal Strategy

Use BFS.

Why:

- easy to explain in the UI
- root and immediate children appear quickly
- predictable behavior for a docs/help-center crawl

### Parent / Child Model

Each discovered page has:

- one `parent_page_id`
- one `depth`
- zero or more child pages

If the same page is discovered from multiple parents, the first accepted parent wins.

That keeps the output as a tree instead of a graph.

### Page States

- `queued`: discovered but not yet processed
- `discovering`: Playwright is loading the page and collecting links
- `extracting`: Jina Reader is extracting content
- `cleaning`: cleanup/finalization is running
- `done`: page processed successfully
- `failed`: discovery or extraction failed
- `skipped`: out of scope, duplicate, or dropped by limits

## End-to-End Flow

### Job Flow

1. User submits a crawl job.
2. API validates the URL and inserts a `jobs` row.
3. Worker picks up the next queued job.
4. Worker enqueues the root page at depth `0`.
5. Worker processes pages in BFS order.
6. For each page:
   - Playwright loads the page
   - visible links are collected
   - in-scope child pages are inserted
   - Jina Reader extracts markdown/text
   - raw outputs are stored
7. When page discovery/extraction completes or limits are reached:
   - worker runs cleanup across all pages in the job
   - worker generates final artifacts
   - job is marked `done` or `failed`

### Per-Page Flow

1. Load page with Playwright.
2. Capture:
   - final URL
   - title
   - raw HTML
   - discovered links
3. Normalize and filter links.
4. Insert accepted child pages with `parent_page_id` and `depth + 1`.
5. Call Jina Reader for the page URL.
6. Store:
   - `raw_markdown`
   - `raw_text`
7. After the crawl:
   - cleanup generates `clean_markdown`
   - plain text is normalized
   - removed blocks are logged

## Cleanup Pipeline

Cleanup is a separate phase after extraction.

This is critical for help-center sites where the same blocks appear on many pages.

### Pass 1: Structural Cleanup

Use the raw HTML to identify the main content region.

Preferred selectors:

- `main`
- `article`
- `[role="main"]`
- per-domain selectors such as `.article-body`, `.hc-article`, `.faq-content`

Drop or ignore obvious chrome:

- `header`
- `footer`
- `nav`
- `aside`
- breadcrumbs
- search box
- sidebar category list
- related articles
- "was this helpful" widgets
- share/support CTA blocks

### Pass 2: Repeated Block Cleanup

For each page:

- split markdown into blocks
- normalize each block
- hash each normalized block

For the whole job:

- count how many pages contain each block
- remove blocks that are repeated across many pages and look like boilerplate

Initial removal heuristics:

- repeated on `>= 30%` of pages and under `200` chars
- repeated on `>= 15%` of pages and high link density
- matches known boilerplate phrases

Always keep:

- page title / first meaningful heading
- code blocks
- tables
- long paragraphs

### Pass 3: Text Cleanup

- collapse whitespace
- remove duplicate consecutive blocks
- remove empty headings
- remove generic boilerplate lines

Examples:

- `Was this article helpful?`
- `Related articles`
- `Contact support`
- cookie or footer text

### Domain Rules

Support optional per-domain cleanup rules:

- `main_selectors`
- `drop_selectors`
- `drop_patterns`

This is especially useful for help-center platforms with stable layouts.

## Data Model

### Table: `jobs`

Tracks one crawl request.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `uuid` / `text` | primary key |
| `start_url` | `text` | root URL |
| `allowed_host` | `text` | hostname scope |
| `allowed_path_prefix` | `text` | path scope, eg `/hc/id` |
| `max_depth` | `integer` | inclusive depth limit |
| `max_pages` | `integer` | max accepted pages |
| `status` | `text` | `queued`, `running`, `finalizing`, `done`, `failed`, `cancelled` |
| `pages_discovered` | `integer` | total pages inserted |
| `pages_processed` | `integer` | total pages attempted |
| `pages_succeeded` | `integer` | total pages with extracted content |
| `pages_failed` | `integer` | total failed pages |
| `cleanup_status` | `text` | `pending`, `running`, `done`, `failed` |
| `error_message` | `text` | latest job-level error |
| `started_at` | `timestamptz` | nullable |
| `finished_at` | `timestamptz` | nullable |
| `created_at` | `timestamptz` | required |
| `updated_at` | `timestamptz` | required |

### Table: `pages`

Tracks one accepted page in the crawl tree.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `uuid` / `text` | primary key |
| `job_id` | `text` | foreign key to `jobs.id` |
| `url` | `text` | fetched URL |
| `canonical_url` | `text` | normalized URL |
| `parent_page_id` | `text` | nullable, root page has null |
| `depth` | `integer` | root is `0` |
| `title` | `text` | page title |
| `status` | `text` | `queued`, `discovering`, `extracting`, `cleaning`, `done`, `failed`, `skipped` |
| `discovery_order` | `integer` | BFS order |
| `raw_html` | `text` | stored for cleanup/debugging |
| `raw_markdown` | `text` | direct extractor output |
| `clean_markdown` | `text` | final cleaned markdown |
| `plain_text` | `text` | cleaned plain text |
| `main_content_selector` | `text` | selector used during structural cleanup |
| `cleanup_score` | `numeric` | optional quality indicator |
| `removed_blocks_json` | `jsonb` | removed snippets and reasons |
| `meta_json` | `jsonb` | title, lang, content type, extractor metadata |
| `error_message` | `text` | latest page-level error |
| `created_at` | `timestamptz` | required |
| `updated_at` | `timestamptz` | required |

### Table: `page_links`

Optional but useful for debugging discovery.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `bigserial` | primary key |
| `job_id` | `text` | foreign key |
| `from_page_id` | `text` | source page |
| `to_url` | `text` | raw discovered URL |
| `to_canonical_url` | `text` | normalized target |
| `accepted` | `boolean` | whether it became a page |
| `reject_reason` | `text` | eg `out_of_scope`, `duplicate`, `depth_limit` |
| `created_at` | `timestamptz` | required |

### Table: `job_events`

Audit/debug events.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `bigserial` | primary key |
| `job_id` | `text` | foreign key |
| `level` | `text` | `info`, `warn`, `error` |
| `event_type` | `text` | eg `job_started`, `page_failed`, `cleanup_done` |
| `data_json` | `jsonb` | event payload |
| `created_at` | `timestamptz` | required |

### Table: `job_artifacts`

Metadata for exports.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `bigserial` | primary key |
| `job_id` | `text` | foreign key |
| `kind` | `text` | `pages_jsonl`, `tree_json`, `markdown_zip` |
| `path` | `text` | storage path or object key |
| `size_bytes` | `bigint` | artifact size |
| `sha256` | `text` | optional checksum |
| `created_at` | `timestamptz` | required |

## API

Ignore auth in MVP.

Base prefix: `/v1`

### 1. Create Job

`POST /v1/jobs`

Request:

```json
{
  "start_url": "https://help-center.talenta.co/hc/id",
  "allowed_path_prefix": "/hc/id",
  "max_depth": 2,
  "max_pages": 100,
  "ignore_path_prefixes": [
    "/hc/id/requests"
  ]
}
```

Behavior:

- validates URL
- infers `allowed_host`
- defaults `allowed_path_prefix` from `start_url` if not provided
- creates a queued job
- inserts root page

Response:

```json
{
  "job_id": "job_123",
  "status": "queued",
  "start_url": "https://help-center.talenta.co/hc/id",
  "allowed_host": "help-center.talenta.co",
  "allowed_path_prefix": "/hc/id",
  "max_depth": 2,
  "max_pages": 100
}
```

### 2. List Jobs

`GET /v1/jobs`

Query params:

- `status`
- `limit`
- `offset`

Response:

```json
{
  "jobs": [
    {
      "job_id": "job_123",
      "status": "running",
      "start_url": "https://help-center.talenta.co/hc/id",
      "pages_discovered": 24,
      "pages_succeeded": 12,
      "created_at": "2026-03-06T08:00:00Z"
    }
  ]
}
```

### 3. Get Job

`GET /v1/jobs/{job_id}`

Response:

```json
{
  "job_id": "job_123",
  "status": "running",
  "start_url": "https://help-center.talenta.co/hc/id",
  "allowed_host": "help-center.talenta.co",
  "allowed_path_prefix": "/hc/id",
  "max_depth": 2,
  "max_pages": 100,
  "pages_discovered": 24,
  "pages_processed": 18,
  "pages_succeeded": 16,
  "pages_failed": 2,
  "cleanup_status": "pending",
  "started_at": "2026-03-06T08:00:03Z",
  "finished_at": null
}
```

### 4. Cancel Job

`POST /v1/jobs/{job_id}/cancel`

Response:

```json
{
  "job_id": "job_123",
  "status": "cancelled"
}
```

### 5. Get Job Tree

`GET /v1/jobs/{job_id}/tree`

Response:

```json
{
  "job_id": "job_123",
  "root_page_id": "page_root",
  "nodes": [
    {
      "page_id": "page_root",
      "parent_page_id": null,
      "url": "https://help-center.talenta.co/hc/id",
      "title": "Talenta Help Center",
      "depth": 0,
      "status": "done",
      "child_page_ids": ["page_2", "page_3"]
    }
  ]
}
```

### 6. List Pages

`GET /v1/jobs/{job_id}/pages`

Query params:

- `depth`
- `parent_page_id`
- `status`
- `limit`
- `offset`

Response:

```json
{
  "job_id": "job_123",
  "total": 24,
  "pages": [
    {
      "page_id": "page_2",
      "url": "https://help-center.talenta.co/hc/id/articles/123",
      "title": "How to use feature X",
      "parent_page_id": "page_root",
      "depth": 1,
      "status": "done"
    }
  ]
}
```

### 7. Get Page Detail

`GET /v1/jobs/{job_id}/pages/{page_id}`

Response:

```json
{
  "page_id": "page_2",
  "job_id": "job_123",
  "url": "https://help-center.talenta.co/hc/id/articles/123",
  "canonical_url": "https://help-center.talenta.co/hc/id/articles/123",
  "parent_page_id": "page_root",
  "depth": 1,
  "title": "How to use feature X",
  "status": "done",
  "raw_markdown": "# Raw content...",
  "clean_markdown": "# Clean content...",
  "plain_text": "Clean text...",
  "removed_blocks": [
    {
      "type": "paragraph",
      "reason": "repeated_across_pages",
      "text_preview": "Was this article helpful?"
    }
  ]
}
```

### 8. Get Artifacts

`GET /v1/jobs/{job_id}/artifacts`

Response:

```json
{
  "job_id": "job_123",
  "artifacts": [
    {
      "kind": "pages_jsonl",
      "download_url": "/v1/jobs/job_123/download/pages.jsonl"
    },
    {
      "kind": "tree_json",
      "download_url": "/v1/jobs/job_123/download/tree.json"
    },
    {
      "kind": "markdown_zip",
      "download_url": "/v1/jobs/job_123/download/markdown.zip"
    }
  ]
}
```

### 9. Download Artifacts

- `GET /v1/jobs/{job_id}/download/pages.jsonl`
- `GET /v1/jobs/{job_id}/download/tree.json`
- `GET /v1/jobs/{job_id}/download/markdown.zip`

### 10. Health Check

`GET /health`

Response:

```json
{
  "status": "ok"
}
```

## Output Formats

### `pages.jsonl`

One line per page.

```json
{
  "job_id": "job_123",
  "page_id": "page_2",
  "url": "https://help-center.talenta.co/hc/id/articles/123",
  "canonical_url": "https://help-center.talenta.co/hc/id/articles/123",
  "parent_page_id": "page_root",
  "depth": 1,
  "title": "How to use feature X",
  "clean_markdown": "# How to use feature X\n...",
  "plain_text": "How to use feature X ...",
  "status": "done"
}
```

### `tree.json`

```json
{
  "job_id": "job_123",
  "start_url": "https://help-center.talenta.co/hc/id",
  "max_depth": 2,
  "nodes": [
    {
      "page_id": "page_root",
      "parent_page_id": null,
      "url": "https://help-center.talenta.co/hc/id",
      "title": "Talenta Help Center",
      "depth": 0,
      "children": ["page_2", "page_3"]
    }
  ]
}
```

### `markdown.zip`

Contains:

- one `.md` file per successful page
- optional `manifest.json`

Suggested file naming:

- `{depth}_{slug_or_page_id}.md`

## Operational Notes

### Cloud Deployment

MVP deployment target:

- one API container
- one worker container
- one Postgres instance
- one persistent volume for artifacts

### Scaling

MVP assumptions:

- low concurrency
- personal/team usage
- one worker is enough

Scale later by:

- running multiple workers
- moving artifacts to object storage
- adding retry/backoff for extraction calls

## Implementation Notes for This Repo

The current repo already has the right high-level split:

- API service
- worker process
- crawler layer
- artifact finalization

The main design changes required are:

1. move from crawl-first text extraction to:
   - Playwright for discovery
   - Jina Reader for page extraction
2. make `max_depth` a job-level field
3. store explicit `parent_page_id`
4. add crawl-wide repeated-block cleanup
5. produce `tree.json` and `markdown.zip`
6. move from SQLite to Postgres for the cloud MVP

## Future Enhancements

- optional domain rule editor
- retry and backoff policies for extractor failures
- page screenshots
- page diffing between crawls
- HTML preview alongside markdown
- search across crawled pages
