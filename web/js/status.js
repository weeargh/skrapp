document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    const jobId = params.get("job_id");

    if (!jobId) {
        showFatal("Missing job_id");
        return;
    }

    const state = {
        jobId,
        pages: [],
        orderedPages: [],
        tree: null,
        currentPage: null,
        jobStatus: null,
        previousJobStatus: null,
        completionSoundPlayed: false,
        pageDetailsById: new Map(),
        selectedPageId: null,
        activeTab: "clean",
        pollHandle: null,
    };

    const cancelBtn = document.getElementById("cancel-btn");
    const retryBtn = document.getElementById("retry-btn");
    const deleteBtn = document.getElementById("delete-btn");
    const previewBtn = document.getElementById("preview-btn");
    const pagesTbody = document.getElementById("pages-tbody");
    const artifactActions = document.getElementById("artifact-actions");
    const tabButtons = Array.from(document.querySelectorAll(".tab-button"));
    const tabPanels = Array.from(document.querySelectorAll(".tab-panel"));
    const downloadTableCsvBtn = document.getElementById("download-table-csv-btn");
    const copyContentBtn = document.getElementById("copy-content-btn");

    cancelBtn.addEventListener("click", () => cancelJob(state.jobId));
    retryBtn.addEventListener("click", () => retryJob(state.jobId));
    deleteBtn.addEventListener("click", () => deleteJob(state.jobId));
    downloadTableCsvBtn.addEventListener("click", downloadTableCsv);
    copyContentBtn.addEventListener("click", copyCurrentContent);
    previewBtn.href = `/${encodeURIComponent(state.jobId)}/preview`;
    tabButtons.forEach((button) => {
        button.addEventListener("click", () => activateTab(button.dataset.tab));
    });

    async function refresh() {
        try {
            const [job, pagesPayload, treePayload] = await Promise.all([
                fetchJson(`/v1/jobs/${state.jobId}`),
                fetchJson(`/v1/jobs/${state.jobId}/pages?limit=1000`),
                fetchJson(`/v1/jobs/${state.jobId}/tree`),
            ]);

            state.pages = pagesPayload.pages || [];
            state.tree = treePayload;
            state.orderedPages = orderPagesByTree(state.tree, state.pages);

            renderJob(job);
            renderPages(state.orderedPages);

            if (state.selectedPageId) {
                loadPage(state.selectedPageId, { preserveSelection: true });
            } else if (state.orderedPages.length > 0) {
                loadPage(state.orderedPages[0].page_id);
            }

            if (["done", "cancelled"].includes(job.status)) {
                loadArtifacts();
                stopPolling();
            } else if (["failed"].includes(job.status)) {
                stopPolling();
            }
        } catch (error) {
            showFatal(error.message);
            stopPolling();
        }
    }

    async function loadArtifacts() {
        try {
            const payload = await fetchJson(`/v1/jobs/${state.jobId}/artifacts`);
            const knownOrder = [
                "page_json_zip",
                "llm_ready_jsonl",
                "raw_markdown_jsonl",
                "plain_text_jsonl",
                "tree_json",
            ];
            const artifactsByKind = new Map(
                (payload.artifacts || [])
                    .filter((artifact) => knownOrder.includes(artifact.kind))
                    .map((artifact) => [artifact.kind, artifact])
            );
            const rendered = knownOrder.map((kind) => {
                const artifact = artifactsByKind.get(kind);
                const emphasisClass = kind === "page_json_zip" ? "btn-primary artifact-link is-primary" : "btn-secondary artifact-link";
                if (artifact) {
                    return `
                        <a class="btn btn-inline has-tooltip ${emphasisClass}" href="${artifact.download_url}" data-tooltip="${escapeHtml(artifactTooltip(kind))}">
                            ${labelForArtifact(kind)}
                        </a>
                    `;
                }
                return `
                    <button class="btn btn-inline has-tooltip artifact-fallback-btn ${emphasisClass}" type="button" data-kind="${kind}" data-tooltip="${escapeHtml(artifactTooltip(kind))}">
                        ${labelForArtifact(kind)}
                    </button>
                `;
            });

            if (!rendered.length) {
                artifactActions.innerHTML = '<span class="text-muted">No artifacts yet.</span>';
                return;
            }

            artifactActions.innerHTML = rendered.join("");
            artifactActions.querySelectorAll(".artifact-fallback-btn").forEach((button) => {
                button.addEventListener("click", () => exportWholeJob(button.dataset.kind, button));
            });
        } catch (error) {
            artifactActions.innerHTML = `<span class="text-muted">${escapeHtml(error.message)}</span>`;
        }
    }

    async function loadPage(pageId, options = {}) {
        try {
            const page = await fetchJson(`/v1/jobs/${state.jobId}/pages/${pageId}`);
            state.selectedPageId = page.page_id;
            renderSelectedPage(page);
            highlightSelectedPage(page.page_id);
            if (!options.preserveSelection) {
                window.history.replaceState({}, "", `/status?job_id=${encodeURIComponent(state.jobId)}&page_id=${encodeURIComponent(page.page_id)}`);
            }
        } catch (error) {
            document.getElementById("page-detail-empty").textContent = error.message;
        }
    }

    function renderJob(job) {
        state.previousJobStatus = state.jobStatus;
        state.jobStatus = job.status;
        document.getElementById("job-url-subtitle").textContent = job.start_url;
        document.getElementById("job-id").textContent = job.job_id;
        document.getElementById("job-host").textContent = job.allowed_host || "-";
        document.getElementById("job-path-prefix").textContent = job.allowed_path_prefix || "/";
        document.getElementById("job-cleanup-status").textContent = job.cleanup_status || "-";
        document.getElementById("job-created-at").textContent = formatDate(job.created_at);
        document.getElementById("job-finished-at").textContent = formatDate(job.finished_at);
        document.getElementById("job-pages-discovered").textContent = job.pages_discovered || 0;
        document.getElementById("job-pages-processed").textContent = job.pages_processed || 0;
        document.getElementById("job-pages-succeeded").textContent = job.pages_succeeded || 0;
        document.getElementById("job-pages-failed").textContent = job.pages_failed || 0;
        document.getElementById("job-max-depth").textContent = job.max_depth ?? "-";
        document.getElementById("job-elapsed").textContent = formatDuration(job.elapsed_seconds);
        renderProgress(job);

        const statusBadge = document.getElementById("status-badge");
        statusBadge.className = `chip ${statusClass(job.status)}`;
        statusBadge.textContent = job.status;

        maybePlayCompletionSound(job.status);

        const errorEl = document.getElementById("job-error");
        if (job.error_message) {
            errorEl.className = "notice notice-danger";
            errorEl.textContent = job.error_message;
        } else {
            errorEl.className = "notice notice-danger hidden";
            errorEl.textContent = "";
        }

        const isActive = ["queued", "starting", "running", "finalizing"].includes(job.status);
        const isTerminal = ["done", "cancelled", "failed"].includes(job.status);
        cancelBtn.classList.toggle("hidden", !isActive);
        retryBtn.classList.toggle("hidden", !isTerminal);
        deleteBtn.classList.toggle("hidden", !isTerminal);
    }

    function renderProgress(job) {
        const progress = computeJobProgress(job);
        document.getElementById("job-progress-fill").style.width = `${progress.percent}%`;
        document.getElementById("job-progress-label").textContent = progress.label;
        document.getElementById("job-eta").textContent = progress.etaLabel;

        [
            ["queued", progress.stageState.queued],
            ["running", progress.stageState.running],
            ["finalizing", progress.stageState.finalizing],
            ["ready", progress.stageState.ready],
        ].forEach(([stageName, stageValue]) => {
            const element = document.getElementById(`stage-${stageName}`);
            element.className = `stage-chip ${stageValue ? `is-${stageValue}` : ""}`.trim();
        });
    }

    function renderPages(pages) {
        document.getElementById("pages-total-badge").textContent = `${pages.length} pages`;
        downloadTableCsvBtn.disabled = pages.length === 0;

        if (!pages.length) {
            pagesTbody.innerHTML = '<tr><td colspan="6" class="empty-state-cell">No pages yet.</td></tr>';
            return;
        }

        pagesTbody.innerHTML = pages.map((page) => `
            <tr class="page-row ${page.page_id === state.selectedPageId ? "is-selected" : ""}" data-page-id="${page.page_id}">
                <td class="truncate-cell">
                    <button class="page-title-button" type="button" style="--page-depth:${page.depth || 0}" title="${escapeHtml(page.title || page.url)}">
                        <span class="page-title-indent"></span>
                        <span class="page-title-text">${escapeHtml(page.title || page.url)}</span>
                    </button>
                </td>
                <td><span class="chip chip-neutral">${escapeHtml(page.page_type || "-")}</span></td>
                <td><span class="chip ${statusClass(page.status)}">${escapeHtml(page.status)}</span></td>
                <td>${page.depth}</td>
                <td>${formatTextLength(page.text_length)}</td>
                <td>${formatConfidence(page.cleanup_confidence, page.cleanup_score)}</td>
            </tr>
        `).join("");

        pagesTbody.querySelectorAll(".page-row").forEach((row) => {
            row.addEventListener("click", () => loadPage(row.dataset.pageId));
        });
    }

    function renderSelectedPage(page) {
        state.currentPage = page;
        state.pageDetailsById.set(page.page_id, page);
        document.getElementById("page-detail-empty").classList.add("hidden");
        document.getElementById("page-detail-content").classList.remove("hidden");

        document.getElementById("page-detail-title").textContent = page.title || page.url;
        document.getElementById("page-detail-type").textContent = page.page_type || "-";
        document.getElementById("page-detail-status").textContent = page.status || "-";
        document.getElementById("page-detail-depth").textContent = page.depth ?? "-";
        document.getElementById("page-detail-confidence").textContent = formatConfidence(page.cleanup_confidence, page.cleanup_score);
        document.getElementById("page-detail-url").href = page.url;
        document.getElementById("page-detail-url").textContent = page.url;
        document.getElementById("page-clean-markdown").textContent = page.clean_markdown || "";
        document.getElementById("page-raw-markdown").textContent = page.raw_markdown || "";
        document.getElementById("page-plain-text").textContent = page.plain_text || "";
        updateCopyButton();
    }

    function highlightSelectedPage(pageId) {
        document.querySelectorAll(".page-row").forEach((row) => {
            row.classList.toggle("is-selected", row.dataset.pageId === pageId);
        });
    }

    async function cancelJob(jobIdValue) {
        if (!window.confirm("Cancel this crawl? Finalization will keep any completed pages.")) {
            return;
        }
        cancelBtn.disabled = true;
        cancelBtn.textContent = "Cancelling...";
        try {
            await fetchJson(`/v1/jobs/${jobIdValue}/cancel`, { method: "POST" });
            await refresh();
        } catch (error) {
            showFatal(error.message);
        } finally {
            cancelBtn.disabled = false;
            cancelBtn.textContent = "Cancel job";
        }
    }

    async function retryJob(jobIdValue) {
        retryBtn.disabled = true;
        retryBtn.textContent = "Retrying...";
        try {
            const data = await fetchJson(`/v1/jobs/${jobIdValue}/retry`, { method: "POST" });
            window.location.href = `/status?job_id=${encodeURIComponent(data.job_id)}`;
        } catch (error) {
            showFatal(error.message);
            retryBtn.disabled = false;
            retryBtn.textContent = "Retry";
        }
    }

    async function deleteJob(jobIdValue) {
        if (!window.confirm("Delete this job and all its data? This cannot be undone.")) return;
        deleteBtn.disabled = true;
        deleteBtn.textContent = "Deleting...";
        try {
            await fetchJson(`/v1/jobs/${jobIdValue}/delete`, { method: "POST" });
            window.location.href = "/";
        } catch (error) {
            showFatal(error.message);
            deleteBtn.disabled = false;
            deleteBtn.textContent = "Delete";
        }
    }

    function activateTab(tabName) {
        state.activeTab = tabName;
        tabButtons.forEach((button) => {
            button.classList.toggle("is-active", button.dataset.tab === tabName);
        });
        tabPanels.forEach((panel) => {
            panel.classList.toggle("is-active", panel.dataset.panel === tabName);
        });
        updateCopyButton();
    }

    async function copyCurrentContent() {
        const content = contentForActiveTab(state.currentPage, state.activeTab);
        if (!content) {
            return;
        }

        try {
            await navigator.clipboard.writeText(content);
            copyContentBtn.textContent = "Copied";
            window.setTimeout(() => {
                copyContentBtn.textContent = "Copy";
            }, 1200);
        } catch {
            copyContentBtn.textContent = "Copy failed";
            window.setTimeout(() => {
                copyContentBtn.textContent = "Copy";
            }, 1200);
        }
    }

    function updateCopyButton() {
        copyContentBtn.disabled = !contentForActiveTab(state.currentPage, state.activeTab);
        copyContentBtn.textContent = "Copy";
    }

    function downloadTableCsv() {
        if (!state.orderedPages.length) {
            return;
        }

        const rows = [
            ["title", "url", "type", "status", "depth", "text_length", "cleanup_percent"],
            ...state.orderedPages.map((page) => [
                page.title || page.url || "",
                page.url || "",
                page.page_type || "",
                page.status || "",
                page.depth ?? "",
                page.text_length ?? "",
                formatConfidence(page.cleanup_confidence, page.cleanup_score),
            ]),
        ];

        const csv = rows.map((row) => row.map(escapeCsv).join(",")).join("\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.download = `${slugifyFilename(state.jobId)}-pages.csv`;
        document.body.appendChild(link);
        link.click();
        link.remove();
        window.setTimeout(() => URL.revokeObjectURL(url), 0);
    }

    async function exportWholeJob(kind, button) {
        const originalLabel = button ? button.textContent : null;
        if (button) {
            button.disabled = true;
            button.textContent = "Preparing...";
        }

        try {
            const response = await fetch(`/v1/jobs/${state.jobId}/artifacts/${kind}/download`);
            let errorPayload = null;
            if (!response.ok) {
                errorPayload = await response.json().catch(() => null);
                throw new Error(errorPayload?.message || errorPayload?.error || "Download failed");
            }

            const blob = await response.blob();
            downloadBlob(blob, `${slugifyFilename(state.jobId)}-${exportFilename(kind)}`);
        } catch (error) {
            artifactActions.innerHTML = `<span class="text-muted">${escapeHtml(error.message)}</span>`;
        } finally {
            if (button) {
                button.disabled = false;
                button.textContent = originalLabel;
            }
        }
    }

    function startPolling() {
        refresh();
        state.pollHandle = window.setInterval(refresh, 3000);
    }

    function maybePlayCompletionSound(status) {
        if (state.completionSoundPlayed) {
            return;
        }
        if (!["done", "cancelled"].includes(status)) {
            return;
        }
        if (!state.previousJobStatus || ["done", "cancelled"].includes(state.previousJobStatus)) {
            return;
        }
        playCompletionDing();
        state.completionSoundPlayed = true;
    }

    function stopPolling() {
        if (state.pollHandle) {
            window.clearInterval(state.pollHandle);
            state.pollHandle = null;
        }
    }

    function showFatal(message) {
        const errorEl = document.getElementById("job-error");
        errorEl.className = "notice notice-danger";
        errorEl.textContent = message;
    }

    const presetPageId = params.get("page_id");
    if (presetPageId) {
        state.selectedPageId = presetPageId;
    }
    startPolling();
});

