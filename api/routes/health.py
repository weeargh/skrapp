"""Health check route."""
from flask import Blueprint, jsonify

from db import database

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    db_status = "ok"
    try:
        database.fetchone("SELECT 1")
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return jsonify({
        "status": "ok" if db_status == "ok" else "degraded",
        "database": db_status
    })
