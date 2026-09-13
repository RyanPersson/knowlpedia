(function () {
  "use strict";

  const reader = document.querySelector(".document-facsimile");
  if (!reader) return;
  const base = reader.dataset.readerBase;
  const count = Number(reader.dataset.pageCount);
  const slot = reader.querySelector(".document-page-slot");
  const status = reader.querySelector(".document-load-status");
  const input = reader.querySelector(".document-page-number");
  const cache = new Map();
  let page = Number(reader.dataset.pageNumber);
  let pending = null;
  let zoom = 1;
  let view = "image";

  function pageFromUrl(url) {
    if (url.origin !== location.origin || !url.pathname.startsWith(base)) return null;
    const fragment = url.hash.match(/^#page-(\d+)(?:-y-[\d.]+)?$/);
    const path = url.pathname.slice(base.length).match(/^pages\/(\d+)\/?$/);
    const value = fragment ? Number(fragment[1]) : path ? Number(path[1]) : url.pathname === base ? 1 : null;
    return Number.isInteger(value) && value >= 1 && value <= count ? value : null;
  }

  function positionFromUrl(url) {
    const match = url.hash.match(/(?:-y-|^#at-)([\d.]+)$/);
    return match && Number.isFinite(Number(match[1])) ? Number(match[1]) : null;
  }

  function locate(y) {
    const viewport = slot.querySelector(".document-viewport");
    const sheet = slot.querySelector(".document-sheet");
    const height = Number(sheet.querySelector("img").getAttribute("height"));
    viewport.scrollTop = y === null ? 0 : Math.max(0, y / height * sheet.getBoundingClientRect().height - 20);
    if (y !== null) viewport.scrollIntoView({ block: "nearest" });
  }

  function clearConcepts() {
    Array.from(reader.querySelectorAll(".document-knowl-slot > .knowl-panel")).forEach((panel) => {
      const close = panel.querySelector(":scope > .knowl-content > .knowl-controls > .knowl-close");
      if (close) close.click();
      else {
        const trigger = reader.querySelector(`[aria-controls="${panel.id}"]`);
        if (trigger) {
          trigger.setAttribute("aria-expanded", "false");
          trigger.removeAttribute("aria-controls");
        }
        panel.remove();
      }
    });
  }

  function applyView() {
    slot.querySelector(".document-image-view").hidden = view !== "image";
    slot.querySelector(".document-transcript-view").hidden = view !== "text";
    reader.querySelector(".document-zoom-controls").hidden = view !== "image";
    reader.querySelectorAll("[data-document-view]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.documentView === view));
    });
    slot.querySelector(".document-sheet").style.width = `${zoom * 100}%`;
    reader.querySelector(".document-zoom-label").textContent = zoom === 1 ? "Fit width" : `${Math.round(zoom * 100)}%`;
  }

  function updateControls() {
    reader.dataset.pageNumber = String(page);
    input.value = String(page);
    input.setCustomValidity("");
    reader.querySelectorAll(".document-toolbar [data-document-page]").forEach((link, index) => {
      const next = index === 0 ? Math.max(1, page - 1) : Math.min(count, page + 1);
      link.dataset.documentPage = String(next);
      link.href = `${base}pages/${String(next).padStart(3, "0")}/`;
      link.setAttribute("aria-disabled", String(next === page));
    });
    document.title = `${reader.querySelector("h1").textContent} · Page ${page}`;
  }

  async function showPage(number, push = true, y = null) {
    if (!Number.isInteger(number) || number < 1 || number > count) {
      input.setCustomValidity(`Choose a page from 1 to ${count}.`);
      input.reportValidity();
      return;
    }
    if (pending) pending.abort();
    if (number === page) {
      pending = null;
      status.textContent = "";
      updateControls();
      if (y !== null) {
        locate(y);
        if (push) history.pushState({ page }, "", `${base}#page-${page}-y-${y}`);
      }
      return;
    }
    const request = new AbortController();
    pending = request;
    status.textContent = `Loading page ${number}…`;
    try {
      let text = cache.get(number);
      if (!text) {
        const response = await fetch(`${base}pages/${String(number).padStart(3, "0")}/body.html`, { signal: request.signal });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        text = await response.text();
        cache.set(number, text);
      }
      if (pending !== request) return;
      const parsed = new DOMParser().parseFromString(text, "text/html");
      const content = parsed.querySelector(".document-page-content");
      if (!content || Number(content.dataset.pageNumber) !== number) throw new Error("Page content did not match");
      clearConcepts();
      slot.replaceChildren(document.importNode(content, true));
      page = number;
      updateControls();
      applyView();
      locate(y);
      if (push) history.pushState({ page }, "", `${base}#page-${page}${y === null ? "" : `-y-${y}`}`);
      status.textContent = `Page ${page} of ${count}`;
      reader.dispatchEvent(new CustomEvent("knowl:content-updated", { bubbles: true }));
    } catch (error) {
      if (error.name !== "AbortError" && pending === request) {
        status.textContent = `Page ${number} could not be loaded. Use its direct page link or try again.`;
        const fallback = document.createElement("a");
        fallback.href = `${base}pages/${String(number).padStart(3, "0")}/`;
        fallback.textContent = ` Open page ${number}`;
        status.appendChild(fallback);
        input.value = String(page);
      }
    } finally {
      if (pending === request) pending = null;
    }
  }

  reader.addEventListener("click", (event) => {
    const mode = event.target.closest("[data-document-view]");
    if (mode) {
      view = mode.dataset.documentView;
      applyView();
      return;
    }
    const zoomButton = event.target.closest("[data-document-zoom]");
    if (zoomButton) {
      const viewport = slot.querySelector(".document-viewport");
      const left = viewport.scrollLeft / Math.max(1, viewport.scrollWidth);
      const top = viewport.scrollTop / Math.max(1, viewport.scrollHeight);
      zoom = zoomButton.dataset.documentZoom === "reset" ? 1 : Math.min(3, Math.max(1, zoom + Number(zoomButton.dataset.documentZoom) * 0.25));
      applyView();
      viewport.scrollLeft = left * viewport.scrollWidth;
      viewport.scrollTop = top * viewport.scrollHeight;
      return;
    }
    if (event.target.closest(".document-clear-concepts")) {
      clearConcepts();
      return;
    }
    const link = event.target.closest("a[href]");
    if (!link || link.classList.contains("knowl") || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const number = pageFromUrl(new URL(link.href));
    if (number !== null) {
      event.preventDefault();
      showPage(number, true, positionFromUrl(new URL(link.href)));
    }
  });
  input.addEventListener("change", () => showPage(Number(input.value)));
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      showPage(Number(input.value));
    }
  });
  reader.querySelector(".document-bookmarks").addEventListener("change", (event) => {
    if (event.target.value) showPage(Number(event.target.value));
    event.target.value = "";
  });
  function restoreLocation() {
    const url = new URL(location.href);
    showPage(pageFromUrl(url) || 1, false, positionFromUrl(url));
  }
  window.addEventListener("popstate", restoreLocation);
  window.addEventListener("hashchange", restoreLocation);
  updateControls();
  applyView();
  restoreLocation();
})();
