"""Constants for the crawler application."""


class JobState:
    """Job state constants."""
    QUEUED = "queued"
    RUNNING = "running"
    FINALIZING = "finalizing"
    DONE = "done"
    FAILED = "failed"
    EXPIRED = "expired"

    ALL = {QUEUED, RUNNING, FINALIZING, DONE, FAILED, EXPIRED}
    TERMINAL = {DONE, FAILED, EXPIRED}
    ACTIVE = {QUEUED, RUNNING, FINALIZING}


class ErrorReason:
    """Error reason constants."""
    ORPHANED = "orphaned"
    STALLED = "stalled"
    HARD_STALLED = "hard_stalled"
    RATE_LIMITED = "rate_limited"
    BLOCKED = "blocked"
    CAPTCHA_DETECTED = "captcha_detected"
    LOGIN_REQUIRED = "login_required"
    ROBOTS_DENIED = "robots_denied"
    DNS_FAILURE = "dns_failure"
    CONNECTION_ERROR = "connection_error"
    TIMEOUT = "timeout"
    DISK_FULL = "disk_full"
    UNKNOWN = "unknown"


class SiteStatus:
    """Site status constants for blocking detection."""
    NORMAL = "normal"
    THROTTLED = "throttled"
    BLOCKED = "blocked"
    ROBOTS_DENIED = "robots_denied"
    LOGIN_REQUIRED = "login_required"
    UNKNOWN = "unknown"


class BlockingSignal:
    """Blocking signal type constants."""
    EXCESSIVE_429 = "excessive_429"
    EXCESSIVE_403 = "excessive_403"
    CAPTCHA = "captcha_detected"
    LOGIN_REDIRECT = "login_redirect"
    DUPLICATE_CONTENT = "duplicate_content_high"


class ExtractionMode:
    """Text extraction mode constants."""
    TRAFILATURA = "trafilatura"
    READABILITY = "readability"
    FALLBACK = "fallback"


class ArtifactKind:
    """Job artifact type constants."""
    PAGES_RAW_JSONL = "pages_raw_jsonl"
    PAGES_JSONL = "pages_jsonl"
    SUMMARY_JSON = "summary_json"
    RUNNER_LOG = "runner_log"
    CRAWLER_LOG = "crawler_log"


class EventLevel:
    """Job event level constants."""
    INFO = "info"
    WARN = "warn"
    ERROR = "error"


class EventType:
    """Job event type constants."""
    STATE_CHANGE = "state_change"
    RESTART = "restart"
    BLOCKED_DETECTED = "blocked_detected"
    FINALIZE = "finalize"
    ERROR = "error"
