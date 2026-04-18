"""Transform a Zendesk article HTML body into MekariRAG-ready markdown with YAML frontmatter."""
from __future__ import annotations

import hashlib
import re

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

from crawler.zendesk_fetcher import ZendeskArticle, ZendeskCategory, ZendeskSection


# CSS classes that Zendesk/Qontak uses for callout boxes.
_CALLOUT_CLASSES: dict[str, tuple[str, str]] = {
    "important-box": ("⚠️", "**Penting**"),
    "note":           ("ℹ️", "**Catatan**"),
    "warning":        ("⚠️", "**Peringatan**"),
    "tip":            ("💡", "**Tips**"),
    "info":           ("ℹ️", "**Info**"),
}

# Tags that represent block-level HTML.
_BLOCK_TAGS = frozenset([
    "p", "div", "h1", "h2", "h3", "h4", "h5", "h6",
    "ul", "ol", "table", "blockquote", "pre", "figure",
    "section", "article", "main", "header", "footer",
])


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def transform_article(
    article: ZendeskArticle,
    sections: dict[int, ZendeskSection],
    categories: dict[int, ZendeskCategory],
) -> str:
    """Return a complete markdown string (YAML frontmatter + body) for one article."""
    frontmatter = _build_frontmatter(article, sections, categories)
    body_md = html_to_markdown(article.body or "")
    return f"{frontmatter}\n\n{body_md}".strip()


def html_to_markdown(html: str) -> str:
    """Convert a Zendesk article HTML body fragment to plain markdown (no frontmatter)."""
    if not html:
        return ""
    soup = BeautifulSoup(html, "lxml")
    root = soup.find("body") or soup
    blocks = _collect_blocks(root)
    return _join_blocks(blocks)


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def _build_frontmatter(
    article: ZendeskArticle,
    sections: dict[int, ZendeskSection],
    categories: dict[int, ZendeskCategory],
) -> str:
    section = sections.get(article.section_id or 0)
    category = categories.get(section.category_id if section else 0)
    content_hash = hashlib.sha256((article.body or "").encode("utf-8")).hexdigest()

    data = {
        "article_id": article.id,
        "title": article.title,
        "canonical_url": article.html_url,
        "section_id": article.section_id,
        "section_title": section.name if section else None,
        "category_id": section.category_id if section else None,
        "category_title": category.name if category else None,
        "locale": article.locale,
        "label_names": article.label_names or [],
        "created_at": article.created_at,
        "updated_at": article.updated_at,
        "source_hash": f"sha256:{content_hash[:16]}",
        "author_id": article.author_id,
        "author_name": article.author_name,
    }
    yaml_str = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---"


# ---------------------------------------------------------------------------
# Block-level conversion
# ---------------------------------------------------------------------------

def _collect_blocks(root) -> list[str]:
    """Walk direct children of root and return markdown blocks."""
    blocks: list[str] = []
    for child in root.children:
        if isinstance(child, NavigableString):
            text = child.strip()
            if text:
                blocks.append(text)
        elif isinstance(child, Tag):
            block = _element_to_block(child)
            if block:
                blocks.append(block)
    return blocks


def _join_blocks(blocks: list[str]) -> str:
    result = "\n\n".join(b for b in blocks if b.strip())
    return re.sub(r"\n{3,}", "\n\n", result).strip()


