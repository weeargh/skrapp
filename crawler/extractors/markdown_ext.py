"""Markdown extractor - converts HTML to markdown with proper links."""
from __future__ import annotations

import re
from typing import Optional, List, Dict
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag


def extract_markdown(html: str, base_url: str) -> tuple[str, List[Dict]]:
    """
    Convert HTML to markdown, preserving links and structure.
    
    Args:
        html: The HTML content
        base_url: Base URL for resolving relative links
    
    Returns:
        (markdown_text, sections) where sections is a list of {id, title, level}
    """
    if not html:
        return '', []
    
    try:
        soup = BeautifulSoup(html, 'lxml')
        
        # Remove unwanted elements
        for tag in soup(['script', 'style', 'noscript', 'nav', 'header', 'footer', 
                         'aside', 'iframe', 'form', 'button']):
            tag.decompose()
        
        # Find main content area
        main = (soup.find('main') or 
                soup.find('article') or 
                soup.find(class_=re.compile(r'content|main|body', re.I)) or
                soup.find('body') or
                soup)
        
        # Extract sections (headings with IDs)
        sections = _extract_sections(main, base_url)
        
        # Convert to markdown
        markdown = _html_to_markdown(main, base_url)
        
        # Clean up whitespace
        markdown = _clean_markdown(markdown)
        
        return markdown, sections
        
    except Exception as e:
        return f'[Error extracting markdown: {e}]', []


def _extract_sections(soup: Tag, base_url: str) -> List[Dict]:
    """Extract heading sections with their anchors."""
    sections = []
    
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        level = int(heading.name[1])
        title = heading.get_text(strip=True)
        
        # Get anchor ID
        anchor_id = heading.get('id')
        if not anchor_id:
            # Check for nested anchor
            anchor = heading.find('a', id=True)
            if anchor:
                anchor_id = anchor.get('id')
            else:
                anchor = heading.find('a', {'name': True})
                if anchor:
                    anchor_id = anchor.get('name')
        
        if title:
            section = {
                'level': level,
                'title': title,
                'anchor': f'{base_url}#{anchor_id}' if anchor_id else base_url
            }
            sections.append(section)
    
    return sections


def _html_to_markdown(element: Tag, base_url: str) -> str:
    """Convert an HTML element to markdown."""
    if isinstance(element, str):
        return element
    
    if not hasattr(element, 'name'):
        return str(element)
    
    tag = element.name
    
    # Handle specific tags
    if tag is None:
        # NavigableString or similar
        return element.get_text()
    
    if tag in ['script', 'style', 'noscript']:
        return ''
    
    if tag == 'br':
        return '\n'
    
    if tag == 'hr':
        return '\n---\n'
    
    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        text = element.get_text(strip=True)
        anchor_id = element.get('id', '')
        if anchor_id:
            return f'\n{"#" * level} {text} {{#{anchor_id}}}\n\n'
        return f'\n{"#" * level} {text}\n\n'
    
    if tag == 'p':
        content = _process_children(element, base_url)
        return f'\n{content}\n'
    
    if tag == 'a':
        href = element.get('href', '')
        text = element.get_text(strip=True)
        if href:
            # Resolve relative URLs
            if not href.startswith(('http://', 'https://', 'mailto:', '#')):
                href = urljoin(base_url, href)
            return f'[{text}]({href})'
        return text
    
    if tag == 'img':
        src = element.get('src', '')
        alt = element.get('alt', '')
        if src:
            if not src.startswith(('http://', 'https://')):
                src = urljoin(base_url, src)
            return f'![{alt}]({src})'
        return ''
    
    if tag in ['strong', 'b']:
        content = _process_children(element, base_url)
        return f'**{content}**'
    
    if tag in ['em', 'i']:
        content = _process_children(element, base_url)
        return f'*{content}*'
    
    if tag == 'code':
        content = element.get_text()
        if '\n' in content:
            return f'\n```\n{content}\n```\n'
        return f'`{content}`'
    
    if tag == 'pre':
        code = element.find('code')
        if code:
            lang = ''
            classes = code.get('class', [])
            for cls in classes:
                if cls.startswith('language-'):
                    lang = cls[9:]
                    break
            content = code.get_text()
            return f'\n```{lang}\n{content}\n```\n'
        return f'\n```\n{element.get_text()}\n```\n'
    
    if tag == 'blockquote':
        content = _process_children(element, base_url)
        lines = content.strip().split('\n')
        quoted = '\n'.join(f'> {line}' for line in lines)
        return f'\n{quoted}\n'
    
    if tag == 'ul':
        items = []
        for li in element.find_all('li', recursive=False):
            content = _process_children(li, base_url).strip()
            items.append(f'- {content}')
        return '\n' + '\n'.join(items) + '\n'
    
    if tag == 'ol':
        items = []
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            content = _process_children(li, base_url).strip()
            items.append(f'{i}. {content}')
        return '\n' + '\n'.join(items) + '\n'
    
    if tag == 'table':
        return _table_to_markdown(element, base_url)
    
    if tag in ['div', 'section', 'article', 'main', 'span']:
        return _process_children(element, base_url)
    
    # Default: process children
    return _process_children(element, base_url)


