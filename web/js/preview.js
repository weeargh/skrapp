document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);

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
        visibleCount: 20,
        visiblePages: [],
        activeViewMode: "document",
        pollHandle: null,
    };

    const elements = {
        subtitle: document.getElementById("preview-subtitle"),
        statusBadge: document.getElementById("preview-status-badge"),
        total: document.getElementById("summary-pages-total"),
        succeeded: document.getElementById("summary-pages-succeeded"),
        failed: document.getElementById("summary-pages-failed"),
        sortLabel: document.getElementById("summary-sort-label"),
        statusLink: document.getElementById("status-link"),
        openStatusBtn: document.getElementById("open-status-btn"),
        search: document.getElementById("review-search"),
        sort: document.getElementById("sort-mode"),
        sortHelper: document.getElementById("sort-helper"),
        queueCount: document.getElementById("queue-count"),
        queueVisible: document.getElementById("queue-visible"),
        queueEmpty: document.getElementById("queue-empty"),
        reviewList: document.getElementById("review-list"),
        loadMoreBtn: document.getElementById("load-more-btn"),
        previewEmpty: document.getElementById("preview-empty"),
        previewContent: document.getElementById("preview-content"),
        previewPageTitle: document.getElementById("preview-page-title"),
        previewPageUrl: document.getElementById("preview-page-url"),
        previewPageOrigin: document.getElementById("preview-page-origin"),
        previewPageDepth: document.getElementById("preview-page-depth"),
        previewPageLength: document.getElementById("preview-page-length"),
        previewPageConfidence: document.getElementById("preview-page-confidence"),
        prevBtn: document.getElementById("prev-page-btn"),
        nextBtn: document.getElementById("next-page-btn"),
        documentPreview: document.getElementById("document-preview"),
        markdownPreview: document.getElementById("markdown-preview"),
        plainPreview: document.getElementById("plain-preview"),
        viewButtons: Array.from(document.querySelectorAll("[data-view-mode]")),
        viewPanels: Array.from(document.querySelectorAll("[data-view-panel]")),
    };

    elements.search.addEventListener("input", () => {
        state.searchTerm = elements.search.value.trim().toLowerCase();
        state.visibleCount = 20;
        renderQueue();
    });

    elements.sort.addEventListener("change", () => {
        state.sortMode = elements.sort.value;
        state.visibleCount = 20;
        renderQueue();
    });

    elements.loadMoreBtn.addEventListener("click", () => {
        state.visibleCount += 20;
        renderQueue();
    });

    elements.prevBtn.addEventListener("click", () => moveSelection(-1));
    elements.nextBtn.addEventListener("click", () => moveSelection(1));

    elements.viewButtons.forEach((button) => {
        button.addEventListener("click", () => {
            state.activeViewMode = button.dataset.viewMode;
            renderViewMode();
        });
    });

    initialize();

    async function initialize() {
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
            renderQueue();

            if (state.selectedPageId) {
                await selectPage(state.selectedPageId, { preserveUrl: true });
            } else if (state.visiblePages.length > 0) {
                await selectPage(state.visiblePages[0].page_id, { preserveUrl: true });
            }

            if (["done", "cancelled", "failed"].includes(job.status)) {
                stopPolling();
            }
        } catch (error) {
            showFatal(error.message);
            stopPolling();
        }
    }

    function renderJobSummary() {
        const job = state.job;
        elements.subtitle.textContent = job
            ? `${job.start_url} • review cleaned content page by page`
            : "Loading job preview…";
        elements.total.textContent = state.orderedPages.length;
        elements.succeeded.textContent = job?.pages_succeeded || 0;
        elements.failed.textContent = job?.pages_failed || 0;
        elements.sortLabel.textContent = sortLabel(state.sortMode);
        elements.statusBadge.className = `chip ${statusClass(job?.status)}`;
        elements.statusBadge.textContent = job?.status || "unknown";
    }

    function renderQueue() {
        const filtered = getFilteredPages();
        state.visiblePages = filtered;
        const visibleRows = filtered.slice(0, state.visibleCount);

        elements.queueCount.textContent = `${filtered.length} pages`;
        elements.queueVisible.textContent = `Showing ${visibleRows.length} of ${filtered.length}`;
        elements.sortHelper.textContent = sortDescription(state.sortMode);
        elements.queueEmpty.classList.toggle("hidden", filtered.length !== 0);
        elements.loadMoreBtn.classList.toggle("hidden", filtered.length <= state.visibleCount);

        if (!visibleRows.length) {
            elements.reviewList.innerHTML = "";
            if (state.selectedPageId) {
                clearPreview();
            }
            return;
        }

        elements.reviewList.innerHTML = visibleRows.map((page, index) => {
            const rank = index + 1;
            const snippet = pageSnippet(page);
            return `
                <button class="review-item ${page.page_id === state.selectedPageId ? "is-selected" : ""}" type="button" data-page-id="${escapeHtml(page.page_id)}">
                    <div class="review-item-header">
                        <div>
                            <h3 class="review-item-title">${escapeHtml(page.title || page.url || "Untitled page")}</h3>
                            <div class="review-item-url">${escapeHtml(page.url || "")}</div>
                        </div>
                        <span class="review-rank">#${rank}</span>
                    </div>
                    <div class="review-item-meta">
                        <span class="chip ${statusClass(page.status)}">${escapeHtml(page.status || "-")}</span>
                        <span class="chip chip-neutral">Depth ${page.depth ?? "-"}</span>
                        <span class="chip chip-neutral">${formatTextLength(page.text_length)}</span>
                        <span class="chip chip-neutral">${formatConfidence(page.cleanup_confidence, page.cleanup_score)}</span>
                    </div>
                    <p class="review-item-snippet">${escapeHtml(snippet)}</p>
                </button>
            `;
        }).join("");

        elements.reviewList.querySelectorAll(".review-item").forEach((item) => {
            item.addEventListener("click", () => {
                selectPage(item.dataset.pageId);
            });
        });

        if (!filtered.some((page) => page.page_id === state.selectedPageId)) {
            selectPage(filtered[0].page_id, { preserveUrl: false });
        }
    }

    async function selectPage(pageId, options = {}) {
        if (!pageId) {
            clearPreview();
            return;
        }

        try {
            let page = state.pageDetailsById.get(pageId);
            if (!page) {
                page = await fetchJson(`/v1/jobs/${state.jobId}/pages/${pageId}`);
                state.pageDetailsById.set(page.page_id, page);
            }

            state.selectedPageId = page.page_id;
            state.currentPage = page;
            renderSelectedPage(page);
            renderQueueSelection();

            if (!options.preserveUrl) {
                window.history.replaceState({}, "", previewUrlFor(state.jobId, page.page_id));
            }
        } catch (error) {
            showFatal(error.message);
        }
    }

    function renderQueueSelection() {
        elements.reviewList.querySelectorAll(".review-item").forEach((item) => {
            item.classList.toggle("is-selected", item.dataset.pageId === state.selectedPageId);
        });
    }

    function renderSelectedPage(page) {
        elements.previewEmpty.classList.add("hidden");
        elements.previewContent.classList.remove("hidden");

        elements.previewPageTitle.textContent = page.title || page.url || "Untitled page";
        const displayUrl = resolveDisplayUrl(page);
        elements.previewPageUrl.href = displayUrl || "#";
        elements.previewPageUrl.textContent = displayUrl || "Open source";
        if (displayUrl && page.url && displayUrl !== page.url) {
            elements.previewPageOrigin.textContent = `Crawled from wrapper URL: ${page.url}`;
            elements.previewPageOrigin.classList.remove("hidden");
        } else {
            elements.previewPageOrigin.textContent = "";
            elements.previewPageOrigin.classList.add("hidden");
        }
        elements.previewPageDepth.textContent = page.depth ?? "-";
        elements.previewPageLength.textContent = formatTextLength(
            (page.plain_text || page.raw_text || "").length
        );
        elements.previewPageConfidence.textContent = formatConfidence(page.cleanup_confidence, page.cleanup_score);

        const documentHtml = buildDocumentHtml(page);
        elements.documentPreview.innerHTML = documentHtml;
        elements.markdownPreview.textContent = page.clean_markdown || page.raw_markdown || "";
        elements.plainPreview.textContent = page.plain_text || page.raw_text || "";

        renderViewMode();
        updatePrevNextState();
    }

    function clearPreview() {
        state.currentPage = null;
        elements.previewEmpty.classList.remove("hidden");
        elements.previewContent.classList.add("hidden");
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
        const index = state.visiblePages.findIndex((page) => page.page_id === state.selectedPageId);
        elements.prevBtn.disabled = index <= 0;
        elements.nextBtn.disabled = index === -1 || index >= state.visiblePages.length - 1;
    }

    function moveSelection(direction) {
        const index = state.visiblePages.findIndex((page) => page.page_id === state.selectedPageId);
        if (index === -1) {
            return;
        }
        const nextPage = state.visiblePages[index + direction];
        if (!nextPage) {
            return;
        }
        selectPage(nextPage.page_id);
    }

    function getFilteredPages() {
        const pages = [...state.orderedPages];
        const filtered = pages.filter((page) => matchesSearch(page, state.searchTerm));
        filtered.sort((left, right) => comparePages(left, right, state.sortMode));
        return filtered;
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
