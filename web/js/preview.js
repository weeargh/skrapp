document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    const frameBaseWidth = 1440;
    const frameBaseHeight = 2200;

    const state = {
        jobId: detectJobId(params),
        job: null,
        pages: [],
        orderedPages: [],
        tree: null,
        selectedPageId: params.get("page_id") || null,
        currentPage: null,
        pageDetailsById: new Map(),
        sortMode: "recommended",
        searchTerm: "",
        browseVisibleCount: 24,
        activeViewMode: "document",
        activeLayoutMode: "compare",
        pollHandle: null,
        frameLoadTimeout: null,
    };

    const elements = {
        subtitle: document.getElementById("preview-subtitle"),
        statusBadge: document.getElementById("preview-status-badge"),
        total: document.getElementById("summary-pages-total"),
        succeeded: document.getElementById("summary-pages-succeeded"),
        failed: document.getElementById("summary-pages-failed"),
        sortLabel: document.getElementById("summary-sort-label"),
        selectionSummary: document.getElementById("selection-summary"),
        statusLink: document.getElementById("status-link"),
        openStatusBtn: document.getElementById("open-status-btn"),
        search: document.getElementById("review-search"),
        sort: document.getElementById("sort-mode"),
        sortHelper: document.getElementById("sort-helper"),
        browseBtn: document.getElementById("browse-btn"),
        backToCompareBtn: document.getElementById("back-to-compare-btn"),
        browseView: document.getElementById("browse-view"),
        compareView: document.getElementById("compare-view"),
        browseResultSummary: document.getElementById("browse-result-summary"),
        browseEmpty: document.getElementById("browse-empty"),
        browseResults: document.getElementById("browse-results"),
        loadMoreBtn: document.getElementById("load-more-btn"),
        webPreviewEmpty: document.getElementById("web-preview-empty"),
        webPreviewShell: document.getElementById("web-preview-shell"),
        webPreviewStage: document.getElementById("web-preview-stage"),
        webPreviewCanvas: document.getElementById("web-preview-canvas"),
        pageFrame: document.getElementById("page-frame"),
        openSourceBtn: document.getElementById("open-source-btn"),
        previewEmpty: document.getElementById("preview-empty"),
        previewContent: document.getElementById("preview-content"),
        previewPageTitle: document.getElementById("preview-page-title"),
        previewPageUrl: document.getElementById("preview-page-url"),
        previewPageOrigin: document.getElementById("preview-page-origin"),
        previewPageDepth: document.getElementById("preview-page-depth"),
        previewPageLength: document.getElementById("preview-page-length"),
        previewPageConfidence: document.getElementById("preview-page-confidence"),
        previewPageStatus: document.getElementById("preview-page-status"),
        prevBtn: document.getElementById("prev-page-btn"),
        nextBtn: document.getElementById("next-page-btn"),
        documentPreview: document.getElementById("document-preview"),
        plainPreview: document.getElementById("plain-preview"),
        jsonPreview: document.getElementById("json-preview"),
        viewButtons: Array.from(document.querySelectorAll("[data-view-mode]")),
        viewPanels: Array.from(document.querySelectorAll("[data-view-panel]")),
    };

    const resizePreview = () => fitFrameWidth(elements, frameBaseWidth, frameBaseHeight);

    elements.search.addEventListener("input", () => {
        state.searchTerm = elements.search.value.trim().toLowerCase();
        state.browseVisibleCount = 24;
        updateBrowseButtonLabel();
        if (state.activeLayoutMode === "browse") {
            renderBrowseResults();
        }
        renderSelectionSummary();
        updatePrevNextState();
    });

    elements.search.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            event.preventDefault();
            showBrowseMode();
        }
    });

    elements.sort.addEventListener("change", () => {
        state.sortMode = elements.sort.value;
        state.browseVisibleCount = 24;
        renderJobSummary();
        renderBrowseResults();
        renderSelectionSummary();
        updatePrevNextState();
    });

    elements.browseBtn.addEventListener("click", showBrowseMode);
    elements.backToCompareBtn.addEventListener("click", showCompareMode);

    elements.loadMoreBtn.addEventListener("click", () => {
        state.browseVisibleCount += 24;
        renderBrowseResults();
    });

    elements.prevBtn.addEventListener("click", () => moveSelection(-1));
    elements.nextBtn.addEventListener("click", () => moveSelection(1));

    elements.pageFrame.addEventListener("load", () => {
        elements.webPreviewShell.classList.remove("is-loading");
        clearTimeout(state.frameLoadTimeout);
    });

    elements.pageFrame.addEventListener("error", () => {
        elements.webPreviewShell.classList.remove("is-loading");
        clearTimeout(state.frameLoadTimeout);
    });

    elements.viewButtons.forEach((button) => {
        button.addEventListener("click", () => {
            state.activeViewMode = button.dataset.viewMode;
            renderViewMode();
        });
    });

    window.addEventListener("resize", resizePreview);
    if (window.ResizeObserver && elements.webPreviewStage) {
        const observer = new ResizeObserver(resizePreview);
        observer.observe(elements.webPreviewStage);
    }

    initialize();

    async function initialize() {
        updateBrowseButtonLabel();
        renderViewMode();
        syncLayoutMode();
        updatePrevNextState();
        try {
            if (!state.jobId) {
                elements.subtitle.textContent = "Loading latest reviewable job…";
                state.jobId = await resolveDefaultJobId();
                if (!state.jobId) {
                    showFatal("No completed job is available for preview yet.");
                    return;
                }
                window.history.replaceState({}, "", previewUrlFor(state.jobId, state.selectedPageId));
            }

            syncJobLinks();
            startPolling();
        } catch (error) {
            showFatal(error.message);
        }
    }

    function startPolling() {
        refresh();
        state.pollHandle = window.setInterval(refresh, 5000);
    }

    function stopPolling() {
        if (!state.pollHandle) {
            return;
        }
        window.clearInterval(state.pollHandle);
        state.pollHandle = null;
    }

    async function refresh() {
        try {
            const [job, pagesPayload, treePayload] = await Promise.all([
                fetchJson(`/v1/jobs/${state.jobId}`),
                fetchJson(`/v1/jobs/${state.jobId}/pages?limit=1000`),
                fetchJson(`/v1/jobs/${state.jobId}/tree`),
            ]);

            state.job = job;
            state.pages = pagesPayload.pages || [];
            state.tree = treePayload;
            state.orderedPages = orderPagesByTree(treePayload, state.pages).map((page, index) => ({
                ...page,
                treeIndex: index,
            }));

            renderJobSummary();
            renderBrowseResults();

            const pageIdToShow = resolvePageIdToShow();
            if (!pageIdToShow) {
                clearPreview();
            } else if (!state.currentPage || state.currentPage.page_id !== pageIdToShow) {
                await selectPage(pageIdToShow, { preserveUrl: true, keepMode: true });
            } else {
                renderSelectionSummary();
                updatePrevNextState();
            }

            if (["done", "cancelled", "failed"].includes(job.status)) {
                stopPolling();
            }
        } catch (error) {
            showFatal(error.message);
            stopPolling();
        }
    }

    function resolvePageIdToShow() {
        if (state.selectedPageId && state.orderedPages.some((page) => page.page_id === state.selectedPageId)) {
            return state.selectedPageId;
        }

        const filtered = getFilteredPages();
        if (filtered.length) {
            return filtered[0].page_id;
        }
        return state.orderedPages[0]?.page_id || null;
    }

    function renderJobSummary() {
        const job = state.job;
        elements.subtitle.textContent = job
            ? `${job.start_url} • compare the live page against the cleaned extraction`
            : "Loading job preview…";
        elements.total.textContent = `${state.orderedPages.length.toLocaleString()} pages`;
        elements.succeeded.textContent = `${(job?.pages_succeeded || 0).toLocaleString()} succeeded`;
        elements.failed.textContent = `${(job?.pages_failed || 0).toLocaleString()} failed`;
        elements.sortLabel.textContent = sortLabel(state.sortMode);
        elements.sortHelper.textContent = sortDescription(state.sortMode);
        elements.statusBadge.className = `chip ${statusClass(job?.status)}`;
        elements.statusBadge.textContent = job?.status || "unknown";
    }

    function renderBrowseResults() {
        const filtered = getFilteredPages();
        const visibleRows = filtered.slice(0, state.browseVisibleCount);

        elements.browseResultSummary.textContent = filtered.length
            ? `${visibleRows.length.toLocaleString()} of ${filtered.length.toLocaleString()} results`
            : "0 results";
        elements.browseEmpty.classList.toggle("hidden", filtered.length !== 0);
        elements.loadMoreBtn.classList.toggle("hidden", filtered.length <= state.browseVisibleCount);

        if (!visibleRows.length) {
            elements.browseResults.innerHTML = "";
            return;
        }

        elements.browseResults.innerHTML = visibleRows.map((page, index) => {
            const rank = index + 1;
            const selected = page.page_id === state.selectedPageId;
            return `
                <button class="browse-result ${selected ? "is-selected" : ""}" type="button" data-page-id="${escapeHtml(page.page_id)}">
                    <div class="browse-result-top">
                        <div>
                            <p class="browse-result-eyebrow">#${rank} in ${escapeHtml(sortLabel(state.sortMode))}</p>
                            <h3 class="browse-result-title">${escapeHtml(page.title || page.url || "Untitled page")}</h3>
                            <div class="browse-result-url">${escapeHtml(page.url || "")}</div>
                        </div>
                        <div class="browse-result-flags">
                            ${selected ? '<span class="chip chip-neutral">Current</span>' : ""}
                            <span class="chip ${statusClass(page.status)}">${escapeHtml(page.status || "-")}</span>
                        </div>
                    </div>
                    <div class="browse-result-meta">
                        <span class="chip chip-neutral">Depth ${page.depth ?? "-"}</span>
                        <span class="chip chip-neutral">${formatTextLength(page.text_length)}</span>
                        <span class="chip chip-neutral">${formatConfidence(page.cleanup_confidence, page.cleanup_score)}</span>
                    </div>
                    <p class="browse-result-snippet">${escapeHtml(pageSnippet(page))}</p>
                </button>
            `;
        }).join("");

        elements.browseResults.querySelectorAll(".browse-result").forEach((item) => {
            item.addEventListener("click", async () => {
                await selectPage(item.dataset.pageId);
                showCompareMode();
            });
        });
    }

    async function selectPage(pageId, options = {}) {
        if (!pageId) {
            clearPreview();
            return;
        }

        try {
            let page = state.pageDetailsById.get(pageId);
            if (!page || options.forceRefresh) {
                page = await fetchJson(`/v1/jobs/${state.jobId}/pages/${pageId}`);
                state.pageDetailsById.set(page.page_id, page);
            }

            state.selectedPageId = page.page_id;
            state.currentPage = page;
            renderSelectedPage(page);
            renderSelectionSummary();

            if (!options.preserveUrl) {
                window.history.replaceState({}, "", previewUrlFor(state.jobId, page.page_id));
            }

            if (!options.keepMode) {
                showCompareMode();
            }
        } catch (error) {
            showFatal(error.message);
        }
    }

    function renderSelectedPage(page) {
        const displayUrl = resolveDisplayUrl(page);
        const plainText = page.plain_text || "";

        elements.previewEmpty.classList.add("hidden");
        elements.previewContent.classList.remove("hidden");
        elements.webPreviewEmpty.classList.add("hidden");
        elements.webPreviewShell.classList.remove("hidden");

        elements.previewPageTitle.textContent = page.title || displayUrl || page.url || "Untitled page";
        setLinkState(elements.previewPageUrl, displayUrl, displayUrl || "Unavailable");
        setLinkState(elements.openSourceBtn, displayUrl, "Open source");

        if (displayUrl && page.url && displayUrl !== page.url) {
            elements.previewPageOrigin.textContent = `Crawled from wrapper URL: ${page.url}`;
            elements.previewPageOrigin.classList.remove("hidden");
        } else {
            elements.previewPageOrigin.textContent = "";
            elements.previewPageOrigin.classList.add("hidden");
        }

        elements.previewPageStatus.className = `chip ${statusClass(page.status)}`;
        elements.previewPageStatus.textContent = page.status || "-";
        elements.previewPageDepth.textContent = page.depth ?? "-";
        elements.previewPageLength.textContent = formatTextLength(plainText.length);
        elements.previewPageConfidence.textContent = formatConfidence(page.cleanup_confidence, page.cleanup_score);

        elements.documentPreview.innerHTML = buildDocumentHtml(page);
        elements.plainPreview.textContent = plainText;
        elements.jsonPreview.textContent = JSON.stringify(buildPageJsonPreview(page, displayUrl), null, 2);

        elements.webPreviewShell.classList.add("is-loading");
        clearTimeout(state.frameLoadTimeout);
        state.frameLoadTimeout = window.setTimeout(() => {
            elements.webPreviewShell.classList.remove("is-loading");
        }, 4000);
        elements.pageFrame.src = displayUrl || "about:blank";

        renderViewMode();
        updatePrevNextState();
        fitFrameWidth(elements, frameBaseWidth, frameBaseHeight);
    }

    function clearPreview() {
        state.currentPage = null;
        state.selectedPageId = null;
        elements.previewEmpty.classList.remove("hidden");
        elements.previewContent.classList.add("hidden");
        elements.webPreviewEmpty.classList.remove("hidden");
        elements.webPreviewShell.classList.add("hidden");
        elements.webPreviewShell.classList.remove("is-loading");
        elements.pageFrame.removeAttribute("src");
        setLinkState(elements.previewPageUrl, "", "Unavailable");
        setLinkState(elements.openSourceBtn, "", "Open source");
        renderSelectionSummary();
        updatePrevNextState();
    }

    function renderViewMode() {
        elements.viewButtons.forEach((button) => {
            button.classList.toggle("is-active", button.dataset.viewMode === state.activeViewMode);
        });
        elements.viewPanels.forEach((panel) => {
            panel.classList.toggle("is-active", panel.dataset.viewPanel === state.activeViewMode);
        });
    }

    function updatePrevNextState() {
        const filtered = getFilteredPages();
        const index = filtered.findIndex((page) => page.page_id === state.selectedPageId);
        elements.prevBtn.disabled = index <= 0;
        elements.nextBtn.disabled = index === -1 || index >= filtered.length - 1;
    }

    function moveSelection(direction) {
        const filtered = getFilteredPages();
        if (!filtered.length) {
            return;
        }

        const index = filtered.findIndex((page) => page.page_id === state.selectedPageId);
        if (index === -1) {
            selectPage(filtered[0].page_id);
            return;
        }

        const nextPage = filtered[index + direction];
        if (!nextPage) {
            return;
        }
        selectPage(nextPage.page_id);
    }

    function renderSelectionSummary() {
        const filtered = getFilteredPages();
        if (!filtered.length) {
            elements.selectionSummary.textContent = "No pages available for review yet.";
            return;
        }

        if (!state.selectedPageId) {
            elements.selectionSummary.textContent = `Start with the top page in ${sortLabel(state.sortMode)} order.`;
            return;
        }

        const index = filtered.findIndex((page) => page.page_id === state.selectedPageId);
        if (index === -1) {
            elements.selectionSummary.textContent = `Current page is outside the active search. Open browse to pick from ${filtered.length.toLocaleString()} filtered results.`;
            return;
        }

        elements.selectionSummary.textContent = `Reviewing ${index + 1} of ${filtered.length.toLocaleString()} in ${sortLabel(state.sortMode)} order.`;
    }

    function getFilteredPages() {
        const pages = [...state.orderedPages];
        const filtered = pages.filter((page) => matchesSearch(page, state.searchTerm));
        filtered.sort((left, right) => comparePages(left, right, state.sortMode));
        return filtered;
    }

    function showBrowseMode() {
        state.activeLayoutMode = "browse";
        syncLayoutMode();
        renderBrowseResults();
    }

    function showCompareMode() {
        state.activeLayoutMode = "compare";
        syncLayoutMode();
        renderSelectionSummary();
        fitFrameWidth(elements, frameBaseWidth, frameBaseHeight);
    }

    function syncLayoutMode() {
        const browsing = state.activeLayoutMode === "browse";
        elements.compareView.classList.toggle("hidden", browsing);
        elements.browseView.classList.toggle("hidden", !browsing);
        elements.backToCompareBtn.classList.toggle("hidden", !browsing);
        updateBrowseButtonLabel();
    }

    function updateBrowseButtonLabel() {
        elements.browseBtn.textContent = state.searchTerm ? "Search" : "Browse pages";
    }

    function syncJobLinks() {
        if (!state.jobId) {
            return;
        }
        const statusHref = `/status?job_id=${encodeURIComponent(state.jobId)}`;
        elements.statusLink.href = statusHref;
        elements.openStatusBtn.href = statusHref;
    }
});

