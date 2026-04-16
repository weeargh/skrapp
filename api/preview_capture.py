"""Server-side screenshot capture for preview pages."""
from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime, timezone
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

from config import settings
from crawler.blocking_signals import detect_captcha, detect_waf


ARTICLE_PATH_PATTERN = re.compile(r"(\/articles\/|\/sections\/|\/categories\/|\/docs\/|\/guide\/|\/help\/)")
URL_PATTERN = re.compile(r"https?:\/\/[^\s)>\"']+")


def screenshot_artifact_paths(job_id: str, page_id: str) -> tuple[str, str]:
    """Return screenshot and metadata paths for a preview page."""
    output_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id, "preview-screenshots")
    os.makedirs(output_dir, exist_ok=True)
    return (
        os.path.join(output_dir, f"{page_id}.jpg"),
        os.path.join(output_dir, f"{page_id}.json"),
    )


def resolve_display_url(page: dict) -> str:
    """Resolve the most likely real content URL for a page."""
    current_url = page.get("url") or page.get("canonical_url") or ""
    if "/related/click" not in current_url:
        return current_url

    content = f"{page.get('clean_markdown') or ''}\n{page.get('raw_markdown') or ''}"
    candidates = extract_urls_from_text(content)
    current_host = host_for_url(current_url)

    preferred = next(
        (
            candidate for candidate in candidates
            if candidate != current_url
            and "/related/click" not in candidate
            and (not current_host or host_for_url(candidate) == current_host)
            and ARTICLE_PATH_PATTERN.search(path_for_url(candidate) or "")
        ),
        None,
    )
    if preferred:
        return preferred

    same_host = next(
        (
            candidate for candidate in candidates
            if candidate != current_url
            and "/related/click" not in candidate
            and (not current_host or host_for_url(candidate) == current_host)
        ),
        None,
    )
    return same_host or current_url


def ensure_page_screenshot(job_id: str, page: dict, force_refresh: bool = False) -> tuple[str, dict]:
    """Create or reuse a cached page screenshot."""
    screenshot_path, metadata_path = screenshot_artifact_paths(job_id, page["id"])
    display_url = resolve_display_url(page)
    if not display_url:
        raise ValueError("No content URL is available for this page")

    cached = _read_metadata(metadata_path)
    if (
        not force_refresh
        and os.path.exists(screenshot_path)
        and cached.get("display_url") == display_url
    ):
        return screenshot_path, cached

    metadata = _capture_screenshot(screenshot_path, display_url)
    metadata.update({
        "job_id": job_id,
        "page_id": page["id"],
        "page_url": page.get("url"),
        "canonical_url": page.get("canonical_url"),
        "display_url": display_url,
    })
    with open(metadata_path, "w", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=True, indent=2)

    return screenshot_path, metadata


def _capture_screenshot(output_path: str, target_url: str) -> dict:
    """Capture a full-page browser screenshot to disk."""
    viewport = {
        "width": settings.PREVIEW_SCREENSHOT_WIDTH,
        "height": settings.PREVIEW_SCREENSHOT_HEIGHT,
    }

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        context = browser.new_context(
            user_agent=f"{settings.CRAWLER_USER_AGENT} (preview screenshot)",
            viewport=viewport,
            java_script_enabled=True,
            ignore_https_errors=True,
        )
        page = context.new_page()
        try:
            response = page.goto(
                target_url,
                wait_until="domcontentloaded",
                timeout=settings.PREVIEW_SCREENSHOT_TIMEOUT_MS,
            )
            _wait_for_content(page)
            status_code = response.status if response else 0
            final_url = page.url
            title = page.title() or ""
            html = page.content()

            _prepare_page_for_capture(page)

            directory = os.path.dirname(output_path)
            fd, temp_path = tempfile.mkstemp(prefix="preview-", suffix=".jpg", dir=directory)
            os.close(fd)
            try:
                page.screenshot(
                    path=temp_path,
                    type="jpeg",
                    quality=settings.PREVIEW_SCREENSHOT_QUALITY,
                    full_page=True,
                    animations="disabled",
                )
                os.replace(temp_path, output_path)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

            return {
                "captured_at": datetime.now(timezone.utc).isoformat(),
                "status_code": status_code,
                "final_url": final_url,
                "title": title,
                "blocked_signals": blocking_signals(html),
            }
        finally:
            page.close()
            context.close()
            browser.close()


def _wait_for_content(page) -> None:
    """Wait briefly for dynamic content or challenge pages to settle."""
    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except Exception:
        pass

    total_waited = 0
    while total_waited < settings.PREVIEW_SCREENSHOT_EXTRA_WAIT_MS:
        page.wait_for_timeout(1_500)
        total_waited += 1_500
        if not blocking_signals(page.content()):
            break


def _prepare_page_for_capture(page) -> None:
    """Disable motion for a more stable screenshot."""
    try:
        page.add_style_tag(content="""
            *,
            *::before,
            *::after {
              animation-duration: 0s !important;
              animation-delay: 0s !important;
              transition-duration: 0s !important;
              scroll-behavior: auto !important;
            }
            html {
              scroll-behavior: auto !important;
            }
        """)
    except Exception:
        return


def blocking_signals(html: str) -> list[str]:
    """Return detected blocking signals for rendered HTML."""
    signals: list[str] = []
    is_captcha, captcha_patterns = detect_captcha(html)
    if is_captcha:
        signals.extend(captcha_patterns)
    is_waf, waf_patterns = detect_waf(html)
    if is_waf:
        signals.extend(waf_patterns)
    return sorted(set(signals))


def _read_metadata(path: str) -> dict:
    """Read screenshot metadata if present."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def extract_urls_from_text(value: str) -> list[str]:
    """Extract unique URLs from text."""
    seen: set[str] = set()
    urls: list[str] = []
    for match in URL_PATTERN.findall(value or ""):
        if match in seen:
            continue
        seen.add(match)
        urls.append(match)
    return urls


def host_for_url(url: str) -> str:
    """Return a URL host."""
    try:
        return urlparse(url).netloc
    except Exception:
        return ""


def path_for_url(url: str) -> str:
    """Return a URL path."""
    try:
        return urlparse(url).path
    except Exception:
        return ""