async function fetchJson(url, options = {}) {
    const response = await fetch(url, options);
    const data = await response.json();
    if (!response.ok) {
        throw new Error(data.message || data.error || "Request failed");
    }
    return data;
}

function orderPagesByTree(tree, pages) {
    if (!Array.isArray(pages) || pages.length === 0) {
        return [];
    }
    if (!tree || !Array.isArray(tree.nodes) || tree.nodes.length === 0) {
        return pages;
    }

    const pageMap = new Map(pages.map((page) => [page.page_id, page]));
    const nodesByParent = new Map();

    tree.nodes.forEach((node) => {
        const parentKey = node.parent_page_id || "root";
        if (!nodesByParent.has(parentKey)) {
            nodesByParent.set(parentKey, []);
        }
        nodesByParent.get(parentKey).push(node);
    });

    const ordered = [];
    const seen = new Set();

    function visit(parentKey) {
        const children = nodesByParent.get(parentKey) || [];
        children.forEach((node) => {
            const page = pageMap.get(node.page_id);
            if (page) {
                ordered.push(page);
                seen.add(page.page_id);
            }
            visit(node.page_id);
        });
    }

    visit("root");

    pages.forEach((page) => {
        if (!seen.has(page.page_id)) {
            ordered.push(page);
        }
    });

    return ordered;
}

