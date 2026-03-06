"""Retry logic for blocked or failed crawl jobs."""
import json
import logging
from typing import Optional

from config import settings
from config.constants import JobState, SiteStatus
from db import queries
from api.validators import generate_job_id, hash_token

logger = logging.getLogger(__name__)

# Retry configuration
MAX_RETRY_ATTEMPTS = 2  # 0=original, 1=slower, 2=playwright
RETRY_MODES = {
    1: 'slower',     # First retry: reduce speed
    2: 'playwright'  # Second retry: use browser
}

# Slower mode settings (vs normal: concurrent=128, delay=0.02)
SLOWER_CONCURRENT_REQUESTS = 16
SLOWER_DOWNLOAD_DELAY = 1.0


def should_retry_job(job: dict) -> bool:
    """
    Determine if a job should be retried based on its state and blocking status.
    
    Returns True if:
    - Job was cancelled or failed due to blocking
    - Site status is 'blocked'
    - Has not exceeded max retry attempts
    """
    if not job:
        return False
    
    # Check if job was blocked
    site_status = job.get('site_status')
    if site_status != SiteStatus.BLOCKED:
        return False
    
    # Check if already at max retries
    retry_attempt = job.get('retry_attempt', 0)
    if retry_attempt >= MAX_RETRY_ATTEMPTS:
        logger.info(f"Job {job['id']} has reached max retry attempts ({MAX_RETRY_ATTEMPTS})")
        return False
    
    # Check if job state is terminal (cancelled/failed)
    state = job.get('state')
    if state not in (JobState.CANCELLED, JobState.FAILED):
        return False
    
    # Check if we have some pages (worth retrying)
    pages_fetched = job.get('pages_fetched', 0)
    if pages_fetched < 10:
        logger.info(f"Job {job['id']} only fetched {pages_fetched} pages, not worth retrying")
        return False
    
    return True


def create_retry_job(original_job: dict) -> Optional[dict]:
    """
    Create a retry job with adjusted settings based on retry attempt.
    
    Args:
        original_job: The original job that was blocked
    
    Returns:
        The created retry job dict, or None if creation failed
    """
    # Determine the original job ID (in case this is already a retry)
    original_id = original_job.get('retry_of_job_id') or original_job['id']
    
    # Calculate next retry attempt
    current_attempt = original_job.get('retry_attempt', 0)
    next_attempt = current_attempt + 1
    
    if next_attempt > MAX_RETRY_ATTEMPTS:
        logger.warning(f"Cannot create retry: already at max attempts for job {original_id}")
        return None
    
    # Determine retry mode
    retry_mode = RETRY_MODES.get(next_attempt, 'unknown')
    
    # Generate new job ID and reuse token
    new_job_id = generate_job_id()
    token_hash = original_job['token_hash']
    
    # Copy job parameters
    start_url = original_job['start_url']
    allowed_host = original_job['allowed_host']
    max_pages = original_job['max_pages']
    timeout_seconds = original_job['timeout_seconds']
    ignore_prefixes = json.loads(original_job.get('ignore_path_prefixes', '[]'))
    requester_ip_hash = original_job['requester_ip_hash']
    
    # Adjust settings based on retry mode
    use_js = False
    if retry_mode == 'playwright':
        use_js = True
        logger.info(f"Retry {next_attempt}: Using Playwright mode for {start_url}")
    elif retry_mode == 'slower':
        # Slower mode will be applied in settings override
        logger.info(f"Retry {next_attempt}: Using slower mode for {start_url}")
    
    # Create the retry job
    try:
        retry_job = queries.create_job(
            job_id=new_job_id,
            token_hash=token_hash,
            start_url=start_url,
            allowed_host=allowed_host,
            max_pages=max_pages,
            timeout_seconds=timeout_seconds,
            ignore_path_prefixes=ignore_prefixes,
            requester_ip_hash=requester_ip_hash,
            expiry_hours=settings.JOB_EXPIRY_HOURS,
            use_js=use_js
        )
        
        # Set retry metadata
        queries.update_job(
            new_job_id,
            retry_of_job_id=original_id,
            retry_attempt=next_attempt,
            retry_mode=retry_mode,
            retry_reason=f"Blocked by {original_job.get('site_status', 'unknown')}"
        )
        
        # Log the retry creation
        queries.insert_job_event(
            new_job_id,
            'info',
            'retry_created',
            {
                'original_job_id': original_id,
                'retry_attempt': next_attempt,
                'retry_mode': retry_mode,
                'reason': 'cloudflare_blocking'
            }
        )
        
        logger.info(f"Created retry job {new_job_id} (attempt {next_attempt}, mode: {retry_mode}) for {original_id}")
        return retry_job
        
    except Exception as e:
        logger.error(f"Failed to create retry job for {original_id}: {e}")
        return None


def get_retry_status_message(job: dict) -> Optional[str]:
    """
    Generate a user-friendly status message for retry jobs.
    
    Args:
        job: The job dict
    
    Returns:
        A status message string, or None if not a retry job
    """
    retry_attempt = job.get('retry_attempt', 0)
    retry_mode = job.get('retry_mode')
    retry_of_job_id = job.get('retry_of_job_id')
    
    if retry_attempt == 0:
        # This is an original job, check if it has retries
        latest_retry = queries.get_latest_retry(job['id'])
        if latest_retry:
            return f"Auto-retry in progress (attempt {latest_retry['retry_attempt']}, mode: {latest_retry.get('retry_mode', 'unknown')})"
        return None
    
    # This is a retry job
    if retry_attempt == 1:
        return f"⚠️ Cloudflare detected on attempt 1. Retrying with slower crawling (attempt {retry_attempt})..."
    elif retry_attempt == 2:
        return f"⚠️ Still blocked on attempt 2. Final retry with browser rendering (Playwright)..."
    
    return f"Retry attempt {retry_attempt} (mode: {retry_mode})"
