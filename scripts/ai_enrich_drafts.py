#!/usr/bin/env python3
"""
Phase 1c — AI-assisted draft enrichment.

Reads prepared drafts from kb-ai-ready/drafts/, uses Claude to:
  1. Fill in scaffold sections (Prerequisites / Steps / etc.)
  2. Assign a confidence score per section (high / medium / low)
  3. Write filled sections at the top of the body, keeping the original
     content below a separator so reviewers can verify.

Frontmatter additions:
    ai_enriched: true
    ai_model: claude-haiku-4-5-20251001
    section_confidence:
      Prerequisites: high
      Steps: medium
      ...
    overall_confidence: low   ← min of all section scores

Usage:
    python scripts/ai_enrich_drafts.py [--drafts DIR] [--resume]
                                        [--model MODEL] [--limit N]
                                        [--dry-run]

Review only low-confidence results:
    python scripts/review_article.py --max-confidence low
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import defaultdict

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


# ── Required sections per type (mirrors prepare_drafts.py) ────────────────

REQUIRED_SECTIONS: dict[str, list[str]] = {
    "task": ["Prerequisites", "Steps", "Expected Result", "Error States", "Escalation"],
    "concept": ["Definition", "Why It Matters", "Key Attributes", "Related Tasks"],
    "troubleshooting": ["Symptom", "Root Cause", "Solution", "Escalation"],
}

SECTION_HINTS: dict[str, dict[str, str]] = {
    "task": {
        "Prerequisites": "Required role/permission, plan tier, prior setup steps. Be specific to Qontak.",
        "Steps": "Numbered action steps extracted/reorganized from the article. Each: UI action → expected screen change.",
        "Expected Result": "What the user sees when successfully done (confirmation message, redirect, updated list).",
        "Error States": "Common errors users hit and how to fix them. If none documented, write exactly: No common errors documented.",
        "Escalation": "When to contact Qontak support and what info to provide (screenshot, account ID, error message).",
    },
    "concept": {
        "Definition": "One clear paragraph defining the feature/concept in Qontak context.",
        "Why It Matters": "Business value — why this feature helps Qontak users (CRM / Omnichannel).",
        "Key Attributes": "Bullet list of key properties, limits, behaviours, or configuration options.",
        "Related Tasks": "Titles of task articles that show how to use this concept (based on related context or infer).",
    },
    "troubleshooting": {
        "Symptom": "Exact error message or observable behaviour the user sees.",
        "Root Cause": "Why this happens — brief technical reason.",
        "Solution": "Step-by-step fix using numbered steps.",
        "Escalation": "When self-service fix fails: what info to send to Qontak support.",
    },
}

CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1}


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


# ── Scaffold parsing ───────────────────────────────────────────────────────

def _parse_scaffold(body: str) -> tuple[list[str], str]:
    """
    Returns (missing_section_names, clean_body_without_scaffold).
    The scaffold is the outer <!-- ═══ ... --> comment block.
    """
    # Match from <!-- ═══ to a standalone --> line
    m = re.search(r"<!-- ═══.+?\n-->", body, re.DOTALL)
    if not m:
        return [], body

    scaffold_text = m.group()
    # Extract ## Section headers from inside the scaffold
    missing = re.findall(r"^## (.+)$", scaffold_text, re.MULTILINE)
    # Remove scaffold from body
    clean_body = body[: m.start()] + body[m.end():]
    clean_body = clean_body.lstrip("\n")
    return missing, clean_body


# ── Cross-article context ──────────────────────────────────────────────────

def _build_article_index(drafts_dir: str) -> dict[str, list[dict]]:
    """Index articles by section_title for related-article context."""
    index: dict[str, list[dict]] = defaultdict(list)
    for filename in sorted(os.listdir(drafts_dir)):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(drafts_dir, filename)
        try:
            fm, body = _read_fm_and_body(path)
            key = fm.get("section_title") or fm.get("category_title") or ""
            if key:
                # Strip scaffold before indexing
                _, clean = _parse_scaffold(body)
                index[key].append({
                    "title": fm.get("title", ""),
                    "type": fm.get("article_type", ""),
                    "snippet": clean[:1000],
                })
        except Exception:
            pass
    return dict(index)


def _related_context(fm: dict, index: dict, max_articles: int = 3) -> str:
    key = fm.get("section_title") or fm.get("category_title") or ""
    current_title = fm.get("title", "")
    candidates = [a for a in index.get(key, []) if a["title"] != current_title]
    chosen = candidates[:max_articles]
    if not chosen:
        return ""
    parts = []
    for a in chosen:
        parts.append(f"### [{a['type']}] {a['title']}\n{a['snippet']}")
    return "\n\n".join(parts)


# ── Confidence helpers ─────────────────────────────────────────────────────

def _overall_confidence(section_confidence: dict[str, str]) -> str:
    if not section_confidence:
        return "low"
    min_rank = min(CONFIDENCE_RANK.get(v, 1) for v in section_confidence.values())
    return {3: "high", 2: "medium", 1: "low"}[min_rank]


# ── Prompt builder ─────────────────────────────────────────────────────────

def _build_prompt(fm: dict, clean_body: str, missing_sections: list[str], related: str) -> str:
    article_type = fm.get("article_type", "concept")
    title = fm.get("title", "")
    products = ", ".join(fm.get("products") or ["Mekari Qontak"])
    hints = SECTION_HINTS.get(article_type, {})

    section_block = ""
    for sec in missing_sections:
        hint = hints.get(sec, f"Fill in {sec} based on article context.")
        section_block += f'\n  "{sec}": {{ "content": "...", "confidence": "high|medium|low" }},'
        section_block += f"\n  // hint: {hint}"

    related_block = (
        f"\n\nRELATED ARTICLES IN SAME SECTION (use as context):\n{related}"
        if related else ""
    )

    lang = fm.get("language", "id")
    lang_name = "Bahasa Indonesia" if lang == "id" else "English"

    return f"""BAHASA: Tulis semua konten dalam {lang_name}. JANGAN gunakan bahasa lain.
