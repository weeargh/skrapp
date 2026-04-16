"""MVP job and page routes."""
from __future__ import annotations

import os
from datetime import datetime, timezone

from flask import Blueprint, abort, jsonify, request, send_file

from api.preview_capture import ensure_page_screenshot
from api.validators import (
    generate_job_id,
    validate_ignore_prefixes,
    validate_max_depth,
    validate_max_pages,
    validate_path_prefix,
    validate_timeout,
    validate_url,
)
from config import settings
from config.constants import ArtifactKind, JobState
from crawler.url_utils import get_path
from db import queries
from worker.job_artifacts import build_page_json_record, ensure_artifact


jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/v1/jobs", methods=["POST"])
def create_job():
    """Create a new crawl job."""
    data = request.get_json() or {}

    start_url = (data.get("start_url") or "").strip()
    is_valid, error_message, hostname = validate_url(start_url)
    if not is_valid or not hostname:
        return jsonify({"error": "Invalid URL", "message": error_message}), 400

    max_pages = validate_max_pages(
        data.get("max_pages"),
        settings.DEFAULT_MAX_PAGES,
        settings.MIN_PAGES_LIMIT,
        settings.MAX_PAGES_LIMIT,
    )
    max_depth = validate_max_depth(
        data.get("max_depth"),
        settings.DEFAULT_MAX_DEPTH,
        settings.MIN_DEPTH_LIMIT,
        settings.MAX_DEPTH_LIMIT,
    )
    timeout_seconds = validate_timeout(
        data.get("timeout_seconds"),
        settings.DEFAULT_TIMEOUT_SECONDS,
        settings.MIN_TIMEOUT_SECONDS,
        settings.MAX_TIMEOUT_SECONDS,
    )
    ignore_prefixes = validate_ignore_prefixes(data.get("ignore_path_prefixes"))
    allowed_path_prefix = validate_path_prefix(data.get("allowed_path_prefix"))
    if not allowed_path_prefix:
        allowed_path_prefix = _derive_allowed_path_prefix(start_url)

    job_id = generate_job_id()
    os.makedirs(os.path.join(settings.JOBS_OUTPUT_DIR, job_id), exist_ok=True)
    os.makedirs(os.path.join(settings.JOBS_OUTPUT_DIR, job_id, "state"), exist_ok=True)

    job = queries.create_crawl_job(
        job_id=job_id,
        start_url=start_url,
        allowed_host=hostname,
        allowed_path_prefix=allowed_path_prefix,
        max_depth=max_depth,
        max_pages=max_pages,
        ignore_path_prefixes=ignore_prefixes,
        timeout_seconds=timeout_seconds,
    )
    return jsonify(_serialize_job(job)), 201


@jobs_bp.route("/v1/jobs", methods=["GET"])
def list_jobs():
    """List jobs."""
    status = request.args.get("status") or None
    limit = _parse_int(request.args.get("limit"), 50)
    offset = _parse_int(request.args.get("offset"), 0)
    jobs = queries.list_crawl_jobs(status=status, limit=limit, offset=offset)
    return jsonify({"jobs": [_serialize_job_summary(job) for job in jobs]})


@jobs_bp.route("/v1/jobs/<job_id>", methods=["GET"])
def get_job(job_id: str):
    """Get one job."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404
    return jsonify(_serialize_job(job))


@jobs_bp.route("/v1/jobs/<job_id>/delete", methods=["POST"])
def delete_job(job_id: str):
    """Delete a job and all its data."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    if job["status"] in (JobState.QUEUED, JobState.STARTING, JobState.RUNNING, JobState.FINALIZING):
        return jsonify({
            "error": "Bad Request",
            "message": "Cannot delete an active job. Cancel it first.",
        }), 400

    # Remove artifact files from disk
    job_output_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    if os.path.isdir(job_output_dir):
        import shutil
        shutil.rmtree(job_output_dir, ignore_errors=True)

    queries.delete_crawl_job(job_id)
    return jsonify({"job_id": job_id, "deleted": True})


@jobs_bp.route("/v1/jobs/<job_id>/retry", methods=["POST"])
def retry_job(job_id: str):
    """Create a new job with the same parameters as an existing one."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    new_job_id = generate_job_id()
    os.makedirs(os.path.join(settings.JOBS_OUTPUT_DIR, new_job_id), exist_ok=True)
    os.makedirs(os.path.join(settings.JOBS_OUTPUT_DIR, new_job_id, "state"), exist_ok=True)

    new_job = queries.create_crawl_job(
        job_id=new_job_id,
        start_url=job["start_url"],
        allowed_host=job["allowed_host"],
        allowed_path_prefix=job.get("allowed_path_prefix"),
        max_depth=job.get("max_depth", settings.DEFAULT_MAX_DEPTH),
        max_pages=job.get("max_pages", settings.DEFAULT_MAX_PAGES),
        ignore_path_prefixes=job.get("ignore_path_prefixes") or [],
        timeout_seconds=job.get("timeout_seconds", settings.DEFAULT_TIMEOUT_SECONDS),
    )
    return jsonify(_serialize_job(new_job)), 201


@jobs_bp.route("/v1/jobs/<job_id>/cancel", methods=["POST"])
def cancel_job(job_id: str):
    """Cancel a queued or running job."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    if job["status"] not in (JobState.QUEUED, JobState.STARTING, JobState.RUNNING, JobState.FINALIZING):
        return jsonify({
            "error": "Bad Request",
            "message": f"Cannot cancel job in '{job['status']}' state",
        }), 400

    updated = queries.update_crawl_job_status(job_id, JobState.CANCELLED)
    return jsonify({
        "job_id": job_id,
        "status": updated["status"],
        "message": "Job cancellation requested. Finalization will finish shortly.",
    })


