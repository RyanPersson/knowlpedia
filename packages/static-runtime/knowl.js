(function () {
  "use strict";

  const fragmentCache = new Map();
  const pending = new Map();
  const preloadQueue = [];
  const observedKnowls = new WeakSet();
  const themeKey = "knowl-theme";
  const maxPreloads = 6;
  let activePreloads = 0;
  let preloadObserver = null;
  const pendingObservationRoots = new Set();
  let observationTask = null;
  let searchData = null;
  let searchRequest = null;
  let searchReturnFocus = null;

  function shouldUseNormalNavigation(event) {
    return event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey;
  }

  function getKnowlDepth(element) {
    let depth = 0;
    let parent = element.closest(".knowl-panel");
    while (parent) {
      depth += 1;
      parent = parent.parentElement && parent.parentElement.closest(".knowl-panel");
    }
    return depth;
  }

  function findInsertionPoint(trigger) {
    const boundary = trigger.closest(".knowl-panel");
    let current = trigger;
    while (current && current.parentElement) {
      const parent = current.parentElement;
      if (boundary && !boundary.contains(parent)) break;
      if (parent.classList.contains("knowl-body")) return current;
      const display = window.getComputedStyle(parent).display;
      if (parent.tagName === "P" || parent.tagName === "LI" || display === "block" || display === "flex") {
        return current;
      }
      current = parent;
    }
    return current || trigger;
  }

  function insertPanel(trigger, panel) {
    if (trigger.classList.contains("index-knowl")) {
      const indexItem = trigger.closest(".index-item");
      if (indexItem) {
        indexItem.appendChild(panel);
        return;
      }
    }
    const insertAfter = findInsertionPoint(trigger);
    insertAfter.parentNode.insertBefore(panel, insertAfter.nextSibling);
  }

  function closePanel(panel, restoreFocus) {
    const trigger = panel._knowlTrigger || document.querySelector('[aria-controls="' + panel.id + '"]');
    if (trigger) {
      trigger.setAttribute("aria-expanded", "false");
      trigger.removeAttribute("aria-controls");
    }
    panel.remove();
    if (restoreFocus && trigger) trigger.focus({ preventScroll: true });
  }

  function normalizeFragment(fragmentHtml) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(fragmentHtml, "text/html");
    const content = doc.querySelector(".knowl-content");
    return content ? content.outerHTML : fragmentHtml;
  }

  function fetchFragment(url) {
    if (fragmentCache.has(url)) return Promise.resolve(fragmentCache.get(url));
    if (pending.has(url)) return pending.get(url);
    const request = fetch(url)
      .then((response) => {
        if (!response.ok) throw new Error("Failed to load " + url);
        return response.text();
      })
      .then((value) => {
        const normalized = normalizeFragment(value);
        fragmentCache.set(url, normalized);
        return normalized;
      })
      .finally(() => pending.delete(url));
    pending.set(url, request);
    return request;
  }

  function queuePreload(url) {
    if (!url || fragmentCache.has(url) || pending.has(url) || preloadQueue.includes(url)) return;
    preloadQueue.push(url);
    runPreloadQueue();
  }

  function runPreloadQueue() {
    while (activePreloads < maxPreloads && preloadQueue.length) {
      const url = preloadQueue.shift();
      activePreloads += 1;
      fetchFragment(url)
        .catch(() => {})
        .finally(() => {
          activePreloads -= 1;
          runPreloadQueue();
        });
    }
  }

  function knowlTriggers(root) {
    return Array.from(root.querySelectorAll("a.knowl[data-knowl]"));
  }

  function preloadKnowls(root) {
    knowlTriggers(root).forEach((trigger) => queuePreload(trigger.dataset.knowl));
  }

  function observeKnowls(root) {
    if (!("IntersectionObserver" in window)) {
      preloadKnowls(root);
      return;
    }
    if (!preloadObserver) {
      preloadObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            queuePreload(entry.target.dataset.knowl);
            preloadObserver.unobserve(entry.target);
          });
        },
        { rootMargin: "500px 0px" }
      );
    }
    knowlTriggers(root).forEach((trigger) => {
      if (observedKnowls.has(trigger)) return;
      observedKnowls.add(trigger);
      preloadObserver.observe(trigger);
    });
  }

  function scheduleObserveKnowls(root) {
    pendingObservationRoots.add(root);
    if (observationTask !== null) return;

    const flush = () => {
      observationTask = null;
      const roots = Array.from(pendingObservationRoots);
      pendingObservationRoots.clear();
      roots.forEach((pendingRoot) => {
        if (pendingRoot === document || pendingRoot.isConnected) observeKnowls(pendingRoot);
      });
    };

    if ("requestIdleCallback" in window) {
      observationTask = window.requestIdleCallback(flush, { timeout: 500 });
    } else {
      observationTask = window.setTimeout(flush, 50);
    }
  }

  function loadInlineFragments() {
    document.querySelectorAll("template[data-knowl-fragment]").forEach((template) => {
      const url = template.dataset.knowlFragment;
      if (url && !fragmentCache.has(url)) fragmentCache.set(url, template.innerHTML.trim());
    });
  }

  function preloadForDocument() {
    const mode = document.body.dataset.knowlPreload || "eager";
    if (mode === "none") return;
    if (mode === "visible") observeKnowls(document);
    else preloadKnowls(document);
  }

  function preloadFromInteraction(event) {
    const trigger = event.target.closest("a.knowl[data-knowl]");
    if (trigger) queuePreload(trigger.dataset.knowl);
  }

  function typeset(root) {
    if (window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise([root]);
  }

  function afterPanelRender(panel, trigger, keyboardOpen) {
    const content = panel.querySelector(".knowl-content");
    const title = content?.dataset.knowlTitle || "Expanded concept";
    const kind = content?.dataset.knowlKind;
    panel.setAttribute("aria-label", kind ? kind + ": " + title : title);
    typeset(panel);
    scheduleObserveKnowls(panel);
    if (keyboardOpen) {
      const close = panel.querySelector(".knowl-close");
      if (close) close.focus({ preventScroll: true });
    }
    panel._knowlTrigger = trigger;
  }

  async function toggleKnowl(event) {
    const trigger = event.target.closest("a.knowl[data-knowl]");
    if (!trigger || shouldUseNormalNavigation(event)) return;
    event.preventDefault();
    const existingId = trigger.getAttribute("aria-controls");
    if (existingId) {
      const existing = document.getElementById(existingId);
      if (existing) closePanel(existing, false);
      return;
    }

    const panel = document.createElement("aside");
    const depth = getKnowlDepth(trigger);
    panel.className = "knowl-panel knowl-depth-" + (depth % 2 === 0 ? "even" : "odd");
    panel.id = "knowl-panel-" + Math.random().toString(36).slice(2);
    panel.setAttribute("role", "region");
    panel.setAttribute("aria-label", "Loading definition");
    trigger.setAttribute("aria-expanded", "true");
    trigger.setAttribute("aria-controls", panel.id);
    insertPanel(trigger, panel);

    try {
      const cached = fragmentCache.get(trigger.dataset.knowl);
      if (cached) panel.innerHTML = cached;
      else {
        panel.innerHTML = '<div class="loading" role="status">Loading definition…</div>';
        panel.innerHTML = await fetchFragment(trigger.dataset.knowl);
      }
      afterPanelRender(panel, trigger, event.isTrusted && event.detail === 0);
    } catch (error) {
      panel.innerHTML = '<div class="error">This definition could not be loaded. <a href="' + trigger.href + '">Open its full page</a>.</div>';
    }
  }

  function handleClose(event) {
    const button = event.target.closest(".knowl-close");
    if (!button) return;
    const panel = button.closest(".knowl-panel");
    if (panel) closePanel(panel, true);
  }

  async function handleSectionChip(event) {
    const button = event.target.closest(".section-chip");
    if (!button) return;
    const content = button.closest(".knowl-content");
    if (!content) return;
    const slot = content.querySelector(":scope > .knowl-section-slot");
    if (!slot) return;
    const active = Array.from(slot.children).find(
      (section) => section.dataset.sectionPanel === button.dataset.sectionId
    );
    content.querySelectorAll(".section-chip").forEach((chip) => chip.setAttribute("aria-expanded", "false"));
    if (active) {
      active.remove();
      return;
    }
    slot.replaceChildren();
    button.setAttribute("aria-expanded", "true");
    const section = document.createElement("section");
    section.className = "knowl-inline-section";
    section.dataset.sectionPanel = button.dataset.sectionId;
    section.setAttribute("aria-label", button.textContent.trim());
    section.innerHTML = '<div class="loading" role="status">Loading section…</div>';
    slot.appendChild(section);
    try {
      section.innerHTML = await fetchFragment(button.dataset.sectionUrl);
      typeset(section);
      scheduleObserveKnowls(section);
    } catch (error) {
      section.innerHTML = '<p class="error">This section could not be loaded.</p>';
    }
  }

  function handleSwitcher(event) {
    const button = event.target.closest(".switcher-tab");
    if (!button) return;
    const root = button.closest(".tfae");
    if (!root) return;
    const target = button.dataset.switchTarget;
    root.querySelectorAll(".switcher-tab").forEach((tab) => {
      const selected = tab === button;
      tab.classList.toggle("active", selected);
      tab.setAttribute("aria-selected", selected ? "true" : "false");
      tab.tabIndex = selected ? 0 : -1;
    });
    root.querySelectorAll("[data-switch-panel]").forEach((panel) => {
      panel.hidden = panel.dataset.switchPanel !== target;
    });
  }

  function storedTheme() {
    try {
      return localStorage.getItem(themeKey);
    } catch (error) {
      return null;
    }
  }

  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function effectiveTheme() {
    const saved = storedTheme();
    if (saved === "dark" || saved === "light") return saved;
    return systemPrefersDark() ? "dark" : "light";
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    const button = document.getElementById("theme-toggle");
    if (!button) return;
    const isDark = theme === "dark";
    button.setAttribute("aria-pressed", isDark ? "true" : "false");
    button.setAttribute("aria-label", isDark ? "Use light theme" : "Use dark theme");
    const label = button.querySelector(".theme-label");
    if (label) label.textContent = isDark ? "Light" : "Dark";
  }

  function toggleTheme() {
    const nextTheme = effectiveTheme() === "dark" ? "light" : "dark";
    try {
      localStorage.setItem(themeKey, nextTheme);
    } catch (error) {}
    applyTheme(nextTheme);
  }

  function normalizeSearchText(value) {
    return value.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
  }

  function ensureSearchData() {
    if (searchData) return Promise.resolve(searchData);
    if (searchRequest) return searchRequest;
    searchRequest = fetch("/indexes/search.json")
      .then((response) => {
        if (!response.ok) throw new Error("Search index unavailable");
        return response.json();
      })
      .then((items) => {
        searchData = items.map((item) => ({
          ...item,
          _title: normalizeSearchText(item.title),
          _aliases: normalizeSearchText((item.aliases || []).join(" ")),
          _summary: normalizeSearchText(item.summary || ""),
          _id: normalizeSearchText(item.id)
        }));
        return searchData;
      });
    return searchRequest;
  }

  function searchScore(item, query, tokens) {
    let score = 0;
    if (item._title === query) score += 1000;
    else if (item._title.startsWith(query)) score += 600;
    else if (item._title.includes(query)) score += 350;
    if (item._aliases.includes(query)) score += 260;
    if (item._id.includes(query)) score += 120;
    tokens.forEach((token) => {
      if (item._title.includes(token)) score += 100;
      if (item._aliases.includes(token)) score += 55;
      if (item._summary.includes(token)) score += 20;
    });
    return score;
  }

  function renderSearchResults(queryValue) {
    const results = document.getElementById("search-results");
    const status = document.getElementById("search-status");
    if (!results || !status || !searchData) return;
    const query = normalizeSearchText(queryValue.trim());
    results.replaceChildren();
    if (!query) {
      status.textContent = "Start typing to search the mathematical index.";
      return;
    }
    const tokens = query.split(/\s+/).filter(Boolean);
    const matches = searchData
      .map((item) => ({ item, score: searchScore(item, query, tokens) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title))
      .slice(0, 12);
    status.textContent = matches.length ? `${matches.length} best matches` : "No matching concepts found.";
    matches.forEach(({ item }) => {
      const row = document.createElement("li");
      row.setAttribute("role", "none");
      const link = document.createElement("a");
      link.className = "search-result";
      link.href = item.href;
      link.setAttribute("role", "option");
      const title = document.createElement("strong");
      title.textContent = item.title;
      const meta = document.createElement("span");
      meta.className = "search-result-meta";
      meta.textContent = item.kind + " · " + item.id.split("/", 1)[0].replaceAll("-", " ");
      if (item.visibility === "development") {
        const badge = document.createElement("span");
        badge.className = "testing-badge";
        badge.textContent = "Testing";
        meta.append(" · ", badge);
      }
      const summary = document.createElement("span");
      summary.className = "search-result-summary";
      summary.textContent = item.summary;
      link.append(title, meta, summary);
      row.appendChild(link);
      results.appendChild(row);
    });
  }

  async function openSearch() {
    const dialog = document.getElementById("search-dialog");
    const input = document.getElementById("search-input");
    const status = document.getElementById("search-status");
    if (!dialog || !input || !dialog.hidden) return;
    if (window.KNOWLPEDIA_TESTING) window.KNOWLPEDIA_TESTING.close(false);
    searchReturnFocus = document.activeElement;
    dialog.hidden = false;
    document.body.classList.add("search-open");
    input.focus();
    try {
      await ensureSearchData();
      renderSearchResults(input.value);
    } catch (error) {
      if (status) status.textContent = "Search is unavailable. You can still browse by area.";
    }
  }

  function closeSearch() {
    const dialog = document.getElementById("search-dialog");
    if (!dialog || dialog.hidden) return false;
    dialog.hidden = true;
    document.body.classList.remove("search-open");
    if (searchReturnFocus && searchReturnFocus.focus) searchReturnFocus.focus({ preventScroll: true });
    return true;
  }

  function handleSearchKeydown(event) {
    const dialog = document.getElementById("search-dialog");
    if (!dialog || dialog.hidden || event.key !== "Tab") return;
    const focusable = Array.from(dialog.querySelectorAll('button, input, a[href]')).filter((item) => !item.hidden);
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function initTheme() {
    applyTheme(effectiveTheme());
    const button = document.getElementById("theme-toggle");
    if (button) button.addEventListener("click", toggleTheme);
    if (window.matchMedia) {
      const query = window.matchMedia("(prefers-color-scheme: dark)");
      const update = () => { if (!storedTheme()) applyTheme(effectiveTheme()); };
      if (query.addEventListener) query.addEventListener("change", update);
      else if (query.addListener) query.addListener(update);
    }
  }

  function initSearch() {
    document.querySelectorAll("#search-open, [data-open-search]").forEach((button) => button.addEventListener("click", openSearch));
    const close = document.getElementById("search-close");
    const input = document.getElementById("search-input");
    const dialog = document.getElementById("search-dialog");
    if (close) close.addEventListener("click", closeSearch);
    if (input) input.addEventListener("input", () => renderSearchResults(input.value));
    if (dialog) dialog.addEventListener("keydown", handleSearchKeydown);
  }

  function init() {
    loadInlineFragments();
    initTheme();
    initSearch();
    preloadForDocument();
    window.setTimeout(autoExpandKnowls, 0);
  }

  function autoExpandKnowls() {
    const root = document.querySelector('.knowl-page[data-knowls-open="true"]');
    if (!root) return;
    const triggers = knowlTriggers(root);
    root.dataset.knowlsOpenCount = String(triggers.length);
    triggers.forEach((trigger) => {
      if (trigger.getAttribute("aria-expanded") !== "true") trigger.click();
    });
  }

  document.addEventListener("mouseover", preloadFromInteraction);
  document.addEventListener("focusin", preloadFromInteraction);
  document.addEventListener("touchstart", preloadFromInteraction, { passive: true });
  document.addEventListener("click", toggleKnowl);
  document.addEventListener("click", handleClose);
  document.addEventListener("click", handleSectionChip);
  document.addEventListener("click", handleSwitcher);
  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openSearch();
      return;
    }
    if (event.key === "/" && !event.metaKey && !event.ctrlKey && !event.altKey && !event.target.matches("input, textarea, [contenteditable]")) {
      event.preventDefault();
      openSearch();
      return;
    }
    if (event.key === "Escape") {
      if (closeSearch()) return;
      if (window.KNOWLPEDIA_TESTING && window.KNOWLPEDIA_TESTING.close()) return;
      const panels = document.querySelectorAll(".knowl-panel");
      if (panels.length) closePanel(panels[panels.length - 1], true);
    }
  });

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
