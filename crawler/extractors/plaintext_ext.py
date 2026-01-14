"""Plain text fallback extractor."""
from __future__ import annotations

import re
from bs4 import BeautifulSoup


def extract(html: str) -> str | None:
    """
    Extract text content from HTML by stripping all tags.
    This is the last-resort fallback extractor.
    
    Returns:
        Extracted text or None if extraction fails
    """
    if not html:
        return None
    
    try:
        soup = BeautifulSoup(html, 'lxml')
        
        for tag in soup(['script', 'style', 'noscript', 'header', 'footer', 'nav', 'aside']):
            tag.decompose()
        
        text = soup.get_text(separator=' ', strip=True)
        
        text = re.sub(r'\s+', ' ', text)
        
        if text and text.strip():
            return text.strip()
        
        return None
    except Exception:
        return None


def get_title(html: str) -> str | None:
    """
    Extract the title from HTML.
    
    Returns:
        Title string or None if extraction fails
    """
    if not html:
        return None
    
    try:
        soup = BeautifulSoup(html, 'lxml')
        
        title_tag = soup.find('title')
        if title_tag and title_tag.string:
            return title_tag.string.strip()
        
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.get_text(strip=True)
        
        return None
    except Exception:
        return None
