"""URL canonicalization and validation utilities."""
from __future__ import annotations

import re
from urllib.parse import urlparse, urlunparse


def canonicalize_url(url: str) -> str:
    """
    Canonicalize a URL for deduplication.
    
    - Lowercase scheme and host
    - Remove fragment
    - Remove query string (MVP behavior)
    - Normalize path (collapse //, remove trailing slash except root)
    """
    try:
        parsed = urlparse(url)
    except Exception:
        return url
    
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    
    if ':' in netloc:
        host, port = netloc.rsplit(':', 1)
        if (scheme == 'http' and port == '80') or (scheme == 'https' and port == '443'):
            netloc = host
    
    path = parsed.path or '/'
    
    path = re.sub(r'/+', '/', path)
    
    if path.endswith('/index.html') or path.endswith('/index.htm'):
        path = path.rsplit('/', 1)[0] + '/'
    
    if path != '/' and path.endswith('/'):
        path = path.rstrip('/')
    
    if not path:
        path = '/'
    
    canonical = urlunparse((scheme, netloc, path, '', '', ''))
    
    return canonical


def extract_hostname(url: str) -> str | None:
    """Extract the hostname from a URL."""
    try:
        parsed = urlparse(url)
        return parsed.hostname.lower() if parsed.hostname else None
    except Exception:
        return None


def is_same_host(url: str, allowed_host: str) -> bool:
    """Check if a URL belongs to the allowed host."""
    hostname = extract_hostname(url)
    if not hostname:
        return False
    return hostname == allowed_host.lower()


def is_valid_scheme(url: str) -> bool:
    """Check if a URL has a valid scheme (http or https)."""
    try:
        parsed = urlparse(url)
        return parsed.scheme.lower() in ('http', 'https')
    except Exception:
        return False


def get_path(url: str) -> str:
    """Extract the path from a URL."""
    try:
        parsed = urlparse(url)
        return parsed.path or '/'
    except Exception:
        return '/'


def has_excluded_extension(url: str, excluded_extensions: set) -> bool:
    """Check if a URL has an excluded file extension."""
    path = get_path(url).lower()
    
    for ext in excluded_extensions:
        if path.endswith(ext):
            return True
    
    return False


def matches_ignore_prefix(url: str, ignore_prefixes: list[str]) -> bool:
    """Check if a URL path matches any ignore prefix."""
    if not ignore_prefixes:
        return False
    
    path = get_path(url)
    
    for prefix in ignore_prefixes:
        if path.startswith(prefix):
            return True
    
    return False


def is_url_in_scope(
    url: str,
    allowed_host: str,
    ignore_prefixes: list[str],
    excluded_extensions: set
) -> bool:
    """
    Check if a URL is in scope for crawling.
    
    A URL is in scope if:
    - It has http/https scheme
    - Its host matches allowed_host
    - Its path doesn't match any ignore prefix
    - It doesn't have an excluded extension
    """
    if not is_valid_scheme(url):
        return False
    
    if not is_same_host(url, allowed_host):
        return False
    
    if matches_ignore_prefix(url, ignore_prefixes):
        return False
    
    if has_excluded_extension(url, excluded_extensions):
        return False
    
    return True
