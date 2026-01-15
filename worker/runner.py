"""Job runner - manages crawler execution with automatic fallback."""
from __future__ import annotations

import json
import logging
import os
import subprocess
import sys

from config import settings
from config.constants import JobState, ErrorReason, SiteStatus
from config.js_domains import is_js_heavy_domain, get_detected_reason
from db import queries
from worker.heartbeat import HeartbeatThread
from worker.finalizer import finalize_job
from worker.blocking_detector import analyze_blocking_signals, update_job_blocking_status
from crawler.playwright_crawler import run_playwright_crawl


logger = logging.getLogger(__name__)


def run_job(job_id: str) -> bool:
    """
    Run a crawl job with automatic fallback strategy.
    
    This function implements an intelligent crawler selection strategy:
    - Scrapy: Fast, efficient, but doesn't execute JavaScript
    - Playwright: Slower but handles JavaScript-heavy sites
    
    Strategy Decision Tree:
    1. Check if user explicitly requested JS rendering (use_js flag)
       → If yes: Use Playwright directly
    
    2. Check if URL matches known JS-heavy domain patterns (e.g., React, Vue, Angular SPAs)
       → If yes: Use Playwright preemptively to avoid wasted Scrapy attempts
       → Log the detection reason (e.g., 'react_docs', 'spa_framework')
    
    3. Otherwise: Start with Scrapy (faster for traditional HTML sites)
       → After Scrapy completes, analyze results for blocking/failure signals:
          * Zero pages fetched → Likely JS-required or blocked
          * Excessive 429/403 responses → Rate limited or blocked
          * High duplicate content hash ratio → Captcha or login wall
       → If any blocking signals detected: Automatically retry with Playwright
    
    Fallback Retry Policy:
    - Maximum 1 fallback retry per job (prevents infinite loops)
    - Fallback count tracked in job.fallback_retry_count field
    - Events logged for monitoring: 'fallback_triggered', 'js_domain_detected'
    
    Args:
        job_id: The job ID to run
    
    Returns:
        True if the job completed successfully (pages fetched > 0), False otherwise
    
    Side Effects:
        - Updates job state in database (QUEUED → RUNNING → DONE/FAILED)
        - Creates output files in jobs/<job_id>/ directory
        - Starts heartbeat thread to update progress
        - Updates IP concurrent job count
    """
    job = queries.get_job_by_id(job_id)
    if not job:
        logger.error(f"Job {job_id} not found")
        return False
    
    logger.info(f"Starting job {job_id}: {job['start_url']}")
    
    queries.update_job_state(job_id, JobState.RUNNING)
    
    job_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)
    
    state_dir = os.path.join(job_dir, 'state')
    os.makedirs(state_dir, exist_ok=True)
    
    heartbeat = HeartbeatThread(job_id, job_dir)
    heartbeat.start()
    
    try:
        # Determine initial crawler strategy
        # Priority order: user request > auto-detection > default Scrapy
        use_js_flag = job.get('use_js', 0)
        
        if use_js_flag:
            # User explicitly requested JS rendering via API parameter
            strategy = 'playwright_user_requested'
            use_playwright = True
            logger.info(f"Job {job_id}: Using Playwright (user requested)")
        elif is_js_heavy_domain(job['start_url']):
            # Auto-detected JS-heavy domain based on URL patterns
            # This saves time by skipping the Scrapy attempt for known SPA frameworks
            strategy = 'playwright_preemptive'
            use_playwright = True
            detected_reason = get_detected_reason(job['start_url'])
            logger.info(f"Job {job_id}: Using Playwright (auto-detected: {detected_reason})")
            queries.insert_job_event(job_id, 'INFO', 'js_domain_detected', {
                'reason': detected_reason
            })
        else:
            # Start with Scrapy (faster for traditional server-rendered HTML)
            strategy = 'scrapy'
            use_playwright = False
            logger.info(f"Job {job_id}: Starting with Scrapy")
        
        # Update crawler strategy
        queries.update_job(job_id, crawler_strategy=strategy)
        
        # Run initial crawl
        if use_playwright:
            success = _run_playwright(job, job_dir)
        else:
            # Run Scrapy first
            success = _run_scrapy(job, job_dir, state_dir)
            
            # Post-Scrapy analysis: Check if fallback to Playwright is needed
            # This happens when Scrapy fails due to:
            # - Zero pages fetched (likely JS-required content)
            # - Site blocking detected (429/403 errors, captcha, login walls)
            # - Throttling detected (high error rate but not complete block)
            should_fallback, fallback_reason = _should_fallback(job_id, job_dir)
            
            if should_fallback:
                # Check retry limit: Only fallback once per job
                # This prevents infinite loops and excessive resource usage
                fallback_count = job.get('fallback_retry_count', 0)
                if fallback_count < 1:
                    logger.info(f"Job {job_id}: Triggering fallback to Playwright ({fallback_reason})")
                    
                    # Update job metadata for fallback attempt
                    queries.update_job(
                        job_id,
                        fallback_retry_count=1,
                        crawler_strategy='scrapy_fallback_playwright'
                    )
                    queries.insert_job_event(job_id, 'INFO', 'fallback_triggered', {
                        'reason': fallback_reason,
                        'from': 'scrapy',
                        'to': 'playwright'
                    })
                    
                    # Retry with Playwright (this will overwrite Scrapy's output)
                    success = _run_playwright(job, job_dir)
                else:
                    logger.warning(f"Job {job_id}: Fallback already attempted, not retrying")
        
    except Exception as e:
        logger.error(f"Unexpected error running crawler for job {job_id}: {e}", exc_info=True)
        success = False
        queries.update_job(
            job_id,
            last_error=json.dumps({
                "reason": ErrorReason.UNKNOWN,
                "message": f"Unexpected crawler error: {type(e).__name__}: {str(e)}"
            })
        )
    finally:
        heartbeat.stop()
        heartbeat.join(timeout=5)
        
        # Check if cancellation was requested
        if heartbeat.cancellation_requested:
            logger.info(f"Job {job_id} was cancelled by user")
            success = True  # Treat cancellation as successful for finalization
        
        # Final update of pages_fetched before finalization
        # (Heartbeat may not have triggered if job completed quickly)
        final_pages = _count_pages(job_dir)
        if final_pages > 0:
            queries.update_job(job_id, pages_fetched=final_pages)
    
    # Check again if cancelled (could be cancelled during finally block)
    job = queries.get_job_by_id(job_id)
    if job and job['state'] == JobState.CANCELLED:
        logger.info(f"Job {job_id} cancelled - finalizing partial results")
        finalize_job(job_id)
        return True
    
    if success:
        finalize_job(job_id)
    else:
        if job and job['state'] == JobState.RUNNING:
            # Determine more specific failure reason if possible
            error_msg = "Crawler execution failed"
            if final_pages == 0:
                error_msg = "Crawler failed: Zero pages fetched. Site may require authentication, be blocking requests, or have technical issues."
            
            queries.update_job_state(
                job_id,
                JobState.FAILED,
                last_error=json.dumps({
                    "reason": ErrorReason.UNKNOWN,
                    "message": error_msg
                })
            )
            queries.decrement_ip_concurrent(job['requester_ip_hash'])
    
    return success


