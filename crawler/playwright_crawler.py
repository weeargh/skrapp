"""Playwright-based crawler for JavaScript-rendered pages."""
from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from datetime import datetime, timezone
from typing import Set, List, Dict, Any
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

from config import settings
from crawler.url_utils import canonicalize_url, is_url_in_scope, extract_hostname
from crawler.extractors import trafilatura_ext, readability_ext, plaintext_ext, markdown_ext


logger = logging.getLogger(__name__)


class PlaywrightCrawler:
    """Crawler using Playwright for JavaScript-rendered pages."""
    
    def __init__(
        self,
        job_id: str,
        start_url: str,
        allowed_host: str,
        max_pages: int = 1000,
        ignore_prefixes: List[str] = None,
        timeout_seconds: int = 1800,
        output_dir: str = None
    ):
        self.job_id = job_id
        self.start_url = start_url
        self.allowed_host = allowed_host.lower()
        self.max_pages = max_pages
        self.ignore_prefixes = ignore_prefixes or []
        self.timeout_seconds = timeout_seconds
        self.output_dir = output_dir or os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
        
        self.seen_urls: Set[str] = set()
        self.pages_fetched = 0
        self.start_time = None
        
        # Stats
        self.status_codes: Dict[int, int] = {}
        self.errors: List[Dict] = []
        
        # Output file
        self.output_file = None
    
    def crawl(self) -> Dict[str, Any]:
        """
        Run the crawl.
        
        Returns:
            Stats dictionary
        """
        self.start_time = time.time()
        os.makedirs(self.output_dir, exist_ok=True)
        
        output_path = os.path.join(self.output_dir, 'pages.raw.jsonl')
        self.output_file = open(output_path, 'a', encoding='utf-8')
        
        logger.info(f"Starting Playwright crawl: job_id={self.job_id}, "
                   f"start_url={self.start_url}, max_pages={self.max_pages}")
        
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(
                    headless=True,
                    args=['--no-sandbox', '--disable-dev-shm-usage']
                )
                
                context = browser.new_context(
                    user_agent=settings.CRAWLER_USER_AGENT + ' (JS-enabled)',
                    viewport={'width': 1280, 'height': 720},
                    java_script_enabled=True
                )
                
                # Start crawling
                self._crawl_page(context, self.start_url, depth=0)
                
                context.close()
                browser.close()
                
        except Exception as e:
            logger.error(f"Playwright crawl error: {e}")
            self.errors.append({
                'url': self.start_url,
                'error': str(e)
            })
        finally:
            if self.output_file:
                self.output_file.close()
        
        elapsed = time.time() - self.start_time
        
        stats = {
            'pages_fetched': self.pages_fetched,
            'elapsed_seconds': int(elapsed),
            'status_codes': self.status_codes,
            'errors_count': len(self.errors),
            'errors': self.errors[-10:]
        }
        
        logger.info(f"Playwright crawl complete: {self.pages_fetched} pages in {elapsed:.1f}s")
        
        return stats
    
    def _crawl_page(self, context: BrowserContext, url: str, depth: int):
        """Crawl a single page and follow links."""
        # Check limits
        if self.pages_fetched >= self.max_pages:
            return
        
        elapsed = time.time() - self.start_time
        if elapsed >= self.timeout_seconds:
            logger.info("Timeout reached, stopping crawl")
            return
        
        # Check if already seen
        canonical = canonicalize_url(url)
        if canonical in self.seen_urls:
            return
        
        # Check scope
        if not is_url_in_scope(url, self.allowed_host, self.ignore_prefixes, settings.EXCLUDED_EXTENSIONS):
            return
        
        self.seen_urls.add(canonical)
        
        page = None
        try:
            page = context.new_page()
            
            # Navigate with wait for network idle
            response = page.goto(
                url,
                wait_until='networkidle',
                timeout=30000
            )
            
            if response is None:
                logger.warning(f"No response for {url}")
                return
            
            status_code = response.status
            self.status_codes[status_code] = self.status_codes.get(status_code, 0) + 1
            
            # Wait a bit more for dynamic content
            page.wait_for_timeout(1000)
            
            # Get rendered HTML
            html = page.content()
            content_type = response.headers.get('content-type', 'text/html')
            
            # Extract outlinks before processing
            outlinks = self._extract_links(page, url)
            
            # Process the page
            record = self._process_page(url, canonical, html, status_code, content_type, depth, len(outlinks))
            
            # Write to output
            if record:
                self._write_record(record)
                self.pages_fetched += 1
                
                if self.pages_fetched % 10 == 0:
                    logger.info(f"Progress: {self.pages_fetched} pages fetched")
            
            # Follow links (BFS within depth)
            if depth < settings.CRAWLER_DEPTH_LIMIT:
                for link_url in outlinks:
                    if self.pages_fetched >= self.max_pages:
                        break
                    self._crawl_page(context, link_url, depth + 1)
                    
        except Exception as e:
            logger.warning(f"Error crawling {url}: {e}")
            self.errors.append({
                'url': url,
                'error': str(e)
            })
        finally:
            if page:
                try:
                    page.close()
                except:
                    pass
    
    def _extract_links(self, page: Page, base_url: str) -> List[str]:
        """Extract all links from the page."""
        links = []
        try:
            hrefs = page.eval_on_selector_all('a[href]', 'elements => elements.map(e => e.href)')
            
            for href in hrefs:
                if not href:
                    continue
                
                # Make absolute
                if not href.startswith(('http://', 'https://')):
                    href = urljoin(base_url, href)
                
                # Check scope
                if is_url_in_scope(href, self.allowed_host, self.ignore_prefixes, settings.EXCLUDED_EXTENSIONS):
                    canonical = canonicalize_url(href)
                    if canonical not in self.seen_urls:
                        links.append(href)
                        
        except Exception as e:
            logger.debug(f"Error extracting links: {e}")
        
        return links[:50]  # Limit links per page
    
    def _process_page(
        self,
        url: str,
        canonical_url: str,
        html: str,
        status_code: int,
        content_type: str,
        depth: int,
        outlinks_count: int
    ) -> Dict[str, Any] | None:
        """Process a page and extract content."""
        if not html:
            return None
        
        # Text extraction cascade
        text = trafilatura_ext.extract(html)
        extraction_mode = 'trafilatura'
        
        if not text or len(text.strip()) < settings.MIN_TEXT_LENGTH_SUCCESS:
            text = readability_ext.extract(html)
            extraction_mode = 'readability'
        
        if not text or len(text.strip()) < settings.MIN_TEXT_LENGTH_SUCCESS:
            text = plaintext_ext.extract(html) or ''
            extraction_mode = 'fallback'
        
        # Get title
        title = readability_ext.get_title(html) or plaintext_ext.get_title(html) or ''
        
        # Compute text hash
        normalized = ' '.join(text.lower().split())
        text_hash = f"sha256:{hashlib.sha256(normalized.encode()).hexdigest()}"
        
        # Extract markdown and metadata
        try:
            from bs4 import BeautifulSoup
            markdown, sections = markdown_ext.extract_markdown(html, url)
            soup = BeautifulSoup(html, 'lxml')
            breadcrumbs = markdown_ext.extract_breadcrumbs(soup, url)
            last_modified = markdown_ext.extract_last_modified(soup)
        except Exception as e:
            logger.debug(f"Markdown extraction error: {e}")
            markdown = text
            sections = []
            breadcrumbs = []
            last_modified = None
        
        return {
            'job_id': self.job_id,
            'url': url,
            'canonical_url': canonical_url,
            'fetched_at': datetime.now(timezone.utc).isoformat(),
            'status_code': status_code,
            'content_type': content_type,
            'title': title,
            'text': text,
            'markdown': markdown,
            'text_hash': text_hash,
            'extraction_mode': extraction_mode,
            'depth': depth,
            'outlinks_count': outlinks_count,
            'sections': sections,
            'breadcrumbs': breadcrumbs,
            'last_modified': last_modified,
            'error': None,
            'js_rendered': True
        }
    
    def _write_record(self, record: Dict[str, Any]):
        """Write a record to the output file."""
        line = json.dumps(record, ensure_ascii=False)
        self.output_file.write(line + '\n')
        self.output_file.flush()


def run_playwright_crawl(
    job_id: str,
    start_url: str,
    allowed_host: str,
    max_pages: int = 1000,
    ignore_prefixes: List[str] = None,
    timeout_seconds: int = 1800,
    output_dir: str = None
) -> Dict[str, Any]:
    """
    Run a Playwright-based crawl.
    
    This is the main entry point for the Playwright crawler.
    """
    crawler = PlaywrightCrawler(
        job_id=job_id,
        start_url=start_url,
        allowed_host=allowed_host,
        max_pages=max_pages,
        ignore_prefixes=ignore_prefixes,
        timeout_seconds=timeout_seconds,
        output_dir=output_dir
    )
    
    return crawler.crawl()
