"""Rate limiting middleware."""
from functools import wraps

from flask import request, jsonify

from config import settings
from db import queries
from api.validators import hash_ip


def get_client_ip() -> str:
    """Extract the client IP from the request."""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    if request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP').strip()
    return request.remote_addr or '127.0.0.1'


def check_rate_limit(ip_hash: str) -> tuple[bool, int]:
    """
    Check if the IP is within rate limits.
    
    Returns:
        (is_allowed, current_count)
    """
    current_count = queries.get_ip_concurrent_count(ip_hash)
    is_allowed = current_count < settings.CONCURRENT_JOBS_PER_IP
    return is_allowed, current_count


def rate_limit_required(f):
    """Decorator to enforce rate limiting on job creation."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = get_client_ip()
        ip_hash = hash_ip(ip)
        
        is_allowed, current_count = check_rate_limit(ip_hash)
        
        if not is_allowed:
            return jsonify({
                "error": "Rate limit exceeded",
                "message": f"Maximum {settings.CONCURRENT_JOBS_PER_IP} concurrent jobs allowed per IP",
                "current_jobs": current_count
            }), 429
        
        return f(*args, **kwargs)
    
    return decorated_function