def _should_fallback(job_id: str, job_dir: str) -> tuple[bool, str | None]:
    """
    Determine if we should fallback to Playwright after Scrapy.
    
    This function analyzes the Scrapy crawl results to detect blocking or failure signals
    that indicate the site requires JavaScript rendering or is actively blocking the crawler.
    
    Blocking Signal Detection:
    1. Zero Pages Fetched:
       - Most common reason: site requires JavaScript to render content
       - Example: React/Vue/Angular SPAs with empty HTML shell
       - Action: Retry with Playwright
    
    2. Site Status = BLOCKED:
       - Detected via BlockingDetectionPipeline during crawl
       - Signals include:
         * excessive_429: >20% of responses are HTTP 429 (rate limited)
         * excessive_403: >30% of responses are HTTP 403 (forbidden)
         * captcha_detected: CAPTCHA HTML patterns found in response
         * duplicate_content_high: >50% of pages have identical content hash
       - Action: Retry with Playwright (may bypass some blocks)
    
    3. Site Status = THROTTLED:
       - High error rate but not completely blocked
       - Some pages succeeded, but many failed
       - Action: Retry with Playwright with slower rate
    
    4. Site Status = LOGIN_REQUIRED:
       - Login wall detected
       - Action: Do NOT fallback (Playwright won't help without credentials)
    
    Args:
        job_id: The job ID
        job_dir: The job output directory containing blocking_evidence.json
    
    Returns:
        (should_fallback, reason): 
        - should_fallback: True if we should retry with Playwright
        - reason: Human-readable string explaining why (e.g., 'zero_pages', 'blocked:captcha_detected')
    """
    # Read blocking evidence
    evidence_path = os.path.join(job_dir, 'blocking_evidence.json')
    tracker_evidence = {}
    
    if os.path.exists(evidence_path):
        try:
            with open(evidence_path, 'r', encoding='utf-8') as f:
                tracker_evidence = json.load(f)
        except Exception as e:
            logger.warning(f"Failed to read blocking evidence: {e}")
    
    # Analyze blocking signals
    site_status, evidence = analyze_blocking_signals(job_id, tracker_evidence)
    
    # Update job with blocking status
    update_job_blocking_status(job_id, site_status, evidence)
    
    # Count pages fetched
    pages_fetched = _count_pages(job_dir)
    
    logger.info(f"Job {job_id}: Post-Scrapy analysis - status={site_status}, pages={pages_fetched}")
    
    # Decide on fallback
    if pages_fetched == 0:
        return True, 'zero_pages'
    
    if site_status == SiteStatus.BLOCKED:
        return True, f'blocked:{evidence.get("signals_detected", ["unknown"])[0] if evidence.get("signals_detected") else "unknown"}'
    
    if site_status == SiteStatus.THROTTLED:
        return True, 'throttled'
    
    # LOGIN_REQUIRED doesn't benefit from Playwright fallback
    # Normal status means no fallback needed
    return False, None