LANGUAGE: Write ALL section content in {lang_name} ONLY. Do not use English if language is Indonesian.

You are enriching a Mekari Qontak help center article for an AI chatbot knowledge base.

ARTICLE:
  Title: {title}
  Type: {article_type}
  Products: {products}
  Language: {lang_name}

ORIGINAL ARTICLE BODY:
{clean_body[:3000]}
{related_block}

TASK:
Fill in the missing sections below. Apply all MekariRAG content quality rules:

1. SELF-SUFFICIENT: Each section must be readable alone — do not say "see above" or "as mentioned"
2. RESTATE INTENT: Start the first section by echoing the customer's question/goal
3. EXPLICIT NAMES: Never use "ini", "tersebut", "di sini" — always use the full UI name
   ("Klik tombol Publish" not "Klik tombol ini")
4. EXPLICIT OUTCOMES: After each step state what the user sees ("Sistem akan menampilkan...")
5. NO ASSUMED KNOWLEDGE: State all prerequisites — roles, plan tier, prior setup
6. NO MARKETING: Remove promotional language; only factual, actionable content
7. CONVERSATIONAL BRIDGE: Mirror how customers actually ask ("Kenapa tidak bisa...?")

Rate confidence per section:
  "high"   = content explicitly in the original article body
  "medium" = implied/inferable from article + related context
  "low"    = based on general Qontak product knowledge, needs human check

Rules:
- Write in {lang_name} ONLY
- Use Qontak UI terms exactly as they appear in the article (menu names, button labels)
- Numbered steps for procedures; bullet points for lists
- Max 150 words per section

MISSING SECTIONS: {missing_sections}

