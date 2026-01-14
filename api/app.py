"""Flask application factory."""
import os

from flask import Flask
from flask_cors import CORS

from config import settings
from db import database
from api.middleware.error_handler import register_error_handlers
from api.routes.jobs import jobs_bp
from api.routes.health import health_bp


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        static_folder=settings.WEB_STATIC_DIR,
        static_url_path=''
    )
    
    CORS(app)
    
    database.init_db()
    
    register_error_handlers(app)
    
    app.register_blueprint(jobs_bp)
    app.register_blueprint(health_bp)
    
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    @app.route('/status')
    def status_page():
        return app.send_static_file('status.html')
    
    return app