def _count_pages(job_dir: str) -> int:
    """Count the number of pages in the raw output file."""
    output_path = os.path.join(job_dir, 'pages.raw.jsonl')
    if not os.path.exists(output_path):
        return 0
    
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def _run_scrapy(job: dict, job_dir: str, state_dir: str) -> bool:
    """
    Run the Scrapy crawler subprocess.
    
    Returns:
        True if crawler completed successfully
    """
    job_id = job['id']
    
    crawler_log_path = os.path.join(job_dir, 'crawler.log')
    runner_log_path = os.path.join(job_dir, 'runner.log')
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    cmd = [
        sys.executable, '-m', 'scrapy', 'runspider',
        os.path.join(project_root, 'crawler', 'spider.py'),
        '-a', f'job_id={job_id}',
        '-a', f'start_url={job["start_url"]}',
        '-a', f'allowed_host={job["allowed_host"]}',
        '-a', f'max_pages={job["max_pages"]}',
        '-a', f'ignore_prefixes={job["ignore_path_prefixes"]}',
        '-s', f'JOBDIR={state_dir}',
        '-s', f'LOG_FILE={crawler_log_path}',
        '-s', f'CLOSESPIDER_TIMEOUT={job["timeout_seconds"]}',
        '-s', 'ITEM_PIPELINES={"crawler.pipelines.TextExtractionPipeline": 100, "crawler.pipelines.QualityGatePipeline": 120, "crawler.pipelines.ContentCleanupPipeline": 140, "crawler.pipelines.DocumentIdentityPipeline": 160, "crawler.pipelines.BudgetControlPipeline": 170, "crawler.pipelines.MarkdownExtractionPipeline": 180, "crawler.pipelines.BlockingDetectionPipeline": 200, "crawler.pipelines.CrawlLogPipeline": 250, "crawler.pipelines.JSONLWriterPipeline": 300}',
        '-s', 'DOWNLOADER_MIDDLEWARES={"crawler.middlewares.AdaptiveThrottleMiddleware": 100, "crawler.middlewares.BlockingSignalMiddleware": 543}',
        '-s', f'USER_AGENT={settings.CRAWLER_USER_AGENT}',
        '-s', 'ROBOTSTXT_OBEY=True',
        '-s', f'CONCURRENT_REQUESTS={settings.CRAWLER_CONCURRENT_REQUESTS}',
        '-s', f'DOWNLOAD_DELAY={settings.CRAWLER_DOWNLOAD_DELAY}',
        '-s', f'DEPTH_LIMIT={settings.CRAWLER_DEPTH_LIMIT}',
        '-s', 'HTTPERROR_ALLOWED_CODES=[403,404,429,500,502,503,504]',
    ]
    
    env = os.environ.copy()
    env['PYTHONPATH'] = project_root
    
    logger.info(f"Running Scrapy for job {job_id}")
    logger.debug(f"Command: {' '.join(cmd)}")
    
    with open(runner_log_path, 'a', encoding='utf-8') as runner_log:
        runner_log.write(f"\n--- Starting crawler for job {job_id} ---\n")
        runner_log.write(f"Command: {' '.join(cmd)}\n")
        runner_log.flush()
        
        try:
            result = subprocess.run(
                cmd,
                cwd=project_root,
                env=env,
                capture_output=True,
                text=True,
                timeout=job['timeout_seconds'] + 60
            )
            
            if result.stdout:
                runner_log.write(f"STDOUT:\n{result.stdout}\n")
            if result.stderr:
                runner_log.write(f"STDERR:\n{result.stderr}\n")
            
            runner_log.write(f"Exit code: {result.returncode}\n")
            runner_log.flush()
            
            if result.returncode != 0:
                logger.warning(f"Scrapy exited with non-zero code {result.returncode} for job {job_id}")
                
                # Check if this is an expected termination (max pages/timeout reached)
                if 'CloseSpider' in result.stderr or 'max_pages_reached' in result.stderr:
                    logger.info(f"Job {job_id} stopped due to max pages or timeout (expected)")
                    return True
                
                # Check if we got any items despite the error
                # Some Scrapy errors are non-fatal if we fetched pages
                if 'item_scraped_count' in result.stderr:
                    logger.info(f"Job {job_id} exited with error but scraped items successfully")
                    return True
                
                # True failure - no pages scraped and unexpected error
                logger.error(f"Job {job_id} failed with no pages scraped. Exit code: {result.returncode}")
                return False
            
            return True
            
        except subprocess.TimeoutExpired:
            logger.error(f"Scrapy process timed out after {job['timeout_seconds'] + 60}s for job {job_id}")
            runner_log.write(f"ERROR: Crawler process timed out after {job['timeout_seconds'] + 60} seconds\n")
            queries.update_job(
                job_id,
                last_error=json.dumps({
                    "reason": ErrorReason.TIMEOUT,
                    "message": f"Crawler process exceeded timeout limit of {job['timeout_seconds']}s (+60s grace period)"
                })
            )
            return False
            
        except Exception as e:
            logger.error(f"Unexpected error running Scrapy for job {job_id}: {type(e).__name__}: {e}", exc_info=True)
            runner_log.write(f"ERROR: {type(e).__name__}: {e}\n")
            queries.update_job(
                job_id,
                last_error=json.dumps({
                    "reason": ErrorReason.UNKNOWN,
                    "message": f"Scrapy subprocess error: {type(e).__name__}: {str(e)}"
                })
            )
            return False


