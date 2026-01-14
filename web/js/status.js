document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const jobId = params.get('job_id');
    let token = params.get('token');

    if (!token && jobId) {
        token = localStorage.getItem(`job_${jobId}`);
    }

    if (!jobId || !token) {
        showError('Missing job ID or token');
        return;
    }

    let pollInterval = 5000;
    let pollTimer = null;

    async function fetchStatus() {
        try {
            const response = await fetch(`/v1/jobs/${jobId}?token=${token}`);
            const data = await response.json();

            if (!response.ok) {
                if (response.status === 410) {
                    showError('This job has expired and is no longer available.');
                    stopPolling();
                    return;
                }
                throw new Error(data.message || data.error || 'Failed to fetch status');
            }

            updateUI(data);

            if (['done', 'failed', 'expired'].includes(data.state)) {
                stopPolling();
            }

        } catch (error) {
            showError(error.message);
            stopPolling();
        }
    }

    function updateUI(data) {
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('job-details').classList.remove('hidden');

        const badge = document.getElementById('state-badge');
        badge.textContent = data.state;
        badge.className = `badge ${data.state}`;

        document.getElementById('job-id').textContent = data.job_id;
        document.getElementById('start-url').textContent = data.start_url;
        document.getElementById('allowed-host').textContent = data.allowed_host;

        const pagesFetched = data.pages_fetched || 0;
        const maxPages = data.max_pages || 1000;
        const pagesExported = data.pages_exported || 0;
        const progress = Math.min(100, (pagesFetched / maxPages) * 100);

        document.getElementById('pages-fetched').textContent = pagesFetched;
        document.getElementById('pages-exported').textContent = pagesExported;
        document.getElementById('errors-count').textContent = data.errors_count || 0;
        document.getElementById('progress-text').textContent = `${pagesFetched} / ${maxPages} pages`;
        document.getElementById('progress-fill').style.width = `${progress}%`;

        if (data.elapsed_seconds !== null && data.elapsed_seconds !== undefined) {
            document.getElementById('elapsed-time').textContent = formatDuration(data.elapsed_seconds);
        }

        if (data.site_status && data.site_status !== 'normal') {
            document.getElementById('site-status-section').classList.remove('hidden');
            document.getElementById('site-status').textContent = data.site_status;
        } else {
            document.getElementById('site-status-section').classList.add('hidden');
        }

        if (data.last_error) {
            document.getElementById('error-section').classList.remove('hidden');
            const errorText = typeof data.last_error === 'object' 
                ? data.last_error.message || JSON.stringify(data.last_error)
                : data.last_error;
            document.getElementById('last-error').textContent = errorText;
        } else {
            document.getElementById('error-section').classList.add('hidden');
        }

        if (data.state === 'done' && data.download_url) {
            document.getElementById('download-section').classList.remove('hidden');
            document.getElementById('download-pages').href = data.download_url;
            document.getElementById('download-summary').href = 
                `/v1/jobs/${jobId}/download/summary.json?token=${token}`;
        } else {
            document.getElementById('download-section').classList.add('hidden');
        }

        document.getElementById('created-at').textContent = formatDate(data.created_at);
        document.getElementById('started-at').textContent = formatDate(data.started_at);
        document.getElementById('finished-at').textContent = formatDate(data.finished_at);
        document.getElementById('expires-at').textContent = formatDate(data.expires_at);
    }

    function formatDuration(seconds) {
        if (seconds < 60) return `${seconds}s`;
        if (seconds < 3600) return `${Math.floor(seconds / 60)}m ${seconds % 60}s`;
        const hours = Math.floor(seconds / 3600);
        const mins = Math.floor((seconds % 3600) / 60);
        return `${hours}h ${mins}m`;
    }

    function formatDate(isoString) {
        if (!isoString) return '-';
        try {
            const date = new Date(isoString);
            return date.toLocaleString();
        } catch {
            return isoString;
        }
    }

    function showError(message) {
        document.getElementById('loading').classList.add('hidden');
        const errorEl = document.getElementById('error-message');
        errorEl.textContent = message;
        errorEl.classList.remove('hidden');
    }

    function startPolling() {
        fetchStatus();
        pollTimer = setInterval(fetchStatus, pollInterval);
    }

    function stopPolling() {
        if (pollTimer) {
            clearInterval(pollTimer);
            pollTimer = null;
        }
    }

    startPolling();
});
