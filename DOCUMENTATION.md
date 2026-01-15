# Skrapp Documentation

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Process Design](#process-design)
- [Known Limitations](#known-limitations)
- [Configuration](#configuration)

---

## Overview

Skrapp is a high-performance web crawler designed for extracting structured content from documentation sites. It intelligently handles both traditional HTML sites and JavaScript-heavy single-page applications (SPAs), with automatic fallback mechanisms and quality control.

**Key Features:**
- Dual crawler strategy (Scrapy + Playwright)
- Automatic JavaScript detection and fallback
- Content quality scoring and filtering
- Real-time progress tracking
- Job cancellation with partial result preservation
- Duplicate content detection
- Rate limiting and bot detection handling

---

## Architecture

### System Components

```
┌─────────────────┐
│   Web Browser   │
│   (User UI)     │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐      ┌──────────────────┐
│   Flask API     │◄────►│   SQLite DB      │
│   (Port 8080)   │      │   (Jobs/Events)  │
└────────┬────────┘      └──────────────────┘
         │
         │ Job Queue
         ▼
┌─────────────────┐      ┌──────────────────┐
│  Worker Process │◄────►│  Crawler Engine  │
│  (Polling)      │      │  Scrapy/Playwright│
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐
│  File System    │
│  (JSONL Output) │
└─────────────────┘
```

### Component Details

#### 1. **Flask API Server** (`api/`)
- RESTful API for job management
- Token-based authentication (SHA-256)
- Request validation and rate limiting
- File serving for downloads
- Health check endpoints

**Key Routes:**
- `POST /v1/jobs` - Create new crawl job
- `GET /v1/jobs/{job_id}` - Get job status
- `POST /v1/jobs/{job_id}/cancel` - Cancel running job
- `GET /v1/jobs/{job_id}/download/pages.jsonl` - Download results
- `GET /v1/jobs/{job_id}/pages` - Real-time page listing

#### 2. **Worker Process** (`worker/`)
- Polls for queued jobs every 1 second
- Manages crawler subprocess execution
- Handles job lifecycle and state transitions
- Detects and recovers from stuck jobs
- Automatic finalization of cancelled jobs

**Responsibilities:**
- Job state management
- Heartbeat monitoring
- Stuck job detection (orphaned, stalled, hard-stalled)
- Crawler selection and execution
- Result finalization and deduplication

#### 3. **Crawler Engine** (`crawler/`)
- **Scrapy Spider**: Fast HTML crawler (128 concurrent requests)
- **Playwright Crawler**: JavaScript-enabled browser automation
- **Intelligent Fallback**: Auto-switches to Playwright when needed

**Pipeline Stages:**
1. Text Extraction (Trafilatura/Readability/Fallback)
2. Quality Gate (content scoring and filtering)
3. Content Cleanup (boilerplate removal)
4. Document Identity (deduplication via content hash)
5. Budget Control (max pages enforcement)
6. Markdown Extraction (structured content)
7. Blocking Detection (rate limiting, CAPTCHA)
8. JSONL Writer (output generation)

#### 4. **Database** (`db/`)
- SQLite for job state and events
- Frontier management for URL tracking
- Document deduplication tracking
- Event logging for debugging

**Tables:**
- `jobs` - Job metadata and state
- `job_events` - State transitions and errors
- `frontier` - URL discovery tracking
- `documents` - Content deduplication
- `document_urls` - URL aliases for same content

---

## Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework for REST API
- **Scrapy 2.11+** - Fast HTTP crawler framework
- **Playwright** - Browser automation for JavaScript sites
- **SQLite** - Lightweight database
- **Trafilatura** - Content extraction library
- **Readability** - Alternative extraction fallback

### Frontend
- **Vanilla JavaScript** - No frameworks
- **Modern CSS** (CSS custom properties)
- **Inter Font** - Google Fonts typography

### Infrastructure
- **Process-based architecture** (API + Worker)
- **File-based output** (JSONL format)
- **Token-based auth** (SHA-256 hashed)

### Key Libraries
```python
flask>=3.0.0
scrapy>=2.11.0
playwright>=1.40.0
trafilatura>=1.6.0
readability-lxml>=0.8.1
sqlite3 (built-in)
```

---

## Process Design

### Job Lifecycle

```
QUEUED → RUNNING → FINALIZING → DONE
                ↓
              FAILED
                ↓
            CANCELLED
```

**State Descriptions:**
- **QUEUED**: Job created, waiting for worker
- **RUNNING**: Crawler is actively fetching pages
- **FINALIZING**: Deduplicating and generating outputs
- **DONE**: Completed successfully, downloads available
- **FAILED**: Unrecoverable error occurred
- **CANCELLED**: User-requested cancellation, partial results saved
- **EXPIRED**: Job deleted after 24 hours

### Crawler Selection Strategy

```
┌─────────────────────┐
│  Job Submitted      │
└──────────┬──────────┘
           │
           ▼
    ┌──────────────┐
    │  Check URL   │
    └──────┬───────┘
           │
           ├─→ use_js flag set? ──→ Use Playwright
           │
           ├─→ Known JS-heavy domain? ──→ Use Playwright
           │
           └─→ Otherwise ──→ Try Scrapy first
                              │
                              ├─→ Success? ──→ Done
                              │
                              └─→ Blocking detected?
                                  │
                                  └─→ Fallback to Playwright
```

**JS-Heavy Domain Detection:**
- Pattern matching (e.g., `*.gitbook.io`, `*.zendesk.com`)
- Explicit domain list (`help-center.talenta.co`)
- Manual override via `use_js` parameter

**Fallback Triggers:**
- Zero pages fetched (likely JS-required)
- Site status = BLOCKED (429/403/CAPTCHA)
- High duplicate content ratio (login walls)

### Content Quality Scoring

Each page is scored based on:
- **Text length** (min 200 chars for success)
- **Link density** (text vs links ratio)
- **Text density** (content vs HTML ratio)

**Score Thresholds:**
- `≥ 0.6`: Quality content (exported)
- `0.3-0.6`: Marginal (try alternate extraction)
- `< 0.3`: Low quality (not exported, but still crawled for links)

**Quality Reasons:**
```
text_too_short:101<200
high_link_density:0.95
low_text_density:0.001
```

### Deduplication Strategy

**Two-level deduplication:**

1. **URL Canonicalization**: Normalize URLs before crawling
   - Remove query parameters (except whitelisted)
   - Normalize trailing slashes
   - Lowercase hostnames

2. **Content Hash Deduplication**: After extraction
   - SHA-256 hash of extracted text
   - Multiple URLs with same content → single document
   - Aliases tracked for reference

### Blocking Detection

**Signals Monitored:**
- **HTTP Status Codes**: 429 (rate limit), 403 (forbidden)
- **CAPTCHA Patterns**: Text like "verify you are human"
- **WAF Signatures**: Cloudflare challenge pages
- **Login Redirects**: Repeated redirects to `/login`
- **Duplicate Content**: >50% identical content hashes

**Actions:**
- Log blocking evidence
- Update site status (BLOCKED/THROTTLED/LOGIN_REQUIRED)
- Trigger Playwright fallback (if not already using)

### Heartbeat & Monitoring

**Worker Heartbeat:**
- Updates every 15 seconds
- Tracks pages fetched
- Detects cancellation requests

**Stuck Job Detection:**
- **Orphaned**: Running but no heartbeat for 120s → Restart (max 2 times)
- **Stalled**: No progress for 300s → Restart (max 2 times)
- **Hard-stalled**: 0 pages for 180s → Fail immediately

### Finalization Process

1. **Read raw output**: `pages.raw.jsonl`
2. **Deduplicate**: Remove duplicate content hashes
3. **Write final output**: `pages.jsonl`
4. **Generate summary**: `summary.json` with statistics
5. **Create knowledge base**: Markdown files in `kb/` directory
6. **Register artifacts**: Track downloadable files
7. **Update job state**: DONE or CANCELLED (with export counts)

### Cancellation Handling

When user clicks "Cancel Job":

1. Job state updated to CANCELLED in database
2. Heartbeat thread detects cancellation (within 15s)
3. Crawler subprocess continues until natural completion
4. Worker checks state after crawler exits
5. If CANCELLED: Runs finalization with partial results
6. Downloads become available immediately

**Key Design Decision:** We don't forcefully kill the crawler subprocess to avoid:
- Corrupted output files
- Incomplete page writes
- Resource leaks (browser processes)

---

## Known Limitations

### 1. Fragment URL Handling

**Issue:** URLs with fragment identifiers (e.g., `#article`, `#section`, `#page`) break navigation.

**Why:** 
- Fragments are client-side routing in SPAs
- Crawlers normalize `#page1` and `#page2` to the same URL
- HTTP requests ignore fragments (never sent to server)
- Results in only 1 page crawled

**Solution:**
- Remove fragments from start URL
- Use category/section URLs instead
- Start from specific article URLs
- UI warning box automatically detects and guides users

**Example:**
```
❌ https://site.com/#article
❌ https://site.com/#section/123
❌ https://site.com/docs#getting-started
✅ https://site.com/
✅ https://site.com/categories
✅ https://site.com/articles/123-title
```

### 2. Cloudflare & Anti-Bot Protection

**Issue:** Sites with aggressive bot protection may block crawlers.

**Impact:**
- 403/429 errors
- Challenge pages requiring human interaction
- JavaScript-based fingerprinting

**Mitigation:**
- Playwright bypasses most challenges automatically
- Custom User-Agent string
- Respect robots.txt
- No guarantee of bypass for all sites

### 3. Rate Limiting

**Issue:** High concurrent requests (128) may trigger rate limits.

**Symptoms:**
- Excessive 429 responses
- IP bans (temporary or permanent)
- Degraded site performance

**Recommendations:**
- Reduce CRAWLER_CONCURRENT_REQUESTS for sensitive sites
- Increase CRAWLER_DOWNLOAD_DELAY
- Use during off-peak hours
- Respect site's crawl-delay in robots.txt

### 4. JavaScript Execution Performance

**Issue:** Playwright is significantly slower than Scrapy.

**Numbers:**
- Scrapy: ~100-200 pages/minute (128 concurrent)
- Playwright: ~20-40 pages/minute (sequential with 2s render wait)

**Trade-off:**
- Use Scrapy for traditional HTML sites (fast)
- Use Playwright only for JS-required sites (accurate)

### 5. Memory Usage

**Issue:** Large crawls consume significant memory.

**Factors:**
- Frontier (URL queue) in memory
- Content hashing requires loading full text
- Playwright browser instances (200-500MB each)

**Typical Usage:**
- 1000 pages: ~500MB-1GB RAM
- Consider pagination for larger crawls

### 6. Authentication & Cookies

**Issue:** Sites requiring login cannot be crawled.

**Why:**
- No session management implemented
- No cookie persistence
- No authentication flow

**Workaround:**
- Only crawl public documentation
- Consider manual session injection (not supported)

### 7. Dynamic Content Loading

**Issue:** Infinite scroll and lazy loading may not be fully captured.

**Impact:**
- Some content may not be discovered
- Playwright waits 2s for render, but not for all async loads

**Recommendation:**
- Start from sitemap or index pages
- Use category listings instead of homepage

### 8. Concurrent Job Execution

**Issue:** Only one job runs at a time (single worker process).

**Why:**
- Simple architecture for reliability
- Resource constraints (memory, CPU, browser instances)

**Scaling:**
- Run multiple worker processes manually
- Each polls independently
- No coordination required (job state in DB)

### 9. Output File Size

**Issue:** Large crawls generate large JSONL files.

**Numbers:**
- ~10KB per page (text + metadata)
- 1000 pages = ~10MB JSONL file

**Storage:**
- Local filesystem only
- No compression implemented
- Files expire after 24 hours

### 10. Depth-based Crawling Only

**Issue:** No URL pattern-based include/exclude rules.

**Current:**
- Crawls by depth (BFS traversal)
- Only `ignore_path_prefixes` for filtering

**Missing Features:**
- Regex-based URL filtering
- Sitemap.xml parsing
- Selective subdomain crawling

---

## Configuration

### Environment Variables

```bash
# API Server
API_HOST=0.0.0.0
API_PORT=8080

# Paths
DATABASE_PATH=data/crawler.db
JOBS_OUTPUT_DIR=out/jobs

# Job Limits
MAX_PAGES_LIMIT=1000
DEFAULT_MAX_PAGES=100
MIN_PAGES_LIMIT=1

# Crawler Performance
CRAWLER_CONCURRENT_REQUESTS=128
CRAWLER_DOWNLOAD_DELAY=0.02  # seconds
CRAWLER_DEPTH_LIMIT=20
CRAWLER_USER_AGENT=SkrappBot/1.0 (docs crawler)

# Worker Behavior
WORKER_POLL_INTERVAL_SECONDS=1
HEARTBEAT_INTERVAL_SECONDS=15

# Timeouts
ORPHANED_THRESHOLD_SECONDS=120
STALLED_THRESHOLD_SECONDS=300
HARD_STALLED_THRESHOLD_SECONDS=180

# Content Quality
MIN_TEXT_LENGTH_SUCCESS=200
MIN_TEXT_LENGTH_MARGINAL=50

# Job Expiry
JOB_EXPIRY_HOURS=24
```

### Performance Tuning

**For Speed (Aggressive):**
```python
CRAWLER_CONCURRENT_REQUESTS = 128
CRAWLER_DOWNLOAD_DELAY = 0.02
```

**For Politeness (Conservative):**
```python
CRAWLER_CONCURRENT_REQUESTS = 32
CRAWLER_DOWNLOAD_DELAY = 0.5
```

**For Reliability (Balanced):**
```python
CRAWLER_CONCURRENT_REQUESTS = 64
CRAWLER_DOWNLOAD_DELAY = 0.1
```

### Adding JS-Heavy Domains

Edit `config/js_domains.py`:

```python
JS_DOMAIN_PATTERNS = [
    '*.gitbook.io',
    '*.zendesk.com',
    'help-center.talenta.co',  # Add specific domains
]
```

### Custom Ignore Patterns

**Per-Job (UI):**
```
/search, /tag, /login, /api
```

**Global (Code):**
Edit `config/settings.py`:
```python
EXCLUDED_EXTENSIONS = [
    '.pdf', '.zip', '.jpg', '.png', '.gif', '.svg',
    '.css', '.js', '.xml', '.json'
]
```

---

## Deployment

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run API server
PORT=8080 python3 run_api.py

# Run worker (separate terminal)
PORT=8080 python3 run_worker.py
```

### Production Considerations

**Not Production-Ready:**
- Flask development server (use Gunicorn/uWSGI)
- No HTTPS/SSL
- No database backups
- No monitoring/alerting
- Single server deployment only

**For Production:**
1. Use production WSGI server
2. Add reverse proxy (Nginx)
3. Implement proper logging (ELK stack)
4. Add monitoring (Prometheus/Grafana)
5. Database migration system
6. Distributed worker pool
7. S3 or object storage for outputs
8. Rate limiting at proxy level

---

## Troubleshooting

### Job Stuck in QUEUED
- Check worker process is running
- Check worker logs for errors
- Verify database permissions

### Only 1 Page Crawled
- Check for fragment URLs (#)
- Verify site isn't blocking requests
- Check crawler logs for errors
- Try enabling JavaScript rendering

### High Error Rate (429/403)
- Reduce concurrent requests
- Increase download delay
- Site may have bot protection
- Check if IP is banned

### Playwright Timeout
- Site may require longer render wait
- Cloudflare challenge failed
- Network connectivity issues

### Download Shows "Not Found"
- Job not finalized yet (wait for DONE state)
- Check file exists: `out/jobs/{job_id}/pages.jsonl`
- Job may have expired (24 hours)

---

## Future Enhancements

**Planned:**
- [ ] Sitemap.xml parsing
- [ ] Regex-based URL filtering
- [ ] Distributed worker pool
- [ ] S3/cloud storage integration
- [ ] Webhook notifications
- [ ] API key authentication
- [ ] Job scheduling/recurring crawls
- [ ] Browser cache persistence for Playwright
- [ ] Incremental crawling (delta updates)
- [ ] Export to multiple formats (CSV, Excel, Markdown)

**Under Consideration:**
- [ ] Headless Chrome pool for parallel Playwright
- [ ] Machine learning for content quality
- [ ] Automatic site structure detection
- [ ] Screenshot capture for pages
- [ ] RSS/Atom feed monitoring
- [ ] Change detection and alerts

---

**Version:** 1.0.0  
**Last Updated:** January 15, 2026  
**License:** MIT (or specify your license)