def _element_to_block(el: Tag) -> str:
    tag = (el.name or "").lower()

    # Headings
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        text = el.get_text(" ", strip=True)
        return f"{'#' * level} {text}" if text else ""

    # Paragraphs — most logic lives here
    if tag == "p":
        return _convert_paragraph(el)

    # Unordered / ordered lists
    if tag == "ul":
        return _convert_list(el, ordered=False)
    if tag == "ol":
        return _convert_list(el, ordered=True)

    # Tables
    if tag == "table":
        return _convert_table(el)

    # Pre / code blocks
    if tag == "pre":
        code = el.find("code")
        raw = (code or el).get_text()
        lang = ""
        if code:
            cls = " ".join(code.get("class") or [])
            m = re.search(r"language-(\w+)", cls)
            lang = m.group(1) if m else ""
        return f"```{lang}\n{raw.strip()}\n```"

    # Blockquote
    if tag == "blockquote":
        inner = html_to_markdown(str(el.decode_contents()))
        lines = inner.splitlines()
        return "\n".join(f"> {line}" if line.strip() else ">" for line in lines)

    # Figure wrappers (images with optional captions)
    if tag == "figure":
        return _convert_figure(el)

    # Standalone image
    if tag == "img":
        return _convert_img(el)

    # Horizontal rule
    if tag == "hr":
        return "---"

    # Generic container — recurse
    if tag in _BLOCK_TAGS or tag == "div":
        blocks = _collect_blocks(el)
        return _join_blocks(blocks)

    # Inline elements promoted to block context — just extract text inline
    text = el.get_text(" ", strip=True)
    return text if text else ""


# ---------------------------------------------------------------------------
# Paragraph conversion (handles callouts, pseudo-headings, images)
# ---------------------------------------------------------------------------

def _convert_paragraph(el: Tag) -> str:
    css_classes = set(el.get("class") or [])

    # ── Callout boxes ──────────────────────────────────────────────────────
    for cls, (emoji, label) in _CALLOUT_CLASSES.items():
        if cls in css_classes:
            return _build_callout(el, emoji, label)

    # ── Pseudo-headings via wysiwyg large-font class + bold text ──────────
    large_font = "wysiwyg-font-size-large" in css_classes or "wysiwyg-font-size-xlarge" in css_classes
    if large_font:
        strong = el.find("strong")
        if strong:
            text = strong.get_text(" ", strip=True)
            if text:
                return f"### {text}"

    # ── Paragraphs whose only visible child is a <strong> (section labels) ─
    visible_children = [
        c for c in el.children
        if isinstance(c, Tag) or (isinstance(c, NavigableString) and c.strip())
    ]
    if (
        len(visible_children) == 1
        and isinstance(visible_children[0], Tag)
        and visible_children[0].name == "strong"
    ):
        text = visible_children[0].get_text(" ", strip=True)
        # Only promote if it looks like a short section label (≤ 12 words)
        if text and len(text.split()) <= 12:
            return f"### {text}"

    # ── Paragraph with inline images ───────────────────────────────────────
    if el.find("img"):
        parts: list[str] = []
        for child in el.children:
            if isinstance(child, NavigableString):
                text = child.strip()
                if text:
                    parts.append(text)
            elif child.name == "img":
                img_md = _convert_img(child)
                if img_md:
                    parts.append(img_md)
            else:
                parts.append(_inline_to_md(child))
        return "\n".join(p for p in parts if p)

    # ── Normal paragraph ───────────────────────────────────────────────────
    inline = _children_inline(el)
    return inline.strip()


def _build_callout(el: Tag, emoji: str, label: str) -> str:
    """Render a Zendesk callout box as a markdown blockquote."""
    plain_label = re.sub(r"[\*_`⚠️ℹ️💡]", "", label).strip().lower()

    parts: list[str] = []
    first_strong_skipped = False
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif child.name == "br":
            parts.append("\n")
        elif not first_strong_skipped and child.name in ("strong", "b"):
            # Skip the embedded label element if it matches the callout label.
            child_text = child.get_text("", strip=True).lower()
            if child_text == plain_label:
                first_strong_skipped = True
                continue
            parts.append(_inline_to_md(child))
            first_strong_skipped = True
        else:
            parts.append(_inline_to_md(child))

    content = "".join(parts).strip()
    # Also strip the label if it appears as plain text at the start.
    if content.lower().startswith(plain_label):
        content = content[len(plain_label):].lstrip(": \n")

    header = f"> {emoji} {label}"
    body_lines = content.splitlines()
    quoted = [f"> {line}" if line.strip() else ">" for line in body_lines]
    return "\n".join([header] + quoted)


# ---------------------------------------------------------------------------
# List conversion
# ---------------------------------------------------------------------------

