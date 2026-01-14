"""Readability text extractor."""
from __future__ import annotations

from readability import Document
from bs4 import BeautifulSoup


def extract(html: str) -> str | None:
    """
    Extract text content from HTML using Readability.
    
    Returns:
        Extracted text or None if extraction fails
    """
    if not html:
        return None
    
    try:
        doc = Document(html)
        summary_html = doc.summary()
        
        if not summary_html:
            return None
        
        soup = BeautifulSoup(summary_html, 'lxml')
        
        text = soup.get_text(separator=' ', strip=True)
        
        if text and text.strip():
            return text.strip()
        
        return None
    except Exception:
        return None


def get_title(html: str) -> str | None:
    """
    Extract the title from HTML using Readability.
    
    Returns:
        Title string or None if extraction fails
    """
    if not html:
        return None
    
    try:
        doc = Document(html)
        title = doc.title()
        
        if title and title.strip():
            return title.strip()
        
        return None
    except Exception:
        return None
