"""Stuck job detection - identifies orphaned, stalled, and hard-stalled jobs."""
import json
import logging
import os

from config import settings
from config.constants import JobState, ErrorReason, EventLevel, EventType
from db import queries
from worker.finalizer import finalize_job


logger = logging.getLogger(__name__)

MAX_RESTARTS = 2


def detect_and_handle_stuck_jobs():
    """
    Detect and handle stuck jobs.
    
    This should be called periodically by the worker main loop.
    """
    _handle_cancelled_jobs()
    _handle_orphaned_jobs()
    _handle_stalled_jobs()
    _handle_hard_stalled_jobs()


def _handle_cancelled_jobs():
    """
    Handle cancelled jobs that need finalization.
    
    When a user cancels a job, it's marked as CANCELLED but the crawler
    subprocess keeps running. Once it stops, we need to finalize the results.
    """
    # Find cancelled jobs that haven't been exported yet
    cancelled_jobs = queries.get_jobs_by_state(JobState.CANCELLED)
    
    for job in cancelled_jobs:
        job_id = job['id']
        pages_fetched = job['pages_fetched']
        pages_exported = job['pages_exported']
        
        # If pages_exported is 0 but we have fetched pages, finalize it
        if pages_exported == 0 and pages_fetched > 0:
            logger.info(f"Finalizing cancelled job {job_id} ({pages_fetched} pages)")
            
            try:
                finalize_job(job_id)
                logger.info(f"Successfully finalized cancelled job {job_id}")
            except Exception as e:
                logger.error(f"Error finalizing cancelled job {job_id}: {e}")
        
        # If it's been cancelled with 0 pages, just mark as done
        elif pages_fetched == 0:
            logger.info(f"Cancelled job {job_id} had 0 pages, marking as complete")
            queries.decrement_ip_concurrent(job['requester_ip_hash'])


def _handle_orphaned_jobs():
    """
    Handle orphaned jobs (worker died without finishing).
    
    Orphaned = running/finalizing state with stale heartbeat
    """
    orphaned_jobs = queries.find_orphaned_jobs(settings.ORPHANED_THRESHOLD_SECONDS)
    
    for job in orphaned_jobs:
        job_id = job['id']
        restart_count = job['restart_count']
        
        logger.warning(f"Detected orphaned job: {job_id} (restarts: {restart_count})")
        
        if restart_count < MAX_RESTARTS:
            queries.increment_restart_count(job_id)
            queries.update_job_state(job_id, JobState.QUEUED)
            
            queries.insert_job_event(job_id, EventLevel.WARN, EventType.RESTART, {
                "reason": ErrorReason.ORPHANED,
                "restart_count": restart_count + 1
            })
            
            logger.info(f"Re-queued orphaned job {job_id} for restart")
        else:
            queries.update_job_state(
                job_id,
                JobState.FAILED,
                last_error=json.dumps({
                    "reason": ErrorReason.ORPHANED,
                    "message": f"Job orphaned after {restart_count} restarts"
                })
            )
            
            queries.decrement_ip_concurrent(job['requester_ip_hash'])
            
            queries.insert_job_event(job_id, EventLevel.ERROR, EventType.STATE_CHANGE, {
                "reason": ErrorReason.ORPHANED,
                "restart_count": restart_count
            })
            
            logger.error(f"Failed orphaned job {job_id} after {restart_count} restarts")


def _handle_stalled_jobs():
    """
    Handle stalled jobs (no progress for a while).
    
    Stalled = running state with no progress update for threshold period
    """
    stalled_jobs = queries.find_stalled_jobs(settings.STALLED_THRESHOLD_SECONDS)
    
    for job in stalled_jobs:
        job_id = job['id']
        restart_count = job['restart_count']
        pages_fetched = job['pages_fetched']
        
        logger.warning(f"Detected stalled job: {job_id} "
                      f"(pages: {pages_fetched}, restarts: {restart_count})")
        
        if restart_count < MAX_RESTARTS:
            queries.increment_restart_count(job_id)
            queries.update_job_state(job_id, JobState.QUEUED)
            
            queries.insert_job_event(job_id, EventLevel.WARN, EventType.RESTART, {
                "reason": ErrorReason.STALLED,
                "pages_fetched": pages_fetched,
                "restart_count": restart_count + 1
            })
            
            logger.info(f"Re-queued stalled job {job_id} for restart")
        else:
            queries.update_job_state(
                job_id,
                JobState.FAILED,
                last_error=json.dumps({
                    "reason": ErrorReason.STALLED,
                    "message": f"Job stalled at {pages_fetched} pages after {restart_count} restarts"
                })
            )
            
            queries.decrement_ip_concurrent(job['requester_ip_hash'])
            
            queries.insert_job_event(job_id, EventLevel.ERROR, EventType.STATE_CHANGE, {
                "reason": ErrorReason.STALLED,
                "pages_fetched": pages_fetched,
                "restart_count": restart_count
            })
            
            logger.error(f"Failed stalled job {job_id} after {restart_count} restarts")


def _handle_hard_stalled_jobs():
    """
    Handle hard-stalled jobs (never fetched any pages).
    
    Hard-stalled = running state with 0 pages fetched for a long time
    """
    hard_stalled_jobs = queries.find_hard_stalled_jobs(settings.HARD_STALLED_THRESHOLD_SECONDS)
    
    for job in hard_stalled_jobs:
        job_id = job['id']
        restart_count = job['restart_count']
        
        logger.warning(f"Detected hard-stalled job: {job_id} (0 pages, restarts: {restart_count})")
        
        queries.update_job_state(
            job_id,
            JobState.FAILED,
            last_error=json.dumps({
                "reason": ErrorReason.HARD_STALLED,
                "message": "Job failed to fetch any pages"
            })
        )
        
        queries.decrement_ip_concurrent(job['requester_ip_hash'])
        
        queries.insert_job_event(job_id, EventLevel.ERROR, EventType.STATE_CHANGE, {
            "reason": ErrorReason.HARD_STALLED,
            "restart_count": restart_count
        })
        
        logger.error(f"Failed hard-stalled job {job_id}")