function contentForActiveTab(page, activeTab) {
    if (!page) {
        return "";
    }
    if (activeTab === "clean") return page.clean_markdown || "";
    if (activeTab === "raw") return page.raw_markdown || "";
    if (activeTab === "plain") return page.plain_text || "";
    return "";
}

function computeJobProgress(job) {
    const status = job.status || "queued";
    const maxPages = Math.max(1, Number(job.max_pages) || 1);
    const discovered = Math.max(0, Number(job.pages_discovered) || 0);
    const processed = Math.max(0, Number(job.pages_processed) || 0);
    const elapsed = Math.max(0, Number(job.elapsed_seconds) || 0);

    const targetPages = Math.max(maxPages, discovered, processed, 1);
    const crawlRatio = Math.max(0, Math.min(1, processed / targetPages));

    let percent = 4;
    let label = "Queued";
    let etaLabel = "ETA -";
    const stageState = {
        queued: "current",
        running: "",
        finalizing: "",
        ready: "",
    };

    if (status === "starting") {
        percent = 8;
        label = "Preparing crawl";
        etaLabel = "ETA soon";
        stageState.queued = "done";
        stageState.running = "current";
    } else if (status === "running") {
        percent = Math.max(8, Math.min(88, 10 + crawlRatio * 75));
        label = `${Math.round(percent)}% complete`;
        stageState.queued = "done";
        stageState.running = "current";
        if (elapsed > 0 && processed > 0) {
            const pagesPerSecond = processed / elapsed;
            const remainingPages = Math.max(targetPages - processed, 0);
            etaLabel = remainingPages > 0 ? `ETA ${formatDuration(Math.round(remainingPages / pagesPerSecond))}` : "ETA soon";
        } else {
            etaLabel = "ETA estimating...";
        }
    } else if (status === "finalizing") {
        percent = 92;
        label = "Finalizing outputs";
        etaLabel = "ETA soon";
        stageState.queued = "done";
        stageState.running = "done";
        stageState.finalizing = "current";
    } else if (status === "done" || status === "cancelled") {
        percent = 100;
        label = status === "cancelled" ? "Cancelled with partial results" : "Complete";
        etaLabel = "ETA done";
        stageState.queued = "done";
        stageState.running = "done";
        stageState.finalizing = "done";
        stageState.ready = "done";
    } else if (status === "failed") {
        percent = Math.max(6, Math.round(10 + crawlRatio * 60));
        label = "Stopped";
        etaLabel = "ETA unavailable";
        stageState.queued = "done";
        stageState.running = processed > 0 ? "done" : "current";
    }

    return { percent, label, etaLabel, stageState };
}

