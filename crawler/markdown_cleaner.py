"""Generic markdown content distillation utilities."""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import math
import re

from crawler.text_utils import markdown_to_text


GENERIC_NOISE_PATTERNS = [
    re.compile(r"\b(all rights reserved|copyright)\b", re.IGNORECASE),
    re.compile(r"\b(privacy policy|cookie policy|terms(?: of service| and conditions)?|legal)\b", re.IGNORECASE),
    re.compile(r"\b(share (?:this|article|page)|follow us|newsletter|subscribe)\b", re.IGNORECASE),
    re.compile(r"\b(related articles|recommended articles|similar articles)\b", re.IGNORECASE),
    re.compile(r"\b(was this article helpful|submit a request|contact support|contact us)\b", re.IGNORECASE),
]

FOOTER_HEADING_PATTERNS = [
    re.compile(r"^#{1,6}\s*(related|recommended|resources|references|support|legal|privacy|terms)\b", re.IGNORECASE),
    re.compile(r"^#{1,6}\s*(follow us|share|newsletter|contact)\b", re.IGNORECASE),
]

INLINE_DROP_PATTERNS = [
    re.compile(r"^!\[.*?\]\(https://bat\.bing\.com/.*\)$", re.IGNORECASE),
    re.compile(r"^\[\s*\]\(https?://(www\.)?(facebook|twitter|x|linkedin|instagram)\.com/.*\)$", re.IGNORECASE),
    re.compile(r"^©\s*\d{4}.*$", re.IGNORECASE),
]

STOP_WORDS = {
    "the", "and", "that", "this", "with", "from", "have", "your", "into",
    "about", "atau", "yang", "untuk", "dengan", "dari", "dalam", "pada",
    "anda", "kami", "mengenai", "sebagai", "cara", "menu",
}