function detectJobId(params) {
    const queryJobId = params.get("job_id");
    if (queryJobId) {
        return queryJobId;
    }

    const parts = window.location.pathname.split("/").filter(Boolean);
    if (parts.length >= 2 && parts[1] === "preview") {
        return parts[0];
    }

    return null;
}

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

function matchesSearch(page, searchTerm) {
    if (!searchTerm) {
        return true;
    }

    const haystack = `${page.title || ""} ${page.url || ""}`.toLowerCase();
    return haystack.includes(searchTerm);
}

function comparePages(left, right, sortMode) {
    if (sortMode === "recommended") {
        return compareNumbers(recommendedPriority(right), recommendedPriority(left))
            || compareNumbers(left.treeIndex, right.treeIndex)
            || compareTitle(left, right);
    }
    if (sortMode === "tree") {
        return compareNumbers(left.treeIndex, right.treeIndex) || compareTitle(left, right);
    }
    if (sortMode === "shortest") {
        return compareNumbers(left.text_length ?? 0, right.text_length ?? 0) || compareTitle(left, right);
    }
    if (sortMode === "confidence") {
        return compareNumbers(confidenceValue(left), confidenceValue(right)) || compareTitle(left, right);
    }
    if (sortMode === "title") {
        return compareTitle(left, right) || compareNumbers(left.treeIndex, right.treeIndex);
    }

    return compareNumbers(reviewPriority(right), reviewPriority(left))
        || compareNumbers(left.text_length ?? 0, right.text_length ?? 0)
        || compareNumbers(left.treeIndex, right.treeIndex)
        || compareTitle(left, right);
}