function formatDate(value) {
    if (!value) return "-";
    try {
        return new Date(value).toLocaleString();
    } catch {
        return value;
    }
}

function formatDuration(seconds) {
    if (seconds === null || seconds === undefined) return "-";
    if (seconds < 60) return `${seconds}s`;
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ${seconds % 60}s`;
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${minutes}m`;
}

function formatTextLength(value) {
    const length = value || 0;
    if (length >= 1000) return `${(length / 1000).toFixed(1)}k`;
    return `${length}`;
}

function formatConfidence(confidence, fallbackScore) {
    const value = confidence ?? fallbackScore;
    if (value === null || value === undefined || Number.isNaN(Number(value))) return "-";
    return `${Math.round(Number(value) * 100)}%`;
}

function statusClass(status) {
    return `chip-${(status || "neutral").toLowerCase()}`;
}

function labelForArtifact(kind) {
    if (kind === "page_json_zip") return "JSON ZIP";
    if (kind === "llm_ready_jsonl") return "LLM-ready JSONL";
    if (kind === "raw_markdown_jsonl") return "Raw markdown JSONL";
    if (kind === "plain_text_jsonl") return "Plain text JSONL";
    if (kind === "tree_json") return "Tree JSON";
    return kind;
}

function artifactTooltip(kind) {
    if (kind === "page_json_zip") {
        return "One JSON file per page with metadata plus cleaned markdown, raw markdown, and plain text. Best when you want the most complete export.";
    }
    if (kind === "llm_ready_jsonl") {
        return "Cleaned markdown with headings and lists preserved. Best default for chatbot and RAG ingestion.";
    }
    if (kind === "raw_markdown_jsonl") {
        return "Original extracted markdown before cleanup. Best for debugging or custom post-processing.";
    }
    if (kind === "plain_text_jsonl") {
        return "Flattened text with markdown formatting removed. Best for simple text-only pipelines.";
    }
    if (kind === "tree_json") {
        return "Hierarchy and parent-child structure for the crawl.";
    }
    return kind;
}

