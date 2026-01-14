"""Job finalizer - deduplicates output and generates summary."""
import hashlib
import json
import logging
import os
import re
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urlparse

from config import settings
from config.constants import JobState, ArtifactKind, EventLevel, EventType
from crawler.url_utils import canonicalize_url
from db import queries


logger = logging.getLogger(__name__)


def finalize_job(job_id: str) -> bool:
    """
    Finalize a job by deduplicating output and generating summary.
    
    Returns:
        True if finalization succeeded, False otherwise
    """
    logger.info(f"Starting finalization for job {job_id}")
    
    job = queries.get_job_by_id(job_id)
    if not job:
        logger.error(f"Job {job_id} not found")
        return False
    
    queries.update_job_state(job_id, JobState.FINALIZING)
    
    job_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    raw_file = os.path.join(job_dir, 'pages.raw.jsonl')
    final_file = os.path.join(job_dir, 'pages.jsonl')
    summary_file = os.path.join(job_dir, 'summary.json')
    
    if not os.path.exists(raw_file):
        logger.warning(f"No raw file found for job {job_id}")
        _write_empty_summary(summary_file, job)
        queries.update_job_state(
            job_id,
            JobState.DONE,
            pages_exported=0
        )
        return True
    
    try:
        stats = _deduplicate_pages(raw_file, final_file)
        logger.info(f"Deduplication complete for job {job_id}: "
                   f"{stats['total_raw']} raw -> {stats['total_deduped']} deduped")
    except Exception as e:
        logger.error(f"Error during deduplication for job {job_id}: {e}")
        queries.update_job_state(
            job_id,
            JobState.FAILED,
            last_error=json.dumps({"reason": "finalization_failed", "message": str(e)})
        )
        return False
    
    try:
        summary = _generate_summary(job, stats, job_dir)
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        logger.info(f"Summary written for job {job_id}")
    except Exception as e:
        logger.error(f"Error writing summary for job {job_id}: {e}")
    
    # Generate knowledge base output (markdown files + manifest)
    try:
        kb_stats = _generate_knowledge_base_output(job_id, job_dir, final_file)
        logger.info(f"Knowledge base output generated: {kb_stats['pages_count']} pages")
    except Exception as e:
        logger.error(f"Error generating KB output for job {job_id}: {e}")
    
    try:
        _register_artifacts(job_id, job_dir)
    except Exception as e:
        logger.error(f"Error registering artifacts for job {job_id}: {e}")
    
    queries.update_job_state(
        job_id,
        JobState.DONE,
        pages_exported=stats['total_deduped']
    )
    
    queries.decrement_ip_concurrent(job['requester_ip_hash'])
    
    queries.insert_job_event(job_id, EventLevel.INFO, EventType.FINALIZE, {
        "pages_raw": stats['total_raw'],
        "pages_deduped": stats['total_deduped'],
        "duplicates_removed": stats['duplicates_removed']
    })
    
    logger.info(f"Finalization complete for job {job_id}")
    return True


