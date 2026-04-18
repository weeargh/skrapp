#!/usr/bin/env python3
"""
Standalone MekariRAG fetch script.

Fetches all published articles from a Zendesk Help Center, transforms them to
MekariRAG-ready markdown, and writes one .md file per article plus an
index.jsonl summary file.  No database, no worker, no Flask required.

Usage:
    python scripts/zendesk_fetch.py <help_center_base_url> [options]

Examples:
    # Full fetch — all articles
    python scripts/zendesk_fetch.py https://help-center.qontak.com

    # First 20 articles only (smoke test)
    python scripts/zendesk_fetch.py https://help-center.qontak.com --limit 20

    # Custom output dir and locale
    python scripts/zendesk_fetch.py https://help-center.qontak.com --locale id --out out/mekarirag

Options:
    --locale   Zendesk locale code (default: id)
    --out      Output directory    (default: out/zendesk_preview)
    --limit    Max articles; 0 = all (default: 0)
    --preview  Print first article to stdout after writing (default: on)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crawler.zendesk_fetcher import make_zendesk_fetcher
from crawler.zendesk_transformer import transform_article
from crawler.text_utils import markdown_to_text


def _safe_filename(title: str, article_id: int) -> str:
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")[:60]
    return f"{article_id}-{slug}.md"


def main():
    parser = argparse.ArgumentParser(description="Fetch Zendesk articles → MekariRAG markdown.")
    parser.add_argument("base_url", help="Help Center base URL, e.g. https://help-center.qontak.com")
    parser.add_argument("--locale",  default="id",                  help="Locale code (default: id)")
    parser.add_argument("--out",     default="out/zendesk_preview", help="Output directory")
    parser.add_argument("--limit",   type=int, default=0,           help="Max articles (0 = all)")
    parser.add_argument("--delay", type=float, default=1.5,
                        help="Seconds to wait between paginated API requests (default: 1.5). "
                             "Increase if you hit 429s. Set to 0 only with API auth.")
    parser.add_argument("--no-preview", dest="preview", action="store_false", default=True,
                        help="Skip printing first article preview")
    args = parser.parse_args()

    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    fetcher = make_zendesk_fetcher(args.base_url, locale=args.locale, request_delay=args.delay)

    # ── Taxonomy ──────────────────────────────────────────────────────────
    print(f"Fetching taxonomy from {args.base_url} (locale={args.locale}) ...")
    sections   = fetcher.fetch_sections()
    categories = fetcher.fetch_categories()
    print(f"  {len(sections)} sections, {len(categories)} categories")

    # ── Article listing ───────────────────────────────────────────────────
    print("Fetching article list ...")
    t0 = time.time()
    articles = fetcher.fetch_articles()
    print(f"  {len(articles)} articles fetched in {time.time() - t0:.1f}s")

    if args.limit:
        articles = articles[: args.limit]
        print(f"  (capped at {args.limit})")

    total = len(articles)

    # ── Transform & write ─────────────────────────────────────────────────
    print(f"\nTransforming {total} articles → {out_dir}/")

    index_rows: list[dict] = []
    ok      = 0
    errors  = 0
    t_start = time.time()

    for i, article in enumerate(articles, 1):
        filename = _safe_filename(article.title, article.id)
        path     = os.path.join(out_dir, filename)

        try:
            md         = transform_article(article, sections, categories)
            plain      = markdown_to_text(md)
            char_count = len(plain)

            with open(path, "w", encoding="utf-8") as fh:
                fh.write(md)

            # Build index row (no body — just metadata + filename pointer)
            from crawler.zendesk_fetcher import ZendeskSection, ZendeskCategory
            section  = sections.get(article.section_id or 0)
            category = categories.get(section.category_id if section else 0)
            index_rows.append({
                "article_id":     article.id,
                "filename":       filename,
                "title":          article.title,
                "canonical_url":  article.html_url,
                "section_id":     article.section_id,
                "section_title":  section.name  if section  else None,
                "category_id":    section.category_id if section else None,
                "category_title": category.name if category else None,
                "locale":         article.locale,
                "label_names":    article.label_names,
                "updated_at":     article.updated_at,
                "char_count":     char_count,
            })

            elapsed = time.time() - t_start
            rate    = i / elapsed if elapsed > 0 else 0
            eta     = (total - i) / rate if rate > 0 else 0
            print(f"  [{i:>4}/{total}] {filename}  ({char_count} chars)  eta {eta:.0f}s")
            ok += 1

        except Exception as exc:
            print(f"  [{i:>4}/{total}] ERROR article {article.id}: {exc}")
            errors += 1

    # ── Write index.jsonl ─────────────────────────────────────────────────
    index_path = os.path.join(out_dir, "index.jsonl")
    with open(index_path, "w", encoding="utf-8") as fh:
        for row in index_rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    # ── Summary ───────────────────────────────────────────────────────────
    total_elapsed = time.time() - t_start
    total_chars   = sum(r["char_count"] for r in index_rows)
    print(f"\n{'─'*60}")
    print(f"Done in {total_elapsed:.1f}s")
    print(f"  {ok} articles written, {errors} errors")
    print(f"  {total_chars:,} total chars of clean content")
    print(f"  index → {os.path.abspath(index_path)}")
    print(f"  files → {os.path.abspath(out_dir)}/")

    # ── Preview first article ─────────────────────────────────────────────
    if args.preview and index_rows:
        first = index_rows[0]
        first_path = os.path.join(out_dir, first["filename"])
        print(f"\n{'─'*60}")
        print(f"Preview: {first['title']}")
        print(f"{'─'*60}")
        if os.path.exists(first_path):
            with open(first_path, encoding="utf-8") as fh:
                content = fh.read()
            print(content[:3000])
            if len(content) > 3000:
                print(f"\n... ({len(content) - 3000} more chars — open the file to read fully)")


if __name__ == "__main__":
    main()
