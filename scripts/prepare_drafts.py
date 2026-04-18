#!/usr/bin/env python3
"""
Phase 1b — automated draft preparation (no LLM).

Runs on kb-ai-ready/drafts/ after enrich_articles.py.  Makes two passes:

  1. IMAGE FORMAT — converts every bare  ![alt](url)  line to the spec format:
         > Screenshot: [alt or placeholder]
         > Image: url

  2. BODY SCAFFOLD — for articles whose body does NOT yet contain the
     required section headers, inserts a commented scaffold at the top of
     the body so the reviewer knows exactly what to fill in.

     task          → ## Prerequisites  ## Steps  ## Expected Result
                     ## Error States  ## Escalation
     concept       → ## Definition  ## Why It Matters  ## Key Attributes
                     ## Related Tasks
     troubleshooting → ## Symptom  ## Root Cause  ## Solution  ## Escalation

  Existing structure is left untouched.  Only missing headers are added.

Usage:
    python scripts/prepare_drafts.py [--drafts DIR] [--resume]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ── Required sections per type ─────────────────────────────────────────────

REQUIRED_SECTIONS: dict[str, list[str]] = {
    "task": [
        "Prerequisites",
        "Steps",
        "Expected Result",
        "Error States",
        "Escalation",
    ],
    "concept": [
        "Definition",
        "Why It Matters",
        "Key Attributes",
        "Related Tasks",
    ],
    "troubleshooting": [
        "Symptom",
        "Root Cause",
        "Solution",
        "Escalation",
    ],
}


# ── Image transformation ───────────────────────────────────────────────────

_IMG_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", re.MULTILINE)


def _transform_images(body: str) -> tuple[str, int]:
    """Replace bare image lines with Screenshot/Image block format."""
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        alt = m.group(1).strip()
        url = m.group(2).strip()
        # Skip tracking pixels and tiny icons (common noise)
        if re.search(r"bat\.bing|1x1|pixel|tracking", url, re.IGNORECASE):
            return ""
        description = alt if alt and not re.match(r"^\d+\.?(png|jpg|jpeg|gif|webp)$", alt, re.IGNORECASE) \
                      else "Describe what this screenshot shows and what action to take"
        count += 1
        return f"> Screenshot: {description}\n> Image: {url}"

    new_body = _IMG_RE.sub(replacer, body)
    return new_body, count


# ── Body scaffold ──────────────────────────────────────────────────────────

def _existing_h2_sections(body: str) -> set[str]:
    return {m.group(1).strip().lower() for m in re.finditer(r"^## (.+)$", body, re.MULTILINE)}


def _needs_scaffold(body: str, article_type: str) -> list[str]:
    """Return section names that are missing from the body."""
    required = REQUIRED_SECTIONS.get(article_type, [])
    if not required:
        return []
    existing = _existing_h2_sections(body)
    return [s for s in required if s.lower() not in existing]


def _insert_scaffold(body: str, missing: list[str], article_type: str) -> str:
    """
    Prepend a scaffold block listing missing sections.
    Uses HTML comments so the reviewer can delete the hint block once done.
    """
    scaffold_lines = [
        "<!-- ═══════════════════════════════════════════════════════════",
        f"     REVIEW SCAFFOLD — {article_type.upper()}",
        "     The sections below are missing. Fill them in, then delete",
        "     this comment block before approving.",
        "     ═══════════════════════════════════════════════════════════",
    ]
    for section in missing:
        scaffold_lines.append(f"")
        scaffold_lines.append(f"## {section}")
        scaffold_lines.append(f"")
        if article_type == "task":
            HINTS = {
                "Prerequisites": "<!-- List required conditions, permissions, or setup steps -->",
                "Steps":         "<!-- Numbered action steps. Each step: action → expected UI response -->",
                "Expected Result": "<!-- What the user should see / confirmation message after completion -->",
                "Error States": "<!-- Common errors and their fixes. Leave empty if none. -->",
                "Escalation":   "<!-- When to contact support and what info to provide -->",
            }
        elif article_type == "concept":
            HINTS = {
                "Definition":    "<!-- One-paragraph definition. Restate the question the user asked. -->",
                "Why It Matters": "<!-- Business impact / why the user cares about this feature -->",
                "Key Attributes": "<!-- Bullet list of key properties, limits, or behaviours -->",
                "Related Tasks": "<!-- Links to task articles that use this concept -->",
            }
        else:  # troubleshooting
            HINTS = {
                "Symptom":    "<!-- Exact error message or behaviour the user observes -->",
                "Root Cause": "<!-- Why this happens (technical reason, briefly) -->",
                "Solution":   "<!-- Step-by-step fix -->",
                "Escalation": "<!-- When self-service fails: what info to send to support -->",
            }
        scaffold_lines.append(HINTS.get(section, f"<!-- Fill in {section} -->"))

    scaffold_lines.append("")
    scaffold_lines.append("-->")
    scaffold_lines.append("")

    return "\n".join(scaffold_lines) + "\n" + body


# ── IO helpers ─────────────────────────────────────────────────────────────

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
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{yaml_str}---\n\n{body}")


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Prepare drafts for human review (images + scaffold).")
    parser.add_argument("--drafts", default="kb-ai-ready/drafts", help="Drafts directory")
    parser.add_argument("--resume", action="store_true",
                        help="Skip files that already have 'prepared' flag in frontmatter")
    args = parser.parse_args()

    if not os.path.isdir(args.drafts):
        print(f"ERROR: {args.drafts} not found. Run enrich_articles.py first.")
        sys.exit(1)

    files = sorted(f for f in os.listdir(args.drafts) if f.endswith(".md"))
    total = len(files)

    imgs_converted = 0
    scaffolded     = 0
    skipped        = 0

    print(f"Preparing {total} drafts in {args.drafts}/\n")

    for i, filename in enumerate(files, 1):
        path = os.path.join(args.drafts, filename)
        fm, body = _read_fm_and_body(path)

        if args.resume and fm.get("_prepared"):
            skipped += 1
            continue

        article_type = fm.get("article_type", "concept")

        # 1. Image transformation
        new_body, n_imgs = _transform_images(body)
        imgs_converted += n_imgs

        # 2. Body scaffold for missing sections
        missing = _needs_scaffold(new_body, article_type)
        if missing:
            new_body = _insert_scaffold(new_body, missing, article_type)
            scaffolded += 1

        # Mark as prepared (so --resume works)
        fm["_prepared"] = True

        _write_md(path, fm, new_body)

        status = []
        if n_imgs:   status.append(f"{n_imgs} img")
        if missing:  status.append(f"scaffold({','.join(m[:4] for m in missing)})")
        tag = "  ".join(status) if status else "clean"

        print(f"  [{i:>4}/{total}]  {filename[:60]}  {tag}")

    print(f"\nDone.")
    print(f"  {imgs_converted} images converted to Screenshot/Image format")
    print(f"  {scaffolded} articles got section scaffolds")
    print(f"  {skipped} skipped (already prepared)")
    print(f"\nNext: python scripts/review_article.py")


if __name__ == "__main__":
    main()
