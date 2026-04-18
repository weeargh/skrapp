"""Zendesk Help Center API client for MekariRAG mode."""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field

import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

_PAGE_SIZE = 100
_MAX_RETRIES = 6
_RETRY_STATUSES = {500, 502, 503, 504}
# Backoff schedule (seconds) for 5xx errors: 5, 10, 20, 40, 80, 160
_BACKOFF_BASE = 5


@dataclass
class ZendeskArticle:
    id: int
    url: str
    html_url: str
    title: str
    body: str
    locale: str
    section_id: int | None
    author_id: int | None
    author_name: str | None
    label_names: list[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""
    draft: bool = False


@dataclass
class ZendeskSection:
    id: int
    name: str
    category_id: int


@dataclass
class ZendeskCategory:
    id: int
    name: str


class ZendeskFetcher:
    """Fetch articles, sections, and categories from the Zendesk Help Center API.

    Rate-limit handling:
    - ``request_delay`` seconds are injected between every paged request.
    - HTTP 429 responses are retried after the ``Retry-After`` header value
      (default 60 s if the header is absent).
    - HTTP 5xx responses are retried with exponential back-off.
    - Both retry loops respect ``_MAX_RETRIES``.
    """

    def __init__(
        self,
        base_url: str,
        locale: str = "id",
        email: str | None = None,
        api_token: str | None = None,
        timeout: int = 30,
        request_delay: float = 1.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.locale = locale
        self.timeout = timeout
        self.request_delay = request_delay
        self._session = requests.Session()
        self._session.headers.update({
            "Accept": "application/json",
            "User-Agent": "SkrappBot/1.0 (MekariRAG)",
        })
        if email and api_token:
            self._session.auth = (f"{email}/token", api_token)

    # ------------------------------------------------------------------
    # Public fetch methods
    # ------------------------------------------------------------------

    def fetch_articles(self) -> list[ZendeskArticle]:
        """Return all published articles (paginated, rate-limit safe)."""
        url: str | None = (
            f"{self.base_url}/api/v2/help_center/{self.locale}/articles.json"
        )
        params: dict | None = {
            "per_page": _PAGE_SIZE,
            "sort_by": "created_at",
            "sort_order": "asc",
        }
        articles: list[ZendeskArticle] = []

        page = 1
        while url:
            logger.debug("Fetching articles page %d …", page)
            data = self._get(url, params=params)
            params = None  # params are embedded in next_page URL
            for item in data.get("articles", []):
                if not item.get("draft"):
                    articles.append(_parse_article(item))
            url = data.get("next_page") or None
            page += 1
            if url:
                time.sleep(self.request_delay)

        logger.info("Fetched %d articles from %s", len(articles), self.base_url)
        return articles

    def fetch_article(self, article_id: int) -> ZendeskArticle | None:
        """Fetch one article by ID (full body included)."""
        url = (
            f"{self.base_url}/api/v2/help_center"
            f"/{self.locale}/articles/{article_id}.json"
        )
        try:
            data = self._get(url)
            return _parse_article(data.get("article") or data)
        except Exception as exc:
            logger.warning("Failed to fetch article %d: %s", article_id, exc)
            return None

    def fetch_sections(self) -> dict[int, ZendeskSection]:
        """Return all sections keyed by section ID."""
        return self._fetch_paged(
            f"{self.base_url}/api/v2/help_center/{self.locale}/sections.json",
            "sections",
            lambda item: ZendeskSection(
                id=item["id"],
                name=item.get("name") or "",
                category_id=item.get("category_id") or 0,
            ),
        )

    def fetch_categories(self) -> dict[int, ZendeskCategory]:
        """Return all categories keyed by category ID."""
        return self._fetch_paged(
            f"{self.base_url}/api/v2/help_center/{self.locale}/categories.json",
            "categories",
            lambda item: ZendeskCategory(
                id=item["id"],
                name=item.get("name") or "",
            ),
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _fetch_paged(self, start_url: str, key: str, factory) -> dict:
        url: str | None = start_url
        params: dict | None = {"per_page": _PAGE_SIZE}
        result = {}
        while url:
            data = self._get(url, params=params)
            params = None
            for item in data.get(key, []):
                obj = factory(item)
                result[obj.id] = obj
            url = data.get("next_page") or None
            if url:
                time.sleep(self.request_delay)
        return result

    def _get(self, url: str, params: dict | None = None) -> dict:
        """GET with 429 back-off and 5xx exponential retry."""
        for attempt in range(_MAX_RETRIES):
            try:
                response = self._session.get(url, params=params, timeout=self.timeout)
            except RequestException as exc:
                if attempt == _MAX_RETRIES - 1:
                    raise
                wait = _BACKOFF_BASE * (2 ** attempt)
                logger.warning(
                    "Request error (attempt %d/%d): %s — retrying in %ds",
                    attempt + 1, _MAX_RETRIES, exc, wait,
                )
                time.sleep(wait)
                continue

            # 429 — respect Retry-After
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After") or 60)
                logger.warning(
                    "HTTP 429 rate-limited (attempt %d/%d). "
                    "Sleeping %ds (Retry-After header).",
                    attempt + 1, _MAX_RETRIES, retry_after,
                )
                time.sleep(retry_after)
                continue

            # 5xx — exponential back-off
            if response.status_code in _RETRY_STATUSES:
                if attempt == _MAX_RETRIES - 1:
                    response.raise_for_status()
                wait = _BACKOFF_BASE * (2 ** attempt)
                logger.warning(
                    "HTTP %d (attempt %d/%d). Retrying in %ds.",
                    response.status_code, attempt + 1, _MAX_RETRIES, wait,
                )
                time.sleep(wait)
                continue

            # Any other 4xx — raise immediately, no point retrying
            response.raise_for_status()
            return response.json()

        raise RuntimeError(f"All {_MAX_RETRIES} attempts failed for {url}")


def make_zendesk_fetcher(
    base_url: str,
    locale: str = "id",
    request_delay: float = 1.0,
) -> ZendeskFetcher:
    """Construct a fetcher, picking up optional auth from environment variables."""
    email = os.environ.get("ZENDESK_API_EMAIL") or None
    api_token = os.environ.get("ZENDESK_API_TOKEN") or None
    return ZendeskFetcher(
        base_url=base_url,
        locale=locale,
        email=email,
        api_token=api_token,
        request_delay=request_delay,
    )


def _parse_article(item: dict) -> ZendeskArticle:
    return ZendeskArticle(
        id=item["id"],
        url=item.get("url") or "",
        html_url=item.get("html_url") or "",
        title=item.get("title") or "",
        body=item.get("body") or "",
        locale=item.get("locale") or "",
        section_id=item.get("section_id"),
        author_id=item.get("author_id"),
        author_name=item.get("author_name"),
        label_names=item.get("label_names") or [],
        created_at=item.get("created_at") or "",
        updated_at=item.get("updated_at") or "",
        draft=bool(item.get("draft", False)),
    )
