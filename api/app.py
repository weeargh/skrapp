"""Flask application factory."""
import os
from datetime import timedelta

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
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(days=1)

    CORS(app)

    database.init_db()

    register_error_handlers(app)

    app.register_blueprint(jobs_bp)
    app.register_blueprint(health_bp)

    def _asset_version() -> str:
        latest_mtime = 0
        for relative_dir in ("css", "js"):
            asset_dir = os.path.join(settings.WEB_STATIC_DIR, relative_dir)
            if not os.path.isdir(asset_dir):
                continue
            for filename in os.listdir(asset_dir):
                asset_path = os.path.join(asset_dir, filename)
                if os.path.isfile(asset_path):
                    latest_mtime = max(latest_mtime, int(os.path.getmtime(asset_path)))
        return str(latest_mtime or 0)

    def _render_static_html(filename: str):
        path = os.path.join(settings.WEB_STATIC_DIR, filename)
        with open(path, "r", encoding="utf-8") as handle:
            html = handle.read().replace("__ASSET_VERSION__", _asset_version())
        return app.response_class(html, mimetype="text/html")

    def _no_cache_html(response):
        response.cache_control.no_store = True
        response.cache_control.max_age = 0
        response.expires = 0
        return response

    @app.route('/')
    def index():
        return _no_cache_html(_render_static_html("index.html"))

    @app.route('/status')
    def status_page():
        return _no_cache_html(_render_static_html("status.html"))

    @app.route('/preview')
    def preview_page():
        return _no_cache_html(_render_static_html("preview.html"))

    @app.route('/<job_id>/preview')
    def preview_page_for_job(job_id: str):
        del job_id
        return _no_cache_html(_render_static_html("preview.html"))

    return app
