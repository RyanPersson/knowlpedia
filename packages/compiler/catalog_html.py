"""The catalogue explorer shell; mathematical records stay in the JSON index."""

from __future__ import annotations

from html import escape
from typing import Callable, Any


def render_catalog_explorer(
    html_document: Callable[..., str],
    profile: Any,
    data_url: str = "/indexes/catalog.json",
    asset_version: str = "1",
) -> str:
    """Use the site's ordinary navigation, theme, search, and public knowl links."""
    body = f'''<main class="page-shell catalog-shell" id="main-content"
  data-catalog-explorer data-catalog-url="{escape(data_url, quote=True)}">
  <header class="catalog-header">
    <h1>Category explorer</h1>
    <p class="page-summary">Explore an object's maps by changing the structure they preserve.</p>
    <nav class="catalog-links" aria-label="Catalogue">
      <a href="/catalog/">Catalogue</a>
      <a id="catalog-finite-link" href="/catalog/finite-groups/table/" hidden>Finite groups</a>
      <a id="catalog-lie-link" href="/catalog/lie-groups/table/" hidden>Lie groups</a>
      <details class="catalog-resources"><summary>More</summary><div>
        <a href="/catalog/relationships/compact-freudenthal-magic-square/">Magic square</a>
        <a href="/catalog/created-knowls/">New knowls</a>
        <a href="{escape(data_url, quote=True)}" download>Download JSON</a>
        <a href="/indexes/catalog.sqlite" download>Download SQLite</a>
        <p id="catalog-counts" class="catalog-muted"></p>
      </div></details>
    </nav>
    <p id="catalog-status" class="catalog-muted" role="status">Loading catalogue…</p>
  </header>
  <noscript><p>The explorer needs JavaScript. You can still <a href="/catalog/">read the catalogue</a>.</p></noscript>
  <div id="catalog-controls" hidden>
    <section class="catalog-panel catalog-query" aria-label="Choose objects and maps">
      <div class="catalog-pair catalog-object-cards" id="catalog-object-cards">
        <article id="catalog-source-card" aria-label="Source object"></article>
        <article id="catalog-target-card" aria-label="Target object"></article>
      </div>
      <div class="catalog-map-controls">
        <div><label for="catalog-operation">Maps</label><select id="catalog-operation">
          <option value="aut">Automorphisms · Aut</option>
          <option value="end">Endomorphisms · End</option>
          <option value="hom">Maps between objects · Hom</option>
        </select></div>
        <div><label for="catalog-category">Category</label><select id="catalog-category"></select></div>
      </div>
      <div class="catalog-pair catalog-view-controls" id="catalog-view-controls" hidden>
        <div id="catalog-source-view-field"><label for="catalog-source-view">Source structure</label><select id="catalog-source-view"></select><div id="catalog-source-view-info" class="catalog-muted"></div></div>
        <div id="catalog-target-view-field"><label for="catalog-target-view">Target structure</label><select id="catalog-target-view"></select><div id="catalog-target-view-info" class="catalog-muted"></div></div>
      </div>
      <div id="catalog-category-info"></div>
    </section>
    <section class="catalog-panel catalog-results" aria-labelledby="catalog-morphisms-title">
      <div class="catalog-section-heading"><h2 id="catalog-morphisms-title">Automorphisms</h2><span id="catalog-coverage" class="catalog-badge"></span></div>
      <p id="catalog-query-label" class="catalog-muted"></p>
      <div id="catalog-morphisms" aria-live="polite"></div>
      <div id="catalog-suggestions"></div>
    </section>
    <section class="catalog-panel" aria-labelledby="catalog-relations-title">
      <div class="catalog-section-heading"><h2 id="catalog-relations-title">Related objects</h2><span id="catalog-relations-status" class="catalog-muted"></span></div>
      <details id="catalog-diagram-details" hidden><summary>Pair diagram</summary>
        <p class="catalog-muted">Solid arrows: maps in the selected category. Dashed arrows: constructions or structural relationships.</p>
        <div id="catalog-diagram"></div>
      </details>
      <div id="catalog-relations"></div>
    </section>
  </div>
  <dialog id="catalog-picker" class="catalog-picker" aria-labelledby="catalog-picker-title">
    <div class="catalog-section-heading"><h2 id="catalog-picker-title">Choose an object</h2><button type="button" id="catalog-picker-close" class="catalog-button">Close</button></div>
    <label for="catalog-picker-search">Search objects</label>
    <input id="catalog-picker-search" type="search" placeholder="Name, notation, or family…" autocomplete="off" autofocus aria-describedby="catalog-picker-count">
    <p id="catalog-picker-count" class="catalog-muted" role="status"></p>
    <div id="catalog-picker-results" class="catalog-picker-results" aria-label="Matching objects"></div>
    <button type="button" id="catalog-picker-more" class="catalog-button" hidden>Show more</button>
  </dialog>
</main>'''
    page = html_document(
        "Category explorer · Knowlpedia",
        body,
        preload_mode="none",
        profile=profile,
        page_script="catalog.js",
    )
    version = escape(str(asset_version), quote=True)
    # KaTeX is already a pinned local site dependency; this page never loads a CDN.
    return page.replace(
        '</head>',
        f'<link rel="stylesheet" href="/assets/catalog.css?v={version}">\n</head>',
    ).replace(
        '<script defer src="/assets/catalog.js',
        f'<script defer src="/assets/katex.min.js?v={version}"></script>\n  <script defer src="/assets/catalog.js',
    )