def _deduplicate_pages(raw_file: str, final_file: str) -> dict:
    """
    Deduplicate pages by canonical URL, keeping the last occurrence.
    
    Returns:
        Stats dict with total_raw, total_deduped, duplicates_removed
    """
    pages_by_canonical = {}
    total_raw = 0
    
    with open(raw_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                record = json.loads(line)
                canonical = record.get('canonical_url') or canonicalize_url(record.get('url', ''))
                pages_by_canonical[canonical] = line
                total_raw += 1
            except json.JSONDecodeError:
                continue
    
    with open(final_file, 'w', encoding='utf-8') as f:
        for line in pages_by_canonical.values():
            f.write(line + '\n')
    
    total_deduped = len(pages_by_canonical)
    
    return {
        'total_raw': total_raw,
        'total_deduped': total_deduped,
        'duplicates_removed': total_raw - total_deduped
    }


def _generate_summary(job: dict, stats: dict, job_dir: str) -> dict:
    """Generate a summary of the crawl job."""
    status_codes = Counter()
    extraction_modes = Counter()
    text_lengths = []
    errors = []
    
    final_file = os.path.join(job_dir, 'pages.jsonl')
    
    if os.path.exists(final_file):
        with open(final_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    record = json.loads(line)
                    
                    status_codes[record.get('status_code', 0)] += 1
                    
                    mode = record.get('extraction_mode', 'unknown')
                    extraction_modes[mode] += 1
                    
                    text = record.get('text', '')
                    text_lengths.append(len(text))
                    
                    if record.get('error'):
                        errors.append({
                            'url': record.get('url'),
                            'error': record.get('error')
                        })
                except json.JSONDecodeError:
                    continue
    
    successful_extractions = sum(1 for length in text_lengths if length >= settings.MIN_TEXT_LENGTH_SUCCESS)
    extraction_success_rate = successful_extractions / len(text_lengths) if text_lengths else 0
    
    started_at = datetime.fromisoformat(job['started_at']) if job.get('started_at') else None
    finished_at = datetime.now(timezone.utc)
    duration_seconds = int((finished_at - started_at).total_seconds()) if started_at else 0
    
    summary = {
        'job_id': job['id'],
        'start_url': job['start_url'],
        'allowed_host': job['allowed_host'],
        'completed_at': finished_at.isoformat(),
        'duration_seconds': duration_seconds,
        'pages_fetched': stats['total_raw'],
        'pages_exported': stats['total_deduped'],
        'duplicates_removed': stats['duplicates_removed'],
        'status_code_distribution': dict(status_codes),
        'extraction_mode_distribution': dict(extraction_modes),
        'extraction_success_rate': round(extraction_success_rate, 3),
        'avg_text_length': round(sum(text_lengths) / len(text_lengths)) if text_lengths else 0,
        'crawler_strategy': job.get('crawler_strategy'),
        'fallback_occurred': job.get('fallback_retry_count', 0) > 0,
        'site_status': job.get('site_status'),
        'block_evidence': json.loads(job['block_evidence']) if job.get('block_evidence') else None,
        'restart_count': job['restart_count'],
        'last_errors': errors[-10:]
    }
    
    return summary


def _write_empty_summary(summary_file: str, job: dict):
    """Write an empty summary when no pages were fetched."""
    summary = {
        'job_id': job['id'],
        'start_url': job['start_url'],
        'allowed_host': job['allowed_host'],
        'completed_at': datetime.now(timezone.utc).isoformat(),
        'duration_seconds': 0,
        'pages_fetched': 0,
        'pages_exported': 0,
        'duplicates_removed': 0,
        'status_code_distribution': {},
        'extraction_mode_distribution': {},
        'extraction_success_rate': 0,
        'avg_text_length': 0,
        'crawler_strategy': job.get('crawler_strategy'),
        'fallback_occurred': job.get('fallback_retry_count', 0) > 0,
        'site_status': job.get('site_status'),
        'block_evidence': json.loads(job['block_evidence']) if job.get('block_evidence') else None,
        'restart_count': job['restart_count'],
        'last_errors': []
    }
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


def _register_artifacts(job_id: str, job_dir: str):
    """Register job artifacts in the database."""
    artifacts = [
        (ArtifactKind.PAGES_RAW_JSONL, 'pages.raw.jsonl'),
        (ArtifactKind.PAGES_JSONL, 'pages.jsonl'),
        (ArtifactKind.SUMMARY_JSON, 'summary.json'),
        (ArtifactKind.RUNNER_LOG, 'runner.log'),
        (ArtifactKind.CRAWLER_LOG, 'crawler.log'),
    ]
    
    for kind, filename in artifacts:
        filepath = os.path.join(job_dir, filename)
        
        if not os.path.exists(filepath):
            continue
        
        try:
            byte_size = os.path.getsize(filepath)
            
            sha256 = None
            if byte_size < 100 * 1024 * 1024:
                with open(filepath, 'rb') as f:
                    sha256 = hashlib.sha256(f.read()).hexdigest()
            
            queries.create_artifact(
                job_id=job_id,
                kind=kind,
                path=filepath,
                byte_size=byte_size,
                sha256=sha256
            )
        except Exception as e:
            logger.error(f"Error registering artifact {filename} for job {job_id}: {e}")


def _generate_knowledge_base_output(job_id: str, job_dir: str, final_file: str) -> dict:
    """
    Generate knowledge base output: individual markdown files + manifest.json.
    
    Structure:
        kb/
            manifest.json       # Index of all pages with metadata
            pages/
                page_001.md     # Individual markdown files
                page_002.md
                ...
    
    Each markdown file has YAML frontmatter with:
        - source_url: Original URL for citation
        - title: Page title
        - breadcrumbs: Navigation path
        - sections: List of section anchors
        - last_modified: When source was last updated
        - fetched_at: When we crawled it
    """
    kb_dir = os.path.join(job_dir, 'kb')
    pages_dir = os.path.join(kb_dir, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    
    manifest_pages = []
    page_count = 0
    
    if not os.path.exists(final_file):
        # Write empty manifest
        _write_manifest(kb_dir, job_id, [])
        return {'pages_count': 0}
    
    with open(final_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                record = json.loads(line)
                page_count += 1
                
                # Generate filename from URL
                filename = _url_to_filename(record.get('url', ''), page_count)
                filepath = os.path.join(pages_dir, filename)
                
                # Write markdown file with frontmatter
                _write_markdown_file(filepath, record)
                
                # Add to manifest
                manifest_entry = {
                    'id': f'page_{page_count:04d}',
                    'filename': f'pages/{filename}',
                    'source_url': record.get('url', ''),
                    'title': record.get('title', ''),
                    'breadcrumbs': record.get('breadcrumbs', []),
                    'sections': record.get('sections', []),
                    'last_modified': record.get('last_modified'),
                    'fetched_at': record.get('fetched_at'),
                    'text_length': len(record.get('markdown', '') or record.get('text', '')),
                }
                manifest_pages.append(manifest_entry)
                
            except json.JSONDecodeError:
                continue
    
    # Write manifest
    _write_manifest(kb_dir, job_id, manifest_pages)
    
    return {'pages_count': page_count}


def _url_to_filename(url: str, index: int) -> str:
    """Convert a URL to a safe filename."""
    try:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        if not path:
            path = 'index'
        
        # Clean up the path
        path = re.sub(r'[^\w\-/]', '_', path)
        path = path.replace('/', '_')
        path = re.sub(r'_+', '_', path)
        path = path[:80]  # Limit length
        
        if not path:
            path = f'page_{index:04d}'
        
        return f'{path}.md'
    except Exception:
        return f'page_{index:04d}.md'


def _write_markdown_file(filepath: str, record: dict):
    """Write a markdown file with YAML frontmatter."""
    url = record.get('url', '')
    title = record.get('title', '') or 'Untitled'
    markdown = record.get('markdown', '') or record.get('text', '')
    breadcrumbs = record.get('breadcrumbs', [])
    sections = record.get('sections', [])
    last_modified = record.get('last_modified')
    fetched_at = record.get('fetched_at')
    
    # Build frontmatter
    frontmatter_lines = [
        '---',
        f'source_url: "{url}"',
        f'title: "{_escape_yaml(title)}"',
    ]
    
    if breadcrumbs:
        bc_str = ' > '.join(bc.get('title', '') for bc in breadcrumbs)
        frontmatter_lines.append(f'breadcrumbs: "{_escape_yaml(bc_str)}"')
        frontmatter_lines.append('breadcrumbs_links:')
        for bc in breadcrumbs:
            frontmatter_lines.append(f'  - title: "{_escape_yaml(bc.get("title", ""))}"')
            frontmatter_lines.append(f'    url: "{bc.get("url", "")}"')
    
    if sections:
        frontmatter_lines.append('sections:')
        for sec in sections[:20]:  # Limit to first 20 sections
            frontmatter_lines.append(f'  - title: "{_escape_yaml(sec.get("title", ""))}"')
            frontmatter_lines.append(f'    anchor: "{sec.get("anchor", "")}"')
            frontmatter_lines.append(f'    level: {sec.get("level", 1)}')
    
    if last_modified:
        frontmatter_lines.append(f'last_modified: "{last_modified}"')
    
    if fetched_at:
        frontmatter_lines.append(f'fetched_at: "{fetched_at}"')
    
    frontmatter_lines.append('---')
    frontmatter_lines.append('')
    
    # Add title as H1 if not already in markdown
    if not markdown.strip().startswith('#'):
        frontmatter_lines.append(f'# {title}')
        frontmatter_lines.append('')
    
    # Add source citation at the end
    frontmatter_lines.append(markdown)
    frontmatter_lines.append('')
    frontmatter_lines.append('---')
    frontmatter_lines.append(f'*Source: [{url}]({url})*')
    
    content = '\n'.join(frontmatter_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def _escape_yaml(text: str) -> str:
    """Escape special characters for YAML string."""
    if not text:
        return ''
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')


def _write_manifest(kb_dir: str, job_id: str, pages: list):
    """Write the manifest.json file."""
    manifest = {
        'job_id': job_id,
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'format_version': '1.0',
        'total_pages': len(pages),
        'pages': pages
    }
    
    manifest_path = os.path.join(kb_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
