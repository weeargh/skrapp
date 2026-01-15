"""Job management routes."""
import json
import os
from datetime import datetime, timezone

from flask import Blueprint, request, jsonify, send_file, abort

from config import settings
from config.constants import JobState, ArtifactKind
from db import queries
from api.validators import (
    validate_url,
    validate_max_pages,
    validate_timeout,
    validate_ignore_prefixes,
    generate_job_id,
    generate_token,
    hash_token,
    hash_ip
)
from api.middleware.rate_limit import get_client_ip, rate_limit_required

jobs_bp = Blueprint('jobs', __name__)


@jobs_bp.route('/v1/jobs', methods=['POST'])
@rate_limit_required
def create_job():
    """Create a new crawl job."""
    data = request.get_json() or {}
    
    start_url = data.get('start_url', '').strip()
    is_valid, error, hostname = validate_url(start_url)
    if not is_valid:
        return jsonify({"error": "Invalid URL", "message": error}), 400
    
    max_pages = validate_max_pages(
        data.get('max_pages'),
        settings.DEFAULT_MAX_PAGES,
        settings.MIN_PAGES_LIMIT,
        settings.MAX_PAGES_LIMIT
    )
    
    timeout_seconds = validate_timeout(
        data.get('timeout_seconds'),
        settings.DEFAULT_TIMEOUT_SECONDS,
        settings.MIN_TIMEOUT_SECONDS,
        settings.MAX_TIMEOUT_SECONDS
    )
    
    ignore_prefixes = validate_ignore_prefixes(data.get('ignore_path_prefixes'))
    
    # Use Playwright for JavaScript rendering
    use_js = bool(data.get('use_js', False))
    
    job_id = generate_job_id()
    token = generate_token()
    token_hashed = hash_token(token)
    
    client_ip = get_client_ip()
    ip_hash = hash_ip(client_ip)
    
    job_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)
    os.makedirs(os.path.join(job_dir, 'state'), exist_ok=True)
    
    job = queries.create_job(
        job_id=job_id,
        token_hash=token_hashed,
        start_url=start_url,
        allowed_host=hostname,
        max_pages=max_pages,
        timeout_seconds=timeout_seconds,
        ignore_path_prefixes=ignore_prefixes,
        requester_ip_hash=ip_hash,
        expiry_hours=settings.JOB_EXPIRY_HOURS,
        use_js=use_js
    )
    
    queries.increment_ip_concurrent(ip_hash)
    
    return jsonify({
        "job_id": job_id,
        "token": token,
        "status_url": f"/v1/jobs/{job_id}?token={token}",
        "state": job['state'],
        "max_pages": max_pages,
        "timeout_seconds": timeout_seconds,
        "use_js": use_js
    }), 201


@jobs_bp.route('/v1/jobs/<job_id>', methods=['GET'])
def get_job_status(job_id: str):
    """Get the status of a job."""
    token = request.args.get('token', '')
    if not token:
        return jsonify({"error": "Unauthorized", "message": "Token is required"}), 401
    
    token_hashed = hash_token(token)
    job = queries.get_job_for_auth(job_id, token_hashed)
    
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found or invalid token"}), 404
    
    if job['state'] != JobState.EXPIRED:
        expires_at = datetime.fromisoformat(job['expires_at'])
        if datetime.now(timezone.utc) > expires_at:
            queries.update_job_state(job_id, JobState.EXPIRED)
            return jsonify({"error": "Gone", "message": "Job has expired"}), 410
    
    if job['state'] == JobState.EXPIRED:
        return jsonify({"error": "Gone", "message": "Job has expired"}), 410
    
    elapsed_seconds = None
    if job['started_at']:
        started = datetime.fromisoformat(job['started_at'])
        if job['finished_at']:
            finished = datetime.fromisoformat(job['finished_at'])
            elapsed_seconds = int((finished - started).total_seconds())
        else:
            elapsed_seconds = int((datetime.now(timezone.utc) - started).total_seconds())
    
    response = {
        "job_id": job_id,
        "state": job['state'],
        "start_url": job['start_url'],
        "allowed_host": job['allowed_host'],
        "max_pages": job['max_pages'],
        "pages_fetched": job['pages_fetched'],
        "pages_exported": job['pages_exported'],
        "errors_count": job['errors_count'],
        "elapsed_seconds": elapsed_seconds,
        "restart_count": job['restart_count'],
        "created_at": job['created_at'],
        "started_at": job['started_at'],
        "finished_at": job['finished_at'],
        "expires_at": job['expires_at']
    }
    
    if job['site_status']:
        response['site_status'] = job['site_status']
    
    if job['block_evidence']:
        try:
            response['block_evidence'] = json.loads(job['block_evidence'])
        except (json.JSONDecodeError, TypeError):
            pass
    
    if job['last_error']:
        try:
            response['last_error'] = json.loads(job['last_error'])
        except (json.JSONDecodeError, TypeError):
            pass
    
    if job['state'] == JobState.DONE:
        response['download_url'] = f"/v1/jobs/{job_id}/download/pages.jsonl?token={token}"
    
    return jsonify(response)


