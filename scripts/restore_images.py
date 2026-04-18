#!/usr/bin/env python3
"""
Restore original instructional content (with inline images) into kb-ai-ready/drafts/.

For each draft that has a matching original article in the downloads directory:
  - Extracts the real instructional body (between author line and social-share footer)
  - Converts all image URLs to /mekarirag/proxy/image?url=...
  - Demotes any ## sub-headings to ### so they don't break section parsing
  - Replaces the Steps section body with this original content

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

SKIP_URL_RE = re.compile(
    r'theming_assets|bat\.bing|1x1|pixel|tracking|mekari\.com/system/photos'
    r'|help-center\.mekari\.com/system',
    re.IGNORECASE,
)

SECTION_RE = re.compile(r'^## (.+?)(?:\s+<!--[^>]*-->)?\s*$', re.MULTILINE)

# Markers for where real content starts/ends in original articles
CONTENT_START_RE = re.compile(
    r'\*\s*Diperbarui.+?\n|^\s*Diperbarui .+?\n',
    re.MULTILINE,
)
CONTENT_END_RE = re.compile(
    r'Bagikan artikel ini|^## Sumber informasi|^#{1,3} Punya saran',
    re.MULTILINE,
)

# Previously injected image lines to strip before re-injecting
OLD_IMG_LINE_RE = re.compile(
    r'!\[[^\]]*\]\(/mekarirag/proxy/image\?url=[^\)]+\)\n?',
)
OLD_BLOCK_RE = re.compile(
    r'\n\n(?:> Screenshot: [^\n]*\n> Image: https?://[^\n]+\n*)+',
    re.MULTILINE,
)


def _build_source_lookup(source_dir: str) -> dict[str, str]:
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


def _extract_original_body(source_path: str) -> str | None:
    """Return cleaned instructional body from the original downloaded article."""
    with open(source_path, encoding="utf-8") as fh:
        raw = fh.read()

    # Find content start
    m_start = CONTENT_START_RE.search(raw)
    start = m_start.end() if m_start else 0

    # Find content end
    m_end = CONTENT_END_RE.search(raw, start)
    end = m_end.start() if m_end else len(raw)

    body = raw[start:end].strip()
    if not body:
        return None

    # Check there's at least one image — otherwise nothing to restore
    has_image = bool(IMG_MARKDOWN_RE.search(body)) and any(
        not SKIP_URL_RE.search(m.group(2)) for m in IMG_MARKDOWN_RE.finditer(body)
    )
    if not has_image:
        return None

    # Demote ## sub-headings to ### so they don't create new top-level sections
    body = re.sub(r'^## ', '### ', body, flags=re.MULTILINE)

    # Proxy images; remove noise images entirely
    def proxy_img(m: re.Match) -> str:
        url = m.group(2).strip()
        if SKIP_URL_RE.search(url):
            return ''
        alt = m.group(1).strip() or 'Screenshot'
        return f'![{alt}]({_proxy_url(url)})'

    body = IMG_MARKDOWN_RE.sub(proxy_img, body)

    # Collapse excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)

    return body.strip()


def _replace_steps_body(draft_path: str, new_body: str) -> bool:
    """Replace the Steps section body with new_body. Returns True if modified."""
    with open(draft_path, encoding="utf-8") as fh:
        content = fh.read()

    # Strip any previously injected image blocks/lines
    content = OLD_IMG_LINE_RE.sub('', content)
    content = OLD_BLOCK_RE.sub('', content)

    matches = list(SECTION_RE.finditer(content))
    target_idx = None
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        if 'Step' in name or 'Langkah' in name:
            target_idx = i
            break
    if target_idx is None and matches:
        target_idx = 0
    if target_idx is None:
        return False

    sec_header_end = matches[target_idx].end()
    sec_end = (
        matches[target_idx + 1].start()
        if target_idx + 1 < len(matches)
        else len(content)
    )

    before = content[:sec_header_end]
    after = content[sec_end:].lstrip('\n')
    new_content = before + '\n\n' + new_body + '\n\n' + after

    with open(draft_path, 'w', encoding='utf-8') as fh:
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

        body = _extract_original_body(lookup[article_id])
        if not body:
            no_images += 1
            continue

        if args.dry_run:
            img_count = sum(1 for m in IMG_MARKDOWN_RE.finditer(body)
                            if not SKIP_URL_RE.search(m.group(2)))
            print(f"[DRY] {fname}: {img_count} images")
            updated += 1
            continue

        if _replace_steps_body(draft_path, body):
            img_count = sum(1 for m in IMG_MARKDOWN_RE.finditer(body)
                            if not SKIP_URL_RE.search(m.group(2)))
            print(f"  ✓ {fname}: {img_count} inline images")
            updated += 1
        else:
            skipped += 1

    print(f"\nDone — updated: {updated}, no inline images: {no_images}, "
          f"no source: {no_source}, skipped: {skipped}")


if __name__ == "__main__":
    main()
