#!/usr/bin/env python3
"""
Phase 2 — Human review (one article at a time).

Walks through kb-ai-ready/drafts/ in order, shows each article, lets you
approve, edit, skip, or flag for rewrite.  Approved articles are moved to
kb-ai-ready/articles/{primary-intent-tag}/.

Usage:
    python scripts/review_article.py [--drafts DIR] [--out DIR] [--filter TYPE]

    --drafts   Source directory of enriched drafts (default: kb-ai-ready/drafts)
    --out      Approved output directory           (default: kb-ai-ready/articles)
    --filter   Only review articles of given type  (task | concept | troubleshooting)

Commands during review:
    a / approve   Approve and move to articles/{intent-tag}/
    e / edit      Open in $EDITOR, then approve on save
    s / skip      Skip for now (stays in drafts)
    f / flag      Flag as needing a rewrite (adds review_status: flagged)
    q / quit      Stop reviewing

After all articles are approved, run:
    python scripts/build_catalog.py
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import date

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


def _write_fm_and_body(path: str, fm: dict, body: str) -> None:
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{yaml_str}---\n\n{body}")


def _primary_tag(fm: dict) -> str:
    tags = fm.get("intent_tags") or []
    return tags[0] if tags else "uncategorized"


def _destination_path(out_dir: str, fm: dict, filename: str) -> str:
    tag = re.sub(r"[^\w-]", "-", _primary_tag(fm))
    return os.path.join(out_dir, tag, filename)


_CONF_LABEL = {"high": "✓ HIGH", "medium": "~ MED", "low": "? LOW", None: "  n/a"}
_CONF_RANK  = {"high": 3, "medium": 2, "low": 1}


def _confidence_meets(overall: str | None, max_conf: str | None) -> bool:
    """Return True if article should be shown given the --max-confidence filter."""
    if max_conf is None:
        return True
    rank = _CONF_RANK.get(overall or "low", 1)
    threshold = _CONF_RANK.get(max_conf, 1)
    return rank <= threshold


def _print_summary(fm: dict, body: str, filename: str, idx: int, total: int) -> None:
    bar = "─" * 70
    overall = fm.get("overall_confidence")
    conf_label = _CONF_LABEL.get(overall, "  n/a")
    ai_tag = f"  [AI:{conf_label}]" if fm.get("ai_enriched") else ""

    print(f"\n{bar}")
    print(f"  [{idx}/{total}]  {filename}{ai_tag}")
    print(bar)
    print(f"  Title         : {fm.get('title', '—')}")
    print(f"  Type          : {fm.get('article_type', '—')}  /  {fm.get('solvability_type', '—')}")
    print(f"  Products      : {', '.join(fm.get('products') or []) or '—'}")
    print(f"  Surface       : {fm.get('product_surface', '—')}")
    print(f"  Compliance    : {fm.get('compliance_sensitive', False)}")
    print(f"  Intent tags   : {', '.join(fm.get('intent_tags') or [])}")
    print(f"  Query examples:")
    for q in (fm.get("query_examples") or []):
        print(f"      • {q}")
    if fm.get("ai_enriched"):
        sec_conf = fm.get("section_confidence") or {}
        conf_parts = "  ".join(
            f"{s[:5]}:{_CONF_LABEL.get(c, c)}" for s, c in sec_conf.items()
        )
        print(f"  AI confidence : overall={conf_label}  [{conf_parts}]")
        if fm.get("ai_notes"):
            print(f"  AI notes      : {fm['ai_notes']}")
    print(f"  Summary       : {fm.get('summary', '—')}")
    print(f"\n  Body preview ({len(body)} chars):")
    print("  " + "\n  ".join(body[:700].splitlines()))
    if len(body) > 700:
        print(f"  ... ({len(body) - 700} more chars)")
    print(bar)


def _prompt_command() -> str:
    print("\n  [a]pprove  [e]dit  [s]kip  [f]lag  [q]uit  > ", end="", flush=True)
    try:
        return input().strip().lower()
    except (EOFError, KeyboardInterrupt):
        return "q"


def _open_editor(path: str) -> None:
    editor = os.environ.get("EDITOR", "nano")
    subprocess.call([editor, path])


def main():
    parser = argparse.ArgumentParser(description="Review and approve enriched articles.")
    parser.add_argument("--drafts", default="kb-ai-ready/drafts",   help="Drafts directory")
    parser.add_argument("--out",    default="kb-ai-ready/articles",  help="Approved output directory")
    parser.add_argument("--filter", dest="type_filter", default=None,
                        help="Only review articles of this type (task|concept|troubleshooting)")
    parser.add_argument("--max-confidence", dest="max_confidence", default=None,
                        choices=["low", "medium", "high"],
                        help="Only review AI-enriched articles at or below this confidence level")
    args = parser.parse_args()

    if not os.path.isdir(args.drafts):
        print(f"ERROR: drafts directory not found: {args.drafts}")
        print("Run enrich_articles.py first.")
        sys.exit(1)

    os.makedirs(args.out, exist_ok=True)

    # Collect pending drafts (status != approved)
    files = sorted(f for f in os.listdir(args.drafts) if f.endswith(".md"))
    pending = []
    for filename in files:
        path = os.path.join(args.drafts, filename)
        fm, body = _read_fm_and_body(path)
        if fm.get("review_status") == "approved":
            continue
        if args.type_filter and fm.get("article_type") != args.type_filter:
            continue
        if args.max_confidence and not _confidence_meets(fm.get("overall_confidence"), args.max_confidence):
            continue
        pending.append((filename, path, fm, body))

    total_pending = len(pending)
    total_all     = len(files)
    approved_so_far = total_all - total_pending

    print(f"\nReview queue: {total_pending} pending  ({approved_so_far} already approved of {total_all} total)")
    if args.type_filter:
        print(f"Filter: article_type = {args.type_filter}")
    if args.max_confidence:
        print(f"Filter: confidence ≤ {args.max_confidence}  (AI-enriched low-confidence articles only)")

    approved = 0
    skipped  = 0
    flagged  = 0

    for idx, (filename, draft_path, fm, body) in enumerate(pending, 1):
        _print_summary(fm, body, filename, idx, total_pending)

        while True:
            cmd = _prompt_command()

            if cmd in ("a", "approve"):
                fm["review_status"] = "approved"
                fm["last_verified"] = str(date.today())
                dst = _destination_path(args.out, fm, filename)
                _write_fm_and_body(draft_path, fm, body)  # update draft status too
                _write_fm_and_body(dst, fm, body)
                print(f"\n  ✓ Approved → {dst}")
                approved += 1
                break

            elif cmd in ("e", "edit"):
                # Write current state to draft, open editor, re-read
                _write_fm_and_body(draft_path, fm, body)
                _open_editor(draft_path)
                fm, body = _read_fm_and_body(draft_path)
                # Show updated summary then loop back for approve/skip
                _print_summary(fm, body, filename, idx, total_pending)
                # Auto-approve after edit (user saved intentionally)
                fm["review_status"] = "approved"
                fm["last_verified"] = str(date.today())
                dst = _destination_path(args.out, fm, filename)
                _write_fm_and_body(draft_path, fm, body)
                _write_fm_and_body(dst, fm, body)
                print(f"\n  ✓ Edited + Approved → {dst}")
                approved += 1
                break

            elif cmd in ("s", "skip"):
                print("  → Skipped.")
                skipped += 1
                break

            elif cmd in ("f", "flag"):
                fm["review_status"] = "flagged"
                _write_fm_and_body(draft_path, fm, body)
                print("  ⚑ Flagged for rewrite.")
                flagged += 1
                break

            elif cmd in ("q", "quit"):
                print(f"\nStopped. Session: {approved} approved, {skipped} skipped, {flagged} flagged.")
                print("Run again to continue where you left off.")
                return

            else:
                print("  Unknown command. Use: a / e / s / f / q")

    print(f"\n{'─'*70}")
    print(f"Queue complete!")
    print(f"  {approved} approved  {skipped} skipped  {flagged} flagged")
    print(f"  Approved articles → {os.path.abspath(args.out)}/")
    print(f"\nNext: python scripts/build_catalog.py")


if __name__ == "__main__":
    main()
