"""URL canonicalization and validation utilities."""
from __future__ import annotations

import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


# Tracking parameters to strip from URLs
TRACKING_PARAMS = {
    # Google Analytics / Ads
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'utm_id', 'utm_source_platform', 'utm_creative_format',
    'gclid', 'gclsrc', 'dclid',
    # Facebook
    'fbclid', 'fb_action_ids', 'fb_action_types', 'fb_source', 'fb_ref',
    # Other ad platforms
    'msclkid', 'twclid', 'li_fat_id', 'igshid', 'mc_cid', 'mc_eid',
    # Generic tracking
    'ref', 'ref_src', 'ref_url', 'referrer', 'source',
    '_ga', '_gl', '_hsenc', '_hsmi', 'hsCtaTracking',
    # Session/click tracking
    'sessionid', 'clickid', 'affiliate_id', 'partner_id',
    # Zendesk/helpdesk specific
    'return_to', 'locale', 'locale_id',
}

# Global deny list patterns for non-content URLs
DENY_PATH_PATTERNS = [
    # Language/locale switchers
    r'/hc/change_language',
    r'/locale/',
    r'/set_locale',
    
    # Authentication/account
    r'/login', r'/signin', r'/sign-in', r'/signup', r'/sign-up',
    r'/logout', r'/signout', r'/sign-out',
    r'/auth/', r'/oauth/', r'/sso/',
    r'/account/', r'/profile/', r'/settings/',
    r'/password/', r'/forgot-password', r'/reset-password',
    
    # Search and filters  
    r'/search[?/]', r'/filter[?/]', r'/sort[?/]',
    
    # Comments/community
    r'/comments', r'/discussions', r'/community/',
    r'/forum/', r'/topics/',
    
    # Actions/forms
    r'/subscribe', r'/unsubscribe', r'/newsletter',
    r'/feedback', r'/contact', r'/submit',
    r'/vote', r'/rate', r'/flag',
    r'/print/', r'/pdf/', r'/export/',
    
    # Tags/categories (often low-value index pages)
    r'/tags?/', r'/labels?/',
    
    # Pagination with query params handled separately
]

# External share/social links to never follow
DENY_EXTERNAL_PATTERNS = [
    r'facebook\.com/share',
    r'twitter\.com/(share|intent)',
    r'linkedin\.com/share',
    r'pinterest\.com/pin',
    r'reddit\.com/submit',
    r'wa\.me/', r'api\.whatsapp\.com',
    r'telegram\.me/', r't\.me/',
    r'mailto:',
    r'tel:',
    r'docs\.google\.com/forms',
    r'forms\.gle/',
    r'calendly\.com/',
    r'typeform\.com/',
]


def strip_tracking_params(url: str) -> str:
    """
    Remove tracking parameters from URL query string.
    Preserves meaningful query params like page IDs or article slugs.
    """
    try:
        parsed = urlparse(url)
        if not parsed.query:
            return url
        
        params = parse_qs(parsed.query, keep_blank_values=True)
        
        # Filter out tracking params
        filtered = {
            k: v for k, v in params.items()
            if k.lower() not in TRACKING_PARAMS
        }
        
        # Rebuild URL
        new_query = urlencode(filtered, doseq=True) if filtered else ''
        return urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            new_query,
            ''  # Remove fragment
        ))
    except Exception:
        return url


def canonicalize_url(url: str) -> str:
    """
    Canonicalize a URL for deduplication.
    
    - Lowercase scheme and host
    - Remove fragment
    - Strip tracking parameters
    - Normalize path (collapse //, remove trailing slash except root)
    """
    try:
        # First strip tracking params
        url = strip_tracking_params(url)
        
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
    
    # Keep non-tracking query params for canonicalization
    query = parsed.query if parsed.query else ''
    
    canonical = urlunparse((scheme, netloc, path, '', query, ''))
    
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


def matches_deny_pattern(url: str) -> bool:
    """
    Check if URL matches global deny patterns (non-content pages).
    """
    try:
        path = get_path(url).lower()
        full_url = url.lower()
        
        # Check path patterns
        for pattern in DENY_PATH_PATTERNS:
            if re.search(pattern, path, re.IGNORECASE):
                return True
        
        # Check external share patterns
        for pattern in DENY_EXTERNAL_PATTERNS:
            if re.search(pattern, full_url, re.IGNORECASE):
                return True
        
        return False
    except Exception:
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
    - It doesn't match global deny patterns
    """
    if not is_valid_scheme(url):
        return False
    
    if not is_same_host(url, allowed_host):
        return False
    
    if matches_ignore_prefix(url, ignore_prefixes):
        return False
    
    if has_excluded_extension(url, excluded_extensions):
        return False
    
    if matches_deny_pattern(url):
        return False
    
    return True
