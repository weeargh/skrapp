"""Blocking signal detection utilities."""
from __future__ import annotations

import re
from typing import Any


CAPTCHA_PATTERNS = [
    r'cf-browser-verification',
    r'cf-challenge',
    r'cloudflare',
    r'checking\s+your\s+browser',
    r'please\s+wait.*redirect',
    r'g-recaptcha',
    r'recaptcha/api',
    r'hcaptcha',
    r'challenge-platform',
    r'verify\s+you\s+are\s+(human|not\s+a\s+robot)',
    r'please\s+complete\s+the\s+security\s+check',
    r'access\s+denied',
    r'blocked\s+by.*firewall',
]

WAF_PATTERNS = [
    r'blocked\s+by\s+mod_security',
    r'web\s+application\s+firewall',
    r'request\s+blocked',
    r'sucuri',
    r'incapsula',
    r'akamai',
    r'imperva',
]

LOGIN_REDIRECT_PATTERNS = [
    r'/login',
    r'/signin',
    r'/sign-in',
    r'/auth',
    r'/authenticate',
    r'/sso',
    r'/oauth',
    r'/account/login',
    r'/user/login',
]


def detect_captcha(html: str) -> tuple[bool, list[str]]:
    """
    Detect if the HTML contains captcha indicators.
    
    Returns:
        (is_captcha, matched_patterns)
    """
    if not html:
        return False, []
    
    html_lower = html.lower()
    matched = []
    
    for pattern in CAPTCHA_PATTERNS:
        if re.search(pattern, html_lower):
            matched.append(pattern)
    
    return len(matched) > 0, matched


def detect_waf(html: str) -> tuple[bool, list[str]]:
    """
    Detect if the HTML indicates a WAF block.
    
    Returns:
        (is_blocked, matched_patterns)
    """
    if not html:
        return False, []
    
    html_lower = html.lower()
    matched = []
    
    for pattern in WAF_PATTERNS:
        if re.search(pattern, html_lower):
            matched.append(pattern)
    
    return len(matched) > 0, matched


def detect_login_redirect(url: str | None = None, location_header: str | None = None) -> bool:
    """
    Detect if a URL or Location header indicates a login redirect.
    """
    check_url = location_header or url
    if not check_url:
        return False
    
    check_url_lower = check_url.lower()
    
    for pattern in LOGIN_REDIRECT_PATTERNS:
        if pattern in check_url_lower:
            return True
    
    return False


def detect_meta_refresh_login(html: str) -> bool:
    """
    Detect if HTML contains a meta refresh to a login page.
    """
    if not html:
        return False
    
    meta_refresh = re.search(
        r'<meta[^>]+http-equiv=["\']?refresh["\']?[^>]+content=["\']?\d+;\s*url=([^"\'>\s]+)',
        html,
        re.IGNORECASE
    )
    
    if meta_refresh:
        redirect_url = meta_refresh.group(1)
        return detect_login_redirect(url=redirect_url)
    
    return False


class BlockingSignalTracker:
    """Track blocking signals during a crawl."""
    
    def __init__(self):
        self.status_codes: dict[int, int] = {}
        self.total_responses = 0
        self.captcha_hits = 0
        self.waf_hits = 0
        self.login_redirects = 0
        self.text_hashes: dict[str, int] = {}
        self.sample_urls: list[str] = []
        self.signature_hits: list[str] = []
    
    def record_response(
        self,
        url: str,
        status_code: int,
        html: str | None = None,
        location_header: str | None = None,
        text_hash: str | None = None
    ):
        """Record a response and check for blocking signals."""
        self.total_responses += 1
        
        self.status_codes[status_code] = self.status_codes.get(status_code, 0) + 1
        
        if html:
            is_captcha, patterns = detect_captcha(html)
            if is_captcha:
                self.captcha_hits += 1
                self.signature_hits.extend(patterns)
                if len(self.sample_urls) < 5:
                    self.sample_urls.append(url)
            
            is_waf, patterns = detect_waf(html)
            if is_waf:
                self.waf_hits += 1
                self.signature_hits.extend(patterns)
            
            if detect_meta_refresh_login(html):
                self.login_redirects += 1
        
        if location_header and detect_login_redirect(location_header=location_header):
            self.login_redirects += 1
            if len(self.sample_urls) < 5:
                self.sample_urls.append(url)
        
        if text_hash:
            self.text_hashes[text_hash] = self.text_hashes.get(text_hash, 0) + 1
    
    def get_status_code_ratio(self, status_code: int) -> float:
        """Get the ratio of a specific status code."""
        if self.total_responses == 0:
            return 0.0
        return self.status_codes.get(status_code, 0) / self.total_responses
    
    def get_duplicate_ratio(self) -> float:
        """Get the ratio of duplicate content (by text hash)."""
        if not self.text_hashes:
            return 0.0
        
        total = sum(self.text_hashes.values())
        unique = len(self.text_hashes)
        
        if total == 0:
            return 0.0
        
        return 1.0 - (unique / total)
    
    def get_evidence(self) -> dict[str, Any]:
        """Get evidence of blocking signals."""
        return {
            "total_responses": self.total_responses,
            "status_codes": self.status_codes,
            "captcha_hits": self.captcha_hits,
            "waf_hits": self.waf_hits,
            "login_redirects": self.login_redirects,
            "duplicate_ratio": round(self.get_duplicate_ratio(), 3),
            "sample_urls": self.sample_urls[:5],
            "signature_hits": list(set(self.signature_hits))[:10]
        }
