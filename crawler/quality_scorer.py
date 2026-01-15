"""Content quality scoring and gating."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class QualityScore:
    """Quality assessment result for extracted content."""
    score: float  # 0.0 to 1.0
    passed: bool
    reasons: List[str]
    metrics: dict


# Boilerplate phrases to detect low-quality content
BOILERPLATE_PHRASES = [
    # Loading/placeholder
    r'page is loading',
    r'please wait',
    r'loading\.\.\.',
    r'halaman ini sedang dimuat',
    r'enable javascript',
    r'javascript is required',
    r'please enable cookies',
    
    # Navigation chrome
    r'^search$',
    r'^menu$',
    r'^navigation$',
    r'^skip to (main )?content',
    r'^back to top',
    r'^table of contents',
    
    # Social/share
    r'share this (article|page)',
    r'share on (facebook|twitter|linkedin)',
    r'follow us on',
    r'subscribe to our',
    
    # Cookie/privacy
    r'we use cookies',
    r'cookie (policy|settings|preferences)',
    r'accept (all )?cookies',
    r'privacy (policy|notice)',
    
    # Generic footer
    r'all rights reserved',
    r'terms (of service|and conditions)',
    r'contact us',
    r'powered by',
]

# Compiled patterns for efficiency
_BOILERPLATE_PATTERNS = [re.compile(p, re.IGNORECASE) for p in BOILERPLATE_PHRASES]


def count_boilerplate_matches(text: str) -> int:
    """Count how many boilerplate phrases appear in text."""
    count = 0
    text_lower = text.lower()
    for pattern in _BOILERPLATE_PATTERNS:
        if pattern.search(text_lower):
            count += 1
    return count


def calculate_link_density(text: str, html: str) -> float:
    """
    Calculate the ratio of link text to total text.
    High link density indicates navigation/menu content.
    """
    if not text or len(text) < 10:
        return 1.0
    
    # Count links in HTML
    link_count = len(re.findall(r'<a\s', html, re.IGNORECASE)) if html else 0
    
    # Estimate link text (rough heuristic)
    # Average link text ~20 chars
    estimated_link_chars = link_count * 20
    
    return min(1.0, estimated_link_chars / len(text))


def calculate_text_density(text: str, html: str) -> float:
    """
    Calculate text to HTML ratio.
    Very low ratio indicates mostly markup/scripts.
    """
    if not html or len(html) < 10:
        return 0.0
    
    text_len = len(text) if text else 0
    html_len = len(html)
    
    return min(1.0, text_len / html_len)


def detect_duplicate_lines(text: str) -> Tuple[int, int]:
    """
    Detect duplicate consecutive lines (common in bad extractions).
    Returns (duplicate_count, total_lines).
    """
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if len(lines) < 2:
        return 0, len(lines)
    
    duplicates = 0
    prev_line = None
    for line in lines:
        if line == prev_line and len(line) > 10:
            duplicates += 1
        prev_line = line
    
    return duplicates, len(lines)


def score_content(
    text: str,
    html: str = '',
    title: str = '',
    min_chars: int = 200,
    max_link_density: float = 0.5,
    max_boilerplate_ratio: float = 0.3,
) -> QualityScore:
    """
    Score content quality on a 0-1 scale.
    
    Factors:
    - Text length (min threshold)
    - Boilerplate phrase density
    - Link density
    - Duplicate line ratio
    - Text/HTML ratio
    
    Returns QualityScore with pass/fail and detailed metrics.
    """
    reasons = []
    metrics = {}
    
    # Base score starts at 1.0
    score = 1.0
    
    # 1. Text length check
    text_len = len(text) if text else 0
    metrics['text_length'] = text_len
    
    if text_len < min_chars:
        score -= 0.4
        reasons.append(f'text_too_short:{text_len}<{min_chars}')
    elif text_len < min_chars * 2:
        score -= 0.1
    
    # 2. Boilerplate detection
    if text:
        boilerplate_count = count_boilerplate_matches(text)
        # Normalize by text length (per 500 chars)
        boilerplate_density = boilerplate_count / max(1, text_len / 500)
        metrics['boilerplate_count'] = boilerplate_count
        metrics['boilerplate_density'] = round(boilerplate_density, 3)
        
        if boilerplate_density > max_boilerplate_ratio:
            score -= 0.3
            reasons.append(f'high_boilerplate:{boilerplate_density:.2f}')
        elif boilerplate_density > max_boilerplate_ratio * 0.5:
            score -= 0.1
    
    # 3. Link density check
    if html:
        link_density = calculate_link_density(text or '', html)
        metrics['link_density'] = round(link_density, 3)
        
        if link_density > max_link_density:
            score -= 0.3
            reasons.append(f'high_link_density:{link_density:.2f}')
        elif link_density > max_link_density * 0.7:
            score -= 0.1
    
    # 4. Duplicate line detection
    if text:
        dup_count, total_lines = detect_duplicate_lines(text)
        dup_ratio = dup_count / max(1, total_lines)
        metrics['duplicate_lines'] = dup_count
        metrics['duplicate_ratio'] = round(dup_ratio, 3)
        
        if dup_ratio > 0.2:
            score -= 0.2
            reasons.append(f'duplicate_lines:{dup_count}/{total_lines}')
    
    # 5. Text/HTML ratio
    if html:
        text_density = calculate_text_density(text or '', html)
        metrics['text_density'] = round(text_density, 3)
        
        if text_density < 0.05:
            score -= 0.2
            reasons.append(f'low_text_density:{text_density:.3f}')
    
    # 6. Title presence
    if not title or len(title.strip()) < 3:
        score -= 0.1
        reasons.append('missing_title')
    
    # Clamp score
    score = max(0.0, min(1.0, score))
    
    # Pass threshold
    passed = score >= 0.5 and text_len >= min_chars
    
    if not passed and not reasons:
        reasons.append('score_below_threshold')
    
    return QualityScore(
        score=round(score, 3),
        passed=passed,
        reasons=reasons,
        metrics=metrics
    )


def should_retry_extraction(quality: QualityScore) -> bool:
    """
    Determine if we should retry with a different extraction method.
    """
    # Retry if score is marginal (0.3-0.5) or specific issues detected
    if 0.3 <= quality.score < 0.5:
        return True
    
    if 'text_too_short' in str(quality.reasons):
        return True
    
    if 'high_boilerplate' in str(quality.reasons):
        return True
    
    return False