function recommendedPriority(page) {
    const url = page.url || "";
    let score = 0;

    if (page.status === "done") {
        score += 500;
    } else if (page.status === "failed") {
        score -= 500;
    }

    if (url.includes("/hc/id/articles/")) {
        score += 220;
    } else if (url.includes("/hc/id/sections/")) {
        score += 120;
    }

    if (url.includes("/related/click")) {
        score -= 260;
    }

    const textLength = page.text_length ?? 0;
    score += Math.min(260, Math.round(Math.log10(textLength + 10) * 90));

    const confidence = confidenceValue(page);
    if (Number.isFinite(confidence)) {
        score += Math.round(confidence * 120);
    }

    score -= Math.min(30, (page.depth || 0) * 3);
    return score;
}

function reviewPriority(page) {
    let score = 0;

    if (page.status === "failed") {
        score += 1000;
    }
    if ((page.url || "").includes("/related/click")) {
        score += 260;
    }
    if (!page.title) {
        score += 80;
    }

    const textLength = page.text_length ?? 0;
    if (textLength === 0) {
        score += 220;
    } else if (textLength < 300) {
        score += 160;
    } else if (textLength < 800) {
        score += 90;
    }

    const confidence = confidenceValue(page);
    if (Number.isFinite(confidence)) {
        score += Math.round((1 - confidence) * 120);
    }

    score += Math.min(24, (page.depth || 0) * 3);
    return score;
}

