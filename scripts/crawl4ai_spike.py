#!/usr/bin/env python3
"""Run a standalone Crawl4AI spike and write comparable artifacts."""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from urllib.parse import urlparse

from crawl4ai import (
    AsyncWebCrawler,
    BFSDeepCrawlStrategy,
    BrowserConfig,
    CrawlerRunConfig,
    DomainFilter,
    FilterChain,
    URLPatternFilter,
)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from crawler.markdown_cleaner import clean_pages


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run a Crawl4AI spike crawl.")
    parser.add_argument("start_url", help="Root URL to crawl")
    parser.add_argument("--max-depth", type=int, default=2, help="Maximum crawl depth")
    parser.add_argument("--max-pages", type=int, default=25, help="Maximum pages to crawl")
    parser.add_argument(
        "--allowed-path-prefix",
        default=None,
        help="Optional path prefix to restrict the crawl, eg /hc/id",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Optional output directory; defaults to out/crawl4ai_spike/<slug>",
    )
    return parser.parse_args()


async def run_spike(
    start_url: str,
    max_depth: int,
    max_pages: int,
    allowed_path_prefix: str | None,
    output_dir: str,
):
    """Run the Crawl4AI spike and persist artifacts."""
    parsed = urlparse(start_url)
    hostname = parsed.hostname
    if not hostname:
        raise ValueError(f"Could not extract hostname from {start_url}")

    allowed_path_prefix = normalize_prefix(allowed_path_prefix) or derive_allowed_path_prefix(start_url)
    patterns = build_path_patterns(hostname, allowed_path_prefix)
    filter_chain = FilterChain([
        DomainFilter(allowed_domains=[hostname]),
        URLPatternFilter(patterns=patterns),
    ])

    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        verbose=False,
        stream=False,
        page_timeout=60000,
        wait_until="domcontentloaded",
        remove_overlay_elements=True,
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False,
            filter_chain=filter_chain,
        ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(start_url, config=run_config)

    os.makedirs(output_dir, exist_ok=True)
    pages = []
    nodes = []
    by_parent: dict[str | None, list[str]] = {}

    for index, result in enumerate(results):
        markdown = str(getattr(result, "markdown", "") or "")
        metadata = getattr(result, "metadata", {}) or {}
        url = getattr(result, "url", None) or start_url
        title = metadata.get("title")
        depth = metadata.get("depth", 0)
        parent_url = metadata.get("parent_url")
        page_id = f"page_{index:04d}"

        pages.append({
            "page_id": page_id,
            "url": url,
            "parent_url": parent_url,
            "depth": depth,
            "title": title,
            "success": getattr(result, "success", False),
            "raw_markdown": markdown,
            "markdown_length": len(markdown),
            "metadata": metadata,
        })
        by_parent.setdefault(parent_url, []).append(page_id)

    pages = clean_pages(pages, id_key="page_id", markdown_key="raw_markdown")

    root_page_id = None
    for page in pages:
        if page["parent_url"] is None and root_page_id is None:
            root_page_id = page["page_id"]
        nodes.append({
            "page_id": page["page_id"],
            "parent_url": page["parent_url"],
            "url": page["url"],
            "title": page["title"],
            "depth": page["depth"],
            "child_page_ids": by_parent.get(page["url"], []),
        })

    summary = {
        "start_url": start_url,
        "allowed_host": hostname,
        "allowed_path_prefix": allowed_path_prefix,
        "max_depth": max_depth,
        "max_pages": max_pages,
        "pages_returned": len(pages),
        "successful_pages": sum(1 for page in pages if page["success"]),
        "average_cleanup_score": round(
            sum(page["cleanup_score"] for page in pages) / max(1, len(pages)),
            3,
        ),
    }

    with open(os.path.join(output_dir, "summary.json"), "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, ensure_ascii=False)

    with open(os.path.join(output_dir, "tree.json"), "w", encoding="utf-8") as handle:
        json.dump(
            {
                "start_url": start_url,
                "root_page_id": root_page_id,
                "nodes": nodes,
            },
            handle,
            indent=2,
            ensure_ascii=False,
        )

    with open(os.path.join(output_dir, "pages.jsonl"), "w", encoding="utf-8") as handle:
        for page in pages:
            handle.write(json.dumps(page, ensure_ascii=False) + "\n")

    raw_pages_dir = os.path.join(output_dir, "raw_pages")
    clean_pages_dir = os.path.join(output_dir, "clean_pages")
    os.makedirs(raw_pages_dir, exist_ok=True)
    os.makedirs(clean_pages_dir, exist_ok=True)
    for page in pages:
        filename = f"{page['depth']:02d}_{slugify(page['title'] or page['page_id'])}.md"
        with open(os.path.join(raw_pages_dir, filename), "w", encoding="utf-8") as handle:
            handle.write(page["raw_markdown"])
        with open(os.path.join(clean_pages_dir, filename), "w", encoding="utf-8") as handle:
            handle.write(page["clean_markdown"])


def normalize_prefix(prefix: str | None) -> str | None:
    """Normalize a path prefix."""
    if not prefix:
        return None
    prefix = prefix.strip()
    if not prefix:
        return None
    if not prefix.startswith("/"):
        prefix = "/" + prefix
    if len(prefix) > 1 and prefix.endswith("/"):
        prefix = prefix.rstrip("/")
    return prefix


def derive_allowed_path_prefix(start_url: str) -> str | None:
    """Default the path scope to the start URL path."""
    path = urlparse(start_url).path or "/"
    if path == "/":
        return None
    if path.endswith((".html", ".htm", ".php", ".jsp", ".asp")):
        return path.rsplit("/", 1)[0] or "/"
    return path.rstrip("/") or "/"


def build_path_patterns(hostname: str, allowed_path_prefix: str | None) -> list[str]:
    """Build Crawl4AI URL glob patterns."""
    if not allowed_path_prefix:
        return [f"https://{hostname}/*", f"http://{hostname}/*"]
    return [
        f"https://{hostname}{allowed_path_prefix}*",
        f"http://{hostname}{allowed_path_prefix}*",
    ]


def slugify(value: str) -> str:
    """Create a filesystem-safe slug."""
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "page"


def default_output_dir(start_url: str) -> str:
    """Build a deterministic output directory for the spike."""
    parsed = urlparse(start_url)
    hostname = parsed.hostname or "site"
    path = (parsed.path or "/").strip("/")
    slug = slugify(f"{hostname}-{path}" if path else hostname)
    return os.path.join("out", "crawl4ai_spike", slug)


def main():
    """Entrypoint."""
    args = parse_args()
    output_dir = args.output_dir or default_output_dir(args.start_url)
    asyncio.run(
        run_spike(
            start_url=args.start_url,
            max_depth=args.max_depth,
            max_pages=args.max_pages,
            allowed_path_prefix=args.allowed_path_prefix,
            output_dir=output_dir,
        )
    )
    print(output_dir)


if __name__ == "__main__":
    main()
