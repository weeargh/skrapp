"""Scrapy pipelines for text extraction and output."""
import hashlib
import json
import logging
import os
import re
from datetime import datetime, timezone

from bs4 import BeautifulSoup
from scrapy.exceptions import DropItem

from config import settings
from config.constants import ExtractionMode
from crawler.extractors import trafilatura_ext, readability_ext, plaintext_ext
from crawler.extractors import markdown_ext
from crawler.quality_scorer import score_content, should_retry_extraction


logger = logging.getLogger(__name__)


# Try to import frontier functions (may not exist on first run)
try:
    from db.frontier import (
        create_document, find_document_by_content, find_document_by_url,
        add_document_url, log_crawl_event
    )
    HAS_FRONTIER = True
except ImportError:
    HAS_FRONTIER = False


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


class QualityGatePipeline:
    """Pipeline to score content quality and mark low-quality pages."""
    
    def process_item(self, item, spider):
        """Score content and add quality metadata."""
        text = item.get('text', '')
        html = item.get('html', '')
        title = item.get('title', '')
        
        quality = score_content(
            text=text,
            html=html,
            title=title,
            min_chars=settings.MIN_TEXT_LENGTH_SUCCESS,
        )
        
        item['quality_score'] = quality.score
        item['quality_passed'] = quality.passed
        item['quality_reasons'] = quality.reasons
        
        # If quality is marginal and we haven't tried all extraction modes
        if should_retry_extraction(quality):
            current_mode = item.get('extraction_mode', '')
            
            # Try alternate extraction if not already using fallback
            if current_mode != ExtractionMode.FALLBACK and html:
                # Try readability if we used trafilatura
                if current_mode == ExtractionMode.TRAFILATURA:
                    alt_text = readability_ext.extract(html)
                    if alt_text:
                        alt_quality = score_content(text=alt_text, html=html, title=title)
                        if alt_quality.score > quality.score:
                            item['text'] = alt_text
                            item['extraction_mode'] = ExtractionMode.READABILITY
                            item['quality_score'] = alt_quality.score
                            item['quality_passed'] = alt_quality.passed
                            item['quality_reasons'] = alt_quality.reasons
                            logger.debug(f"Re-extracted with readability, score improved: {quality.score} -> {alt_quality.score}")
        
        if not item['quality_passed']:
            logger.debug(f"Low quality page ({quality.score}): {item.get('url', '')} - {quality.reasons}")
        
        return item


class ContentCleanupPipeline:
    """Pipeline to clean extracted content - remove boilerplate, fix formatting."""
    
    # Boilerplate line patterns to remove
    REMOVE_PATTERNS = [
        # Share/social
        r'^share this (article|page|post)',
        r'^share on (facebook|twitter|linkedin|email)',
        r'^tweet\s*$',
        r'^like\s*$',
        r'^pin it\s*$',
        
        # Navigation
        r'^(previous|next) (article|page|post)',
        r'^back to (top|home|list)',
        r'^skip to (main )?content',
        r'^table of contents\s*$',
        r'^on this page\s*$',
        
        # Cookie/legal
        r'^we use cookies',
        r'^accept (all )?cookies',
        r'^cookie (policy|settings)',
        r'^\s*©\s*\d{4}',
        r'^all rights reserved',
        
        # Subscription
        r'^subscribe to',
        r'^sign up for',
        r'^newsletter',
        
        # Loading placeholders
        r'^loading\.{3,}',
        r'^please wait',
        
        # Empty headers
        r'^#{1,6}\s*$',
        
        # Repeated separators
        r'^[-=_]{5,}$',
    ]
    
    def __init__(self):
        self._patterns = [re.compile(p, re.IGNORECASE) for p in self.REMOVE_PATTERNS]
    
    def process_item(self, item, spider):
        """Clean up extracted text and markdown."""
        # Clean text
        text = item.get('text', '')
        if text:
            item['text'] = self._clean_content(text)
        
        # Clean markdown
        markdown = item.get('markdown', '')
        if markdown:
            item['markdown'] = self._clean_content(markdown)
        
        return item
    
    def _clean_content(self, content: str) -> str:
        """Apply cleanup rules to content."""
        if not content:
            return content
        
        lines = content.split('\n')
        cleaned_lines = []
        prev_line = None
        
        for line in lines:
            stripped = line.strip()
            
            # Skip empty lines (but allow one)
            if not stripped:
                if prev_line != '':
                    cleaned_lines.append('')
                prev_line = ''
                continue
            
            # Skip lines matching boilerplate patterns
            skip = False
            for pattern in self._patterns:
                if pattern.search(stripped):
                    skip = True
                    break
            
            if skip:
                continue
            
            # Skip duplicate consecutive lines (common extraction bug)
            if stripped == prev_line and len(stripped) > 20:
                continue
            
            cleaned_lines.append(line)
            prev_line = stripped
        
        # Remove trailing empty lines
        while cleaned_lines and not cleaned_lines[-1].strip():
            cleaned_lines.pop()
        
        # Remove leading empty lines
        while cleaned_lines and not cleaned_lines[0].strip():
            cleaned_lines.pop(0)
        
        return '\n'.join(cleaned_lines)


