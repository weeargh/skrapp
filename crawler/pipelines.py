"""Scrapy pipelines for text extraction and output."""
import hashlib
import json
import logging
import os
from datetime import datetime, timezone

from bs4 import BeautifulSoup

from config import settings
from config.constants import ExtractionMode
from crawler.extractors import trafilatura_ext, readability_ext, plaintext_ext
from crawler.extractors import markdown_ext


logger = logging.getLogger(__name__)


class TextExtractionPipeline:
    """Pipeline to extract text from HTML responses."""
    
    def process_item(self, item, spider):
        """Extract text using the cascade: trafilatura -> readability -> fallback."""
        html = item.get('html', '')
        
        if not html:
            item['text'] = ''
            item['extraction_mode'] = ExtractionMode.FALLBACK
            item['text_hash'] = self._compute_hash('')
            return item
        
        text = trafilatura_ext.extract(html)
        if text and len(text.strip()) >= settings.MIN_TEXT_LENGTH_SUCCESS:
            item['text'] = text
            item['extraction_mode'] = ExtractionMode.TRAFILATURA
            item['text_hash'] = self._compute_hash(text)
            item['title'] = item.get('title') or readability_ext.get_title(html) or plaintext_ext.get_title(html)
            return item
        
        text = readability_ext.extract(html)
        if text and len(text.strip()) >= settings.MIN_TEXT_LENGTH_SUCCESS:
            item['text'] = text
            item['extraction_mode'] = ExtractionMode.READABILITY
            item['text_hash'] = self._compute_hash(text)
            item['title'] = item.get('title') or readability_ext.get_title(html) or plaintext_ext.get_title(html)
            return item
        
        text = plaintext_ext.extract(html) or ''
        item['text'] = text
        item['extraction_mode'] = ExtractionMode.FALLBACK
        item['text_hash'] = self._compute_hash(text)
        item['title'] = item.get('title') or plaintext_ext.get_title(html)
        
        return item
    
    def _compute_hash(self, text: str) -> str:
        """Compute SHA256 hash of normalized text."""
        normalized = ' '.join(text.lower().split())
        return f"sha256:{hashlib.sha256(normalized.encode()).hexdigest()}"


class BlockingDetectionPipeline:
    """Pipeline to track blocking signals from extracted content."""
    
    def process_item(self, item, spider):
        """Track text hash for duplicate detection."""
        if hasattr(spider, 'blocking_tracker'):
            text_hash = item.get('text_hash')
            if text_hash:
                spider.blocking_tracker.text_hashes[text_hash] = \
                    spider.blocking_tracker.text_hashes.get(text_hash, 0) + 1
        
        return item


class MarkdownExtractionPipeline:
    """Pipeline to extract markdown and metadata for knowledge base use."""
    
    def process_item(self, item, spider):
        """Extract markdown, breadcrumbs, sections, and last-modified."""
        html = item.get('html', '')
        url = item.get('url', '')
        
        if not html:
            item['markdown'] = ''
            item['sections'] = []
            item['breadcrumbs'] = []
            item['last_modified'] = None
            return item
        
        try:
            # Extract markdown with proper links
            markdown, sections = markdown_ext.extract_markdown(html, url)
            item['markdown'] = markdown
            item['sections'] = sections
            
            # Extract breadcrumbs
            soup = BeautifulSoup(html, 'lxml')
            item['breadcrumbs'] = markdown_ext.extract_breadcrumbs(soup, url)
            
            # Extract last modified
            item['last_modified'] = markdown_ext.extract_last_modified(soup)
            
        except Exception as e:
            logger.warning(f"Error extracting markdown metadata: {e}")
            item['markdown'] = item.get('text', '')
            item['sections'] = []
            item['breadcrumbs'] = []
            item['last_modified'] = None
        
        return item


class JSONLWriterPipeline:
    """Pipeline to write items to a JSONL file."""
    
    def __init__(self):
        self.file = None
        self.items_count = 0
    
    def open_spider(self, spider):
        """Open the output file when the spider starts."""
        job_id = getattr(spider, 'job_id', 'unknown')
        output_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = os.path.join(output_dir, 'pages.raw.jsonl')
        self.file = open(output_path, 'a', encoding='utf-8')
        
        logger.info(f"Opened output file: {output_path}")
    
    def close_spider(self, spider):
        """Close the output file when the spider finishes."""
        if self.file:
            self.file.close()
            logger.info(f"Closed output file. Total items written: {self.items_count}")
    
    def process_item(self, item, spider):
        """Write item to the JSONL file."""
        record = {
            'job_id': getattr(spider, 'job_id', 'unknown'),
            'url': item.get('url', ''),
            'canonical_url': item.get('canonical_url', ''),
            'fetched_at': datetime.now(timezone.utc).isoformat(),
            'status_code': item.get('status_code', 0),
            'content_type': item.get('content_type', ''),
            'title': item.get('title', ''),
            'text': item.get('text', ''),
            'markdown': item.get('markdown', ''),
            'text_hash': item.get('text_hash', ''),
            'extraction_mode': item.get('extraction_mode', ''),
            'depth': item.get('depth', 0),
            'outlinks_count': item.get('outlinks_count', 0),
            'sections': item.get('sections', []),
            'breadcrumbs': item.get('breadcrumbs', []),
            'last_modified': item.get('last_modified'),
            'error': item.get('error'),
        }
        
        del item['html']
        
        line = json.dumps(record, ensure_ascii=False)
        self.file.write(line + '\n')
        self.file.flush()
        
        self.items_count += 1
        
        return item