function confidenceValue(page) {
    if (typeof page.cleanup_confidence === "number") {
        return page.cleanup_confidence;
    }
    return 1;
}

function pageSnippet(page) {
    if (page.status === "failed") {
        return "Failed page. Open this first to inspect the URL and the extracted content.";
    }
    if ((page.url || "").includes("/related/click")) {
        return "Wrapper or redirect-style URL. Review whether this should stay in the crawl.";
    }
    if ((page.text_length ?? 0) < 300) {
        return "Thin page. Check if useful content was omitted or if the page is mostly navigation chrome.";
    }
    return "Review cleaned content, headings, and steps to confirm the useful text survived cleanup.";
}

function buildDocumentHtml(page) {
    const source = (page.clean_markdown || page.raw_markdown || "").trim();
    const plainText = (page.plain_text || page.raw_text || "").trim();
    const bodyHtml = source
        ? renderMarkdownDocument(source, { title: page.title || "" })
        : plainText
            ? renderPlainTextDocument(plainText)
            : `<p class="text-muted">No content available for this page.</p>`;

    return `
        <div class="document-shell">
            <header class="document-header">
                <p class="document-kicker">Cleaned content preview</p>
                <h1 class="document-title">${escapeHtml(page.title || page.url || "Untitled page")}</h1>
                <p class="document-subtitle">
                    Read this as a simplified document view. Headings, bullets, numbered steps, tables, and code blocks are preserved where possible.
                </p>
                <div class="document-meta">
                    <span class="chip ${statusClass(page.status)}">${escapeHtml(page.status || "-")}</span>
                    <span class="chip chip-neutral">Depth ${page.depth ?? "-"}</span>
                    <span class="chip chip-neutral">${formatTextLength((page.plain_text || page.raw_text || "").length)}</span>
                    <span class="chip chip-neutral">${formatConfidence(page.cleanup_confidence, page.cleanup_score)}</span>
                </div>
            </header>
            ${bodyHtml}
        </div>
    `;
}

