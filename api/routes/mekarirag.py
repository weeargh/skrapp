"""
MekariRAG Review API
GET  /mekarirag/review                → filterable review table
GET  /mekarirag/pages/<slug>          → individual article page (rendered + edit)
GET  /mekarirag/api/articles          → list all draft articles as JSON
GET  /mekarirag/api/article/<slug>    → single article with sections + prev/next
PUT  /mekarirag/api/article/<slug>    → save edits back to .md file
"""
from __future__ import annotations

import os
import re

import yaml
from flask import Blueprint, jsonify, request, send_file

mekarirag_bp = Blueprint("mekarirag", __name__)

DRAFTS_DIR = os.environ.get("MEKARIRAG_DRAFTS_DIR", "kb-ai-ready/drafts")

REQUIRED_SECTIONS: dict[str, list[str]] = {
    "task":             ["Prerequisites", "Steps", "Expected Result", "Error States", "Escalation"],
    "concept":          ["Definition", "Why It Matters", "Key Attributes", "Related Tasks"],
    "troubleshooting":  ["Symptom", "Root Cause", "Solution", "Escalation"],
}

CONF_BADGE = {"high": "✓", "medium": "~", "low": "?"}


# ── Helpers ────────────────────────────────────────────────────────────────

def _read(path: str) -> tuple[dict, str]:
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


def _write(path: str, fm: dict, body: str) -> None:
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{yaml_str}---\n\n{body}")


def _parse_sections(body: str) -> dict[str, dict]:
    """Split body into {section_name: {content, confidence}} dict."""
    header_re = re.compile(
        r'^## (.+?)(?:\s*<!--\s*confidence:(\w+)[^>]*-->)?\s*$',
        re.MULTILINE,
    )
    matches = list(header_re.finditer(body))
    sections: dict[str, dict] = {}
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        confidence = m.group(2) or "medium"
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[start:end].strip()
        sections[name] = {"content": content, "confidence": confidence}
    return sections


def _build_body(sections: dict[str, dict], article_type: str) -> str:
    order = REQUIRED_SECTIONS.get(article_type, list(sections.keys()))
    # Include any extra sections not in canonical order
    extra = [k for k in sections if k not in order]
    parts = []
    for name in order + extra:
        if name not in sections:
            continue
        conf = sections[name].get("confidence", "medium")
        badge = CONF_BADGE.get(conf, "~")
        content = sections[name]["content"].strip()
        parts.append(f"## {name}  <!-- confidence:{conf} {badge} -->\n\n{content}")
    return "\n\n".join(parts)


def _conf_label(score) -> str:
    if score is None:
        return "unknown"
    if score >= 0.85:
        return "high"
    if score >= 0.55:
        return "medium"
    return "low"


def _slug(filename: str) -> str:
    return filename.replace(".md", "")


def _filename(slug: str) -> str:
    return slug + ".md"


# ── Routes ─────────────────────────────────────────────────────────────────

def _all_slugs() -> list[str]:
    """Sorted list of all draft slugs (alphabetical)."""
    if not os.path.isdir(DRAFTS_DIR):
        return []
    return sorted(_slug(f) for f in os.listdir(DRAFTS_DIR) if f.endswith(".md"))


@mekarirag_bp.route("/mekarirag/review")
def review_page():
    html_path = os.path.join(os.path.dirname(__file__), "../../web/mekarirag.html")
    return send_file(os.path.abspath(html_path))


@mekarirag_bp.route("/mekarirag/pages/<path:slug>")
def article_page(slug: str):
    html_path = os.path.join(os.path.dirname(__file__), "../../web/mekarirag-page.html")
    return send_file(os.path.abspath(html_path))


@mekarirag_bp.route("/mekarirag/api/articles")
def list_articles():
    if not os.path.isdir(DRAFTS_DIR):
        return jsonify({"error": f"Drafts dir not found: {DRAFTS_DIR}"}), 404

    articles = []
    for filename in sorted(os.listdir(DRAFTS_DIR)):
        if not filename.endswith(".md"):
            continue
        path = os.path.join(DRAFTS_DIR, filename)
        try:
            fm, body = _read(path)
            sections = _parse_sections(body)
            score = fm.get("faithfulness_threshold")
            articles.append({
                "slug":                _slug(filename),
                "title":               fm.get("title", filename),
                "article_type":        fm.get("article_type", ""),
                "solvability_type":    fm.get("solvability_type", ""),
                "products":            fm.get("products") or [],
                "product_surface":     fm.get("product_surface", ""),
                "language":            fm.get("language", "id"),
                "intent_tags":         fm.get("intent_tags") or [],
                "compliance_sensitive": fm.get("compliance_sensitive", False),
                "faithfulness_threshold": score,
                "confidence_label":    _conf_label(score),
                "verified_by":         fm.get("verified_by"),
                "last_verified":       fm.get("last_verified"),
                "section_names":       list(sections.keys()),
                "section_count":       len(sections),
            })
        except Exception as e:
            articles.append({"slug": _slug(filename), "title": filename, "error": str(e)})

    return jsonify(articles)


@mekarirag_bp.route("/mekarirag/api/article/<path:slug>")
def get_article(slug: str):
    path = os.path.join(DRAFTS_DIR, _filename(slug))
    if not os.path.exists(path):
        return jsonify({"error": "Not found"}), 404

    fm, body = _read(path)
    sections = _parse_sections(body)

    # Prev / next navigation (alphabetical order)
    slugs = _all_slugs()
    idx = slugs.index(slug) if slug in slugs else -1
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx != -1 and idx < len(slugs) - 1 else None

    return jsonify({
        "slug":                slug,
        "position":            idx + 1,
        "total":               len(slugs),
        "prev_slug":           prev_slug,
        "next_slug":           next_slug,
        "title":               fm.get("title", ""),
        "canonical_url":       fm.get("canonical_url", ""),
        "article_type":        fm.get("article_type", ""),
        "solvability_type":    fm.get("solvability_type", ""),
        "products":            fm.get("products") or [],
        "product_surface":     fm.get("product_surface", ""),
        "language":            fm.get("language", "id"),
        "intent_tags":         fm.get("intent_tags") or [],
        "query_examples":      fm.get("query_examples") or [],
        "compliance_sensitive": fm.get("compliance_sensitive", False),
        "plan_scope":          fm.get("plan_scope"),
        "chunk_groups":        fm.get("chunk_groups") or [],
        "related_chunks":      fm.get("related_chunks") or [],
        "faithfulness_threshold": fm.get("faithfulness_threshold"),
        "verified_by":         fm.get("verified_by"),
        "last_verified":       fm.get("last_verified"),
        "sections":            sections,
    })


@mekarirag_bp.route("/mekarirag/api/article/<path:slug>", methods=["PUT"])
def save_article(slug: str):
    path = os.path.join(DRAFTS_DIR, _filename(slug))
    if not os.path.exists(path):
        return jsonify({"error": "Not found"}), 404

    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No JSON body"}), 400

    fm, _ = _read(path)

    # Update frontmatter fields that are safe to edit
    for field in ("title", "article_type", "solvability_type", "products",
                  "product_surface", "language", "intent_tags", "query_examples",
                  "compliance_sensitive", "plan_scope", "faithfulness_threshold",
                  "verified_by", "last_verified", "chunk_groups", "related_chunks"):
        if field in data:
            fm[field] = data[field]

    # Rebuild body from edited sections
    sections = data.get("sections", {})
    article_type = fm.get("article_type", "concept")
    new_body = _build_body(sections, article_type)

    _write(path, fm, new_body)
    return jsonify({"ok": True, "slug": slug})
