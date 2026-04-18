#!/usr/bin/env python3
"""
Restore images from the original crawled Zendesk articles into kb-ai-ready/drafts/.

Images are injected as standard markdown  ![alt](url)  inline at the end of the
Steps section (or first section if no Steps). marked.js renders them as <img>
tags; postprocessHtml() then routes the src through /mekarirag/proxy/image.

Usage:
    python scripts/restore_images.py [--drafts DIR] [--source DIR] [--dry-run]
"""
from __future__ import annotations

import argparse
import os
import re
import urllib.parse

DRAFTS_DIR = "kb-ai-ready/drafts"
SOURCE_DIR = "downloads/job_21c31a25087856a4a2616024005d1994_unique_cleaned_md"

IMG_MARKDOWN_RE = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')

# Skip tracking pixels / tiny icons / theme assets
SKIP_URL_RE = re.compile(
    r'theming_assets|bat\.bing|1x1|pixel|tracking|mekari\.com/system/photos',
    re.IGNORECASE,
)

SECTION_RE = re.compile(r'^## (.+?)(?:\s+<!--[^>]*-->)?\s*$', re.MULTILINE)

# Previously injected formats to strip before re-injecting
OLD_BLOCK_RE = re.compile(
    r'\n\n(?:> Screenshot: [^\n]*\n> Image: https?://[^\n]+\n*)+',
    re.MULTILINE,
)
OLD_IMG_RE = re.compile(
    r'\n!\[[^\]]*\]\(https?://help-center\.qontak\.com/hc/article_attachments/[^\)]+\)',
)


def _build_source_lookup(source_dir: str) -> dict[str, str]:
    """Map article_id -> filepath from the original downloads directory."""
    lookup: dict[str, str] = {}
    id_re = re.compile(r'^\d+_(\d+)[-_]')
    for fname in os.listdir(source_dir):
        if not fname.endswith(".md"):
            continue
        m = id_re.match(fname)
        if m:
            lookup[m.group(1)] = os.path.join(source_dir, fname)
    return lookup


def _proxy_url(url: str) -> str:
    return f"/mekarirag/proxy/image?url={urllib.parse.quote(url, safe='')}"


def _extract_images(source_path: str) -> list[dict]:
    with open(source_path, encoding="utf-8") as fh:
        content = fh.read()

    seen_urls: set[str] = set()
    images: list[dict] = []

    for m in IMG_MARKDOWN_RE.finditer(content):
        url = m.group(2).strip()
        if url in seen_urls or SKIP_URL_RE.search(url):
            continue
        seen_urls.add(url)
        alt = m.group(1).strip() or "Screenshot"
        images.append({"alt": alt, "url": url})

    return images


def _inject_images(draft_path: str, images: list[dict]) -> bool:
    """Inject images inline at end of Steps section. Returns True if modified."""
    with open(draft_path, encoding="utf-8") as fh:
        content = fh.read()

    # Strip any previously injected image blocks
    content = OLD_BLOCK_RE.sub('', content)
    content = OLD_IMG_RE.sub('', content)

    # Skip if images already present
    if "help-center.qontak.com/hc/article_attachments" in content:
        return False

    # Build inline image markdown (standard ![alt](proxy_url))
    img_lines = "\n".join(
        f"![{img['alt']}]({_proxy_url(img['url'])})"
        for img in images
    )

    # Find Steps section; fall back to first section
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
        new_content = content.rstrip() + "\n\n" + img_lines + "\n"
    else:
        sec_end = (
            matches[target_idx + 1].start()
            if target_idx + 1 < len(matches)
            else len(content)
        )
        section_text = content[:sec_end].rstrip()
        new_content = section_text + "\n\n" + img_lines + "\n\n" + content[sec_end:].lstrip("\n")

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
        article_id = fname.split("-")[0]

        if article_id not in lookup:
            no_source += 1
            continue

        images = _extract_images(lookup[article_id])
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