function playCompletionDing() {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) {
        return;
    }

    const context = new AudioContextClass();
    const oscillator = context.createOscillator();
    const gainNode = context.createGain();

    oscillator.type = "sine";
    oscillator.frequency.setValueAtTime(880, context.currentTime);
    oscillator.frequency.exponentialRampToValueAtTime(1320, context.currentTime + 0.18);

    gainNode.gain.setValueAtTime(0.0001, context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.08, context.currentTime + 0.02);
    gainNode.gain.exponentialRampToValueAtTime(0.0001, context.currentTime + 0.5);

    oscillator.connect(gainNode);
    gainNode.connect(context.destination);
    oscillator.start(context.currentTime);
    oscillator.stop(context.currentTime + 0.52);
    oscillator.addEventListener("ended", () => {
        context.close().catch(() => {});
    });
}

function slugifyFilename(value) {
    return String(value || "pages")
        .toLowerCase()
        .replaceAll(/[^a-z0-9]+/g, "-")
        .replaceAll(/^-+|-+$/g, "") || "pages";
}

function exportFilename(kind) {
    if (kind === "page_json_zip") return "pages-json.zip";
    if (kind === "llm_ready_jsonl") return "llm-ready.jsonl";
    if (kind === "raw_markdown_jsonl") return "raw-markdown.jsonl";
    if (kind === "plain_text_jsonl") return "plain-text.jsonl";
    if (kind === "tree_json") return "tree.json";
    return `${kind}.jsonl`;
}

function escapeCsv(value) {
    const text = String(value ?? "");
    return `"${text.replaceAll('"', '""')}"`;
}

function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 0);
}

function escapeHtml(value) {
    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;");
}