function renderMarkdownDocument(markdown, options = {}) {
    const lines = markdown.replace(/\r\n/g, "\n").split("\n");
    const html = [];
    let index = 0;
    let ledeRendered = false;
    const normalizedTitle = normalizeComparableText(options.title || "");
    const firstHeading = findFirstHeading(lines);

    while (index < lines.length) {
        const line = lines[index];
        const trimmed = line.trim();

        if (!trimmed) {
            index += 1;
            continue;
        }

        if (trimmed.startsWith("```")) {
            const codeLines = [];
            index += 1;
            while (index < lines.length && !lines[index].trim().startsWith("```")) {
                codeLines.push(lines[index]);
                index += 1;
            }
            index += 1;
            html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
            continue;
        }

        const headingMatch = trimmed.match(/^(#{1,4})\s+(.*)$/);
        if (headingMatch) {
            const level = headingMatch[1].length;
            const headingText = stripMarkdownFormatting(headingMatch[2]);
            if (level === 1 && normalizedTitle && normalizeComparableText(headingText) === normalizedTitle) {
                index += 1;
                continue;
            }
            html.push(`<h${level}>${renderInlineMarkdown(headingMatch[2])}</h${level}>`);
            index += 1;
            continue;
        }

        if (/^---+$/.test(trimmed)) {
            html.push("<hr>");
            index += 1;
            continue;
        }

        if (/^>\s?/.test(trimmed)) {
            const quoteLines = [];
            while (index < lines.length && /^>\s?/.test(lines[index].trim())) {
                quoteLines.push(lines[index].trim().replace(/^>\s?/, ""));
                index += 1;
            }
            html.push(`<blockquote><p>${renderInlineMarkdown(quoteLines.join(" "))}</p></blockquote>`);
            continue;
        }

        if (looksLikeTableDivider(trimmed, lines[index + 1])) {
            const { tableHtml, nextIndex } = consumeTable(lines, index);
            html.push(tableHtml);
            index = nextIndex;
            continue;
        }

        if (isStandaloneMedia(trimmed)) {
            html.push(`<div class="document-omission">Media omitted from preview</div>`);
            index += 1;
            continue;
        }

        if (/^\s*[-*+]\s+\[[ xX]\]\s+/.test(line)) {
            const items = [];
            while (index < lines.length && /^\s*[-*+]\s+\[[ xX]\]\s+/.test(lines[index])) {
                const current = lines[index].replace(/^\s*[-*+]\s+\[([ xX])\]\s+/, "");
                const checked = /\[[xX]\]/.test(lines[index]);
                items.push({ text: current.trim(), checked });
                index += 1;
            }
            html.push(
                `<ul class="task-list">${items.map((item) => `
                    <li>
                        <span class="task-check ${item.checked ? "is-checked" : ""}" aria-hidden="true"></span>
                        <span>${renderInlineMarkdown(item.text)}</span>
                    </li>
                `).join("")}</ul>`
            );
            continue;
        }

        if (/^\s*[-*+]\s+/.test(line)) {
            const items = [];
            while (index < lines.length && /^\s*[-*+]\s+/.test(lines[index])) {
                items.push(lines[index].replace(/^\s*[-*+]\s+/, "").trim());
                index += 1;
            }
            html.push(`<ul>${items.map((item) => `<li>${renderInlineMarkdown(item)}</li>`).join("")}</ul>`);
            continue;
        }

        if (/^\s*\d+[.)]\s+/.test(line)) {
            const items = [];
            while (index < lines.length && /^\s*\d+[.)]\s+/.test(lines[index])) {
                items.push(lines[index].replace(/^\s*\d+[.)]\s+/, "").trim());
                index += 1;
            }
            html.push(`<ol>${items.map((item) => `<li>${renderInlineMarkdown(item)}</li>`).join("")}</ol>`);
            continue;
        }

        const paragraphLines = [];
        while (index < lines.length) {
            const current = lines[index].trim();
            if (
                !current
                || current.startsWith("```")
                || /^(#{1,4})\s+/.test(current)
                || /^>\s?/.test(current)
                || /^\s*[-*+]\s+/.test(lines[index])
                || /^\s*\d+[.)]\s+/.test(lines[index])
                || /^---+$/.test(current)
            ) {
                break;
            }
            paragraphLines.push(current);
            index += 1;
        }

        const paragraphText = paragraphLines.join(" ");
        const paragraphClass = !ledeRendered && shouldUseAsLede(paragraphText, firstHeading)
            ? ' class="lede"'
            : "";
        html.push(`<p${paragraphClass}>${renderInlineMarkdown(paragraphText)}</p>`);
        ledeRendered = true;
    }

    return html.join("");
}