@jobs_bp.route("/v1/jobs/<job_id>/tree", methods=["GET"])
def get_tree(job_id: str):
    """Return the page tree for a job."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404
    tree = queries.get_job_tree(job_id)
    tree["start_url"] = job["start_url"]
    tree["max_depth"] = job["max_depth"]
    return jsonify(tree)


@jobs_bp.route("/v1/jobs/<job_id>/pages", methods=["GET"])
def list_pages(job_id: str):
    """List pages for a job."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    depth = request.args.get("depth")
    depth = int(depth) if depth is not None and depth != "" else None
    parent_page_id = request.args.get("parent_page_id") or None
    status = request.args.get("status") or None
    limit = _parse_int(request.args.get("limit"), 100)
    offset = _parse_int(request.args.get("offset"), 0)

    pages = queries.list_pages_for_job(
        job_id,
        depth=depth,
        parent_page_id=parent_page_id,
        status=status,
        limit=limit,
        offset=offset,
    )
    total = queries.count_pages_for_job(
        job_id,
        depth=depth,
        parent_page_id=parent_page_id,
        status=status,
    )
    return jsonify({
        "job_id": job_id,
        "total": total,
        "pages": [_serialize_page_summary(page) for page in pages],
    })


@jobs_bp.route("/v1/jobs/<job_id>/pages/<page_id>", methods=["GET"])
def get_page(job_id: str, page_id: str):
    """Get page detail."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    page = queries.get_page_by_id(page_id)
    if not page or page["job_id"] != job_id:
        return jsonify({"error": "Not Found", "message": "Page not found"}), 404

    include_export_json = request.args.get("include_export_json") in {"1", "true", "yes"}
    return jsonify(_serialize_page_detail(page, include_export_json=include_export_json))


@jobs_bp.route("/v1/jobs/<job_id>/pages/<page_id>/screenshot", methods=["GET"])
def get_page_screenshot(job_id: str, page_id: str):
    """Return a cached browser screenshot for a preview page."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    page = queries.get_page_by_id(page_id)
    if not page or page["job_id"] != job_id:
        return jsonify({"error": "Not Found", "message": "Page not found"}), 404

    force_refresh = request.args.get("refresh") in {"1", "true", "yes"}
    try:
        screenshot_path, metadata = ensure_page_screenshot(job_id, page, force_refresh=force_refresh)
    except ValueError as exc:
        return jsonify({"error": "Bad Request", "message": str(exc)}), 400
    except Exception as exc:
        return jsonify({"error": "Capture Failed", "message": str(exc)}), 502

    response = send_file(screenshot_path, mimetype="image/jpeg")
    response.headers["X-Preview-Final-URL"] = metadata.get("final_url", "")
    response.headers["X-Preview-Blocked-Signals"] = ",".join(metadata.get("blocked_signals", []))
    return response


