"""Validation helpers for the MVP API."""
from __future__ import annotations

import ipaddress
import re
import secrets
from urllib.parse import urlparse


def generate_job_id() -> str:
    """Generate a unique job ID."""
    return f"job_{secrets.token_hex(16)}"


def validate_url(url: str) -> tuple[bool, str | None, str | None]:
    """Validate a crawlable URL."""
    if not url:
        return False, "URL is required", None

    url = url.strip()
    if not url.startswith(("http://", "https://")):
        return False, "URL must start with http:// or https://", None

    try:
        parsed = urlparse(url)
    except (ValueError, TypeError) as e:
        return False, f"Invalid URL format: {e}", None

    if not parsed.scheme or not parsed.netloc:
        return False, "Invalid URL format", None

    hostname = parsed.hostname
    if not hostname:
        return False, "Could not extract hostname from URL", None

    hostname = hostname.lower()
    if hostname in ("localhost", "127.0.0.1", "0.0.0.0", "::1"):
        return False, "Cannot crawl localhost", None

    try:
        ip = ipaddress.ip_address(hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return False, "Cannot crawl private or reserved IP addresses", None
    except ValueError:
        pass

    if not re.match(r"^[a-z0-9]([a-z0-9\-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9\-]*[a-z0-9])?)*$", hostname):
        return False, "Invalid hostname format", None

    return True, None, hostname


def validate_max_pages(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Validate and clamp max_pages."""
    return _validate_clamped_int(value, default, min_val, max_val)


def validate_max_depth(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Validate and clamp max_depth."""
    return _validate_clamped_int(value, default, min_val, max_val)


def validate_timeout(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Validate and clamp timeout_seconds."""
    return _validate_clamped_int(value, default, min_val, max_val)


def validate_ignore_prefixes(prefixes: list | None) -> list[str]:
    """Normalize ignore path prefixes."""
    if not prefixes or not isinstance(prefixes, list):
        return []

    result = []
    for prefix in prefixes:
        if not isinstance(prefix, str):
            continue
        normalized = validate_path_prefix(prefix)
        if normalized:
            result.append(normalized)
    return result


def validate_path_prefix(prefix: str | None) -> str | None:
    """Normalize an allowed or ignored path prefix."""
    if prefix is None:
        return None
    if not isinstance(prefix, str):
        return None

    prefix = prefix.strip()
    if not prefix:
        return None
    if not prefix.startswith("/"):
        prefix = "/" + prefix
    if len(prefix) > 1 and prefix.endswith("/"):
        prefix = prefix.rstrip("/")
    return prefix


def _validate_clamped_int(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Shared int clamp helper."""
    if value is None:
        return default
    try:
        value = int(value)
    except (ValueError, TypeError):
        return default
    return max(min_val, min(value, max_val))
