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

    let pollInterval = 3000;
    let pollTimer = null;
    let previousState = null;
    let lastPagesCount = 0;

    // Gong sound using Web Audio API
    function playGongSound() {
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Create oscillator for the main tone
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            // Gong-like frequency
            oscillator.frequency.setValueAtTime(180, audioContext.currentTime);
            oscillator.frequency.exponentialRampToValueAtTime(120, audioContext.currentTime + 0.5);
            oscillator.type = 'sine';
            
            // Envelope for gong-like decay
            gainNode.gain.setValueAtTime(0.8, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 2);
            
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 2);
            
            // Add a second harmonic for richer sound
            const osc2 = audioContext.createOscillator();
            const gain2 = audioContext.createGain();
            osc2.connect(gain2);
            gain2.connect(audioContext.destination);
            osc2.frequency.setValueAtTime(360, audioContext.currentTime);
            osc2.frequency.exponentialRampToValueAtTime(240, audioContext.currentTime + 0.3);
            osc2.type = 'sine';
            gain2.gain.setValueAtTime(0.3, audioContext.currentTime);
            gain2.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 1);
            osc2.start(audioContext.currentTime);
            osc2.stop(audioContext.currentTime + 1);
        } catch (e) {
            console.log('Could not play sound:', e);
        }
    }

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

            // Play gong when job completes successfully
            if (data.state === 'done' && previousState !== 'done') {
                playGongSound();
            }
            previousState = data.state;

            if (['done', 'failed', 'cancelled', 'expired'].includes(data.state)) {
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
        
        // Show download section for cancelled jobs too
        if (data.state === 'cancelled' && data.download_url) {
            document.getElementById('download-section').classList.remove('hidden');
            document.getElementById('download-pages').href = data.download_url;
            document.getElementById('download-summary').href = 
                `/v1/jobs/${jobId}/download/summary.json?token=${token}`;
        }
        
        // Show cancel button only for active jobs
        if (['queued', 'running', 'finalizing'].includes(data.state)) {
            document.getElementById('cancel-section').classList.remove('hidden');
        } else {
            document.getElementById('cancel-section').classList.add('hidden');
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

    async function fetchPages() {
        try {
            const response = await fetch(`/v1/jobs/${jobId}/pages?token=${token}`);
            if (!response.ok) return;
            
            const data = await response.json();
            
            if (data.total_pages !== lastPagesCount) {
                lastPagesCount = data.total_pages;
                renderPagesTable(data.pages);
                document.getElementById('pages-count').textContent = `${data.total_pages} pages`;
            }
        } catch (e) {
            console.log('Failed to fetch pages:', e);
        }
    }

    function renderPagesTable(pages) {
        const tbody = document.getElementById('pages-tbody');
        
        if (!pages || pages.length === 0) {
            tbody.innerHTML = '<tr class="empty-row"><td colspan="6">No pages crawled yet</td></tr>';
            return;
        }
        
        tbody.innerHTML = pages.map(page => {
            const statusClass = page.status_code >= 200 && page.status_code < 300 ? 'success' 
                : page.status_code >= 300 && page.status_code < 400 ? 'redirect' 
                : 'error';
            
            const shortUrl = page.url.length > 60 ? page.url.substring(0, 60) + '...' : page.url;
            const shortTitle = page.title ? (page.title.length > 40 ? page.title.substring(0, 40) + '...' : page.title) : '-';
            const sizeFormatted = page.text_length > 1000 ? `${(page.text_length / 1000).toFixed(1)}k` : page.text_length;
            
            return `
                <tr>
                    <td class="col-status">
                        <span class="status-badge ${statusClass}">${page.status_code}</span>
                    </td>
                    <td class="col-url">
                        <span class="url-cell" title="${page.url}">${shortUrl}</span>
                    </td>
                    <td class="col-title">
                        <span class="title-cell" title="${page.title || ''}">${shortTitle}</span>
                    </td>
                    <td class="col-depth">${page.depth}</td>
                    <td class="col-size">${sizeFormatted}</td>
                    <td class="col-links">${page.outlinks_count}</td>
                </tr>
            `;
        }).join('');
    }

    function startPolling() {
        fetchStatus();
        fetchPages();
        pollTimer = setInterval(() => {
            fetchStatus();
            fetchPages();
        }, pollInterval);
    }

    function stopPolling() {
        if (pollTimer) {
            clearInterval(pollTimer);
            pollTimer = null;
        }
    }
    
    // Cancel button handler
    document.getElementById('cancel-btn').addEventListener('click', async function() {
        if (!confirm('Are you sure you want to cancel this job? Progress up to this point will be saved.')) {
            return;
        }
        
        const btn = this;
        btn.disabled = true;
        btn.textContent = 'Cancelling...';
        
        try {
            const response = await fetch(`/v1/jobs/${jobId}/cancel?token=${token}`, {
                method: 'POST'
            });
            
            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.message || 'Failed to cancel job');
            }
            
            // Immediately update UI
            const badge = document.getElementById('state-badge');
            badge.textContent = 'cancelled';
            badge.className = 'badge cancelled';
            
            // Keep polling to see finalization
            fetchStatus();
        } catch (error) {
            alert('Failed to cancel job: ' + error.message);
            btn.disabled = false;
            btn.textContent = 'Cancel Job';
        }
    });

    startPolling();
});