def _process_children(element: Tag, base_url: str) -> str:
    """Process all children of an element."""
    result = []
    for child in element.children:
        if isinstance(child, str):
            result.append(child)
        elif hasattr(child, 'name'):
            result.append(_html_to_markdown(child, base_url))
    return ''.join(result)


def _table_to_markdown(table: Tag, base_url: str) -> str:
    """Convert an HTML table to markdown."""
    rows = []
    
    # Get headers
    headers = []
    thead = table.find('thead')
    if thead:
        for th in thead.find_all(['th', 'td']):
            headers.append(_process_children(th, base_url).strip())
    else:
        # First row might be headers
        first_row = table.find('tr')
        if first_row:
            for cell in first_row.find_all(['th', 'td']):
                headers.append(_process_children(cell, base_url).strip())
    
    if not headers:
        return ''
    
    rows.append('| ' + ' | '.join(headers) + ' |')
    rows.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
    
    # Get body rows
    tbody = table.find('tbody') or table
    for tr in tbody.find_all('tr'):
        cells = []
        for td in tr.find_all(['td', 'th']):
            cells.append(_process_children(td, base_url).strip())
        if cells and len(cells) == len(headers):
            rows.append('| ' + ' | '.join(cells) + ' |')
    
    return '\n' + '\n'.join(rows) + '\n'


def _clean_markdown(text: str) -> str:
    """Clean up markdown text."""
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove trailing whitespace from lines
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    # Remove leading/trailing whitespace
    text = text.strip()
    return text


def extract_breadcrumbs(soup: BeautifulSoup, base_url: str) -> List[Dict]:
    """
    Extract breadcrumb navigation from the page.
    
    Returns:
        List of {title, url} dictionaries
    """
    breadcrumbs = []
    
    # Common breadcrumb patterns
    bc_selectors = [
        'nav[aria-label*="breadcrumb"]',
        '.breadcrumb',
        '.breadcrumbs', 
        '[class*="breadcrumb"]',
        'ol.breadcrumb',
        'ul.breadcrumb',
    ]
    
    bc_container = None
    for selector in bc_selectors:
        bc_container = soup.select_one(selector)
        if bc_container:
            break
    
    if bc_container:
        for link in bc_container.find_all('a'):
            href = link.get('href', '')
            title = link.get_text(strip=True)
            if title:
                if href and not href.startswith(('http://', 'https://')):
                    href = urljoin(base_url, href)
                breadcrumbs.append({
                    'title': title,
                    'url': href or base_url
                })
    
    return breadcrumbs


def extract_last_modified(soup: BeautifulSoup, response_headers: dict = None) -> Optional[str]:
    """
    Extract last modified date from page or headers.
    
    Returns:
        ISO date string or None
    """
    # Check HTTP headers first
    if response_headers:
        last_mod = response_headers.get('Last-Modified')
        if last_mod:
            return last_mod
    
    # Check meta tags
    meta_patterns = [
        {'name': 'last-modified'},
        {'property': 'article:modified_time'},
        {'property': 'og:updated_time'},
        {'name': 'date'},
        {'name': 'dcterms.modified'},
    ]
    
    for pattern in meta_patterns:
        meta = soup.find('meta', pattern)
        if meta and meta.get('content'):
            return meta.get('content')
    
    # Check for visible dates
    date_patterns = [
        r'(?:Last )?[Uu]pdated:?\s*(\d{4}-\d{2}-\d{2})',
        r'(?:Last )?[Mm]odified:?\s*(\d{4}-\d{2}-\d{2})',
    ]
    
    text = soup.get_text()
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    
    return None