function renderPlainTextDocument(text) {
    const paragraphs = text
        .split(/\n\s*\n/)
        .map((block) => block.trim())
        .filter(Boolean)
        .map((block) => `<p>${escapeHtml(block).replace(/\n/g, "<br>")}</p>`);

    return paragraphs.join("");
}

function buildPageJsonPreview(page, displayUrl) {
    return {
        page_id: page.page_id,
        job_id: page.job_id,
        title: page.title,
        status: page.status,
        page_type: page.page_type,
        url: page.url,
        canonical_url: page.canonical_url,
        display_url: displayUrl,
        parent_page_id: page.parent_page_id,
        depth: page.depth,
        text_length: (page.plain_text || "").length,
        cleanup_score: page.cleanup_score,
        cleanup_confidence: page.cleanup_confidence,
        main_content_selector: page.main_content_selector,
        error_message: page.error_message,
        removed_blocks: page.removed_blocks || [],
        clean_markdown: page.clean_markdown || "",
        raw_markdown: page.raw_markdown || "",
        plain_text: page.plain_text || "",
    };
}

function renderInlineMarkdown(text) {
    let value = escapeHtml(text);
    value = value.replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, '<span class="document-omission">Image omitted</span>');
    value = value.replace(/`([^`]+)`/g, "<code>$1</code>");
    value = value.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    value = value.replace(/\*([^*]+)\*/g, "<em>$1</em>");
    value = value.replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
    value = value.replace(/(^|[\s(])(https?:\/\/[^\s)]+)/g, '$1<a href="$2" target="_blank" rel="noreferrer">$2</a>');
    return value;
}

function findFirstHeading(lines) {
    for (const line of lines) {
        const trimmed = line.trim();
        const match = trimmed.match(/^(#{1,4})\s+(.*)$/);
        if (match) {
            return stripMarkdownFormatting(match[2]);
        }
    }
    return "";
}

function stripMarkdownFormatting(value) {
    return String(value || "")
        .replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, "$1")
        .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, "$1")
        .replace(/[*_`>#-]/g, " ")
        .replace(/\s+/g, " ")
        .trim();
}

