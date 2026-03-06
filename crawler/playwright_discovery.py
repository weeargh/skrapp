"""Playwright-based page discovery for the MVP crawler."""
from __future__ import annotations

from dataclasses import dataclass
import logging
from typing import List

from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from config import settings
from crawler.url_utils import canonicalize_url, is_url_in_scope


logger = logging.getLogger(__name__)


@dataclass
class DiscoveryResult:
    """Result of discovering a single page."""

    url: str
    final_url: str
    canonical_url: str
    status_code: int
    title: str
    html: str
    outlinks: List[str]


class PlaywrightDiscoverySession:
    """Reusable Playwright browser/context for page discovery."""

    def __init__(
        self,
        allowed_host: str,
        allowed_path_prefix: str | None,
        ignore_prefixes: list[str] | None = None,
    ):
        self.allowed_host = allowed_host.lower()
        self.allowed_path_prefix = allowed_path_prefix
        self.ignore_prefixes = ignore_prefixes or []
        self._playwright = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None

    def __enter__(self) -> "PlaywrightDiscoverySession":
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        self._context = self._browser.new_context(
            user_agent=settings.CRAWLER_USER_AGENT + " (discovery)",
            viewport={"width": 1280, "height": 720},
            java_script_enabled=True,
        )
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._context:
            self._context.close()
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()

    def discover(self, url: str) -> DiscoveryResult:
        """Load a page and return rendered HTML plus filtered links."""
        if not self._context:
            raise RuntimeError("PlaywrightDiscoverySession must be used as a context manager")

        page: Page | None = None
        try:
            page = self._context.new_page()
            response = page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=settings.PLAYWRIGHT_PAGE_TIMEOUT_MS,
            )
            page.wait_for_timeout(settings.PLAYWRIGHT_DISCOVERY_WAIT_MS)

            final_url = page.url
            status_code = response.status if response else 0
            html = page.content()
            title = page.title() or ""
            outlinks = self._extract_links(page, final_url)

            return DiscoveryResult(
                url=url,
                final_url=final_url,
                canonical_url=canonicalize_url(final_url),
                status_code=status_code,
                title=title,
                html=html,
                outlinks=outlinks,
            )
        finally:
            if page:
                try:
                    page.close()
                except Exception as e:
                    logger.debug("Failed to close Playwright page: %s", e)

    def _extract_links(self, page: Page, base_url: str) -> List[str]:
        """Extract visible in-scope links from the page."""
        links: list[str] = []
        seen: set[str] = set()
        try:
            hrefs = page.eval_on_selector_all(
                "a[href]",
                "elements => elements.map(e => e.href).filter(Boolean)",
            )
            for href in hrefs:
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
                links.append(href)
        except Exception as e:
            logger.debug("Failed to extract links from %s: %s", base_url, e)
        return links
