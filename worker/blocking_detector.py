"""Blocking detection - analyzes crawl results for site blocking."""
import json
import logging

from config import settings
from config.constants import SiteStatus, BlockingSignal, EventLevel, EventType
from db import queries


logger = logging.getLogger(__name__)


def analyze_blocking_signals(job_id: str, tracker_evidence: dict) -> tuple[str, dict]:
    """
    Analyze blocking signals and determine site status.
    
    Args:
        job_id: The job ID
        tracker_evidence: Evidence from the BlockingSignalTracker
    
    Returns:
        (site_status, evidence_summary)
    """
    total_responses = tracker_evidence.get('total_responses', 0)
    status_codes = tracker_evidence.get('status_codes', {})
    captcha_hits = tracker_evidence.get('captcha_hits', 0)
    waf_hits = tracker_evidence.get('waf_hits', 0)
    login_redirects = tracker_evidence.get('login_redirects', 0)
    duplicate_ratio = tracker_evidence.get('duplicate_ratio', 0)
    
    if total_responses == 0:
        return SiteStatus.UNKNOWN, {}
    
    rate_429 = status_codes.get(429, 0) / total_responses
    rate_403 = status_codes.get(403, 0) / total_responses
    
    signals_detected = []
    
    if captcha_hits > 0 or waf_hits > 0:
        site_status = SiteStatus.BLOCKED
        signals_detected.append(BlockingSignal.CAPTCHA)
        
        queries.insert_job_event(job_id, EventLevel.WARN, EventType.BLOCKED_DETECTED, {
            "signal": BlockingSignal.CAPTCHA,
            "captcha_hits": captcha_hits,
            "waf_hits": waf_hits
        })
        
        logger.warning(f"Job {job_id}: Captcha/WAF detected ({captcha_hits} captcha, {waf_hits} WAF)")
    
    elif login_redirects > total_responses * 0.5:
        site_status = SiteStatus.LOGIN_REQUIRED
        signals_detected.append(BlockingSignal.LOGIN_REDIRECT)
        
        queries.insert_job_event(job_id, EventLevel.WARN, EventType.BLOCKED_DETECTED, {
            "signal": BlockingSignal.LOGIN_REDIRECT,
            "login_redirects": login_redirects
        })
        
        logger.warning(f"Job {job_id}: Login required detected ({login_redirects} redirects)")
    
    elif rate_429 >= settings.BLOCKING_429_THRESHOLD:
        site_status = SiteStatus.THROTTLED
        signals_detected.append(BlockingSignal.EXCESSIVE_429)
        
        queries.insert_job_event(job_id, EventLevel.WARN, EventType.BLOCKED_DETECTED, {
            "signal": BlockingSignal.EXCESSIVE_429,
            "rate": round(rate_429, 3)
        })
        
        logger.warning(f"Job {job_id}: Rate limiting detected ({rate_429:.1%} 429s)")
    
    elif rate_403 >= settings.BLOCKING_403_THRESHOLD:
        site_status = SiteStatus.BLOCKED
        signals_detected.append(BlockingSignal.EXCESSIVE_403)
        
        queries.insert_job_event(job_id, EventLevel.WARN, EventType.BLOCKED_DETECTED, {
            "signal": BlockingSignal.EXCESSIVE_403,
            "rate": round(rate_403, 3)
        })
        
        logger.warning(f"Job {job_id}: Access denied detected ({rate_403:.1%} 403s)")
    
    elif duplicate_ratio >= settings.DUPLICATE_HASH_THRESHOLD:
        site_status = SiteStatus.BLOCKED
        signals_detected.append(BlockingSignal.DUPLICATE_CONTENT)
        
        queries.insert_job_event(job_id, EventLevel.WARN, EventType.BLOCKED_DETECTED, {
            "signal": BlockingSignal.DUPLICATE_CONTENT,
            "duplicate_ratio": round(duplicate_ratio, 3)
        })
        
        logger.warning(f"Job {job_id}: High duplicate content ({duplicate_ratio:.1%})")
    
    else:
        site_status = SiteStatus.NORMAL
    
    evidence = {
        "signals_detected": signals_detected,
        "status_code_summary": {
            "total": total_responses,
            "2xx": sum(v for k, v in status_codes.items() if 200 <= int(k) < 300),
            "4xx": sum(v for k, v in status_codes.items() if 400 <= int(k) < 500),
            "5xx": sum(v for k, v in status_codes.items() if 500 <= int(k) < 600),
        },
        "captcha_hits": captcha_hits,
        "waf_hits": waf_hits,
        "login_redirects": login_redirects,
        "duplicate_ratio": round(duplicate_ratio, 3),
        "sample_urls": tracker_evidence.get('sample_urls', []),
        "signature_hits": tracker_evidence.get('signature_hits', [])
    }
    
    return site_status, evidence


def update_job_blocking_status(job_id: str, site_status: str, evidence: dict):
    """Update the job record with blocking status and evidence."""
    queries.update_job(
        job_id,
        site_status=site_status,
        block_evidence=json.dumps(evidence) if evidence else None
    )


def should_stop_crawl(site_status: str) -> bool:
    """Determine if the crawl should be stopped based on site status."""
    return site_status in (SiteStatus.BLOCKED, SiteStatus.LOGIN_REQUIRED)
