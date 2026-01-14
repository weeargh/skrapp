"""Scrapy middlewares for blocking detection."""
import json
import logging
import os
from scrapy import signals
from scrapy.http import Response

from config import settings
from crawler.blocking_signals import BlockingSignalTracker, detect_login_redirect


logger = logging.getLogger(__name__)


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