Return ONLY valid JSON (no markdown fences):
{{
  "sections": {{{section_block}
  }},
  "notes": "catatan untuk reviewer jika ada yang tidak pasti"
}}"""


# ── Body reconstruction ────────────────────────────────────────────────────

CONF_BADGE = {"high": "✓", "medium": "~", "low": "?"}


def _build_new_body(
    clean_body: str,
    sections: dict[str, dict],
    article_type: str,
    section_confidence: dict[str, str],
) -> str:
    """
    Output structured sections only. No separator, no original body.
    Each section is self-sufficient per MekariRAG design principle.
    """
    order = REQUIRED_SECTIONS.get(article_type, list(sections.keys()))

    parts: list[str] = []
    for sec_name in order:
        if sec_name not in sections:
            continue
        content = sections[sec_name]["content"].strip()
        conf = section_confidence.get(sec_name, "low")
        badge = CONF_BADGE[conf]
        parts.append(f"## {sec_name}  <!-- confidence:{conf} {badge} -->\n\n{content}")

    return "\n\n".join(parts)


# ── JSON parsing with fallback ─────────────────────────────────────────────

def _parse_response(raw: str) -> dict:
    # Strip markdown code fences if present
    raw = re.sub(r"^```(?:json)?\s*\n?", "", raw.strip())
    raw = re.sub(r"\n?```\s*$", "", raw)
    # Strip single-line JS comments (// ...) which Claude sometimes adds
    raw = re.sub(r"\s*//[^\n]*", "", raw)
    # Remove non-printable control characters (except tab and newline)
    raw = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", raw)

    def _try_parse(s: str) -> dict:
        return json.loads(s)

    try:
        return _try_parse(raw)
    except json.JSONDecodeError:
        pass

    # Repair 1: escape literal newlines inside JSON string values
    result, in_string, i = [], False, 0
    while i < len(raw):
        c = raw[i]
        if c == '"' and (i == 0 or raw[i - 1] != "\\"):
            in_string = not in_string
        if c == "\n" and in_string:
            result.append("\\n")
        else:
            result.append(c)
        i += 1
    repaired = "".join(result)

    try:
        return _try_parse(repaired)
    except json.JSONDecodeError:
        pass

    # Repair 2: strip trailing commas before } or ]
    repaired2 = re.sub(r",\s*([}\]])", r"\1", repaired)
    return _try_parse(repaired2)


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AI-assisted draft enrichment with confidence scores.")
    parser.add_argument("--drafts",  default="kb-ai-ready/drafts",      help="Drafts directory")
    parser.add_argument("--resume",  action="store_true",                help="Skip already AI-enriched files")
    parser.add_argument("--rerun",   action="store_true",                help="Re-process already AI-enriched files (overwrite)")
    parser.add_argument("--max-confidence", dest="max_confidence", default=None,
                        choices=["low", "medium", "high"],
                        help="Only process articles at or below this confidence level")
    parser.add_argument("--model",   default="claude-haiku-4-5-20251001", help="Claude model to use")
    parser.add_argument("--limit",   type=int, default=0,               help="Process at most N articles (0=all)")
    parser.add_argument("--dry-run", action="store_true",               help="Build prompts without calling API")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: Set ANTHROPIC_API_KEY environment variable.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key) if not args.dry_run else None

    if not os.path.isdir(args.drafts):
        print(f"ERROR: {args.drafts} not found. Run enrich_articles.py first.")
        sys.exit(1)

    print("Building cross-article index for related context...")
    article_index = _build_article_index(args.drafts)
    sections_count = sum(len(v) for v in article_index.values())
    print(f"  {sections_count} articles indexed across {len(article_index)} sections\n")

    files = sorted(f for f in os.listdir(args.drafts) if f.endswith(".md"))
    total = len(files)

    processed = skipped = errors = 0
    cost_input = cost_output = 0  # rough token tracking

    for i, filename in enumerate(files, 1):
        if args.limit and processed >= args.limit:
            break

        path = os.path.join(args.drafts, filename)
        fm, body = _read_fm_and_body(path)

        if args.resume and fm.get("ai_enriched"):
            skipped += 1
            continue

        # Confidence filter
        if args.max_confidence:
            article_conf = fm.get("overall_confidence") or "low"
            if CONFIDENCE_RANK.get(article_conf, 1) > CONFIDENCE_RANK.get(args.max_confidence, 1):
                skipped += 1
                continue

        # For rerun: strip previously AI-filled sections, keep only original body
        if args.rerun and fm.get("ai_enriched"):
            sep = "\n---\n"
            idx = body.find(sep)
            if idx == -1:
                # Already cleanly processed (no separator) — skip
                skipped += 1
                continue
            body = body[idx + len(sep):]
            # Strip any AI review comment (duplicated on repeated reruns)
            body = re.sub(r"<!-- AI review:.*?-->\s*", "", body, flags=re.DOTALL)
            clean_body = body.strip()
            missing_sections = list((fm.get("section_confidence") or {}).keys())
            if not missing_sections:
                skipped += 1
                continue
        else:
            # Parse scaffold — skip articles that don't need enrichment
            missing_sections, clean_body = _parse_scaffold(body)
            if not missing_sections:
                skipped += 1
                continue

        article_type = fm.get("article_type", "concept")
        related = _related_context(fm, article_index)
        prompt = _build_prompt(fm, clean_body, missing_sections, related)

        label = filename[:52]
        print(f"  [{i:>4}/{total}]  {label}")
        print(f"           missing: {missing_sections}")

        if args.dry_run:
            print(f"           [DRY RUN] prompt={len(prompt)} chars — skipping API call\n")
            processed += 1
            continue

        # ── API call ──────────────────────────────────────────────────────
        try:
            response = client.messages.create(
                model=args.model,
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}],
            )
            raw_text = response.content[0].text

            # Track rough token usage
            cost_input  += response.usage.input_tokens
            cost_output += response.usage.output_tokens

            data = _parse_response(raw_text)
            sections = data.get("sections", {})
            notes = data.get("notes", "")

            if not sections:
                print(f"           WARNING: empty sections in response — skipping\n")
                errors += 1
                continue

            section_confidence = {
                k: v.get("confidence", "low")
                for k, v in sections.items()
                if isinstance(v, dict)
            }
            overall = _overall_confidence(section_confidence)

            # Update frontmatter
            fm["ai_enriched"]       = True
            fm["ai_model"]          = args.model
            fm["section_confidence"] = section_confidence
            fm["overall_confidence"] = overall
            if notes:
                fm["ai_notes"] = notes

            # Rebuild body
            new_body = _build_new_body(clean_body, sections, article_type, section_confidence)
            _write_md(path, fm, new_body)

            badge_map = {"high": "✓✓ HIGH", "medium": "~~ MED ", "low": "?? LOW "}
            print(f"           {badge_map[overall]}  {section_confidence}\n")
            processed += 1

            time.sleep(0.3)  # polite rate limiting

        except json.JSONDecodeError as e:
            print(f"           ERROR: JSON parse failed: {e}")
            print(f"           Raw (first 300): {raw_text[:300]!r}\n")
            errors += 1
        except Exception as e:
            print(f"           ERROR: {e}\n")
            errors += 1

    # ── Summary ───────────────────────────────────────────────────────────
    print("─" * 70)
    print(f"Done.")
    print(f"  {processed} articles AI-enriched")
    print(f"  {skipped}   skipped (no scaffold or already enriched)")
    print(f"  {errors}   errors")
    if not args.dry_run and (cost_input or cost_output):
        # Haiku pricing: $0.80/MTok in, $4/MTok out
        est_cost = (cost_input / 1_000_000 * 0.80) + (cost_output / 1_000_000 * 4.00)
        print(f"\n  Tokens: {cost_input:,} in / {cost_output:,} out  (est. ${est_cost:.2f})")
    print(f"\nNext: python scripts/review_article.py --max-confidence low")


if __name__ == "__main__":
    main()
