#!/usr/bin/env python3
"""
Post-processing — strip internal fields from frontmatter, keep only the
MekariRAG-required schema.

Maps:
  overall_confidence (high/medium/low) → faithfulness_threshold (0.9/0.6/0.3)
  ai_enriched + ai_model              → verified_by ("AI:model-name")

Removes all pipeline-internal fields (article_id, section_id, _prepared,
ai_enriched, ai_notes, review_status, section_confidence, etc.)

Usage:
    python scripts/clean_frontmatter.py [--drafts DIR] [--out DIR]
    python scripts/clean_frontmatter.py               # in-place on drafts
"""
from __future__ import annotations

import argparse
import os
import sys
import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CONF_TO_SCORE = {"high": 0.9, "medium": 0.6, "low": 0.3}

# Canonical field order for the output frontmatter
FIELD_ORDER = [
    "title",
    "canonical_url",
    "article_type",
    "solvability_type",
    "products",
    "product_surface",
    "language",
    "intent_tags",
    "query_examples",
    "compliance_sensitive",
    "plan_scope",
    "chunk_groups",
    "related_chunks",
    "last_verified",
    "verified_by",
    "faithfulness_threshold",
]


def _read_fm_and_body(path: str) -> tuple[dict, str]:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 4)
    if end == -1:
        return {}, raw
    fm = yaml.safe_load(raw[4:end]) or {}
    body = raw[end + 4:].lstrip("\n")
    return fm, body


def _write_md(path: str, fm: dict, body: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{yaml_str}---\n\n{body}")


def _clean_fm(fm: dict) -> dict:
    overall_conf = fm.get("overall_confidence")
    faithfulness = CONF_TO_SCORE.get(overall_conf) if overall_conf else fm.get("faithfulness_threshold")

    if fm.get("ai_enriched"):
        verified_by = f"AI:{fm.get('ai_model', 'claude-haiku')}"
    else:
        verified_by = fm.get("verified_by")

    clean = {
        "title":                fm.get("title"),
        "canonical_url":        fm.get("canonical_url"),
        "article_type":         fm.get("article_type"),
        "solvability_type":     fm.get("solvability_type"),
        "products":             fm.get("products") or [],
        "product_surface":      fm.get("product_surface"),
        "language":             fm.get("language", "id"),
        "intent_tags":          fm.get("intent_tags") or [],
        "query_examples":       fm.get("query_examples") or [],
        "compliance_sensitive": fm.get("compliance_sensitive", False),
        "plan_scope":           fm.get("plan_scope"),
        "chunk_groups":         fm.get("chunk_groups") or [],
        "related_chunks":       fm.get("related_chunks") or [],
        "last_verified":        fm.get("last_verified"),
        "verified_by":          verified_by,
        "faithfulness_threshold": faithfulness,
    }

    # Preserve canonical field order
    return {k: clean[k] for k in FIELD_ORDER if k in clean}


def main():
    parser = argparse.ArgumentParser(description="Clean frontmatter to MekariRAG schema.")
    parser.add_argument("--drafts", default="kb-ai-ready/drafts", help="Source directory")
    parser.add_argument("--out",    default=None,                  help="Output dir (default: in-place)")
    args = parser.parse_args()

    src = args.drafts
    dst = args.out or args.drafts
    os.makedirs(dst, exist_ok=True)

    files = sorted(f for f in os.listdir(src) if f.endswith(".md"))
    updated = 0

    for filename in files:
        in_path  = os.path.join(src, filename)
        out_path = os.path.join(dst, filename)
        fm, body = _read_fm_and_body(in_path)
        clean    = _clean_fm(fm)
        _write_md(out_path, clean, body)
        updated += 1

    print(f"Cleaned frontmatter on {updated} files → {os.path.abspath(dst)}/")
    print(f"  Fields kept: {', '.join(FIELD_ORDER)}")


if __name__ == "__main__":
    main()
