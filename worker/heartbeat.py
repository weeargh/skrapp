"""Background heartbeat thread for updating job progress."""
import logging
import os
import threading
import time

from config import settings
from db import queries


logger = logging.getLogger(__name__)


class HeartbeatThread(threading.Thread):
    """Thread that periodically updates job heartbeat and progress."""
    
    def __init__(self, job_id: str, job_dir: str, interval: int = None):
        super().__init__(daemon=True)
        self.job_id = job_id
        self.job_dir = job_dir
        self.interval = interval or settings.HEARTBEAT_INTERVAL_SECONDS
        self._stop_event = threading.Event()
    
    def run(self):
        """Run the heartbeat loop."""
        logger.info(f"Heartbeat thread started for job {self.job_id}")
        
        while not self._stop_event.is_set():
            try:
                self._update_heartbeat()
            except Exception as e:
                logger.error(f"Error updating heartbeat for job {self.job_id}: {e}")
            
            self._stop_event.wait(self.interval)
        
        logger.info(f"Heartbeat thread stopped for job {self.job_id}")
    
    def stop(self):
        """Signal the thread to stop."""
        self._stop_event.set()
    
    def _update_heartbeat(self):
        """Update the heartbeat and page count in the database."""
        pages_fetched = self._count_pages()
        queries.update_heartbeat(self.job_id, pages_fetched)
        logger.debug(f"Heartbeat updated for job {self.job_id}: {pages_fetched} pages")
    
    def _count_pages(self) -> int:
        """Count the number of pages in the raw JSONL file."""
        raw_file = os.path.join(self.job_dir, 'pages.raw.jsonl')
        
        if not os.path.exists(raw_file):
            return 0
        
        try:
            with open(raw_file, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except Exception:
            return 0