class DocumentIdentityPipeline:
    """Pipeline to assign document identity and track URL aliases."""
    
    def process_item(self, item, spider):
        """Assign or find document ID based on content hash."""
        if not HAS_FRONTIER:
            return item
        
        job_id = getattr(spider, 'job_id', 'unknown')
        url = item.get('url', '')
        canonical_url = item.get('canonical_url', '')
        text_hash = item.get('text_hash', '')
        title = item.get('title', '')
        quality_score = item.get('quality_score')
        quality_passed = item.get('quality_passed', True)
        
        # Extract content hash (remove sha256: prefix)
        content_hash = text_hash.replace('sha256:', '') if text_hash else None
        
        try:
            # Try to find existing document by content hash (deduplication)
            existing_doc = None
            if content_hash:
                existing_doc = find_document_by_content(job_id, content_hash)
            
            if existing_doc:
                # Same content, different URL - add as alias
                item['document_id'] = existing_doc['id']
                item['is_duplicate'] = True
                
                # Add this URL as an alias
                add_document_url(
                    document_id=existing_doc['id'],
                    job_id=job_id,
                    url=url,
                    canonical_url=canonical_url,
                    match_reason='content_hash',
                    is_primary=False
                )
                
                logger.debug(f"Found duplicate content: {url} -> doc {existing_doc['id']}")
            else:
                # New document
                doc = create_document(
                    job_id=job_id,
                    url=url,
                    canonical_url=canonical_url,
                    title=title,
                    content_hash=content_hash,
                    quality_score=quality_score,
                    quality_passed=quality_passed,
                )
                item['document_id'] = doc['id']
                item['is_duplicate'] = False
        
        except Exception as e:
            logger.warning(f"Error in document identity pipeline: {e}")
            item['document_id'] = None
            item['is_duplicate'] = False
        
        return item


class BudgetControlPipeline:
    """Pipeline to enforce quality-based budget limits."""
    
    def __init__(self):
        self.quality_pages_count = 0
        self.total_pages_count = 0
    
    def open_spider(self, spider):
        """Initialize budget tracking."""
        self.max_quality_pages = getattr(spider, 'max_pages', settings.DEFAULT_MAX_PAGES)
        spider.budget_pipeline = self
    
    def process_item(self, item, spider):
        """Track quality pages against budget."""
        self.total_pages_count += 1
        
        quality_passed = item.get('quality_passed', True)
        is_duplicate = item.get('is_duplicate', False)
        
        # Only count quality, non-duplicate pages toward budget
        if quality_passed and not is_duplicate:
            self.quality_pages_count += 1
            item['counts_toward_budget'] = True
        else:
            item['counts_toward_budget'] = False
        
        # Check if we've hit the quality budget
        if self.quality_pages_count >= self.max_quality_pages:
            logger.info(f"Quality budget reached: {self.quality_pages_count} quality pages "
                       f"(total: {self.total_pages_count})")
            spider.crawler.engine.close_spider(spider, 'quality_budget_reached')
        
        return item
    
    def close_spider(self, spider):
        """Log final budget stats."""
        logger.info(f"Budget stats: {self.quality_pages_count} quality pages, "
                   f"{self.total_pages_count} total pages")


class CrawlLogPipeline:
    """Pipeline to log crawl events to database for debugging."""
    
    def process_item(self, item, spider):
        """Log crawl event to database."""
        if not HAS_FRONTIER:
            return item
        
        job_id = getattr(spider, 'job_id', 'unknown')
        
        try:
            log_crawl_event(
                job_id=job_id,
                url=item.get('url', ''),
                canonical_url=item.get('canonical_url'),
                status_code=item.get('status_code'),
                stage='stored',
                extraction_mode=item.get('extraction_mode'),
                quality_score=item.get('quality_score'),
                depth=item.get('depth'),
            )
        except Exception as e:
            logger.debug(f"Error logging crawl event: {e}")
        
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
            'quality_score': item.get('quality_score'),
            'quality_passed': item.get('quality_passed'),
            'quality_reasons': item.get('quality_reasons', []),
            'document_id': item.get('document_id'),
            'is_duplicate': item.get('is_duplicate', False),
            'counts_toward_budget': item.get('counts_toward_budget', True),
            'error': item.get('error'),
        }
        
        # Remove HTML from memory
        if 'html' in item:
            del item['html']
        
        line = json.dumps(record, ensure_ascii=False)
        self.file.write(line + '\n')
        self.file.flush()
        
        self.items_count += 1
        
        return item
