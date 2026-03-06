"""Helpers for discovering URLs from XML sitemaps."""
from __future__ import annotations

from collections import deque
import logging
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from crawler.url_utils import canonicalize_url, is_url_in_scope
from config import settings


logger = logging.getLogger(__name__)


def discover_sitemap_urls(
    start_url: str,
    allowed_host: str,
    allowed_path_prefix: str | None,
    ignore_prefixes: list[str] | None = None,
) -> list[str]:
    """Return in-scope URLs discovered from the site's sitemap, if available."""
    ignore_prefixes = ignore_prefixes or []
    sitemap_queue = deque(_candidate_sitemaps(start_url))
    visited_sitemaps: set[str] = set()
    seen_urls: set[str] = set()
    urls: list[str] = []

    while sitemap_queue:
        sitemap_url = sitemap_queue.popleft()
        canonical_sitemap = canonicalize_url(sitemap_url)
        if canonical_sitemap in visited_sitemaps:
            continue
        visited_sitemaps.add(canonical_sitemap)

        xml_text = _fetch_text(sitemap_url)
        if not xml_text:
            continue

        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as e:
            logger.debug("Failed to parse sitemap %s: %s", sitemap_url, e)
            continue

        tag_name = _local_name(root.tag)
        locations = [loc.text.strip() for loc in root.findall(".//{*}loc") if loc.text and loc.text.strip()]
        if tag_name == "sitemapindex":
            sitemap_queue.extend(locations)
            continue

        if tag_name != "urlset":
            continue

        for location in locations:
            if not is_url_in_scope(
                location,
                allowed_host,
                ignore_prefixes,
                settings.EXCLUDED_EXTENSIONS,
                allowed_path_prefix,
            ):
                continue
            canonical_url = canonicalize_url(location)
            if canonical_url in seen_urls:
                continue
            seen_urls.add(canonical_url)
            urls.append(location)

    return urls


def _candidate_sitemaps(start_url: str) -> list[str]:
    """Find sitemap URLs from robots.txt, falling back to /sitemap.xml."""
    parsed = urlparse(start_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{base}/robots.txt"
    sitemap_urls: list[str] = []

    robots_text = _fetch_text(robots_url)
    if robots_text:
        for line in robots_text.splitlines():
            if line.lower().startswith("sitemap:"):
                location = line.split(":", 1)[1].strip()
                if location:
                    sitemap_urls.append(location)

    if not sitemap_urls:
        sitemap_urls.append(f"{base}/sitemap.xml")

    return sitemap_urls


def _fetch_text(url: str) -> str | None:
    """Fetch a URL as text."""
    request = Request(url, headers={"User-Agent": settings.CRAWLER_USER_AGENT})
    try:
        with urlopen(request, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except Exception as e:
        logger.debug("Failed to fetch %s: %s", url, e)
        return None


def _local_name(tag: str) -> str:
    """Return the non-namespaced XML tag name."""
    return tag.rsplit("}", 1)[-1]
