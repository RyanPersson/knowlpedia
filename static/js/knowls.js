/**
 * Knowl System - Inline expandable definitions
 * Fetches HTML fragments and displays them inline below the trigger element.
 */
(function() {
  'use strict';

  const cache = new Map();

  function getKnowlDepth(element) {
    let depth = 0;
    let parent = element.closest('.knowl-panel');
    while (parent) {
      depth++;
      parent = parent.parentElement?.closest('.knowl-panel');
    }
    return depth;
  }

  function findInsertionPoint(element) {
    // Find the nearest block-level parent to insert after
    let current = element;
    while (current && current.parentElement) {
      const parent = current.parentElement;
      const display = window.getComputedStyle(parent).display;
      if (display === 'block' || display === 'flex' || parent.tagName === 'P' || parent.tagName === 'LI') {
        return current;
      }
      current = parent;
    }
    return element;
  }

  function closeKnowl(panel) {
    const trigger = document.querySelector(`[aria-controls="${panel.id}"]`);
    if (trigger) {
      trigger.setAttribute('aria-expanded', 'false');
    }
    panel.remove();
  }

  async function toggleKnowl(event) {
    const trigger = event.target.closest('.knowl');
    if (!trigger) return;

    event.preventDefault();

    const url = trigger.dataset.knowl;
    const existingPanel = trigger.nextElementSibling?.classList.contains('knowl-panel')
      ? trigger.nextElementSibling
      : document.getElementById(trigger.getAttribute('aria-controls'));

    // If already open, close it
    if (existingPanel) {
      closeKnowl(existingPanel);
      return;
    }

    // Create panel
    const panelId = 'knowl-' + Math.random().toString(36).substr(2, 9);
    const depth = getKnowlDepth(trigger);
    const panel = document.createElement('div');
    panel.className = 'knowl-panel knowl-depth-' + (depth % 2 === 0 ? 'even' : 'odd');
    panel.id = panelId;
    panel.setAttribute('role', 'region');
    panel.setAttribute('aria-label', 'Definition');
    panel.innerHTML = '<div class="knowl-loading">Loading...</div>';

    trigger.setAttribute('aria-expanded', 'true');
    trigger.setAttribute('aria-controls', panelId);

    // Insert after the paragraph/block containing the trigger
    const insertAfter = findInsertionPoint(trigger);
    insertAfter.parentNode.insertBefore(panel, insertAfter.nextSibling);

    // Fetch content
    try {
      let html;
      if (cache.has(url)) {
        html = cache.get(url);
      } else {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to load');
        html = await response.text();

        // Extract just the knowl-content div from the response
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const content = doc.querySelector('.knowl-content');
        html = content ? content.outerHTML : html;

        cache.set(url, html);
      }

      panel.innerHTML = html;

      // Add close button handlers (header and footer)
      panel.querySelectorAll('.knowl-close').forEach(btn => {
        btn.addEventListener('click', () => closeKnowl(panel));
      });

    } catch (error) {
      panel.innerHTML = `<div class="knowl-error">Failed to load definition. <a href="${trigger.href}">View full page</a></div>`;
    }
  }

  // Preload a knowl URL
  async function preloadUrl(url) {
    if (cache.has(url)) return;

    try {
      const response = await fetch(url);
      if (!response.ok) return;
      const html = await response.text();

      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const content = doc.querySelector('.knowl-content');
      cache.set(url, content ? content.outerHTML : html);
    } catch (error) {
      // Silently fail - click will retry
    }
  }

  // Preload on hover (desktop)
  function preloadOnHover(event) {
    const trigger = event.target.closest('.knowl');
    if (!trigger) return;
    preloadUrl(trigger.dataset.knowl);
  }

  // Preload when knowls become visible (mobile + desktop)
  function setupVisibilityPreload() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const url = entry.target.dataset.knowl;
          // Preload during idle time to avoid blocking UI
          if ('requestIdleCallback' in window) {
            requestIdleCallback(() => preloadUrl(url));
          } else {
            setTimeout(() => preloadUrl(url), 100);
          }
          observer.unobserve(entry.target); // Only preload once
        }
      });
    }, { rootMargin: '50px' }); // Start preloading slightly before visible

    document.querySelectorAll('.knowl').forEach(el => observer.observe(el));
  }

  // Event delegation
  document.addEventListener('mouseover', preloadOnHover);
  document.addEventListener('click', toggleKnowl);

  // Start visibility preloading when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupVisibilityPreload);
  } else {
    setupVisibilityPreload();
  }

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const openPanels = document.querySelectorAll('.knowl-panel');
      openPanels.forEach(panel => closeKnowl(panel));
    }
  });
})();
