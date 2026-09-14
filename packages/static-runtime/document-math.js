/* Typeset the flowing private document as its mathematics approaches view. */
(function () {
  "use strict";
  function start() {
  const root = document.querySelector(".document-markdown");
  if (!root) return;
  const pending = new Set();
  let running = null;
  let observer;
  const mathSelector = ".math-inline, .math-display";
  const measuredMath = new Map();
  const owners = new WeakMap();

  function updateOverflow(node) {
    const content = measuredMath.get(node);
    if (!content || !node.isConnected) return;
    // Measure the equation itself, not scrollWidth: glyph bearings and
    // pixel rounding can extend the scroll area of a fully visible term.
    let width = content.getBoundingClientRect().width;
    if (content.classList.contains("katex-html")) {
      const range = document.createRange();
      range.selectNodeContents(content);
      width = range.getBoundingClientRect().width;
    }
    const clipped = width > node.getBoundingClientRect().width + 1;
    node.classList.toggle("math-overflow-x", clipped);
    if (!clipped) node.scrollLeft = 0;
  }

  const sizeObserver = "ResizeObserver" in window ? new ResizeObserver((entries) => {
    new Set(entries.map(({ target }) => owners.get(target))).forEach((node) => {
      if (node) updateOverflow(node);
    });
  }) : null;

  function mathNodes(scope) {
    if (scope.nodeType !== Node.ELEMENT_NODE) return [];
    return scope.matches(mathSelector) ? [scope] : Array.from(scope.querySelectorAll(mathSelector));
  }

  function observeMath(scope) {
    mathNodes(scope).forEach((node) => {
      const content = node.querySelector("mjx-math, .katex-html");
      if (!content || measuredMath.has(node)) return;
      measuredMath.set(node, content);
      for (const target of [node, content]) {
        owners.set(target, node);
        sizeObserver?.observe(target);
      }
      updateOverflow(node);
    });
  }

  function forgetMath(scope) {
    mathNodes(scope).forEach((node) => {
      const content = measuredMath.get(node);
      if (!content || node.isConnected) return;
      sizeObserver?.unobserve(node);
      sizeObserver?.unobserve(content);
      measuredMath.delete(node);
    });
  }

  new MutationObserver((records) => {
    records.forEach(({ addedNodes, removedNodes }) => {
      addedNodes.forEach(observeMath);
      removedNodes.forEach(forgetMath);
    });
  }).observe(root, { childList: true, subtree: true });
  observeMath(root);
  const remeasure = () => measuredMath.forEach((_, node) => updateOverflow(node));
  window.addEventListener("resize", remeasure);
  if (document.fonts) {
    document.fonts.ready.then(remeasure);
    document.fonts.addEventListener("loadingdone", remeasure);
  }
  const ready = new Promise((resolve) => {
    function waitForStartup() {
      const startup = window.MathJax?.startup?.promise;
      if (startup && typeof startup.then === "function") resolve(startup);
      else window.setTimeout(waitForStartup, 20);
    }
    waitForStartup();
  });

  function drain() {
    if (running) return running;
    running = ready.then(async () => {
      while (pending.size) {
        const batch = Array.from(pending).slice(0, 60);
        batch.forEach((node) => pending.delete(node));
        const connected = batch.filter((node) => node.isConnected && !node.dataset.mathReady);
        if (!connected.length) continue;
        await window.MathJax.typesetPromise(connected);
        connected.forEach((node) => {
          node.dataset.mathReady = "true";
          observeMath(node);
        });
        await new Promise((resolve) => requestAnimationFrame(resolve));
      }
    }).finally(() => { running = null; });
    return running;
  }

  function enqueue(nodes) {
    nodes.forEach((node) => {
      if (!node.dataset.mathReady) pending.add(node);
      if (observer) observer.unobserve(node);
    });
    return drain();
  }

  const nodes = Array.from(root.querySelectorAll("[data-document-math]"));
  if ("IntersectionObserver" in window) {
    observer = new IntersectionObserver((entries) => {
      enqueue(entries.filter((entry) => entry.isIntersecting).map((entry) => entry.target));
    }, { rootMargin: "1000px 0px" });
    nodes.forEach((node) => observer.observe(node));
  } else {
    enqueue(nodes);
  }
  window.KnowlpediaDocumentMath = { typesetAll: () => enqueue(nodes), ready };
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start, { once: true });
  else start();
}());