def _run_playwright(job: dict, job_dir: str) -> bool:
    """
    Run the Playwright crawler.
    
    Returns:
        True if crawler completed successfully
    """
    job_id = job['id']
    
    runner_log_path = os.path.join(job_dir, 'runner.log')
    
    # Parse ignore_path_prefixes if stored as JSON string
    ignore_prefixes = job.get('ignore_path_prefixes', '[]')
    if isinstance(ignore_prefixes, str):
        try:
            ignore_prefixes = json.loads(ignore_prefixes)
        except json.JSONDecodeError:
            ignore_prefixes = []
    
    logger.info(f"Running Playwright crawler for job {job_id}")
    
    with open(runner_log_path, 'a', encoding='utf-8') as runner_log:
        runner_log.write(f"\n--- Starting Playwright crawler for job {job_id} ---\n")
        runner_log.write(f"URL: {job['start_url']}\n")
        runner_log.write(f"use_js: True\n")
        runner_log.flush()
        
        try:
            stats = run_playwright_crawl(
                job_id=job_id,
                start_url=job['start_url'],
                allowed_host=job['allowed_host'],
                max_pages=job['max_pages'],
                ignore_prefixes=ignore_prefixes,
                timeout_seconds=job['timeout_seconds'],
                output_dir=job_dir
            )
            
            runner_log.write(f"Crawl stats: {json.dumps(stats)}\n")
            runner_log.flush()
            
            # Update job progress
            queries.update_job(
                job_id,
                pages_fetched=stats.get('pages_fetched', 0),
                errors_count=stats.get('errors_count', 0)
            )
            
            # Check if we got any pages
            if stats.get('pages_fetched', 0) == 0:
                logger.warning(f"Playwright crawl returned 0 pages for job {job_id}")
                error_detail = "No pages fetched"
                if stats.get('errors'):
                    error_detail = f"Errors encountered: {stats['errors'][0]}"
                
                queries.update_job(
                    job_id,
                    last_error=json.dumps({
                        "reason": ErrorReason.BLOCKED,
                        "message": f"Playwright crawler failed to fetch any pages. {error_detail}"
                    })
                )
                return False
            
            logger.info(f"Playwright crawl complete for job {job_id}: {stats.get('pages_fetched', 0)} pages")
            return True
            
        except Exception as e:
            logger.error(f"Unexpected error running Playwright for job {job_id}: {type(e).__name__}: {e}", exc_info=True)
            runner_log.write(f"ERROR: {type(e).__name__}: {e}\n")
            queries.update_job(
                job_id,
                last_error=json.dumps({
                    "reason": ErrorReason.UNKNOWN,
                    "message": f"Playwright execution error: {type(e).__name__}: {str(e)}"
                })
            )
            return False
