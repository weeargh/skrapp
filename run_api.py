#!/usr/bin/env python3
"""API server entry point."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import settings
from api.app import create_app


def main():
    """Run the API server."""
    app = create_app()
    
    print(f"Starting API server on http://{settings.API_HOST}:{settings.API_PORT}")
    print(f"Database: {settings.DATABASE_PATH}")
    print(f"Jobs output: {settings.JOBS_OUTPUT_DIR}")
    
    app.run(
        host=settings.API_HOST,
        port=settings.API_PORT,
        debug=os.environ.get('FLASK_DEBUG', '0') == '1'
    )


if __name__ == '__main__':
    main()
