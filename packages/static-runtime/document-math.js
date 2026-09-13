/* Typeset the flowing private document as its mathematics approaches view. */
(function () {
  "use strict";
  function start() {
  const root = document.querySelector(".document-markdown");
  if (!root) return;
  const pending = new Set();
  let running = null;
  let observer;
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
        connected.forEach((node) => { node.dataset.mathReady = "true"; });
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
