(function () {
  "use strict";

  const cache = new Map();
  const pending = new Map();
  const preloadQueue = [];
  const observedKnowls = new WeakSet();
  const maxPreloads = 6;
  const themeKey = "knowl-theme";
  let activePreloads = 0;
  let preloadObserver = null;

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

  function closePanel(panel) {
    const trigger = document.querySelector('[aria-controls="' + panel.id + '"]');
    if (trigger) {
      trigger.setAttribute("aria-expanded", "false");
      trigger.removeAttribute("aria-controls");
    }
    panel.remove();
  }

  function normalizeFragment(html) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    const content = doc.querySelector(".knowl-content");
    return content ? content.outerHTML : html;
  }

  function fetchFragment(url) {
    if (cache.has(url)) return cache.get(url);
    if (pending.has(url)) return pending.get(url);

    const request = fetch(url)
      .then((response) => {
        if (!response.ok) throw new Error("Failed to load " + url);
        return response.text();
      })
      .then((html) => {
        const normalized = normalizeFragment(html);
        cache.set(url, normalized);
        return normalized;
      })
      .finally(() => pending.delete(url));

    pending.set(url, request);
    return request;
  }

  function queuePreload(url) {
    if (!url || cache.has(url) || pending.has(url) || preloadQueue.includes(url)) return;
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
        { rootMargin: "600px 0px" }
      );
    }

    knowlTriggers(root).forEach((trigger) => {
      if (observedKnowls.has(trigger)) return;
      observedKnowls.add(trigger);
      preloadObserver.observe(trigger);
    });
  }

  function preloadForDocument() {
    const mode = document.body.dataset.knowlPreload || "eager";
    if (mode === "none") return;
    if (mode === "visible") {
      observeKnowls(document);
      return;
    }
    preloadKnowls(document);
  }

  function loadInlineFragments() {
    document.querySelectorAll("template[data-knowl-fragment]").forEach((template) => {
      const url = template.dataset.knowlFragment;
      if (url && !cache.has(url)) cache.set(url, template.innerHTML.trim());
    });
  }

  function preloadFromInteraction(event) {
    const trigger = event.target.closest("a.knowl[data-knowl]");
    if (trigger) queuePreload(trigger.dataset.knowl);
  }

  function afterPanelRender(panel) {
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([panel]);
    }
    preloadKnowls(panel);
  }

  async function toggleKnowl(event) {
    const trigger = event.target.closest("a.knowl");
    if (!trigger || !trigger.dataset.knowl) return;
    if (shouldUseNormalNavigation(event)) return;

    event.preventDefault();

    const existingId = trigger.getAttribute("aria-controls");
    if (existingId) {
      const existing = document.getElementById(existingId);
      if (existing) closePanel(existing);
      return;
    }

    const panel = document.createElement("div");
    const depth = getKnowlDepth(trigger);
    panel.className = "knowl-panel knowl-depth-" + (depth % 2 === 0 ? "even" : "odd");
    panel.id = "knowl-panel-" + Math.random().toString(36).slice(2);
    panel.setAttribute("role", "region");
    panel.setAttribute("aria-label", "Definition");

    trigger.setAttribute("aria-expanded", "true");
    trigger.setAttribute("aria-controls", panel.id);

    insertPanel(trigger, panel);

    try {
      const cached = cache.get(trigger.dataset.knowl);
      if (cached) {
        panel.innerHTML = cached;
        afterPanelRender(panel);
        return;
      }

      panel.innerHTML = '<div class="loading">Loading...</div>';
      panel.innerHTML = await fetchFragment(trigger.dataset.knowl);
      afterPanelRender(panel);
    } catch (error) {
      panel.innerHTML = '<div class="error">Unable to load knowl. <a href="' + trigger.href + '">Open full page</a>.</div>';
    }
  }

  function handleClose(event) {
    const button = event.target.closest(".knowl-close");
    if (!button) return;
    const panel = button.closest(".knowl-panel");
    if (panel) closePanel(panel);
  }

  function handleSwitcher(event) {
    const button = event.target.closest(".switcher-tab");
    if (!button) return;
    const root = button.closest(".tfae");
    if (!root) return;
    const target = button.dataset.switchTarget;
    root.querySelectorAll(".switcher-tab").forEach((tab) => tab.classList.toggle("active", tab === button));
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
    button.textContent = isDark ? "Light" : "Dark";
  }

  function toggleTheme() {
    const nextTheme = effectiveTheme() === "dark" ? "light" : "dark";
    try {
      localStorage.setItem(themeKey, nextTheme);
    } catch (error) {}
    applyTheme(nextTheme);
  }

  function initTheme() {
    applyTheme(effectiveTheme());
    const button = document.getElementById("theme-toggle");
    if (button) button.addEventListener("click", toggleTheme);

    if (window.matchMedia) {
      const themeQuery = window.matchMedia("(prefers-color-scheme: dark)");
      const handleSystemThemeChange = () => {
        if (!storedTheme()) applyTheme(effectiveTheme());
      };
      if (themeQuery.addEventListener) {
        themeQuery.addEventListener("change", handleSystemThemeChange);
      } else if (themeQuery.addListener) {
        themeQuery.addListener(handleSystemThemeChange);
      }
    }
  }

  function init() {
    loadInlineFragments();
    initTheme();
    preloadForDocument();
  }

  document.addEventListener("mouseover", preloadFromInteraction);
  document.addEventListener("focusin", preloadFromInteraction);
  document.addEventListener("touchstart", preloadFromInteraction, { passive: true });
  document.addEventListener("click", toggleKnowl);
  document.addEventListener("click", handleClose);
  document.addEventListener("click", handleSwitcher);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      document.querySelectorAll(".knowl-panel").forEach(closePanel);
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
