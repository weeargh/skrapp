"""Railway entry point - Flask app for gunicorn auto-detection."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.app import create_app

# Flask app instance for gunicorn
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
