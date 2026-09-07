(function () {
  "use strict";

  const config = window.KNOWLPEDIA_CONFIG;
  if (!config || config.profile !== "development" || !config.features.testingUi) return;

  const paletteKey = "knowl-palette";
  const feedbackTokenKey = "knowl-codex-access-key";
  const palettes = ["current", "original", "washi", "sumi", "aizome"];
  let returnFocus = null;
  let feedbackKnowl = null;
  let feedbackPoll = null;
  let feedbackRequest = 0;

  function storedPalette() {
    try {
      const saved = localStorage.getItem(paletteKey);
      return palettes.includes(saved) ? saved : null;
    } catch (error) {
      return null;
    }
  }

  function effectivePalette() {
    const active = document.documentElement.dataset.palette;
    if (palettes.includes(active)) return active;
    return storedPalette() || "current";
  }

  function applyPalette(palette) {
    const next = palettes.includes(palette) ? palette : "current";
    document.documentElement.dataset.palette = next;
    document.querySelectorAll(".palette-option[data-palette-value]").forEach((button) => {
      const selected = button.dataset.paletteValue === next;
      button.setAttribute("aria-checked", selected ? "true" : "false");
      button.tabIndex = selected ? 0 : -1;
    });
  }

  function choosePalette(palette) {
    const next = palettes.includes(palette) ? palette : "current";
    try {
      localStorage.setItem(paletteKey, next);
    } catch (error) {}
    applyPalette(next);
  }

  function closeTesting(restoreFocus = true) {
    const panel = document.getElementById("testing-panel");
    const trigger = document.getElementById("testing-open");
    if (!panel || panel.hidden) return false;
    panel.hidden = true;
    if (trigger) trigger.setAttribute("aria-expanded", "false");
    if (restoreFocus && returnFocus && returnFocus.focus) returnFocus.focus({ preventScroll: true });
    return true;
  }

  function openTesting() {
    const panel = document.getElementById("testing-panel");
    const trigger = document.getElementById("testing-open");
    if (!panel || !trigger || !panel.hidden) return;
    const searchClose = document.getElementById("search-close");
    const searchDialog = document.getElementById("search-dialog");
    if (searchClose && searchDialog && !searchDialog.hidden) searchClose.click();
    returnFocus = document.activeElement;
    panel.hidden = false;
    trigger.setAttribute("aria-expanded", "true");
    const selected = panel.querySelector('.palette-option[aria-checked="true"]');
    if (selected) selected.focus({ preventScroll: true });
  }

  function toggleTesting() {
    const panel = document.getElementById("testing-panel");
    if (!panel) return;
    if (panel.hidden) openTesting();
    else closeTesting();
  }

  function handlePaletteClick(event) {
    const button = event.target.closest(".palette-option[data-palette-value]");
    if (button) choosePalette(button.dataset.paletteValue);
  }

  function handlePaletteKeydown(event) {
    if (!["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End"].includes(event.key)) return;
    const buttons = Array.from(event.currentTarget.querySelectorAll(".palette-option[data-palette-value]"));
    const current = buttons.indexOf(document.activeElement);
    if (current < 0 || !buttons.length) return;
    event.preventDefault();
    let next = current;
    if (event.key === "Home") next = 0;
    else if (event.key === "End") next = buttons.length - 1;
    else if (event.key === "ArrowLeft" || event.key === "ArrowUp") next = (current - 1 + buttons.length) % buttons.length;
    else next = (current + 1) % buttons.length;
    buttons[next].focus();
    choosePalette(buttons[next].dataset.paletteValue);
  }

  function feedbackDialog() {
    let dialog = document.getElementById("codex-feedback-dialog");
    if (dialog) return dialog;
    dialog = document.createElement("dialog");
    dialog.id = "codex-feedback-dialog";
    dialog.className = "codex-feedback-dialog";
    dialog.setAttribute("aria-labelledby", "codex-feedback-title");
    dialog.innerHTML = `
      <form method="dialog" class="codex-feedback-shell">
        <div class="codex-feedback-heading">
          <div><p class="kind">Development review</p><h2 id="codex-feedback-title">Message Codex</h2></div>
          <button type="submit" class="icon-button" value="cancel" aria-label="Close Codex feedback">&times;</button>
        </div>
        <p class="codex-feedback-context" data-feedback-context></p>
        <a href="/conversation/" target="_blank" rel="noopener" data-conversation-link>Open shared conversation ↗</a>
        <details class="knowl-review-history">
          <summary>Refactor ledger</summary>
          <p>Recorded editorial reviews, latest batch first. These are historical records, not a certification of the current text. Dependency-only reviews concern prerequisite lists.</p>
          <button type="button" data-review-load>Load review history</button>
          <div data-review-results aria-live="polite"></div>
        </details>
        <div class="codex-feedback-intents" role="radiogroup" aria-label="What should Codex do?">
          <label><input type="radio" name="feedback-intent" value="ask" checked><span>Ask</span></label>
          <label><input type="radio" name="feedback-intent" value="flag"><span>Flag issue</span></label>
          <label><input type="radio" name="feedback-intent" value="change"><span>Request change</span></label>
        </div>
        <label class="codex-feedback-message"><span>Your message</span><textarea rows="5" maxlength="8000" required placeholder="What looks wrong, or what should change?"></textarea></label>
        <label class="codex-feedback-access"><span>Access key</span><input type="password" autocomplete="off" spellcheck="false" placeholder="Test server access key"><small>Saved only in this browser.</small></label>
        <p class="codex-feedback-selection" data-feedback-selection hidden></p>
        <div class="codex-feedback-actions">
          <span class="codex-feedback-status" role="status" aria-live="polite"></span>
          <button type="button" class="codex-feedback-send">Send to Codex</button>
        </div>
        <div class="codex-feedback-response" data-feedback-response hidden></div>
      </form>`;
    document.body.appendChild(dialog);
    try {
      dialog.querySelector(".codex-feedback-access input").value = localStorage.getItem(feedbackTokenKey) || "";
    } catch (error) {}
    dialog.querySelector('[aria-label="Close Codex feedback"]').addEventListener("click", (event) => {
      event.preventDefault();
      dialog.close();
    });
    dialog.addEventListener("close", () => {
      feedbackRequest += 1;
      dialog.querySelector(".codex-feedback-send").disabled = false;
      if (feedbackPoll) window.clearTimeout(feedbackPoll);
      feedbackPoll = null;
      if (returnFocus && returnFocus.focus) returnFocus.focus({ preventScroll: true });
    });
    dialog.querySelector("[data-review-load]").addEventListener("click", loadReviewHistory);
    dialog.querySelector(".codex-feedback-send").addEventListener("click", sendFeedback);
    return dialog;
  }

  function selectedTextInside(knowl) {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed || !selection.rangeCount) return "";
    const range = selection.getRangeAt(0);
    if (!knowl.contains(range.commonAncestorContainer)) return "";
    return selection.toString().trim().slice(0, 4000);
  }

  function openFeedback(button) {
    const knowl = button.closest(".knowl-content, .knowl-page");
    if (!knowl) return;
    closeTesting(false);
    returnFocus = button;
    feedbackKnowl = {
      knowlId: knowl.dataset.knowlId || "",
      title: knowl.dataset.knowlTitle || knowl.querySelector(":scope > .page-header h1")?.textContent?.trim() || "",
      selectedText: selectedTextInside(knowl),
    };
    const dialog = feedbackDialog();
    dialog.querySelector("[data-conversation-link]").href = `/conversation/?knowlId=${encodeURIComponent(feedbackKnowl.knowlId)}`;
    dialog.querySelector("[data-feedback-context]").textContent = `${feedbackKnowl.title} · ${feedbackKnowl.knowlId}`;
    const selectionNote = dialog.querySelector("[data-feedback-selection]");
    selectionNote.hidden = !feedbackKnowl.selectedText;
    selectionNote.textContent = feedbackKnowl.selectedText ? `Selected text: “${feedbackKnowl.selectedText}”` : "";
    dialog.querySelector(".codex-feedback-status").textContent = "";
    const response = dialog.querySelector("[data-feedback-response]");
    response.hidden = true;
    response.textContent = "";
    dialog.querySelector(".knowl-review-history").open = false;
    dialog.querySelector("[data-review-results]").replaceChildren();
    dialog.querySelector("[data-review-load]").disabled = false;
    dialog.showModal();
    dialog.querySelector("textarea").focus();
  }

  async function loadReviewHistory() {
    const dialog = feedbackDialog();
    const knowl = feedbackKnowl;
    const results = dialog.querySelector("[data-review-results]");
    const button = dialog.querySelector("[data-review-load]");
    const token = dialog.querySelector(".codex-feedback-access input").value.trim();
    button.disabled = true;
    results.textContent = "Loading review history…";
    try {
      const response = await fetch(`/__knowlpedia/reviews?knowlId=${encodeURIComponent(knowl.knowlId)}`, {
        cache: "no-store", headers: {Authorization: `Bearer ${token}`},
      });
      const history = await response.json();
      if (feedbackKnowl !== knowl || !dialog.open) return;
      if (!response.ok) throw new Error(history.error || "Could not load review history.");
      results.replaceChildren();
      if (!history.entries.length) results.textContent = "No entries for this knowl in the refactor ledger. Separate dependency-review reports may contain additional history.";
      for (const {batch, record} of history.entries) {
        const entry = document.createElement("details");
        const heading = document.createElement("summary");
        heading.textContent = `${(record.outcome || "recorded").replaceAll("_", " ")} · ${record.scope || "unspecified scope"} · ${batch}`;
        entry.append(heading);
        const fields = document.createElement("dl");
        for (const [key, value] of Object.entries(record)) {
          if (["id", "scope", "outcome"].includes(key)) continue;
          const label = document.createElement("dt");
          label.textContent = key.replaceAll("_", " ");
          const body = document.createElement("dd");
          for (const item of Array.isArray(value) ? value : [value]) {
            const line = document.createElement("p");
            if (key === "sources" && typeof item === "string" && /^https?:\/\//i.test(item)) {
              const link = document.createElement("a");
              link.href = item;
              link.textContent = item;
              link.target = "_blank";
              link.rel = "noopener noreferrer";
              line.append(link);
            } else line.textContent = typeof item === "object" ? JSON.stringify(item) : String(item);
            body.append(line);
          }
          fields.append(label, body);
        }
        entry.append(fields);
        results.append(entry);
      }
    } catch (error) {
      if (feedbackKnowl === knowl && dialog.open) results.textContent = error.message;
    } finally {
      if (feedbackKnowl === knowl) button.disabled = false;
    }
  }

  function addFeedbackButtons(root = document) {
    const knowls = [];
    if (root.nodeType === Node.ELEMENT_NODE && root.matches(".knowl-content, .knowl-page")) knowls.push(root);
    if (root.querySelectorAll) knowls.push(...root.querySelectorAll(".knowl-content, .knowl-page"));
    knowls.forEach((knowl) => {
      const controls = knowl.matches(".knowl-page")
        ? knowl.querySelector(":scope > .page-header")
        : knowl.querySelector(":scope > .knowl-controls");
      if (!controls || controls.querySelector(":scope > .codex-feedback-open")) return;
      const button = document.createElement("button");
      const title = knowl.dataset.knowlTitle || knowl.querySelector(":scope > .page-header h1")?.textContent?.trim() || "this knowl";
      button.type = "button";
      button.className = "codex-feedback-open";
      button.title = "Ask Codex about this knowl";
      button.setAttribute("aria-label", `Ask Codex about ${title}`);
      button.innerHTML = '<span aria-hidden="true">✦</span><span>Ask Codex</span>';
      button.addEventListener("click", () => openFeedback(button));
      if (knowl.matches(".knowl-page")) controls.append(button);
      else controls.prepend(button);
    });
  }

  async function pollFeedback(jobId, token, requestId) {
    if (requestId !== feedbackRequest) return;
    const dialog = feedbackDialog();
    const status = dialog.querySelector(".codex-feedback-status");
    const response = dialog.querySelector("[data-feedback-response]");
    try {
      const request = await fetch(`/__knowlpedia/codex/${encodeURIComponent(jobId)}`, {
        cache: "no-store",
        headers: { "Authorization": `Bearer ${token}` },
      });
      const result = await request.json();
      if (requestId !== feedbackRequest || !dialog.open) return;
      if (!request.ok) throw new Error(result.error || "Could not read the Codex response.");
      if (result.status === "queued" || result.status === "running") {
        status.textContent = result.status === "queued" ? "Queued…" : "Codex is working…";
        feedbackPoll = window.setTimeout(() => pollFeedback(jobId, token, requestId), 1200);
        return;
      }
      if (result.status !== "completed") throw new Error(result.error || `Codex stopped with status ${result.status}.`);
      status.textContent = "Codex replied";
      response.textContent = result.response || "Done.";
      response.hidden = false;
    } catch (error) {
      if (requestId !== feedbackRequest || !dialog.open) return;
      status.textContent = "Could not reach Codex";
      response.textContent = error.message;
      response.hidden = false;
    }
  }

  async function sendFeedback() {
    if (!feedbackKnowl) return;
    const dialog = feedbackDialog();
    const message = dialog.querySelector("textarea").value.trim();
    const token = dialog.querySelector(".codex-feedback-access input").value.trim();
    const status = dialog.querySelector(".codex-feedback-status");
    const response = dialog.querySelector("[data-feedback-response]");
    if (!message) {
      status.textContent = "Write a message first.";
      dialog.querySelector("textarea").focus();
      return;
    }
    if (!token) {
      status.textContent = "Enter the test server access key.";
      dialog.querySelector(".codex-feedback-access input").focus();
      return;
    }
    const requestId = ++feedbackRequest;
    if (feedbackPoll) window.clearTimeout(feedbackPoll);
    const button = dialog.querySelector(".codex-feedback-send");
    button.disabled = true;
    response.hidden = true;
    status.textContent = "Sending…";
    try {
      const request = await fetch("/__knowlpedia/codex", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${token}` },
        body: JSON.stringify({
          ...feedbackKnowl,
          intent: dialog.querySelector('input[name="feedback-intent"]:checked').value,
          message,
          url: window.location.href,
        }),
      });
      const result = await request.json();
      if (requestId !== feedbackRequest || !dialog.open) return;
      if (!request.ok) throw new Error(result.error || "The preview server rejected the message.");
      try {
        localStorage.setItem(feedbackTokenKey, token);
      } catch (error) {}
      status.textContent = "Queued…";
      pollFeedback(result.jobId, token, requestId);
    } catch (error) {
      if (requestId !== feedbackRequest || !dialog.open) return;
      status.textContent = "Could not send";
      const serverHint = error instanceof TypeError
        ? " Open the feedback-enabled preview; this server may only serve static pages."
        : "";
      response.textContent = `${error.message}${serverHint}`;
      response.hidden = false;
    } finally {
      if (requestId === feedbackRequest) button.disabled = false;
    }
  }

  function init() {
    applyPalette(effectivePalette());
    const trigger = document.getElementById("testing-open");
    const close = document.getElementById("testing-close");
    const options = document.querySelector(".palette-options");
    const panel = document.getElementById("testing-panel");
    if (trigger) trigger.addEventListener("click", toggleTesting);
    if (close) close.addEventListener("click", () => closeTesting());
    if (options) {
      options.addEventListener("click", handlePaletteClick);
      options.addEventListener("keydown", handlePaletteKeydown);
    }
    if (panel) {
      document.addEventListener("click", (event) => {
        const themeToggle = document.getElementById("theme-toggle");
        if (panel.hidden || panel.contains(event.target) || (trigger && trigger.contains(event.target)) || (themeToggle && themeToggle.contains(event.target))) return;
        closeTesting(false);
      });
    }
    addFeedbackButtons();
    new MutationObserver((mutations) => {
      mutations.forEach((mutation) => mutation.addedNodes.forEach((node) => addFeedbackButtons(node)));
    }).observe(document.body, { childList: true, subtree: true });
  }

  window.KNOWLPEDIA_TESTING = Object.freeze({ close: closeTesting });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
