"""JS-heavy domain detection for automatic Playwright selection."""
from __future__ import annotations

import fnmatch
import re
from urllib.parse import urlparse


# Known JS-heavy domain patterns
# These sites typically require JavaScript rendering to work properly
JS_DOMAIN_PATTERNS = [
    # Help desk / Support platforms
    '*.zendesk.com',
    '*.freshdesk.com',
    '*.intercom.help',
    '*.helpscoutdocs.com',
    '*.helpjuice.com',
    '*.document360.io',
    
    # Documentation platforms (known to be JS-heavy)
    '*.gitbook.io',
    '*.readme.io',
    '*.notion.site',
    '*.slite.com',
    '*.archbee.io',
    '*.mintlify.app',
    '*.docusaurus.io',
    
    # SPA framework indicators in subdomains
    '*.vercel.app',
    '*.netlify.app',
    '*.pages.dev',
    
    # Specific help centers that require JS
    'help-center.talenta.co',
]

# URL path patterns that indicate JS-heavy content
JS_PATH_PATTERNS = [
    # Removed overly aggressive patterns
    # Only add specific known problematic paths here
]


def _matches_pattern(hostname: str, pattern: str) -> bool:
    """Check if hostname matches a glob-style pattern."""
    # Convert glob pattern to regex
    # *.example.com should match sub.example.com but not example.com
    if pattern.startswith('*.'):
        # Match any subdomain
        base = pattern[2:]
        return hostname.endswith('.' + base) or hostname == base
    elif pattern.endswith('.*'):
        # Match any TLD
        base = pattern[:-2]
        return hostname.startswith(base + '.') or hostname == base
    elif '*' in pattern:
        # General glob matching
        return fnmatch.fnmatch(hostname, pattern)
    else:
        # Exact match
        return hostname == pattern


def is_js_heavy_domain(url: str) -> bool:
    """
    Check if a URL is from a known JS-heavy domain.
    
    Args:
        url: The URL to check
        
    Returns:
        True if the domain is known to require JavaScript rendering
    """
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        if not hostname:
            return False
        
        hostname = hostname.lower()
        
        # Check domain patterns
        for pattern in JS_DOMAIN_PATTERNS:
            if _matches_pattern(hostname, pattern):
                return True
        
        # Check path patterns (some sites use specific paths for JS content)
        path = parsed.path.lower()
        for path_pattern in JS_PATH_PATTERNS:
            if path_pattern in path:
                # Only trigger for specific known problematic hosts
                # to avoid false positives on static sites
                if any(kw in hostname for kw in ['zendesk', 'help', 'support', 'docs']):
                    return True
        
        return False
        
    except Exception:
        return False


def get_detected_reason(url: str) -> str | None:
    """
    Get the reason why a URL was detected as JS-heavy.
    
    Args:
        url: The URL to check
        
    Returns:
        The matching pattern, or None if not JS-heavy
    """
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname
        if not hostname:
            return None
        
        hostname = hostname.lower()
        
        for pattern in JS_DOMAIN_PATTERNS:
            if _matches_pattern(hostname, pattern):
                return f"domain_pattern:{pattern}"
        
        path = parsed.path.lower()
        for path_pattern in JS_PATH_PATTERNS:
            if path_pattern in path:
                if any(kw in hostname for kw in ['zendesk', 'help', 'support', 'docs']):
                    return f"path_pattern:{path_pattern}"
        
        return None
        
    except Exception:
        return None
