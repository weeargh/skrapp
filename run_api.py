#!/usr/bin/env python3
"""API server entry point."""
import sys
import os
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import settings
from api.app import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run the API server."""
    app = create_app()
    
    logger.info(f"Starting API server on http://{settings.API_HOST}:{settings.API_PORT}")
    logger.info(f"Database: {settings.DATABASE_PATH}")
    logger.info(f"Jobs output: {settings.JOBS_OUTPUT_DIR}")
    
    app.run(
        host=settings.API_HOST,
        port=settings.API_PORT,
        debug=os.environ.get('FLASK_DEBUG', '0') == '1'
    )


if __name__ == '__main__':
    main()
