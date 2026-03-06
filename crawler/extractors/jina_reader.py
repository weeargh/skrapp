"""Jina Reader extractor integration."""
from __future__ import annotations

from dataclasses import dataclass
import logging
import re
from urllib import error, request

from config import settings


logger = logging.getLogger(__name__)


@dataclass
class JinaExtractionResult:
    """Structured result for extracted content."""

    url: str
    markdown: str
    text: str
    meta: dict


def extract_url(url: str) -> JinaExtractionResult:
    """Fetch markdown from Jina Reader and derive plain text."""
    reader_url = settings.JINA_READER_BASE_URL.rstrip("/") + "/" + url
    headers = {
        "x-respond-with": "markdown",
        "User-Agent": settings.CRAWLER_USER_AGENT + " (jina-reader)",
    }
    if settings.JINA_READER_TARGET_SELECTOR:
        headers["x-target-selector"] = settings.JINA_READER_TARGET_SELECTOR
    if settings.JINA_READER_WAIT_FOR_SELECTOR:
        headers["x-wait-for-selector"] = settings.JINA_READER_WAIT_FOR_SELECTOR

    req = request.Request(reader_url, headers=headers, method="GET")
    try:
        with request.urlopen(req, timeout=settings.JINA_READER_TIMEOUT_SECONDS) as response:
            body = response.read().decode("utf-8", errors="replace")
            meta = {
                "reader_url": reader_url,
                "status_code": getattr(response, "status", 200),
                "content_type": response.headers.get("Content-Type"),
            }
            return JinaExtractionResult(
                url=url,
                markdown=body,
                text=markdown_to_text(body),
                meta=meta,
            )
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
        raise RuntimeError(
            f"Jina Reader HTTP {e.code} for {url}: {body[:500]}"
        ) from e
    except error.URLError as e:
        raise RuntimeError(f"Jina Reader request failed for {url}: {e.reason}") from e


def markdown_to_text(markdown: str) -> str:
    """Convert markdown-ish content to plain text for the MVP."""
    text = markdown or ""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
