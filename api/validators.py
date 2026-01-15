"""URL and token validation utilities."""
from __future__ import annotations

import hashlib
import ipaddress
import re
import secrets
from urllib.parse import urlparse


def generate_job_id() -> str:
    """Generate a unique job ID."""
    return f"job_{secrets.token_hex(16)}"


def generate_token() -> str:
    """Generate a secure token."""
    return secrets.token_hex(32)


def hash_token(token: str) -> str:
    """Hash a token for storage."""
    return hashlib.sha256(token.encode()).hexdigest()


def hash_ip(ip: str) -> str:
    """Hash an IP address for storage."""
    return hashlib.sha256(ip.encode()).hexdigest()


def validate_url(url: str) -> tuple[bool, str | None, str | None]:
    """
    Validate a URL for crawling.
    
    Returns:
        (is_valid, error_message, hostname)
    """
    if not url:
        return False, "URL is required", None
    
    url = url.strip()
    
    if not url.startswith(('http://', 'https://')):
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
    
    if hostname in ('localhost', '127.0.0.1', '0.0.0.0', '::1'):
        return False, "Cannot crawl localhost", None
    
    try:
        ip = ipaddress.ip_address(hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return False, "Cannot crawl private or reserved IP addresses", None
    except ValueError:
        pass
    
    if not re.match(r'^[a-z0-9]([a-z0-9\-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9\-]*[a-z0-9])?)*$', hostname):
        return False, "Invalid hostname format", None
    
    return True, None, hostname


def validate_token_format(token: str) -> bool:
    """Validate that a token has the expected format."""
    if not token or not isinstance(token, str):
        return False
    
    if len(token) != 64:
        return False
    
    return bool(re.match(r'^[a-f0-9]{64}$', token))


def validate_max_pages(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Validate and clamp max_pages value."""
    if value is None:
        return default
    try:
        value = int(value)
    except (ValueError, TypeError):
        return default
    return max(min_val, min(value, max_val))


def validate_timeout(value: int | None, default: int, min_val: int, max_val: int) -> int:
    """Validate and clamp timeout value."""
    if value is None:
        return default
    try:
        value = int(value)
    except (ValueError, TypeError):
        return default
    return max(min_val, min(value, max_val))


def validate_ignore_prefixes(prefixes: list | None) -> list[str]:
    """Validate and normalize ignore path prefixes."""
    if not prefixes or not isinstance(prefixes, list):
        return []
    
    result = []
    for prefix in prefixes:
        if not isinstance(prefix, str):
            continue
        prefix = prefix.strip()
        if not prefix:
            continue
        if not prefix.startswith('/'):
            prefix = '/' + prefix
        result.append(prefix)
    
    return result
