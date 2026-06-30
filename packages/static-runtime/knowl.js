(function () {
  "use strict";

  const cache = new Map();

  function shouldUseNormalNavigation(event) {
    return event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey;
  }

  function findInsertionPoint(element) {
    let current = element;
    while (current && current.parentElement) {
      const tag = current.parentElement.tagName;
      if (tag === "P" || tag === "LI" || tag === "DIV" || tag === "SECTION") {
        return current.parentElement;
      }
      current = current.parentElement;
    }
    return element;
  }

  function closePanel(panel) {
    const trigger = document.querySelector('[aria-controls="' + panel.id + '"]');
    if (trigger) {
      trigger.setAttribute("aria-expanded", "false");
      trigger.removeAttribute("aria-controls");
    }
    panel.remove();
  }

  async function fetchFragment(url) {
    if (cache.has(url)) return cache.get(url);
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to load " + url);
    const html = await response.text();
    cache.set(url, html);
    return html;
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
    panel.className = "knowl-panel";
    panel.id = "knowl-panel-" + Math.random().toString(36).slice(2);
    panel.setAttribute("role", "region");
    panel.innerHTML = '<div class="loading">Loading...</div>';

    trigger.setAttribute("aria-expanded", "true");
    trigger.setAttribute("aria-controls", panel.id);

    const insertionPoint = findInsertionPoint(trigger);
    insertionPoint.insertAdjacentElement("afterend", panel);

    try {
      panel.innerHTML = await fetchFragment(trigger.dataset.knowl);
      if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([panel]);
      }
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

  document.addEventListener("click", toggleKnowl);
  document.addEventListener("click", handleClose);
  document.addEventListener("click", handleSwitcher);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      document.querySelectorAll(".knowl-panel").forEach(closePanel);
    }
  });
})();