@jobs_bp.route("/v1/jobs/<job_id>/artifacts", methods=["GET"])
def list_artifacts(job_id: str):
    """List generated artifacts for a job."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404

    artifacts = queries.get_artifacts_for_job(job_id)
    items = []
    for artifact in artifacts:
        items.append({
            "kind": artifact["kind"],
            "download_url": f"/v1/jobs/{job_id}/artifacts/{artifact['kind']}/download",
            "size_bytes": artifact["byte_size"],
        })
    return jsonify({"job_id": job_id, "artifacts": items})


@jobs_bp.route("/v1/jobs/<job_id>/artifacts/<kind>/download", methods=["GET"])
def download_artifact(job_id: str, kind: str):
    """Download a generated artifact by kind."""
    mime_types = {
        ArtifactKind.PAGE_JSON_ZIP: "application/zip",
        ArtifactKind.LLM_READY_JSONL: "application/x-ndjson",
        ArtifactKind.RAW_MARKDOWN_JSONL: "application/x-ndjson",
        ArtifactKind.PLAIN_TEXT_JSONL: "application/x-ndjson",
        ArtifactKind.PAGES_JSONL: "application/x-ndjson",
        ArtifactKind.TREE_JSON: "application/json",
        ArtifactKind.MARKDOWN_ZIP: "application/zip",
    }
    return _download_artifact(job_id, kind, mime_types.get(kind, "application/octet-stream"))


def _download_artifact(job_id: str, kind: str, mimetype: str):
    """Generic artifact downloader."""
    job = queries.get_crawl_job(job_id)
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found"}), 404
    if job["status"] not in (JobState.DONE, JobState.CANCELLED):
        return jsonify({
            "error": "Bad Request",
            "message": f"Job is not complete. Current status: {job['status']}",
        }), 400

    if kind == ArtifactKind.PAGE_JSON_ZIP:
        ensure_artifact(job_id, kind, force_refresh=True)

    artifact = queries.get_artifact_by_kind(job_id, kind)
    if not artifact or not os.path.exists(artifact["path"]):
        try:
            ensure_artifact(job_id, kind)
        except ValueError:
            return jsonify({"error": "Not Found", "message": "Artifact not found"}), 404
        artifact = queries.get_artifact_by_kind(job_id, kind)
        if not artifact or not os.path.exists(artifact["path"]):
            return jsonify({"error": "Not Found", "message": "Artifact not found"}), 404

    response = send_file(
        artifact["path"],
        mimetype=mimetype,
        as_attachment=True,
        download_name=os.path.basename(artifact["path"]),
    )
    response.cache_control.no_store = True
    response.cache_control.max_age = 0
    response.expires = 0
    return response


def _serialize_job(job: dict) -> dict:
    """Serialize a job for detail responses."""
    started_at = job.get("started_at")
    finished_at = job.get("finished_at")
    elapsed_seconds = None
    if started_at:
        start_dt = datetime.fromisoformat(started_at)
        end_dt = datetime.fromisoformat(finished_at) if finished_at else datetime.now(timezone.utc)
        elapsed_seconds = int((end_dt - start_dt).total_seconds())

    response = {
        "job_id": job["id"],
        "status": job["status"],
        "start_url": job["start_url"],
        "allowed_host": job["allowed_host"],
        "allowed_path_prefix": job.get("allowed_path_prefix"),
        "max_depth": job.get("max_depth"),
        "max_pages": job.get("max_pages"),
        "pages_discovered": job.get("pages_discovered", 0),
        "pages_processed": job.get("pages_processed", 0),
        "pages_succeeded": job.get("pages_succeeded", 0),
        "pages_failed": job.get("pages_failed", 0),
        "cleanup_status": job.get("cleanup_status"),
        "error_message": job.get("error_message"),
        "created_at": job.get("created_at"),
        "started_at": started_at,
        "finished_at": finished_at,
        "elapsed_seconds": elapsed_seconds,
    }

    if job["status"] in (JobState.DONE, JobState.CANCELLED):
        response["artifacts_url"] = f"/v1/jobs/{job['id']}/artifacts"
    return response


def _serialize_job_summary(job: dict) -> dict:
    """Serialize a compact job summary."""
    return {
        "job_id": job["id"],
        "status": job["status"],
        "start_url": job["start_url"],
        "pages_discovered": job.get("pages_discovered", 0),
        "pages_succeeded": job.get("pages_succeeded", 0),
        "created_at": job.get("created_at"),
    }


def _serialize_page_summary(page: dict) -> dict:
    """Serialize a compact page response."""
    text_length = len(page.get("plain_text") or page.get("raw_text") or "")
    return {
        "page_id": page["id"],
        "url": page["url"],
        "canonical_url": page["canonical_url"],
        "parent_page_id": page.get("parent_page_id"),
        "depth": page["depth"],
        "title": page.get("title"),
        "page_type": page.get("page_type"),
        "status": page["status"],
        "text_length": text_length,
        "cleanup_score": page.get("cleanup_score"),
        "cleanup_confidence": page.get("cleanup_confidence"),
    }


def _serialize_page_detail(page: dict, *, include_export_json: bool = False) -> dict:
    """Serialize detailed page content."""
    response = _serialize_page_summary(page)
    response.update({
        "job_id": page["job_id"],
        "raw_markdown": page.get("raw_markdown"),
        "clean_markdown": page.get("clean_markdown"),
        "plain_text": page.get("plain_text"),
        "removed_blocks": page.get("removed_blocks_json", []),
        "main_content_selector": page.get("main_content_selector"),
        "error_message": page.get("error_message"),
    })
    if include_export_json:
        response["export_json"] = build_page_json_record(page)
    return response


def _parse_int(value, default: int) -> int:
    """Best-effort integer parsing."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _derive_allowed_path_prefix(start_url: str) -> str | None:
    """Default scope to the provided start URL subtree."""
    path = get_path(start_url)
    if not path or path == "/":
        return None
    if path.endswith((".html", ".htm", ".php", ".jsp", ".asp")):
        return path.rsplit("/", 1)[0] or "/"
    return path.rstrip("/") or "/"
