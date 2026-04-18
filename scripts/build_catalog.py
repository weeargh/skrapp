#!/usr/bin/env python3
"""
Phase 3 — Build catalog.yaml, intent-map.yaml, categories.yaml.

Reads all approved articles from kb-ai-ready/articles/ and generates the
three index files at kb-ai-ready/.  Run this after each review session.

Usage:
    python scripts/build_catalog.py [--articles DIR] [--out DIR]
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import defaultdict

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_fm(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if not raw.startswith("---"):
        return {}
    end = raw.find("\n---", 4)
    if end == -1:
        return {}
    return yaml.safe_load(raw[4:end]) or {}


def main():
    parser = argparse.ArgumentParser(description="Build MekariRAG catalog files.")
    parser.add_argument("--articles", default="kb-ai-ready/articles", help="Approved articles dir")
    parser.add_argument("--out",      default="kb-ai-ready",          help="Output dir for catalogs")
    args = parser.parse_args()

    if not os.path.isdir(args.articles):
        print(f"No articles directory found at {args.articles}. Nothing to catalog.")
        sys.exit(0)

    os.makedirs(args.out, exist_ok=True)

    # Walk all .md files recursively
    all_articles: list[dict] = []
    for root, _, filenames in os.walk(args.articles):
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            path = os.path.join(root, filename)
            fm = _read_fm(path)
            relative = os.path.relpath(path, args.out)
            entry = {
                "article_id":     fm.get("article_id"),
                "slug":           filename.replace(".md", ""),
                "path":           relative,
                "title":          fm.get("title"),
                "article_type":   fm.get("article_type"),
                "solvability_type": fm.get("solvability_type"),
                "intent_tags":    fm.get("intent_tags") or [],
                "products":       fm.get("products") or [],
                "product_surface": fm.get("product_surface"),
                "language":       fm.get("language", "id"),
                "compliance_sensitive": fm.get("compliance_sensitive", False),
                "plan_scope":     fm.get("plan_scope"),
                "last_verified":  fm.get("last_verified"),
                "verified_by":    fm.get("verified_by"),
                "section_title":  fm.get("section_title"),
                "category_title": fm.get("category_title"),
                "summary":        fm.get("summary"),
            }
            all_articles.append(entry)

    # ── catalog.yaml ──────────────────────────────────────────────────────
    catalog = {
        "total": len(all_articles),
        "articles": all_articles,
    }
    catalog_path = os.path.join(args.out, "catalog.yaml")
    with open(catalog_path, "w", encoding="utf-8") as fh:
        yaml.dump(catalog, fh, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # ── intent-map.yaml ───────────────────────────────────────────────────
    intent_map: dict[str, list[str]] = defaultdict(list)
    for entry in all_articles:
        for tag in (entry.get("intent_tags") or []):
            intent_map[tag].append(entry["path"])
    intent_map_sorted = dict(sorted(intent_map.items()))

    intent_path = os.path.join(args.out, "intent-map.yaml")
    with open(intent_path, "w", encoding="utf-8") as fh:
        yaml.dump(intent_map_sorted, fh, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # ── categories.yaml ───────────────────────────────────────────────────
    by_category: dict[str, dict] = defaultdict(lambda: {"sections": defaultdict(list)})
    for entry in all_articles:
        cat  = entry.get("category_title") or "Uncategorized"
        sec  = entry.get("section_title")  or "General"
        by_category[cat]["sections"][sec].append({
            "slug":  entry["slug"],
            "title": entry["title"],
            "path":  entry["path"],
            "type":  entry["article_type"],
        })

    # Convert defaultdicts to plain dicts for YAML serialization
    categories_plain = {
        cat: {"sections": dict(data["sections"])}
        for cat, data in sorted(by_category.items())
    }

    categories_path = os.path.join(args.out, "categories.yaml")
    with open(categories_path, "w", encoding="utf-8") as fh:
        yaml.dump(categories_plain, fh, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # ── Summary ───────────────────────────────────────────────────────────
    by_type: dict[str, int] = defaultdict(int)
    for entry in all_articles:
        by_type[entry.get("article_type") or "unclassified"] += 1

    print(f"Catalog built from {len(all_articles)} approved articles.")
    print(f"  Types: {dict(by_type)}")
    print(f"  Intent tags: {len(intent_map)} unique")
    print(f"  Categories:  {len(by_category)}")
    print(f"\n  {catalog_path}")
    print(f"  {intent_path}")
    print(f"  {categories_path}")


if __name__ == "__main__":
    main()
