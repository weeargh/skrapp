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
WORKER_POLL_INTERVAL_SECONDS = 2
HEARTBEAT_INTERVAL_SECONDS = 30

# Stuck detection thresholds
ORPHANED_THRESHOLD_SECONDS = 120
STALLED_THRESHOLD_SECONDS = 300
HARD_STALLED_THRESHOLD_SECONDS = 900

# Rate limiting
CONCURRENT_JOBS_PER_IP = 5

# Job defaults and limits
DEFAULT_MAX_PAGES = 20
MAX_PAGES_LIMIT = 100
MIN_PAGES_LIMIT = 1

DEFAULT_TIMEOUT_SECONDS = 1800
MAX_TIMEOUT_SECONDS = 1800
MIN_TIMEOUT_SECONDS = 60

MAX_OUTPUT_BYTES = 100 * 1024 * 1024  # 100MB

# Job retention
JOB_EXPIRY_HOURS = 24

# Token settings
TOKEN_LENGTH_BYTES = 32

# Crawler settings
CRAWLER_CONCURRENT_REQUESTS = 32
CRAWLER_DOWNLOAD_DELAY = 0.1
CRAWLER_DEPTH_LIMIT = 20
CRAWLER_USER_AGENT = "SkrappBot/1.0 (docs crawler)"

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
