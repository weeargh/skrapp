"""Worker main loop - polls for jobs and runs them."""
import logging
import signal
import sys
import time

from config import settings
from config.constants import JobState
from db import database, queries
from worker.runner import run_job
from worker.stuck_detector import detect_and_handle_stuck_jobs


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

_shutdown_requested = False


def signal_handler(signum, frame):
    """Handle shutdown signals."""
    global _shutdown_requested
    logger.info(f"Received signal {signum}, shutting down...")
    _shutdown_requested = True


def main():
    """Main worker loop."""
    global _shutdown_requested
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    logger.info("Worker starting...")
    
    database.init_db()
    
    logger.info(f"Worker started. Polling every {settings.WORKER_POLL_INTERVAL_SECONDS}s")
    
    while not _shutdown_requested:
        try:
            detect_and_handle_stuck_jobs()
            
            job = queries.get_next_queued_job()
            
            if job:
                job_id = job['id']
                logger.info(f"Found queued job: {job_id}")
                
                try:
                    run_job(job_id)
                except Exception as e:
                    logger.error(f"Error running job {job_id}: {e}")
            else:
                time.sleep(settings.WORKER_POLL_INTERVAL_SECONDS)
                
        except KeyboardInterrupt:
            logger.info("Keyboard interrupt received")
            break
        except Exception as e:
            logger.error(f"Error in worker loop: {e}")
            time.sleep(settings.WORKER_POLL_INTERVAL_SECONDS)
    
    logger.info("Worker shutting down...")
    database.close_connection()
    logger.info("Worker stopped")


if __name__ == '__main__':
    main()
