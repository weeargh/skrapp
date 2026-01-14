"""Trafilatura text extractor."""
from __future__ import annotations

import trafilatura


def extract(html: str) -> str | None:
    """
    Extract text content from HTML using Trafilatura.
    
    Returns:
        Extracted text or None if extraction fails
    """
    if not html:
        return None
    
    try:
        text = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=True,
            no_fallback=True
        )
        
        if text and text.strip():
            return text.strip()
        
        return None
    except Exception:
        return None
