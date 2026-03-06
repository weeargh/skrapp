"""Crawl4AI-backed page fetch session for discovery and extraction."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

from config import settings
from crawler.text_utils import markdown_to_text
from crawler.url_utils import canonicalize_url, is_url_in_scope


logger = logging.getLogger(__name__)


@dataclass
class Crawl4AIPageResult:
    """Structured result for one fetched page."""

    url: str
    final_url: str
    canonical_url: str
    status_code: int
    title: str
    html: str
    cleaned_html: str
    raw_markdown: str
    raw_text: str
    outlinks: list[str]
    meta: dict


class Crawl4AIPageSession:
    """Persistent Crawl4AI browser session for serial page processing."""

    def __init__(
        self,
        allowed_host: str,
        allowed_path_prefix: str | None,
        ignore_prefixes: list[str] | None = None,
    ):
        self.allowed_host = allowed_host.lower()
        self.allowed_path_prefix = allowed_path_prefix
        self.ignore_prefixes = ignore_prefixes or []
        self._loop: asyncio.AbstractEventLoop | None = None
        self._crawler: AsyncWebCrawler | None = None

    def __enter__(self) -> "Crawl4AIPageSession":
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._crawler = AsyncWebCrawler(
            config=BrowserConfig(
                headless=True,
                verbose=False,
                java_script_enabled=True,
                user_agent=settings.CRAWLER_USER_AGENT + " (crawl4ai)",
            )
        )
        self._loop.run_until_complete(self._crawler.__aenter__())
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if self._crawler and self._loop:
                self._loop.run_until_complete(self._crawler.__aexit__(exc_type, exc, tb))
        finally:
            if self._loop:
                self._loop.close()
            self._crawler = None
            self._loop = None
            asyncio.set_event_loop(None)

    def fetch_page(self, url: str) -> Crawl4AIPageResult:
        """Fetch one page, extract markdown, and collect accepted outlinks."""
        if not self._crawler or not self._loop:
            raise RuntimeError("Crawl4AIPageSession must be used as a context manager")
        return self._loop.run_until_complete(self._fetch_page_async(url))

    async def _fetch_page_async(self, url: str) -> Crawl4AIPageResult:
        config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(
                    min_word_threshold=settings.CRAWL4AI_MIN_WORD_THRESHOLD,
                    threshold=settings.CRAWL4AI_PRUNING_THRESHOLD,
                    threshold_type="fixed",
                )
            ),
            cache_mode=CacheMode.BYPASS,
            wait_until=settings.CRAWL4AI_WAIT_UNTIL,
            page_timeout=settings.CRAWL4AI_PAGE_TIMEOUT_MS,
            delay_before_return_html=settings.CRAWL4AI_DELAY_BEFORE_RETURN_HTML_SECONDS,
            remove_overlay_elements=True,
            excluded_tags=settings.CRAWL4AI_EXCLUDED_TAGS,
            exclude_external_links=True,
            verbose=False,
        )
        result = await self._crawler.arun(url, config=config)
        if not result.success:
            message = result.error_message or "unknown crawl4ai error"
            raise RuntimeError(f"Crawl4AI failed for {url}: {message}")

        final_url = result.url or url
        raw_markdown = getattr(result.markdown, "raw_markdown", None) or str(result.markdown or "")
        accepted_links = self._extract_links_from_html(result.html or "", final_url)
        if not accepted_links:
            accepted_links = self._extract_links(result.links or {})
        metadata = dict(result.metadata or {})
        metadata.update({
            "response_headers": dict(result.response_headers or {}),
            "content_filter": "pruning",
            "fit_markdown_length": len(getattr(result.markdown, "fit_markdown", "") or ""),
        })

        return Crawl4AIPageResult(
            url=url,
            final_url=final_url,
            canonical_url=canonicalize_url(final_url),
            status_code=result.status_code or 0,
            title=metadata.get("title") or "",
            html=result.html or "",
            cleaned_html=result.cleaned_html or "",
            raw_markdown=raw_markdown,
            raw_text=markdown_to_text(raw_markdown),
            outlinks=accepted_links,
            meta=metadata,
        )

    def _extract_links(self, links: dict) -> list[str]:
        """Filter internal links using the existing URL scope rules."""
        accepted: list[str] = []
        seen: set[str] = set()
        for item in links.get("internal", []):
            href = item.get("href")
            if not href:
                continue
            if not is_url_in_scope(
                href,
                self.allowed_host,
                self.ignore_prefixes,
                settings.EXCLUDED_EXTENSIONS,
                self.allowed_path_prefix,
            ):
                continue
            canonical = canonicalize_url(href)
            if canonical in seen:
                continue
            seen.add(canonical)
            accepted.append(href)
        return accepted

    def _extract_links_from_html(self, html: str, base_url: str) -> list[str]:
        """Extract in-scope links from the full rendered HTML."""
        if not html:
            return []

        accepted: list[str] = []
        seen: set[str] = set()

        try:
            soup = BeautifulSoup(html, "lxml")
        except Exception as e:
            logger.debug("Failed to parse HTML links from %s: %s", base_url, e)
            return []

        for anchor in soup.select("a[href]"):
            href = (anchor.get("href") or "").strip()
            if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue

            absolute_href = urljoin(base_url, href)
            if not is_url_in_scope(
                absolute_href,
                self.allowed_host,
                self.ignore_prefixes,
                settings.EXCLUDED_EXTENSIONS,
                self.allowed_path_prefix,
            ):
                continue

            canonical = canonicalize_url(absolute_href)
            if canonical == canonicalize_url(base_url):
                continue
            if canonical in seen:
                continue

            seen.add(canonical)
            accepted.append(absolute_href)

        return accepted
