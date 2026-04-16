"""Regression tests for canonical per-page JSON exports."""
from __future__ import annotations

import io
import json
import os
import tempfile
import zipfile
from unittest import TestCase
from unittest.mock import patch

from api.app import create_app
from config import settings
from config.constants import ArtifactKind, JobState, PageState
from db import database, queries
from worker.finalizer import finalize_job


class PageJsonArtifactTests(TestCase):
    """Verify zipped page JSON exports are available for review and download."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.original_database_path = settings.DATABASE_PATH
        self.original_jobs_output_dir = settings.JOBS_OUTPUT_DIR

        database.close_connection()
        settings.DATABASE_PATH = os.path.join(self.temp_dir.name, "data", "crawler.db")
        settings.JOBS_OUTPUT_DIR = os.path.join(self.temp_dir.name, "out", "jobs")
        os.makedirs(settings.JOBS_OUTPUT_DIR, exist_ok=True)
        database.init_db()
        self.addCleanup(self._restore_settings)

    def _restore_settings(self):
        database.close_connection()
        settings.DATABASE_PATH = self.original_database_path
        settings.JOBS_OUTPUT_DIR = self.original_jobs_output_dir

    def _create_job(self, job_id: str) -> dict:
        return queries.create_crawl_job(
            job_id=job_id,
            start_url="https://example.com/docs",
            allowed_host="example.com",
            allowed_path_prefix="/docs",
            max_depth=2,
            max_pages=20,
        )

    def _create_page(
        self,
        job_id: str,
        *,
        url: str,
        status: str,
        title: str,
        depth: int = 0,
        parent_page_id: str | None = None,
    ) -> dict:
        return queries.create_page(
            job_id=job_id,
            url=url,
            canonical_url=url,
            parent_page_id=parent_page_id,
            depth=depth,
            discovery_order=None,
            status=status,
            title=title,
        )

    def _read_zip_records(self, zip_bytes: bytes) -> dict[str, dict]:
        records = {}
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
            for name in archive.namelist():
                with archive.open(name) as handle:
                    record = json.load(handle)
                records[record["page_id"]] = record
        return records

    def test_finalize_job_registers_page_json_zip(self):
        job = self._create_job("job_finalize_json_zip")
        page = self._create_page(
            job["id"],
            url="https://example.com/docs/article-one",
            status=PageState.DONE,
            title="Article One",
        )
        failed_page = self._create_page(
            job["id"],
            url="https://example.com/docs/article-two",
            status=PageState.FAILED,
            title="Article Two",
            depth=1,
            parent_page_id=page["id"],
        )
        queries.update_page(
            failed_page["id"],
            error_message="Extraction timed out",
        )

        cleaned_page = {
            **queries.get_page_by_id(page["id"]),
            "clean_markdown": "# Article One\n\nClean body",
            "plain_text": "Clean body",
            "cleanup_score": 0.88,
            "cleanup_confidence": 0.91,
            "page_type": "article",
            "removed_blocks": [{"kind": "nav", "text": "Skip to main content"}],
        }

        with patch("worker.finalizer.clean_pages", return_value=[cleaned_page]):
            self.assertTrue(finalize_job(job["id"]))

        artifact = queries.get_artifact_by_kind(job["id"], ArtifactKind.PAGE_JSON_ZIP)
        self.assertIsNotNone(artifact)
        self.assertTrue(os.path.exists(artifact["path"]))

        with open(artifact["path"], "rb") as handle:
            records = self._read_zip_records(handle.read())

        self.assertEqual(set(records.keys()), {page["id"], failed_page["id"]})
        self.assertEqual(records[page["id"]]["content"]["clean_markdown"], "# Article One\n\nClean body")
        self.assertEqual(records[page["id"]]["cleanup_confidence"], 0.91)
        self.assertEqual(records[failed_page["id"]]["error_message"], "Extraction timed out")
        self.assertEqual(records[failed_page["id"]]["status"], PageState.FAILED)

    def test_download_route_builds_page_json_zip_for_completed_jobs(self):
        job = self._create_job("job_download_json_zip")
        page = self._create_page(
            job["id"],
            url="https://example.com/docs/article-three",
            status=PageState.DONE,
            title="Article Three",
        )
        queries.update_page(
            page["id"],
            raw_markdown="# Article Three\n\nRaw body",
            clean_markdown="# Article Three\n\nClean body",
            plain_text="Clean body",
            cleanup_score=0.77,
            cleanup_confidence=0.85,
            page_type="article",
            main_content_selector="main article",
            removed_blocks_json=[{"kind": "footer", "text": "Contact us"}],
        )
        queries.recalculate_job_counts(job["id"])
        queries.update_crawl_job_status(job["id"], JobState.DONE, cleanup_status="done")

        app = create_app()
        client = app.test_client()

        page_response = client.get(f"/v1/jobs/{job['id']}/pages/{page['id']}?include_export_json=1")
        self.assertEqual(page_response.status_code, 200)
        page_payload = page_response.get_json()
        self.assertEqual(page_payload["export_json"]["page_id"], page["id"])
        self.assertEqual(page_payload["export_json"]["content"]["plain_text"], "Clean body")
        self.assertEqual(page_payload["export_json"]["main_content_selector"], "main article")

        response = client.get(f"/v1/jobs/{job['id']}/artifacts/{ArtifactKind.PAGE_JSON_ZIP}/download")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/zip")

        records = self._read_zip_records(response.data)
        response.close()
        self.assertEqual(records[page["id"]]["content"], page_payload["export_json"]["content"])
        self.assertEqual(records[page["id"]]["cleanup_confidence"], 0.85)
        self.assertEqual(records[page["id"]]["removed_blocks"][0]["kind"], "footer")

        artifact = queries.get_artifact_by_kind(job["id"], ArtifactKind.PAGE_JSON_ZIP)
        self.assertIsNotNone(artifact)
        self.assertTrue(os.path.exists(artifact["path"]))

    def test_download_route_replaces_generic_title_with_heading_and_refreshes_existing_zip(self):
        job = self._create_job("job_refresh_json_zip")
        page = self._create_page(
            job["id"],
            url="https://help-center.qontak.com/hc/id/articles/12263090746137-Bagaimana-Cara-Mengelola-User-Input-dan-Bot-Response-pada-Chatbot",
            status=PageState.DONE,
            title="Online Help Center | Layanan Bantuan - Mekari Qontak",
        )
        queries.update_page(
            page["id"],
            raw_markdown=(
                "## Panduan pengguna Mekari Qontak\n"
                "# Temukan artikel panduan sesuai kebutuhan Anda\n"
                "# Bagaimana Cara Mengelola User Input dan Bot Response pada Chatbot\n\n"
                "Isi artikel"
            ),
            clean_markdown="Isi artikel yang sudah dibersihkan",
            plain_text="Isi artikel yang sudah dibersihkan",
            cleanup_score=0.83,
            cleanup_confidence=0.93,
            page_type="article",
        )
        queries.recalculate_job_counts(job["id"])
        queries.update_crawl_job_status(job["id"], JobState.DONE, cleanup_status="done")

        stale_dir = os.path.join(settings.JOBS_OUTPUT_DIR, job["id"])
        os.makedirs(stale_dir, exist_ok=True)
        stale_path = os.path.join(stale_dir, "pages-json.zip")
        with zipfile.ZipFile(stale_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(
                "stale.json",
                json.dumps({"page_id": page["id"], "title": "Online Help Center | Layanan Bantuan - Mekari Qontak"}),
            )
        queries.create_artifact(
            job["id"],
            ArtifactKind.PAGE_JSON_ZIP,
            stale_path,
            os.path.getsize(stale_path),
            sha256="stale",
        )

        app = create_app()
        client = app.test_client()

        response = client.get(f"/v1/jobs/{job['id']}/artifacts/{ArtifactKind.PAGE_JSON_ZIP}/download")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.cache_control.no_store, True)

        records = self._read_zip_records(response.data)
        response.close()
        self.assertEqual(
            records[page["id"]]["title"],
            "Bagaimana Cara Mengelola User Input dan Bot Response pada Chatbot",
        )
        self.assertNotEqual(records[page["id"]]["title"], "Online Help Center | Layanan Bantuan - Mekari Qontak")
