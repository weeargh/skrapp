"""Docs crawler spider."""
import json
import logging
import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from config import settings
from crawler.url_utils import canonicalize_url, is_url_in_scope


logger = logging.getLogger(__name__)


class DocsSpider(CrawlSpider):
    """Spider for crawling documentation sites."""
    
    name = 'docs_spider'
    
    custom_settings = {
        'DEPTH_LIMIT': settings.CRAWLER_DEPTH_LIMIT,
    }
    
    def __init__(
        self,
        job_id: str = None,
        start_url: str = None,
        allowed_host: str = None,
        max_pages: int = None,
        ignore_prefixes: str = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        
        self.job_id = job_id or 'unknown'
        
        if not start_url:
            raise ValueError("start_url is required")
        
        self.start_urls = [start_url]
        self.start_url = start_url
        
        if allowed_host:
            self.allowed_host = allowed_host.lower()
            self.allowed_domains = [self.allowed_host]
        else:
            from crawler.url_utils import extract_hostname
            self.allowed_host = extract_hostname(start_url) or ''
            self.allowed_domains = [self.allowed_host] if self.allowed_host else []
        
        self.max_pages = int(max_pages) if max_pages else settings.DEFAULT_MAX_PAGES
        
        if ignore_prefixes:
            try:
                self.ignore_prefixes = json.loads(ignore_prefixes)
            except json.JSONDecodeError:
                self.ignore_prefixes = []
        else:
            self.ignore_prefixes = []
        
        self.pages_fetched = 0
        self.seen_urls = set()
        
        self.rules = (
            Rule(
                LinkExtractor(
                    allow_domains=self.allowed_domains,
                    deny_extensions=list(settings.EXCLUDED_EXTENSIONS),
                ),
                callback='parse_page',
                follow=True
            ),
        )
        
        super()._compile_rules()
        
        logger.info(f"DocsSpider initialized: job_id={self.job_id}, "
                   f"start_url={self.start_url}, allowed_host={self.allowed_host}, "
                   f"max_pages={self.max_pages}, ignore_prefixes={self.ignore_prefixes}")
    
    def start_requests(self):
        """Generate initial request."""
        yield scrapy.Request(
            self.start_url,
            callback=self.parse_page,
            meta={'depth': 0},
            dont_filter=True
        )
    
    def parse_page(self, response):
        """Parse a page and extract content."""
        if self.pages_fetched >= self.max_pages:
            logger.info(f"Reached max pages limit ({self.max_pages}), stopping")
            self.crawler.engine.close_spider(self, 'max_pages_reached')
            return
        
        url = response.url
        canonical = canonicalize_url(url)
        
        if canonical in self.seen_urls:
            logger.debug(f"Skipping duplicate URL: {url}")
            return
        
        if not is_url_in_scope(url, self.allowed_host, self.ignore_prefixes, settings.EXCLUDED_EXTENSIONS):
            logger.debug(f"URL out of scope: {url}")
            return
        
        self.seen_urls.add(canonical)
        self.pages_fetched += 1
        
        content_type = response.headers.get('Content-Type', b'').decode('utf-8', errors='ignore')
        
        html = ''
        if hasattr(response, 'text'):
            try:
                html = response.text
            except (UnicodeDecodeError, AttributeError) as e:
                logger.warning(f"Failed to decode response text for {url}: {e}")
                html = ''
        
        outlinks = []
        if html and hasattr(response, 'xpath'):
            for link in response.xpath('//a/@href').getall():
                try:
                    absolute_url = response.urljoin(link)
                    if is_url_in_scope(absolute_url, self.allowed_host, self.ignore_prefixes, settings.EXCLUDED_EXTENSIONS):
                        outlinks.append(absolute_url)
                except (ValueError, TypeError) as e:
                    # Invalid URL format or type issues when joining/parsing URLs
                    logger.debug(f"Skipping invalid link '{link}' on {url}: {e}")
        
        depth = response.meta.get('depth', 0)
        
        item = {
            'url': url,
            'canonical_url': canonical,
            'status_code': response.status,
            'content_type': content_type,
            'html': html,
            'depth': depth,
            'outlinks_count': len(outlinks),
            'title': None,
            'text': None,
            'text_hash': None,
            'extraction_mode': None,
            'error': None,
        }
        
        yield item
        
        for link_url in outlinks:
            link_canonical = canonicalize_url(link_url)
            if link_canonical not in self.seen_urls:
                yield scrapy.Request(
                    link_url,
                    callback=self.parse_page,
                    meta={'depth': depth + 1}
                )
        
        if self.pages_fetched % 50 == 0:
            logger.info(f"Progress: {self.pages_fetched} pages fetched")
