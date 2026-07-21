(function () {
  "use strict";

  const config = window.KNOWLPEDIA_CONFIG;
  if (!config || config.profile !== "development" || !config.features.testingUi) return;

  const paletteKey = "knowl-palette";
  const palettes = ["current", "original", "washi", "sumi", "aizome"];
  let returnFocus = null;

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
  }

  window.KNOWLPEDIA_TESTING = Object.freeze({ close: closeTesting });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
