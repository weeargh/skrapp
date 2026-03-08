document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("crawl-form");
    const submitBtn = document.getElementById("submit-btn");
    const messageEl = document.getElementById("form-message");
    const refreshJobsBtn = document.getElementById("refresh-jobs-btn");
    const jobsTbody = document.getElementById("jobs-tbody");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        setMessage("", "");
        submitBtn.disabled = true;
        submitBtn.textContent = "Starting...";

        const payload = {
            start_url: document.getElementById("start_url").value.trim(),
            max_depth: parseInt(document.getElementById("max_depth").value, 10) || 2,
            max_pages: parseInt(document.getElementById("max_pages").value, 10) || 100,
            allowed_path_prefix: document.getElementById("allowed_path_prefix").value.trim() || null,
            timeout_seconds: parseInt(document.getElementById("timeout_seconds").value, 10) || 1800,
            ignore_path_prefixes: document.getElementById("ignore_prefixes").value
                .split(",")
                .map((value) => value.trim())
                .filter(Boolean),
        };

        try {
            const response = await fetch("/v1/jobs", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.message || data.error || "Failed to create job");
            }
            window.location.href = `/status?job_id=${encodeURIComponent(data.job_id)}`;
        } catch (error) {
            setMessage(error.message, "danger");
            submitBtn.disabled = false;
            submitBtn.textContent = "Start crawl";
        }
    });

    refreshJobsBtn.addEventListener("click", () => {
        loadJobs();
    });

    async function loadJobs() {
        try {
            const response = await fetch("/v1/jobs?limit=12");
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.message || data.error || "Failed to load jobs");
            }
            renderJobs(data.jobs || []);
        } catch (error) {
            jobsTbody.innerHTML = `<tr><td colspan="6" class="empty-state-cell">${escapeHtml(error.message)}</td></tr>`;
        }
    }

    function renderJobs(jobs) {
        if (!jobs.length) {
            jobsTbody.innerHTML = '<tr><td colspan="7" class="empty-state-cell">No jobs yet.</td></tr>';
            return;
        }

        const active = new Set(["queued", "starting", "running", "finalizing"]);

        jobsTbody.innerHTML = jobs.map((job) => {
            const isActive = active.has(job.status);
            const retryBtn = `<button class="btn btn-secondary btn-inline job-retry-btn" data-job-id="${escapeHtml(job.job_id)}" type="button">Retry</button>`;
            const deleteBtn = isActive
                ? ""
                : `<button class="btn btn-secondary btn-inline job-delete-btn" data-job-id="${escapeHtml(job.job_id)}" type="button">Delete</button>`;
            return `
                <tr class="row-link" data-href="/status?job_id=${encodeURIComponent(job.job_id)}">
                    <td><code>${escapeHtml(job.job_id)}</code></td>
                    <td><span class="chip ${statusClass(job.status)}">${escapeHtml(job.status)}</span></td>
                    <td class="truncate-cell" title="${escapeHtml(job.start_url)}">${escapeHtml(job.start_url)}</td>
                    <td>${job.pages_discovered || 0}</td>
                    <td>${job.pages_succeeded || 0}</td>
                    <td>${formatDate(job.created_at)}</td>
                    <td class="actions-cell">${retryBtn}${deleteBtn}</td>
                </tr>
            `;
        }).join("");

        jobsTbody.querySelectorAll(".row-link").forEach((row) => {
            row.addEventListener("click", (e) => {
                if (e.target.closest("button")) return;
                window.location.href = row.dataset.href;
            });
        });

        jobsTbody.querySelectorAll(".job-retry-btn").forEach((btn) => {
            btn.addEventListener("click", () => retryJob(btn.dataset.jobId));
        });

        jobsTbody.querySelectorAll(".job-delete-btn").forEach((btn) => {
            btn.addEventListener("click", () => deleteJob(btn.dataset.jobId));
        });
    }

    async function retryJob(jobId) {
        try {
            const data = await fetchJson(`/v1/jobs/${jobId}/retry`, { method: "POST" });
            window.location.href = `/status?job_id=${encodeURIComponent(data.job_id)}`;
        } catch (error) {
            setMessage(error.message, "danger");
        }
    }

    async function deleteJob(jobId) {
        if (!window.confirm("Delete this job and all its data? This cannot be undone.")) return;
        try {
            await fetchJson(`/v1/jobs/${jobId}/delete`, { method: "POST" });
            loadJobs();
        } catch (error) {
            setMessage(error.message, "danger");
        }
    }

    async function fetchJson(url, options = {}) {
        const response = await fetch(url, options);
        const data = await response.json();
        if (!response.ok) throw new Error(data.message || data.error || "Request failed");
        return data;
    }

    function setMessage(message, tone) {
        if (!message) {
            messageEl.className = "notice hidden";
            messageEl.textContent = "";
            return;
        }
        messageEl.className = `notice notice-${tone}`;
        messageEl.textContent = message;
    }

    loadJobs();
});

function formatDate(value) {
    if (!value) return "-";
    try {
        return new Date(value).toLocaleString();
    } catch {
        return value;
    }
}

function statusClass(status) {
    return `chip-${(status || "neutral").toLowerCase()}`;
}

function escapeHtml(value) {
    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;");
}
