"""Scrapy middlewares for blocking detection and adaptive throttling."""
import json
import logging
import os
import time
from collections import defaultdict
from scrapy import signals
from scrapy.http import Response
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

from config import settings
from crawler.blocking_signals import BlockingSignalTracker, detect_login_redirect


logger = logging.getLogger(__name__)


class AdaptiveThrottleMiddleware:
    """
    Middleware for adaptive per-host throttling with exponential backoff.
    
    - Tracks 429/503 responses per host
    - Increases delay exponentially on rate limit hits
    - Implements circuit breaker pattern for heavily throttled hosts
    """
    
    # Backoff configuration
    INITIAL_DELAY = 1.0  # seconds
    MAX_DELAY = 60.0  # seconds
    BACKOFF_FACTOR = 2.0
    RECOVERY_RATE = 0.9  # Delay reduction per successful request
    
    # Circuit breaker
    FAILURE_THRESHOLD = 5  # Consecutive failures to trip breaker
    BREAKER_RESET_TIME = 300  # seconds (5 minutes)
    
    def __init__(self):
        # Per-host state
        self.host_delays = defaultdict(lambda: self.INITIAL_DELAY)
        self.host_failures = defaultdict(int)
        self.host_breaker_until = defaultdict(float)  # Unix timestamp
        self.host_last_request = defaultdict(float)
    
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware
    
    def spider_opened(self, spider):
        spider.throttle_middleware = self
    
    def _get_host(self, request):
        """Extract host from request."""
        from urllib.parse import urlparse
        return urlparse(request.url).netloc.lower()
    
    def process_request(self, request, spider):
        """Apply adaptive delay before request."""
        host = self._get_host(request)
        
        # Check circuit breaker
        if time.time() < self.host_breaker_until[host]:
            remaining = int(self.host_breaker_until[host] - time.time())
            logger.warning(f"Host {host} circuit breaker active, {remaining}s remaining")
            # Return None to let Scrapy retry later
            request.meta['throttle_breaker'] = True
            return None
        
        # Apply per-host delay
        current_delay = self.host_delays[host]
        if current_delay > self.INITIAL_DELAY:
            last_request = self.host_last_request[host]
            elapsed = time.time() - last_request
            if elapsed < current_delay:
                wait_time = current_delay - elapsed
                logger.debug(f"Throttling {host}: waiting {wait_time:.1f}s")
                time.sleep(min(wait_time, 5.0))  # Cap sleep to avoid blocking too long
        
        self.host_last_request[host] = time.time()
        return None
    
    def process_response(self, request, response, spider):
        """Adjust throttling based on response."""
        host = self._get_host(request)
        status = response.status
        
        if status in (429, 503):
            # Rate limited - increase delay
            self.host_failures[host] += 1
            old_delay = self.host_delays[host]
            new_delay = min(old_delay * self.BACKOFF_FACTOR, self.MAX_DELAY)
            self.host_delays[host] = new_delay
            
            logger.warning(f"Rate limited by {host} ({status}): delay {old_delay:.1f}s -> {new_delay:.1f}s")
            
            # Check circuit breaker
            if self.host_failures[host] >= self.FAILURE_THRESHOLD:
                self.host_breaker_until[host] = time.time() + self.BREAKER_RESET_TIME
                logger.warning(f"Circuit breaker tripped for {host}: paused for {self.BREAKER_RESET_TIME}s")
            
            # Check Retry-After header
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                try:
                    retry_seconds = int(retry_after)
                    self.host_delays[host] = max(self.host_delays[host], retry_seconds)
                    logger.info(f"Retry-After header: {retry_seconds}s for {host}")
                except (ValueError, TypeError):
                    pass
        
        elif 200 <= status < 400:
            # Success - gradually reduce delay
            if self.host_delays[host] > self.INITIAL_DELAY:
                old_delay = self.host_delays[host]
                new_delay = max(old_delay * self.RECOVERY_RATE, self.INITIAL_DELAY)
                self.host_delays[host] = new_delay
                
                if old_delay != new_delay:
                    logger.debug(f"Reducing delay for {host}: {old_delay:.1f}s -> {new_delay:.1f}s")
            
            # Reset failure count on success
            self.host_failures[host] = 0
        
        return response
    
    def get_host_status(self, host: str) -> dict:
        """Get throttling status for a host."""
        return {
            'host': host,
            'current_delay': self.host_delays[host],
            'failure_count': self.host_failures[host],
            'breaker_active': time.time() < self.host_breaker_until[host],
            'breaker_remaining': max(0, int(self.host_breaker_until[host] - time.time())),
        }


class BlockingSignalMiddleware:
    """Middleware to detect blocking signals from responses."""
    
    def __init__(self):
        self.tracker = BlockingSignalTracker()
    
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware
    
    def spider_opened(self, spider):
        spider.blocking_tracker = self.tracker
    
    def spider_closed(self, spider, reason):
        evidence = self.tracker.get_evidence()
        logger.info(f"Blocking detection summary: {evidence}")
        
        # Write evidence to JSON file for runner to analyze
        job_id = getattr(spider, 'job_id', None)
        if job_id:
            job_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
            evidence_path = os.path.join(job_dir, 'blocking_evidence.json')
            try:
                os.makedirs(job_dir, exist_ok=True)
                with open(evidence_path, 'w', encoding='utf-8') as f:
                    json.dump(evidence, f, ensure_ascii=False)
                logger.info(f"Wrote blocking evidence to {evidence_path}")
            except Exception as e:
                logger.warning(f"Failed to write blocking evidence: {e}")
    
    def process_response(self, request, response: Response, spider):
        """Process each response and track blocking signals."""
        status_code = response.status
        url = response.url
        
        html = None
        location = None
        
        if hasattr(response, 'text'):
            try:
                html = response.text[:10000]
            except Exception:
                pass
        
        if status_code in (301, 302, 303, 307, 308):
            location = response.headers.get('Location', b'').decode('utf-8', errors='ignore')
        
        self.tracker.record_response(
            url=url,
            status_code=status_code,
            html=html,
            location_header=location
        )
        
        return response
    
    def process_exception(self, request, exception, spider):
        """Handle exceptions."""
        return None
