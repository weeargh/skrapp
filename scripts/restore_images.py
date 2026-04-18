#!/usr/bin/env python3
"""
Restore image blocks from for-review 3/ into kb-ai-ready/drafts/.

For each draft, finds the matching source file (which still has the original
body below the <!-- AI review: --> marker), extracts all image URLs, and
appends them to the Steps section (or the first available section) as
> Screenshot / > Image blocks.

Usage:
    python scripts/restore_images.py [--drafts DIR] [--source DIR] [--dry-run]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

DRAFTS_DIR = "kb-ai-ready/drafts"
SOURCE_DIR = "for-review 3"

IMG_SCREENSHOT_RE = re.compile(
    r'> Screenshot: ([^\n]*)\n> Image: (https?://[^\s]+)', re.MULTILINE
)
IMG_MARKDOWN_RE = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')

SECTION_RE = re.compile(r'^## (.+?)(?:\s+<!--[^>]*-->)?\s*$', re.MULTILINE)


def _build_source_lookup(source_dir: str) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for sub in os.listdir(source_dir):
        full = os.path.join(source_dir, sub)
        if not os.path.isdir(full):
            continue
        for fname in os.listdir(full):
            if fname.endswith(".md"):
                lookup[fname] = os.path.join(full, fname)
    return lookup


def _extract_images(source_path: str) -> list[dict]:
    with open(source_path, encoding="utf-8") as fh:
        content = fh.read()

    # Images live in the original body below the <!-- AI review: --> marker
    marker = content.find("<!-- AI review:")
    search_text = content[marker:] if marker != -1 else content

    seen_urls: set[str] = set()
    images: list[dict] = []

    for m in IMG_SCREENSHOT_RE.finditer(search_text):
        url = m.group(2).strip()
        if url not in seen_urls:
            seen_urls.add(url)
            images.append({"alt": m.group(1).strip(), "url": url})

    for m in IMG_MARKDOWN_RE.finditer(search_text):
        url = m.group(2).strip()
        if url not in seen_urls:
            seen_urls.add(url)
            alt = m.group(1).strip() or "Screenshot"
            images.append({"alt": alt, "url": url})

    return images


def _inject_images(draft_path: str, images: list[dict]) -> bool:
    """Append image blocks to the Steps section (or first section). Returns True if modified."""
    with open(draft_path, encoding="utf-8") as fh:
        content = fh.read()

    # Skip if images already present
    if "help-center.qontak.com/hc/article_attachments" in content:
        return False

    # Build the image block text
    img_lines = []
    for img in images:
        alt = img["alt"] if img["alt"] and img["alt"] != "Describe what this screenshot shows and what action to take" else "Screenshot"
        img_lines.append(f"> Screenshot: {alt}\n> Image: {img['url']}")
    img_block = "\n\n".join(img_lines)

    # Find the Steps section to append to; fall back to first section
    matches = list(SECTION_RE.finditer(content))
    target_idx = None
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        if "Step" in name or "Langkah" in name:
            target_idx = i
            break
    if target_idx is None and matches:
        target_idx = 0

    if target_idx is None:
        # No sections found — just append at end
        new_content = content.rstrip() + "\n\n" + img_block + "\n"
    else:
        # Find end of this section (start of next, or EOF)
        sec_start = matches[target_idx].start()
        sec_end = matches[target_idx + 1].start() if target_idx + 1 < len(matches) else len(content)
        section_text = content[sec_start:sec_end].rstrip()
        new_section = section_text + "\n\n" + img_block
        new_content = content[:sec_start] + new_section + "\n\n" + content[sec_end:].lstrip("\n")

    with open(draft_path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--drafts", default=DRAFTS_DIR)
    parser.add_argument("--source", default=SOURCE_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lookup = _build_source_lookup(args.source)
    draft_files = sorted(f for f in os.listdir(args.drafts) if f.endswith(".md"))

    updated = skipped = no_images = no_source = 0

    for fname in draft_files:
        draft_path = os.path.join(args.drafts, fname)

        if fname not in lookup:
            no_source += 1
            continue

        images = _extract_images(lookup[fname])
        if not images:
            no_images += 1
            continue

        if args.dry_run:
            print(f"[DRY] {fname}: {len(images)} images")
            updated += 1
            continue

        if _inject_images(draft_path, images):
            print(f"  ✓ {fname}: {len(images)} images injected")
            updated += 1
        else:
            skipped += 1

    print(f"\nDone — updated: {updated}, already had images: {skipped}, "
          f"no images in source: {no_images}, no source file: {no_source}")


if __name__ == "__main__":
    main()
