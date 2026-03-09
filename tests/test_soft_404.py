"""Regression tests for rendered docs pages that return HTTP 404."""
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import MagicMock, patch

from config.constants import PageState
from worker import runner


def _result(url: str, *, title: str, heading: str, text: str, status_code: int = 404):
    return SimpleNamespace(
        url=url,
        final_url=url,
        canonical_url=url,
        status_code=status_code,
        title=title,
        html="<html></html>",
        cleaned_html="<main>content</main>",
        raw_markdown=f"# {heading}\n\n{text}",
        raw_text=text,
        outlinks=[],
        meta={},
    )


class Soft404Tests(TestCase):
    """Verify page processing keeps useful soft-404 content and rejects fallbacks."""

    def test_accepts_rendered_soft_404_page(self):
        url = "https://api-docs.expense.mekari.com/managing-app/create-application"
        extracted = _result(
            url,
            title="Create Application | Mekari Expense API",
            heading="Create Application",
            text="A" * 400,
        )
        crawler_session = MagicMock()
        crawler_session.fetch_page.return_value = extracted
        job = {"id": "job_1", "max_depth": 4}
        page = {"id": "page_1", "url": url, "depth": 1, "title": None}

        with patch.object(runner, "queries") as queries_mock, \
                patch.object(runner, "_enqueue_child_pages"), \
                patch.object(runner, "detect_openapi_spec_url", return_value=None):
            runner._process_page(job, page, "worker-1", crawler_session)

        status_updates = [call.args[1] for call in queries_mock.update_page_status.call_args_list]
        self.assertEqual(status_updates[-1], PageState.DONE)
        self.assertNotIn(PageState.FAILED, status_updates)

    def test_rejects_overview_fallback_404_page(self):
        url = "https://api-docs.expense.mekari.com/managing-app/create-application"
        extracted = _result(
            url,
            title="Overview | Mekari Expense API",
            heading="Overview",
            text="A" * 400,
        )
        crawler_session = MagicMock()
        crawler_session.fetch_page.return_value = extracted
        job = {"id": "job_1", "max_depth": 4}
        page = {"id": "page_1", "url": url, "depth": 1, "title": None}

        with patch.object(runner, "queries") as queries_mock, \
                patch.object(runner, "_enqueue_child_pages"), \
                patch.object(runner, "detect_openapi_spec_url", return_value=None):
            runner._process_page(job, page, "worker-1", crawler_session)

        final_call = queries_mock.update_page_status.call_args_list[-1]
        self.assertEqual(final_call.args[1], PageState.FAILED)
        self.assertEqual(final_call.kwargs["error_message"], "Page returned HTTP 404")

    def test_retries_empty_404_and_accepts_second_rendered_result(self):
        url = "https://api-docs.expense.mekari.com/authentication/example-ruby"
        first = SimpleNamespace(
            url=url,
            final_url=url,
            canonical_url=url,
            status_code=404,
            title="",
            html="",
            cleaned_html="",
            raw_markdown="",
            raw_text="",
            outlinks=[],
            meta={},
        )
        second = _result(
            url,
            title="Setup HMAC Authentication in Ruby | Mekari Expense API",
            heading="Setup HMAC Authentication in Ruby",
            text="A" * 400,
        )
        crawler_session = MagicMock()
        crawler_session.fetch_page.side_effect = [first, second]
        job = {"id": "job_1", "max_depth": 4}
        page = {"id": "page_1", "url": url, "depth": 1, "title": None}

        with patch.object(runner, "queries") as queries_mock, \
                patch.object(runner, "_enqueue_child_pages"), \
                patch.object(runner, "detect_openapi_spec_url", return_value=None):
            runner._process_page(job, page, "worker-1", crawler_session)

        self.assertEqual(crawler_session.fetch_page.call_count, 2)
        status_updates = [call.args[1] for call in queries_mock.update_page_status.call_args_list]
        self.assertEqual(status_updates[-1], PageState.DONE)
