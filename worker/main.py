"""Worker loop with page-level leasing and configurable concurrency."""
from __future__ import annotations

import logging
import signal
import threading
import time

from config import settings
from config.constants import JobState, PageState
from crawler.crawl4ai_session import Crawl4AIPageSession
from db import database, queries
from worker.runner import finalize_ready_job, process_page, start_next_queued_job
from worker.stuck_detector import detect_and_handle_stuck_jobs


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

_shutdown_requested = False


def signal_handler(signum, frame):
    """Handle shutdown signals."""
    del frame
    global _shutdown_requested
    logger.info("Received signal %s, shutting down...", signum)
    _shutdown_requested = True


class PageWorkerThread(threading.Thread):
    """One worker thread that repeatedly claims and processes pages."""

    def __init__(self, worker_index: int):
        super().__init__(daemon=True, name=f"page-worker-{worker_index}")
        self.worker_id = self.name
        self._session: Crawl4AIPageSession | None = None
        self._session_key: tuple[str, str | None, tuple[str, ...]] | None = None

    def run(self):
        """Run the page worker loop."""
        logger.info("%s started", self.worker_id)
        try:
            while not _shutdown_requested:
                worked = False

                page = queries.claim_next_page_for_processing(
                    self.worker_id,
                    settings.PAGE_LEASE_SECONDS,
                )
                if page:
                    job = queries.get_crawl_job(page["job_id"])
                    if not job or job["status"] != JobState.RUNNING:
                        queries.update_page(
                            page["id"],
                            status=PageState.QUEUED,
                            claimed_by=None,
                            claimed_at=None,
                            lease_expires_at=None,
                        )
                        if job:
                            queries.recalculate_job_counts(job["id"])
                    else:
                        try:
                            process_page(
                                job,
                                page,
                                self.worker_id,
                                self._get_session(job),
                            )
                        except Exception as e:
                            if _is_browser_crash(e):
                                logger.warning(
                                    "%s browser crashed on page %s — resetting session and retrying",
                                    self.worker_id, page["id"],
                                )
                                self._close_session()
                                try:
                                    process_page(
                                        job,
                                        page,
                                        self.worker_id,
                                        self._get_session(job),
                                    )
                                except Exception as retry_e:
                                    logger.error(
                                        "Retry failed for page %s: %s",
                                        page["id"], retry_e, exc_info=True,
                                    )
                            else:
                                logger.error(
                                    "Unhandled error processing page %s for job %s: %s",
                                    page["id"],
                                    job["id"],
                                    e,
                                    exc_info=True,
                                )
                        worked = True

                if finalize_ready_job():
                    worked = True

                if start_next_queued_job():
                    worked = True

                if not worked:
                    time.sleep(settings.WORKER_POLL_INTERVAL_SECONDS)
        finally:
            self._close_session()
            database.close_connection()
            logger.info("%s stopped", self.worker_id)

    def _get_session(self, job: dict) -> Crawl4AIPageSession:
        """Reuse a browser session while the worker stays on the same scope."""
        session_key = (
            job["allowed_host"],
            job.get("allowed_path_prefix"),
            tuple(job.get("ignore_path_prefixes") or []),
        )
        if self._session and self._session_key == session_key:
            return self._session

        self._close_session()
        self._session = Crawl4AIPageSession(
            allowed_host=job["allowed_host"],
            allowed_path_prefix=job.get("allowed_path_prefix"),
            ignore_prefixes=job.get("ignore_path_prefixes"),
        ).__enter__()
        self._session_key = session_key
        return self._session

    def _close_session(self):
        """Close any active Crawl4AI session."""
        if not self._session:
            return
        try:
            self._session.__exit__(None, None, None)
        except Exception as e:
            logger.warning("Failed to close session for %s cleanly: %s", self.worker_id, e)
        finally:
            self._session = None
            self._session_key = None


def _is_browser_crash(exc: Exception) -> bool:
    """Return True if the exception indicates a Playwright browser crash."""
    msg = str(exc).lower()
    return any(phrase in msg for phrase in (
        "browser has been closed",
        "target page, context or browser has been closed",
        "browser.new_context",
        "connection closed",
        "browser closed",
    ))


class SupervisorThread(threading.Thread):
    """Background supervisor for heartbeats and stuck-job handling."""

    def __init__(self):
        super().__init__(daemon=True, name="worker-supervisor")

    def run(self):
        """Run the supervisor loop."""
        logger.info("Supervisor started")
        while not _shutdown_requested:
            try:
                detect_and_handle_stuck_jobs()
                for job in queries.get_running_jobs():
                    queries.touch_job_heartbeat(job["id"])
                finalizing_jobs = queries.get_jobs_by_state(JobState.FINALIZING)
                for job in finalizing_jobs:
                    queries.touch_job_heartbeat(job["id"])
            except Exception as e:
                logger.error("Error in supervisor loop: %s", e, exc_info=True)
            time.sleep(settings.HEARTBEAT_INTERVAL_SECONDS)
        database.close_connection()
        logger.info("Supervisor stopped")


def main():
    """Main worker process entry point."""
    global _shutdown_requested

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info(
        "Worker starting with concurrency=%s, page_lease_seconds=%s",
        settings.WORKER_CONCURRENCY,
        settings.PAGE_LEASE_SECONDS,
    )

    database.init_db()

    supervisor = SupervisorThread()
    supervisor.start()

    workers = [PageWorkerThread(index + 1) for index in range(settings.WORKER_CONCURRENCY)]
    for worker in workers:
        worker.start()

    try:
        while not _shutdown_requested:
            dead_workers = [worker.name for worker in workers if not worker.is_alive()]
            if dead_workers:
                logger.error("Worker threads died unexpectedly: %s", ", ".join(dead_workers))
                _shutdown_requested = True
                break
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
        _shutdown_requested = True

    logger.info("Worker shutting down...")
    for worker in workers:
        worker.join(timeout=10)
    supervisor.join(timeout=5)
    database.close_connection()
    logger.info("Worker stopped")


if __name__ == "__main__":
    main()
