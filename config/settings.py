"""Global settings for the crawler application."""
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(BASE_DIR, "data"))
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", os.path.join(BASE_DIR, "out"))

DATABASE_PATH = os.path.join(DATA_DIR, "crawler.db")
JOBS_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "jobs")
WEB_STATIC_DIR = os.path.join(BASE_DIR, "web")

# API settings
API_HOST = "0.0.0.0"
API_PORT = int(os.environ.get("PORT", 5000))

# Worker settings
WORKER_POLL_INTERVAL_SECONDS = 1
HEARTBEAT_INTERVAL_SECONDS = 15
WORKER_CONCURRENCY = int(os.environ.get("WORKER_CONCURRENCY", "3"))
PAGE_LEASE_SECONDS = int(os.environ.get("PAGE_LEASE_SECONDS", "180"))

# Stuck detection thresholds
ORPHANED_THRESHOLD_SECONDS = 120
STALLED_THRESHOLD_SECONDS = 300
HARD_STALLED_THRESHOLD_SECONDS = 900

# Rate limiting
CONCURRENT_JOBS_PER_IP = 5

# Job defaults and limits
DEFAULT_MAX_PAGES = 100
MAX_PAGES_LIMIT = 1000
MIN_PAGES_LIMIT = 1

DEFAULT_MAX_DEPTH = 2
MAX_DEPTH_LIMIT = 10
MIN_DEPTH_LIMIT = 0

DEFAULT_TIMEOUT_SECONDS = 1800
MAX_TIMEOUT_SECONDS = 1800
MIN_TIMEOUT_SECONDS = 60

MAX_OUTPUT_BYTES = 100 * 1024 * 1024  # 100MB

# Job retention
JOB_EXPIRY_HOURS = 24

# Token settings
TOKEN_LENGTH_BYTES = 32

# Crawler settings
CRAWLER_CONCURRENT_REQUESTS = 128
CRAWLER_DOWNLOAD_DELAY = 0.02
CRAWLER_DEPTH_LIMIT = 20
CRAWLER_USER_AGENT = "SkrappBot/1.0 (docs crawler)"
PLAYWRIGHT_DISCOVERY_WAIT_MS = int(os.environ.get("PLAYWRIGHT_DISCOVERY_WAIT_MS", "2000"))
PLAYWRIGHT_PAGE_TIMEOUT_MS = int(os.environ.get("PLAYWRIGHT_PAGE_TIMEOUT_MS", "45000"))

# Crawl4AI extraction
CRAWL4AI_PAGE_TIMEOUT_MS = int(os.environ.get("CRAWL4AI_PAGE_TIMEOUT_MS", "45000"))
CRAWL4AI_WAIT_UNTIL = os.environ.get("CRAWL4AI_WAIT_UNTIL", "domcontentloaded")
CRAWL4AI_DELAY_BEFORE_RETURN_HTML_SECONDS = float(
    os.environ.get("CRAWL4AI_DELAY_BEFORE_RETURN_HTML_SECONDS", "1.0")
)
CRAWL4AI_PRUNING_THRESHOLD = float(os.environ.get("CRAWL4AI_PRUNING_THRESHOLD", "0.48"))
CRAWL4AI_MIN_WORD_THRESHOLD = int(os.environ.get("CRAWL4AI_MIN_WORD_THRESHOLD", "8"))
CRAWL4AI_EXCLUDED_TAGS = [
    tag.strip()
    for tag in os.environ.get("CRAWL4AI_EXCLUDED_TAGS", "nav,footer,aside,form").split(",")
    if tag.strip()
]

# Blocking detection thresholds
BLOCKING_429_THRESHOLD = 0.20  # 20% of responses
BLOCKING_403_THRESHOLD = 0.30  # 30% of responses
DUPLICATE_HASH_THRESHOLD = 0.50  # 50% duplicate content

# Text extraction
MIN_TEXT_LENGTH_SUCCESS = 200

# Excluded file extensions
EXCLUDED_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.webp', '.bmp',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.zip', '.tar', '.gz', '.rar', '.7z',
    '.css', '.js', '.json', '.xml',
    '.woff', '.woff2', '.ttf', '.eot', '.otf',
    '.mp3', '.mp4', '.avi', '.mov', '.wmv', '.webm',
    '.exe', '.dmg', '.pkg', '.deb', '.rpm',
}