function normalizeComparableText(value) {
    return stripMarkdownFormatting(value).toLowerCase();
}

function isStandaloneMedia(line) {
    return /^!\[[^\]]*\]\(([^)\s]+)\)$/.test(line) || /^\[[^\]]*\]\(([^)\s]+\.(png|jpg|jpeg|svg|webp|gif))\)$/i.test(line);
}

function shouldUseAsLede(text, firstHeading) {
    const normalized = normalizeComparableText(text);
    if (!normalized) {
        return false;
    }
    if (firstHeading && normalized === normalizeComparableText(firstHeading)) {
        return false;
    }
    return text.length > 110;
}

function looksLikeTableDivider(line, nextLine) {
    if (!line || !nextLine) {
        return false;
    }
    return line.includes("|") && /^\s*\|?(\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$/.test(nextLine.trim());
}

function consumeTable(lines, startIndex) {
    const headerCells = splitTableRow(lines[startIndex]);
    let index = startIndex + 2;
    const bodyRows = [];

    while (index < lines.length) {
        const trimmed = lines[index].trim();
        if (!trimmed || !trimmed.includes("|")) {
            break;
        }
        bodyRows.push(splitTableRow(lines[index]));
        index += 1;
    }

    const tableHtml = `
        <table>
            <thead>
                <tr>${headerCells.map((cell) => `<th>${renderInlineMarkdown(cell)}</th>`).join("")}</tr>
            </thead>
            <tbody>
                ${bodyRows.map((row) => `
                    <tr>${row.map((cell) => `<td>${renderInlineMarkdown(cell)}</td>`).join("")}</tr>
                `).join("")}
            </tbody>
        </table>
    `;

    return { tableHtml, nextIndex: index };
}

function splitTableRow(line) {
    let trimmed = line.trim();
    if (trimmed.startsWith("|")) {
        trimmed = trimmed.slice(1);
    }
    if (trimmed.endsWith("|")) {
        trimmed = trimmed.slice(0, -1);
    }
    return trimmed.split("|").map((cell) => cell.trim());
}

function sortLabel(sortMode) {
    if (sortMode === "recommended") return "Recommended";
    if (sortMode === "tree") return "Tree order";
    if (sortMode === "shortest") return "Shortest text first";
    if (sortMode === "confidence") return "Lowest cleanup confidence";
    if (sortMode === "title") return "Title A-Z";
    return "Suspicious pages first";
}

function sortDescription(sortMode) {
    if (sortMode === "recommended") {
        return "Recommended starts with successful article-like pages and deprioritizes wrapper URLs, so you review real content first.";
    }
    if (sortMode === "tree") {
        return "Use tree order when you want to review the crawl in the same parent-child sequence users navigate.";
    }
    if (sortMode === "shortest") {
        return "Shortest text first is useful for finding thin pages, failed extraction, or content that was over-pruned.";
    }
    if (sortMode === "confidence") {
        return "Lowest cleanup confidence surfaces pages where the cleaner was least certain about what to keep.";
    }
    if (sortMode === "title") {
        return "Title sorting helps when you want to review one product area or content family alphabetically.";
    }
    return "Suspicious pages first floats failed pages, wrappers, thin pages, and low-confidence cleanup to the top.";
}

function compareNumbers(left, right) {
    return (left ?? 0) - (right ?? 0);
}

function compareTitle(left, right) {
    return String(left.title || left.url || "").localeCompare(String(right.title || right.url || ""));
}

function formatTextLength(value) {
    const length = Number(value || 0);
    if (!length) return "0 chars";
    return `${length.toLocaleString()} chars`;
}

function formatConfidence(confidence, cleanupScore) {
    if (typeof confidence === "number") {
        return `${Math.round(confidence * 100)}% confidence`;
    }
    if (typeof cleanupScore === "number") {
        return `${Math.round(cleanupScore * 100)}% kept`;
    }
    return "No score";
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

function showFatal(message) {
    const subtitle = document.getElementById("preview-subtitle");
    subtitle.textContent = message;
}

function fitFrameWidth(elements, baseWidth, baseHeight) {
    if (!elements.webPreviewStage || elements.webPreviewShell.classList.contains("hidden")) {
        return;
    }

    const availableWidth = Math.max(320, elements.webPreviewStage.clientWidth - 24);
    const scale = Math.min(1, availableWidth / baseWidth);

    elements.webPreviewCanvas.style.height = `${Math.round(baseHeight * scale)}px`;
    elements.pageFrame.style.width = `${baseWidth}px`;
    elements.pageFrame.style.height = `${baseHeight}px`;
    elements.pageFrame.style.transform = `translateX(-50%) scale(${scale})`;
}

function setLinkState(link, href, label) {
    link.textContent = label;
    if (href) {
        link.href = href;
        link.target = "_blank";
        link.rel = "noreferrer";
        link.classList.remove("is-disabled");
        link.removeAttribute("aria-disabled");
    } else {
        link.removeAttribute("href");
        link.removeAttribute("target");
        link.removeAttribute("rel");
        link.classList.add("is-disabled");
        link.setAttribute("aria-disabled", "true");
    }
}

async function resolveDefaultJobId() {
    const payload = await fetchJson("/v1/jobs?limit=25");
    const jobs = payload.jobs || [];
    if (!jobs.length) {
        return null;
    }

    const reviewable = jobs.find((job) =>
        ["done", "cancelled"].includes(job.status)
        && ((job.pages_succeeded || 0) > 0 || (job.pages_discovered || 0) > 0)
    );
    if (reviewable) {
        return reviewable.job_id;
    }

    const terminal = jobs.find((job) => ["done", "cancelled", "failed"].includes(job.status));
    return terminal?.job_id || jobs[0]?.job_id || null;
}

function previewUrlFor(jobId, pageId) {
    const base = `/${encodeURIComponent(jobId)}/preview`;
    if (!pageId) {
        return base;
    }
    return `${base}?page_id=${encodeURIComponent(pageId)}`;
}

function resolveDisplayUrl(page) {
    const currentUrl = page.url || "";
    if (!currentUrl.includes("/related/click")) {
        return currentUrl;
    }

    const content = `${page.clean_markdown || ""}\n${page.raw_markdown || ""}`;
    const candidates = extractUrlsFromText(content);
    const currentHost = hostForUrl(currentUrl);

    const preferred = candidates.find((candidate) => {
        return candidate !== currentUrl
            && !candidate.includes("/related/click")
            && (!currentHost || hostForUrl(candidate) === currentHost)
            && /(\/articles\/|\/sections\/|\/categories\/|\/docs\/|\/guide\/|\/help\/)/.test(pathForUrl(candidate));
    });

    if (preferred) {
        return preferred;
    }

    const sameHost = candidates.find((candidate) => {
        return candidate !== currentUrl
            && !candidate.includes("/related/click")
            && (!currentHost || hostForUrl(candidate) === currentHost);
    });

    return sameHost || currentUrl;
}

function extractUrlsFromText(value) {
    const matches = String(value || "").match(/https?:\/\/[^\s)>"']+/g) || [];
    const seen = new Set();
    return matches.filter((url) => {
        if (seen.has(url)) {
            return false;
        }
        seen.add(url);
        return true;
    });
}

function hostForUrl(url) {
    try {
        return new URL(url).host;
    } catch {
        return "";
    }
}

function pathForUrl(url) {
    try {
        return new URL(url).pathname;
    } catch {
        return "";
    }
}