@dataclass
class BlockFeatures:
    """Computed signals for one markdown block."""

    block: str
    block_type: str
    text: str
    normalized: str
    index: int
    total_blocks: int
    page_type: str
    char_count: int
    word_count: int
    line_count: int
    link_count: int
    image_count: int
    heading_level: int
    list_item_count: int
    table_row_count: int
    code_block: bool
    phone_count: int
    address_hint_count: int
    title_overlap: int
    repeated_ratio: float
    cluster_repeat_ratio: float
    short_link_ratio: float

    @property
    def position_ratio(self) -> float:
        if self.total_blocks <= 1:
            return 0.0
        return self.index / (self.total_blocks - 1)

    @property
    def is_long_form_text(self) -> bool:
        return self.word_count >= 35 and self.link_count <= max(1, self.word_count // 25)

    @property
    def is_short_link_block(self) -> bool:
        return self.link_count >= 2 and self.word_count <= 30 and self.short_link_ratio >= 0.55

    @property
    def is_footer_like(self) -> bool:
        late = self.position_ratio >= 0.55
        generic_noise = any(pattern.search(self.text) for pattern in GENERIC_NOISE_PATTERNS)
        footer_heading = any(pattern.match(self.block) for pattern in FOOTER_HEADING_PATTERNS)
        return late and (generic_noise or footer_heading or self.is_short_link_block)


def find_repeated_block_hashes(
    pages: list[dict],
    *,
    id_key: str = "id",
    markdown_key: str = "raw_markdown",
) -> set[str]:
    """Return globally repeated normalized block hashes for compatibility."""
    contexts = _build_page_contexts(pages, id_key=id_key, markdown_key=markdown_key)
    return set(contexts["global_counts"].keys())


def clean_markdown(
    markdown: str,
    repeated_hashes: set[str] | None = None,
    *,
    title: str | None = None,
    page_type: str | None = None,
) -> tuple[str, list[dict], str, float]:
    """Clean one markdown document using the generic distillation pipeline."""
    raw_markdown = markdown or ""
    blocks = prepare_markdown_blocks(raw_markdown, title=title)
    detected_page_type = page_type or classify_page_type(blocks, title=title)
    contexts = {
        "global_counts": Counter({block_hash: 2 for block_hash in (repeated_hashes or set())}),
        "global_total": 2 if repeated_hashes else 1,
        "cluster_counts": defaultdict(Counter),
        "cluster_totals": defaultdict(int),
    }
    cleaned_markdown, removed_blocks, confidence = _distill_page(
        raw_markdown,
        blocks,
        title=title,
        page_type=detected_page_type,
        contexts=contexts,
    )
    return cleaned_markdown, removed_blocks, detected_page_type, confidence


def cleanup_score(raw_markdown: str, clean_markdown_value: str) -> float:
    """A simple cleanup score representing kept content ratio."""
    raw_len = max(1, len(raw_markdown or ""))
    clean_len = len(clean_markdown_value or "")
    return round(clean_len / raw_len, 3)


def clean_pages(
    pages: list[dict],
    *,
    id_key: str = "id",
    markdown_key: str = "raw_markdown",
) -> list[dict]:
    """Return page dicts augmented with cleaned markdown and classification."""
    contexts = _build_page_contexts(pages, id_key=id_key, markdown_key=markdown_key)
    cleaned_pages: list[dict] = []
    for page in pages:
        raw_markdown = page.get(markdown_key) or ""
        blocks = prepare_markdown_blocks(raw_markdown, title=page.get("title"))
        page_type = contexts["page_types"].get(page.get(id_key)) or classify_page_type(
            blocks,
            title=page.get("title"),
            url=page.get("url"),
        )
        clean_markdown_value, removed_blocks, confidence = _distill_page(
            raw_markdown,
            blocks,
            title=page.get("title"),
            page_type=page_type,
            contexts=contexts,
        )
        clean_page = dict(page)
        clean_page["page_type"] = page_type
        clean_page["cleanup_confidence"] = confidence
        clean_page["clean_markdown"] = clean_markdown_value
        clean_page["plain_text"] = markdown_to_text(clean_markdown_value)
        clean_page["cleanup_score"] = cleanup_score(raw_markdown, clean_markdown_value)
        clean_page["removed_blocks"] = removed_blocks
        cleaned_pages.append(clean_page)
    return cleaned_pages


def split_markdown_blocks(markdown: str) -> list[str]:
    """Split markdown into paragraph-like blocks."""
    blocks = []
    for block in re.split(r"\n\s*\n", markdown or ""):
        stripped = block.strip()
        if stripped:
            blocks.append(stripped)
    return blocks


def prepare_markdown_blocks(markdown: str, *, title: str | None = None) -> list[str]:
    """Apply lightweight document cleanup before block scoring."""
    text = strip_inline_noise(markdown or "")
    blocks = split_markdown_blocks(text)
    blocks = [strip_block_inline_noise(block) for block in blocks]
    blocks = [block for block in blocks if block]
    return crop_to_main_heading(blocks, title=title)


def normalize_block(block: str) -> str:
    """Normalize a block for repetition and similarity checks."""
    text = markdown_to_text(block).lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def classify_page_type(blocks: list[str], *, title: str | None = None, url: str | None = None) -> str:
    """Classify a page into a broad content family."""
    if not blocks:
        return "generic"

    total_links = 0
    long_form_blocks = 0
    heading_blocks = 0
    contact_blocks = 0
    navigation_blocks = 0

    for index, block in enumerate(blocks):
        features = _extract_block_features(
            block,
            index=index,
            total_blocks=len(blocks),
            page_type="generic",
            title=title,
            repeated_ratio=0.0,
            cluster_repeat_ratio=0.0,
        )
        total_links += features.link_count
        heading_blocks += 1 if features.heading_level else 0
        long_form_blocks += 1 if features.is_long_form_text else 0
        contact_blocks += 1 if (features.phone_count or "get directions" in features.text.lower()) else 0
        navigation_blocks += 1 if features.is_short_link_block else 0

    if contact_blocks >= 2 and total_links >= 2:
        return "location"
    if long_form_blocks >= 2 and long_form_blocks >= navigation_blocks:
        return "article"
    if navigation_blocks >= max(2, len(blocks) // 3) and total_links >= 6:
        return "listing"
    if heading_blocks >= 2 and long_form_blocks >= 1:
        return "marketing"
    if url and any(part in url.lower() for part in ("/contact", "/showroom", "/locations", "/stores")):
        return "location"
    return "generic"


def strip_inline_noise(markdown: str) -> str:
    """Remove obvious asset/tracking lines from markdown."""
    text = markdown or ""
    text = re.sub(r"^Published Time:.*$\n?", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^Warning: This is a cached snapshot of the original page, consider retry with caching opt-out\.\n?",
        "",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(r"^\!\[\]\(https://bat\.bing\.com/.*$\n?", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_block_inline_noise(block: str) -> str:
    """Remove noisy lines from an otherwise useful block."""
    cleaned_lines: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append("")
            continue
        if any(pattern.match(stripped) for pattern in INLINE_DROP_PATTERNS):
            continue
        if stripped.startswith("![](") and len(stripped) > 300:
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines).strip()


def crop_to_main_heading(blocks: list[str], *, title: str | None = None) -> list[str]:
    """Crop obvious promo/navigation preambles before the main title block."""
    if len(blocks) <= 1:
        return blocks

    title_tokens = _significant_tokens(title or "")
    best_index = None
    best_score = 0
    for index, block in enumerate(blocks[:5]):
        if not block.lstrip().startswith("#"):
            continue
        heading_tokens = _significant_tokens(markdown_to_text(block))
        overlap = len(title_tokens & heading_tokens) if title_tokens else 0
        score = overlap * 2 + (1 if block.lstrip().startswith("# ") else 0)
        if score > best_score:
            best_score = score
            best_index = index

    if best_index and best_index > 0:
        preamble = blocks[:best_index]
        if sum(1 for block in preamble if _looks_like_navigation_or_promo(block)) >= max(1, len(preamble) - 1):
            return blocks[best_index:]
    return blocks


def _build_page_contexts(pages: list[dict], *, id_key: str, markdown_key: str) -> dict:
    """Prepare repetition and page-type contexts for a page set."""
    page_types: dict[str, str] = {}
    page_blocks: dict[str, list[str]] = {}
    global_counts: Counter[str] = Counter()
    cluster_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)
    cluster_totals: defaultdict[str, int] = defaultdict(int)

    for page in pages:
        page_id = page.get(id_key)
        if not page_id:
            continue
        blocks = prepare_markdown_blocks(page.get(markdown_key) or "", title=page.get("title"))
        page_type = classify_page_type(blocks, title=page.get("title"), url=page.get("url"))
        page_types[page_id] = page_type
        page_blocks[page_id] = blocks

        unique_hashes = {
            hashlib.sha256(normalize_block(block).encode("utf-8")).hexdigest()
            for block in blocks
            if normalize_block(block)
        }
        for block_hash in unique_hashes:
            global_counts[block_hash] += 1
            cluster_counts[page_type][block_hash] += 1
        cluster_totals[page_type] += 1

    return {
        "page_types": page_types,
        "page_blocks": page_blocks,
        "global_counts": global_counts,
        "global_total": max(1, len(page_blocks)),
        "cluster_counts": cluster_counts,
        "cluster_totals": cluster_totals,
    }


def _distill_page(
    raw_markdown: str,
    blocks: list[str],
    *,
    title: str | None,
    page_type: str,
    contexts: dict,
) -> tuple[str, list[dict], float]:
    """Score blocks and assemble the best-effort cleaned markdown."""
    cleaned_blocks: list[str] = []
    removed_blocks: list[dict] = []
    footer_run = 0
    kept_weight = 0.0
    removed_weight = 0.0

    for index, block in enumerate(blocks):
        features = _extract_block_features(
            block,
            index=index,
            total_blocks=len(blocks),
            page_type=page_type,
            title=title,
            repeated_ratio=_repetition_ratio(block, contexts["global_counts"], contexts["global_total"]),
            cluster_repeat_ratio=_repetition_ratio(
                block,
                contexts["cluster_counts"].get(page_type, Counter()),
                contexts["cluster_totals"].get(page_type, 1),
            ),
        )
        score, reasons, should_truncate = _score_block(features)

        if should_truncate and cleaned_blocks:
            removed_blocks.append({
                "reason": "document_truncate",
                "score": round(score, 3),
                "signals": reasons,
                "text_preview": block[:160],
            })
            break

        if score >= _keep_threshold(page_type, features):
            cleaned_blocks.append(block.strip())
            kept_weight += max(score, 0.1)
            footer_run = 0
            continue

        removed_blocks.append({
            "reason": "low_content_score",
            "score": round(score, 3),
            "signals": reasons,
            "text_preview": block[:160],
        })
        removed_weight += abs(min(score, -0.1))
        footer_run = footer_run + 1 if features.is_footer_like else 0
        if footer_run >= 2 and features.position_ratio >= 0.55 and page_type in {"article", "marketing", "generic"}:
            break

    clean_markdown_value = "\n\n".join(block for block in cleaned_blocks if block).strip()
    clean_markdown_value = strip_inline_noise(clean_markdown_value)

    if not clean_markdown_value and raw_markdown:
        fallback = blocks[: max(1, min(3, len(blocks)))]
        clean_markdown_value = "\n\n".join(fallback).strip()

    confidence = kept_weight / max(0.5, kept_weight + removed_weight)
    return clean_markdown_value, removed_blocks, round(min(0.99, confidence), 3)


def _extract_block_features(
    block: str,
    *,
    index: int,
    total_blocks: int,
    page_type: str,
    title: str | None,
    repeated_ratio: float,
    cluster_repeat_ratio: float,
) -> BlockFeatures:
    text = markdown_to_text(block)
    normalized = normalize_block(block)
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    char_count = len(text)
    words = re.findall(r"\b[\w@.+-]{2,}\b", text)
    word_count = len(words)
    link_count = len(re.findall(r"\[(.*?)\]\((.*?)\)", block))
    image_count = len(re.findall(r"!\[.*?\]\(.*?\)", block))
    heading_match = re.match(r"^(#{1,6})\s+", block.lstrip())
    heading_level = len(heading_match.group(1)) if heading_match else 0
    list_item_count = len(re.findall(r"^\s*([-*+]|\d+\.)\s+", block, flags=re.MULTILINE))
    table_row_count = block.count("|")
    code_block = "```" in block
    phone_count = len(re.findall(r"(?:\+?\d[\d\-\s()]{7,}\d)", text))
    address_hint_count = len(re.findall(r"\b(address|alamat|street|jl\.|jalan|kota|mall|gedung)\b", text, flags=re.IGNORECASE))
    title_overlap = len(_significant_tokens(text) & _significant_tokens(title or ""))
    short_link_ratio = 0.0
    if lines:
        short_link_lines = sum(
            1
            for line in lines
            if re.match(r"^(\d+\.\s+|[-*+]\s+)?\[.*?\]\(.*?\)\s*$", line)
            or (len(line.split()) <= 6 and "[" in line and "](" in line)
        )
        short_link_ratio = short_link_lines / len(lines)

    block_type = "paragraph"
    if code_block:
        block_type = "code"
    elif table_row_count >= 3:
        block_type = "table"
    elif heading_level:
        block_type = "heading"
    elif list_item_count >= 2:
        block_type = "list"

    return BlockFeatures(
        block=block,
        block_type=block_type,
        text=text,
        normalized=normalized,
        index=index,
        total_blocks=total_blocks,
        page_type=page_type,
        char_count=char_count,
        word_count=word_count,
        line_count=len(lines),
        link_count=link_count,
        image_count=image_count,
        heading_level=heading_level,
        list_item_count=list_item_count,
        table_row_count=table_row_count,
        code_block=code_block,
        phone_count=phone_count,
        address_hint_count=address_hint_count,
        title_overlap=title_overlap,
        repeated_ratio=repeated_ratio,
        cluster_repeat_ratio=cluster_repeat_ratio,
        short_link_ratio=short_link_ratio,
    )


def _score_block(features: BlockFeatures) -> tuple[float, list[str], bool]:
    score = 0.0
    reasons: list[str] = []
    should_truncate = False

    if features.heading_level and features.title_overlap:
        score += 1.4
        reasons.append("title_heading_overlap")
    elif features.heading_level:
        score += 0.55
        reasons.append("heading")

    if features.block_type in {"table", "code"}:
        score += 1.0
        reasons.append(features.block_type)

    if features.is_long_form_text:
        score += 1.15
        reasons.append("long_form_text")

    if features.page_type == "location" and (features.phone_count or "get directions" in features.text.lower()):
        score += 0.9
        reasons.append("location_contact_data")

    if features.page_type == "listing" and features.link_count >= 1 and features.word_count <= 40:
        score += 0.45
        reasons.append("listing_item")

    if features.repeated_ratio >= 0.45 and not features.is_long_form_text and features.block_type not in {"table", "code"}:
        score -= 1.0
        reasons.append("repeated_across_crawl")

    if features.cluster_repeat_ratio >= 0.55 and features.word_count <= 40:
        score -= 0.75
        reasons.append("repeated_in_cluster")

    if features.is_short_link_block and features.page_type != "listing":
        score -= 0.95
        reasons.append("navigation_like")

    if features.image_count >= 5 and features.word_count < 20:
        score -= 1.2
        reasons.append("asset_heavy")

    if features.is_footer_like:
        score -= 1.35
        reasons.append("footer_like")
        if features.page_type in {"article", "marketing", "generic"} and features.position_ratio >= 0.5:
            should_truncate = True

    if any(pattern.search(features.text) for pattern in GENERIC_NOISE_PATTERNS):
        score -= 0.85
        reasons.append("generic_noise_phrase")

    if features.word_count <= 4 and not features.heading_level and not features.phone_count:
        score -= 0.35
        reasons.append("very_short")

    if features.position_ratio >= 0.75 and features.link_count >= 3 and features.word_count <= 35:
        score -= 0.65
        reasons.append("late_link_cluster")

    return score, reasons, should_truncate


def _keep_threshold(page_type: str, features: BlockFeatures) -> float:
    if page_type == "listing":
        return -0.05 if features.link_count else 0.1
    if page_type == "location":
        return -0.1 if (features.phone_count or "get directions" in features.text.lower()) else 0.1
    return 0.1


def _repetition_ratio(block: str, counts: Counter[str], total: int) -> float:
    normalized = normalize_block(block)
    if not normalized:
        return 0.0
    block_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    count = counts.get(block_hash, 0)
    if total < 2 or count < 2:
        return 0.0
    return count / total


def _looks_like_navigation_or_promo(block: str) -> bool:
    features = _extract_block_features(
        block,
        index=0,
        total_blocks=1,
        page_type="generic",
        title=None,
        repeated_ratio=0.0,
        cluster_repeat_ratio=0.0,
    )
    return features.is_short_link_block or (features.link_count >= 2 and features.word_count <= 25)


def _significant_tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z0-9]{4,}", (value or "").lower())
        if token not in STOP_WORDS
    }