def _convert_list(el: Tag, ordered: bool) -> str:
    lines: list[str] = []
    counter = 1
    for li in el.find_all("li", recursive=False):
        # Gather the direct text/inline content before any nested list
        main_parts: list[str] = []
        nested_list: Tag | None = None
        for child in li.children:
            if isinstance(child, Tag) and child.name in ("ul", "ol"):
                nested_list = child
                break
            if isinstance(child, NavigableString):
                main_parts.append(str(child))
            else:
                main_parts.append(_inline_to_md(child))

        main_text = "".join(main_parts).strip()
        prefix = f"{counter}." if ordered else "-"
        lines.append(f"{prefix} {main_text}")
        counter += 1

        if nested_list:
            nested_md = _convert_list(nested_list, ordered=nested_list.name == "ol")
            for nested_line in nested_md.splitlines():
                lines.append(f"  {nested_line}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Table conversion
# ---------------------------------------------------------------------------

def _convert_table(el: Tag) -> str:
    """Convert table to markdown, or flatten comparison tables (with images) to narrative."""
    if el.find("img"):
        return _flatten_image_table(el)

    rows: list[list[str]] = []
    for row in el.find_all("tr"):
        cells = row.find_all(["th", "td"])
        rows.append([_children_inline(cell).strip() for cell in cells])

    if not rows:
        return ""

    col_count = max(len(r) for r in rows)
    if col_count == 0:
        return ""

    rows = [r + [""] * (col_count - len(r)) for r in rows]
    md: list[str] = []
    md.append("| " + " | ".join(rows[0]) + " |")
    md.append("| " + " | ".join(["---"] * col_count) + " |")
    for row in rows[1:]:
        md.append("| " + " | ".join(row) + " |")
    return "\n".join(md)


def _flatten_image_table(el: Tag) -> str:
    """Convert a comparison / screenshot table to a flat narrative."""
    blocks: list[str] = []
    for row in el.find_all("tr"):
        for th in row.find_all("th"):
            text = th.get_text(" ", strip=True)
            if text:
                blocks.append(f"**{text}**")
        for td in row.find_all("td"):
            img = td.find("img")
            if img:
                blocks.append(_convert_img(img))
                caption = td.get_text(" ", strip=True)
                if caption:
                    blocks.append(f"*{caption}*")
            else:
                text = _children_inline(td).strip()
                if text:
                    blocks.append(text)
    return "\n\n".join(b for b in blocks if b)


# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------

def _convert_figure(el: Tag) -> str:
    parts: list[str] = []
    img = el.find("img")
    if img:
        parts.append(_convert_img(img))
    caption = el.find("figcaption")
    if caption:
        text = caption.get_text(" ", strip=True)
        if text:
            parts.append(f"*{text}*")
    return "\n".join(p for p in parts if p)


# ---------------------------------------------------------------------------
# Inline helpers
# ---------------------------------------------------------------------------

def _children_inline(el: Tag) -> str:
    """Render all children of el as inline markdown."""
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        else:
            parts.append(_inline_to_md(child))
    return "".join(parts)


def _inline_to_md(el: Tag) -> str:
    """Convert an inline HTML element to markdown."""
    tag = (el.name or "").lower()

    if tag in ("strong", "b"):
        inner = _children_inline(el)
        return f"**{inner.strip()}**" if inner.strip() else inner

    if tag in ("em", "i"):
        inner = _children_inline(el)
        return f"*{inner.strip()}*" if inner.strip() else inner

    if tag == "code":
        text = el.get_text()
        return f"`{text}`" if text else ""

    if tag == "a":
        inner = _children_inline(el).strip()
        href = el.get("href") or ""
        return f"[{inner}]({href})" if href and inner else inner

    if tag == "img":
        return _convert_img(el)

    if tag == "br":
        return "\n"

    if tag in ("span", "label", "small", "sup", "sub", "abbr"):
        return _children_inline(el)

    # Block-ish tags in inline context — fallback to text
    return el.get_text(" ", strip=True)


def _convert_img(el: Tag) -> str:
    src = (el.get("src") or "").strip()
    if not src:
        return ""
    alt = (el.get("alt") or "").strip()
    return f"![{alt}]({src})"
