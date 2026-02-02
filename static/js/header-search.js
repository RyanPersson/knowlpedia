// Header search functionality using Pagefind
(function() {
  let pagefind = null;
  const searchInput = document.getElementById('header-search-input');
  const searchResults = document.getElementById('header-search-results');

  if (!searchInput || !searchResults) return;

  // Debounce function
  function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  // Load Pagefind
  async function loadPagefind() {
    if (pagefind) return pagefind;
    try {
      pagefind = await import('/pagefind/pagefind.js');
      await pagefind.init();
      return pagefind;
    } catch (err) {
      console.error('Failed to load Pagefind:', err);
      return null;
    }
  }

  // Render results
  function renderResults(results) {
    if (!results || results.length === 0) {
      searchResults.innerHTML = '<li class="search-no-results">No results found</li>';
      searchResults.classList.add('active');
      return;
    }

    // Load result data and render
    Promise.all(results.slice(0, 10).map(r => r.data())).then(items => {
      const html = items.map(item => {
        const excerpt = item.excerpt || '';
        return `<li>
          <a href="${item.url}">
            <div class="search-title">${item.meta?.title || 'Untitled'}</div>
            ${excerpt ? `<div class="search-summary">${excerpt}</div>` : ''}
          </a>
        </li>`;
      }).join('');

      searchResults.innerHTML = html;
      searchResults.classList.add('active');
    });
  }

  // Perform search
  const performSearch = debounce(async function(query) {
    if (!query || query.length < 2) {
      searchResults.classList.remove('active');
      searchResults.innerHTML = '';
      return;
    }

    const pf = await loadPagefind();
    if (!pf) {
      searchResults.innerHTML = '<li class="search-no-results">Search unavailable</li>';
      searchResults.classList.add('active');
      return;
    }

    const search = await pf.search(query);
    renderResults(search.results);
  }, 150);

  // Event listeners
  searchInput.addEventListener('input', (e) => {
    performSearch(e.target.value.trim());
  });

  searchInput.addEventListener('focus', () => {
    loadPagefind();
    if (searchInput.value.trim().length >= 2) {
      performSearch(searchInput.value.trim());
    }
  });

  // Close results when clicking outside
  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.classList.remove('active');
    }
  });

  // Keyboard navigation
  searchInput.addEventListener('keydown', (e) => {
    const items = searchResults.querySelectorAll('li a');
    const activeEl = searchResults.querySelector('.header-search-focus');
    let activeIndex = -1;

    items.forEach((item, i) => {
      if (item.classList.contains('header-search-focus')) activeIndex = i;
    });

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (activeEl) activeEl.classList.remove('header-search-focus');
      const nextIndex = activeIndex + 1 < items.length ? activeIndex + 1 : 0;
      if (items[nextIndex]) items[nextIndex].classList.add('header-search-focus');
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (activeEl) activeEl.classList.remove('header-search-focus');
      const prevIndex = activeIndex - 1 >= 0 ? activeIndex - 1 : items.length - 1;
      if (items[prevIndex]) items[prevIndex].classList.add('header-search-focus');
    } else if (e.key === 'Enter') {
      if (activeEl) {
        e.preventDefault();
        activeEl.click();
      }
    } else if (e.key === 'Escape') {
      searchResults.classList.remove('active');
      searchInput.blur();
    }
  });
})();
