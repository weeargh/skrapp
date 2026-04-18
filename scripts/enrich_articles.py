#!/usr/bin/env python3
"""
Phase 1 — Rule-based enrichment (no LLM, no API cost).

Reads raw articles from out/zendesk_preview/, infers article_type,
intent_tags, products, etc. from title/section/body patterns, then writes
enriched drafts to kb-ai-ready/drafts/.  Human review (Phase 2) corrects
anything the rules get wrong.

Usage:
    python scripts/enrich_articles.py [--src DIR] [--out DIR] [--resume]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ── Article type rules ─────────────────────────────────────────────────────
# Checked in order; first match wins.

TASK_TITLE_PATTERNS = [
    r"\bbagaimana\b",          # "Bagaimana cara ..."
    r"\bhow to\b",
    r"\bcara\b",
    r"\blangkah\b",            # steps
    r"\bmelakukan\b",
    r"\bmembuat\b",
    r"\bmengatur\b",
    r"\bmengelola\b",
    r"\bmengaktifkan\b",
    r"\bmenonaktifkan\b",
    r"\bmengintegrasikan\b",
    r"\bmenambahkan\b",
    r"\bmengirimkan\b",
    r"\bmengunduh\b",
    r"\bmengupload\b",
    r"\bmengunggah\b",
    r"\bsetup\b",
    r"\bconfigure\b",
    r"\benable\b",
    r"\bdisable\b",
    r"\binstall\b",
    r"\bsubmit\b",
]

CONCEPT_TITLE_PATTERNS = [
    r"\bsekilas\b",            # "sekilas tentang ..."
    r"\boverview\b",
    r"\bpenjelasan\b",
    r"\bmengenal\b",
    r"\btentang\b",
    r"\bapa itu\b",
    r"\bwhat is\b",
    r"\bperbedaan\b",          # "differences between ..."
    r"\bskema\b",              # "scheme / structure"
    r"\bdefinisi\b",
    r"\brelevan\b",
    r"\bfaq\b",
    r"\bfrequently asked\b",
    r"\bpanduan\b",            # guide/overview
    r"\brelease log\b",
    r"\bchangelog\b",
    r"\buse case\b",
    r"\bprogram referral\b",
    r"\bkuota\b",              # quota explanation articles
    r"\blimit\b",
    r"\bskema\b",
]

TROUBLESHOOTING_TITLE_PATTERNS = [
    r"\bmengatasi\b",
    r"\btroubleshoot\b",
    r"\berror\b",
    r"\bgagal\b",
    r"\btidak bisa\b",
    r"\btidak dapat\b",
    r"\bmasalah\b",
    r"\bkegagalan\b",
    r"\bfailed\b",
    r"\bfail\b",
    r"\bfix\b",
]


def _classify_type(title: str, body: str) -> str:
    t = title.lower()
    for pat in TROUBLESHOOTING_TITLE_PATTERNS:
        if re.search(pat, t, re.IGNORECASE):
            return "troubleshooting"
    for pat in CONCEPT_TITLE_PATTERNS:
        if re.search(pat, t, re.IGNORECASE):
            return "concept"
    for pat in TASK_TITLE_PATTERNS:
        if re.search(pat, t, re.IGNORECASE):
            return "task"
    # Body fallback: if it has numbered steps, it's a task
    if len(re.findall(r"^\d+\.", body, re.MULTILINE)) >= 3:
        return "task"
    return "concept"   # safe default


# ── Product detection ──────────────────────────────────────────────────────

PRODUCT_PATTERNS = {
    "Qontak CRM":         [r"\bcrm\b", r"\bdeals?\b", r"\btasks?\b", r"\bcompan(y|ies)\b"],
    "Qontak Omnichannel": [r"\bomnichannel\b", r"\binbox\b", r"\bcampaign\b", r"\bbroadcast\b"],
    "Qontak Chat":        [r"\bchatbot\b", r"\bbot\b", r"\bwhatsapp\b", r"\btelegram\b",
                           r"\binstagram\b", r"\bfacebook messenger\b", r"\bline\b"],
    "Bizphone":           [r"\bbizphone\b", r"\bcall center\b", r"\bvoice call\b"],
}


def _detect_products(title: str, body: str, section_title: str) -> list[str]:
    combined = f"{title} {section_title} {body[:2000]}".lower()
    found = []
    for product, patterns in PRODUCT_PATTERNS.items():
        if any(re.search(p, combined, re.IGNORECASE) for p in patterns):
            found.append(product)
    return found or ["Mekari Qontak"]


# ── Surface detection ──────────────────────────────────────────────────────

def _detect_surface(title: str, body: str) -> str:
    t = (title + " " + body[:1000]).lower()
    has_web    = bool(re.search(r"\bversi web\b|\bweb version\b|\bdesktop\b", t))
    has_mobile = bool(re.search(r"\bversi mobile\b|\bmobile version\b|\baplikasi\b|\bapp\b", t))
    has_api    = bool(re.search(r"\bapi\b|\btoken\b|\bendpoint\b|\bjson\b", t))
    if has_api and not (has_web or has_mobile):
        return "api"
    if has_web and has_mobile:
        return "all"
    if has_mobile:
        return "mobile"
    if has_web:
        return "web"
    return "web"   # default


# ── Intent tag extraction ──────────────────────────────────────────────────

def _extract_intent_tags(title: str, section_title: str, category_title: str, article_type: str) -> list[str]:
    """
    Derive kebab-case intent tags from structured metadata.
    Primary tag = slugified section, secondary tags from title keywords.
    """
    tags: list[str] = []

    def slugify(text: str) -> str:
        text = text.lower()
        # Remove filler words
        text = re.sub(r"\b(menu|fitur|cara|bagaimana|sekilas|tentang|overview|pada|di|ke|dan|atau|the|how|to|a|an|of|in|for)\b", "", text)
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text).strip("-")
        return text

    # 1. Section → primary tag (most stable)
    if section_title:
        sec_slug = slugify(section_title)
        if sec_slug and len(sec_slug) > 2:
            tags.append(sec_slug)

    # 2. Verb-object pairs from title (e.g. "membuat-template", "mengatur-broadcast")
    VERB_MAP = {
        "membuat":        "create",
        "menambahkan":    "add",
        "mengatur":       "configure",
        "mengedit":       "edit",
        "menghapus":      "delete",
        "mengintegrasikan": "integrate",
        "mengaktifkan":   "enable",
        "menonaktifkan":  "disable",
        "mengirimkan":    "send",
        "mengunduh":      "download",
        "mengunggah":     "upload",
        "memfilter":      "filter",
        "melihat":        "view",
        "melakukan":      "perform",
        "mengelola":      "manage",
        "mengatasi":      "troubleshoot",
        "menggunakan":    "use",
    }
    title_lower = title.lower()
    for id_verb, en_verb in VERB_MAP.items():
        if id_verb in title_lower:
            # Extract what comes after the verb
            rest = re.sub(r".*" + id_verb + r"\s*", "", title_lower, count=1)
            rest = re.sub(r"\b(pada|di|ke|dan|atau|versi|web|mobile)\b.*", "", rest).strip()
            rest_slug = re.sub(r"[^\w\s-]", "", rest)
            rest_slug = re.sub(r"\s+", "-", rest_slug).strip("-")[:30]
            if rest_slug and len(rest_slug) > 2:
                tags.append(f"{en_verb}-{rest_slug}")
            break

    # 3. Category as coarse tag
    if category_title:
        cat_slug = slugify(category_title)[:25]
        if cat_slug and cat_slug not in tags and len(cat_slug) > 2:
            tags.append(cat_slug)

    # Deduplicate, keep max 5
    seen = set()
    unique: list[str] = []
    for tag in tags:
        if tag not in seen and len(tag) > 2:
            seen.add(tag)
            unique.append(tag)
    return unique[:5]


# ── Query example generation ───────────────────────────────────────────────

def _clean_title_for_query(title: str) -> str:
    """Strip instructional prefixes so the noun phrase is left for query templates."""
    t = title.strip()
    # Remove leading "Bagaimana [cara|penerapan|penggunaan|cara kerja|...]"
    t = re.sub(
        r"^bagaimana\s+(cara\s+|penerapan\s+|penggunaan\s+|cara kerja\s+|implementasi\s+)?",
        "", t, flags=re.IGNORECASE,
    )
    # Remove other common instructional prefixes
    t = re.sub(
        r"^(how to\s+|cara\s+|sekilas tentang\s+|sekilas mengenai\s+|sekilas\s+"
        r"|penjelasan\s+|overview\s+|panduan\s+|mengenal\s+)",
        "", t, flags=re.IGNORECASE,
    )
    return t.strip() or title.strip()


def _generate_query_examples(title: str, article_type: str, products: list[str]) -> list[str]:
    """
    Template-based query examples in a mix of Bahasa Indonesia and English,
    matching how Qontak customers actually phrase support questions.
    """
    product_hint = products[0] if products else "Qontak"
    clean = _clean_title_for_query(title)

    if article_type == "task":
        return [
            f"Cara {clean}",
            f"Bagaimana cara {clean}?",
            f"Langkah-langkah {clean} di {product_hint}",
            f"How do I {clean}?",
            f"Mau {clean}, caranya gimana?",
        ]
    elif article_type == "troubleshooting":
        return [
            f"{clean} tidak berhasil, kenapa?",
            f"Ada masalah dengan {clean}",
            f"Kenapa {clean} gagal?",
            f"Error waktu {clean}",
            f"How to fix: {clean}?",
        ]
    else:  # concept
        return [
            f"Apa itu {clean}?",
            f"Apa fungsi {clean} di {product_hint}?",
            f"Penjelasan {clean}",
            f"What is {clean}?",
            f"Bagaimana cara kerja {clean}?",
        ]


# ── Solvability ────────────────────────────────────────────────────────────

def _infer_solvability(article_type: str, body: str) -> str:
    """
    task + steps in product UI → tool
    concept/explanation → content
    troubleshooting → hybrid
    """
    if article_type == "concept":
        return "content"
    if article_type == "troubleshooting":
        return "hybrid"
    # task: if body has numbered steps involving UI actions, it's tool
    ui_action_count = len(re.findall(
        r"\b(klik|pilih|tekan|buka|masuk|login|navigate|click|select|go to|open)\b",
        body, re.IGNORECASE,
    ))
    return "tool" if ui_action_count >= 3 else "hybrid"


# ── Compliance detection ───────────────────────────────────────────────────

COMPLIANCE_PATTERNS = [
    r"\bbilling\b", r"\bharga\b", r"\bpayment\b", r"\bsubscription\b",
    r"\binvoice\b", r"\btop.up\b", r"\bprivacy\b", r"\bdata\b",
    r"\bsecurity\b", r"\bkeamanan\b", r"\bpersonal data\b", r"\botp\b",
    r"\bverification\b", r"\bkontrak\b", r"\bsla\b", r"\bcompliance\b",
    r"\bpayment\b", r"\btransfer\b",
]

def _is_compliance_sensitive(title: str, body: str) -> bool:
    combined = (title + " " + body[:1000]).lower()
    return any(re.search(p, combined) for p in COMPLIANCE_PATTERNS)


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
    os.makedirs(os.path.dirname(path), exist_ok=True)
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{yaml_str}---\n\n{body}")


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Rule-based article enrichment (no LLM).")
    parser.add_argument("--src",    default="out/zendesk_preview", help="Source directory")
    parser.add_argument("--out",    default="kb-ai-ready/drafts",  help="Output directory")
    parser.add_argument("--resume", action="store_true",           help="Skip already-enriched files")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    files = sorted(f for f in os.listdir(args.src) if f.endswith(".md"))
    total = len(files)
    ok = skipped = 0

    print(f"Enriching {total} articles (rule-based, no LLM)  →  {args.out}/\n")

    for i, filename in enumerate(files, 1):
        dst_path = os.path.join(args.out, filename)
        if args.resume and os.path.exists(dst_path):
            skipped += 1
            continue

        src_path = os.path.join(args.src, filename)
        fm, body = _read_fm_and_body(src_path)

        title         = fm.get("title") or ""
        section_title = fm.get("section_title") or ""
        category_title = fm.get("category_title") or ""

        article_type = _classify_type(title, body)
        products     = _detect_products(title, body, section_title)
        surface      = _detect_surface(title, body)
        intent_tags  = _extract_intent_tags(title, section_title, category_title, article_type)
        solvability  = _infer_solvability(article_type, body)
        compliance   = _is_compliance_sensitive(title, body)
        queries      = _generate_query_examples(title, article_type, products)

        # Merge into frontmatter
        fm["article_type"]      = article_type
        fm["solvability_type"]  = solvability
        fm["intent_tags"]       = intent_tags
        fm["query_examples"]    = queries
        fm["products"]          = products
        fm["product_surface"]   = surface
        fm["language"]          = fm.get("language") or "id"
        fm["compliance_sensitive"] = compliance
        fm.setdefault("plan_scope",            None)
        fm.setdefault("chunk_groups",          [])
        fm.setdefault("related_chunks",        [])
        fm.setdefault("last_verified",         None)
        fm.setdefault("verified_by",           None)
        fm.setdefault("faithfulness_threshold", None)
        fm["review_status"] = "draft"

        _write_md(dst_path, fm, body)

        print(f"  [{i:>4}/{total}]  {article_type:<16}  {filename[:55]}  {intent_tags[:2]}")
        ok += 1

    print(f"\nDone. {ok} enriched, {skipped} skipped.")
    print(f"Drafts → {os.path.abspath(args.out)}/")
    print(f"\nNext: python scripts/review_article.py")


if __name__ == "__main__":
    main()