@jobs_bp.route('/v1/jobs/<job_id>/download/pages.jsonl', methods=['GET'])
def download_pages(job_id: str):
    """Download the pages.jsonl file for a completed job."""
    token = request.args.get('token', '')
    if not token:
        return jsonify({"error": "Unauthorized", "message": "Token is required"}), 401
    
    token_hashed = hash_token(token)
    job = queries.get_job_for_auth(job_id, token_hashed)
    
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found or invalid token"}), 404
    
    if job['state'] == JobState.EXPIRED:
        return jsonify({"error": "Gone", "message": "Job has expired"}), 410
    
    if job['state'] != JobState.DONE:
        return jsonify({
            "error": "Bad Request",
            "message": f"Job is not complete. Current state: {job['state']}"
        }), 400
    
    file_path = os.path.join(settings.JOBS_OUTPUT_DIR, job_id, 'pages.jsonl')
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Not Found", "message": "Output file not found"}), 404
    
    return send_file(
        file_path,
        mimetype='application/x-ndjson',
        as_attachment=True,
        download_name=f'{job_id}_pages.jsonl'
    )


@jobs_bp.route('/v1/jobs/<job_id>/download/summary.json', methods=['GET'])
def download_summary(job_id: str):
    """Download the summary.json file for a completed job."""
    token = request.args.get('token', '')
    if not token:
        return jsonify({"error": "Unauthorized", "message": "Token is required"}), 401
    
    token_hashed = hash_token(token)
    job = queries.get_job_for_auth(job_id, token_hashed)
    
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found or invalid token"}), 404
    
    if job['state'] == JobState.EXPIRED:
        return jsonify({"error": "Gone", "message": "Job has expired"}), 410
    
    if job['state'] != JobState.DONE:
        return jsonify({
            "error": "Bad Request",
            "message": f"Job is not complete. Current state: {job['state']}"
        }), 400
    
    file_path = os.path.join(settings.JOBS_OUTPUT_DIR, job_id, 'summary.json')
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Not Found", "message": "Summary file not found"}), 404
    
    return send_file(
        file_path,
        mimetype='application/json',
        as_attachment=True,
        download_name=f'{job_id}_summary.json'
    )


@jobs_bp.route('/v1/jobs/<job_id>/pages', methods=['GET'])
def list_pages(job_id: str):
    """List crawled pages for a job (live progress view)."""
    token = request.args.get('token', '')
    if not token:
        return jsonify({"error": "Unauthorized", "message": "Token is required"}), 401
    
    token_hashed = hash_token(token)
    job = queries.get_job_for_auth(job_id, token_hashed)
    
    if not job:
        return jsonify({"error": "Not Found", "message": "Job not found or invalid token"}), 404
    
    if job['state'] == JobState.EXPIRED:
        return jsonify({"error": "Gone", "message": "Job has expired"}), 410
    
    # Read from raw file (available during crawl)
    raw_file = os.path.join(settings.JOBS_OUTPUT_DIR, job_id, 'pages.raw.jsonl')
    
    pages = []
    if os.path.exists(raw_file):
        try:
            with open(raw_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        page = json.loads(line.strip())
                        # Return minimal data for table display
                        pages.append({
                            'url': page.get('url', ''),
                            'title': page.get('title', ''),
                            'status_code': page.get('status_code', 0),
                            'depth': page.get('depth', 0),
                            'extraction_mode': page.get('extraction_mode', ''),
                            'text_length': len(page.get('text', '')),
                            'outlinks_count': page.get('outlinks_count', 0)
                        })
                    except json.JSONDecodeError:
                        continue
        except Exception:
            pass
    
    return jsonify({
        "job_id": job_id,
        "state": job['state'],
        "total_pages": len(pages),
        "pages": pages
    })
