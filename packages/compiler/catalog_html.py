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
  <header class="page-header catalog-header">
    <p class="kind">Objects, structures, maps</p>
    <h1>Explore the catalogue</h1>
    <p class="page-summary">Choose mathematical objects, then choose the structure their maps must preserve.</p>
    <nav class="catalog-links" aria-label="Catalogue">
      <a href="/catalog/">Read the catalogue and its definitions</a>
      <a href="/catalog/created-knowls/">All newly created knowls</a>
      <a href="/catalog/relationships/compact-freudenthal-magic-square/">Freudenthal magic square</a>
      <a href="{escape(data_url, quote=True)}" download>JSON data</a>
      <a href="/indexes/catalog.sqlite" download>SQLite data</a>
    </nav>
    <p id="catalog-status" class="catalog-muted" role="status">Loading catalogue…</p>
  </header>
  <noscript><p>The explorer needs JavaScript. You can still <a href="/catalog/">read the catalogue</a> and download the data above.</p></noscript>
  <div id="catalog-controls" hidden>
    <section class="catalog-panel" aria-labelledby="catalog-pair-title">
      <h2 id="catalog-pair-title">Choose objects</h2>
      <div class="catalog-pair">
        <fieldset>
          <legend>Source</legend>
          <label for="catalog-source-search">Find a source object</label>
          <input id="catalog-source-search" type="search" placeholder="Name, family, field, or object ID" autocomplete="off" aria-describedby="catalog-source-matches">
          <p id="catalog-source-matches" class="catalog-match-count"></p>
          <label for="catalog-source">Source object</label>
          <select id="catalog-source"></select>
        </fieldset>
        <fieldset>
          <legend>Target</legend>
          <label for="catalog-target-search">Find a target object</label>
          <input id="catalog-target-search" type="search" placeholder="Name, family, field, or object ID" autocomplete="off" aria-describedby="catalog-target-matches catalog-end-note">
          <p id="catalog-target-matches" class="catalog-match-count"></p>
          <label for="catalog-target">Target object</label>
          <select id="catalog-target"></select>
        </fieldset>
      </div>
      <div class="catalog-map-controls">
        <div><label for="catalog-operation">Collection of maps</label><select id="catalog-operation">
          <option value="hom">Hom — homomorphisms</option>
          <option value="end">End — endomorphisms</option>
          <option value="aut">Aut — automorphisms</option>
        </select></div>
        <div><label for="catalog-category">Common category</label><select id="catalog-category"></select></div>
      </div>
      <p id="catalog-end-note" class="catalog-muted" hidden>End and Aut use the same object with the same structure at both endpoints.</p>
      <div class="catalog-pair catalog-view-controls">
        <div><label for="catalog-source-view">Source structure</label><select id="catalog-source-view"></select><div id="catalog-source-view-info" class="catalog-muted"></div></div>
        <div><label for="catalog-target-view">Target structure</label><select id="catalog-target-view"></select><div id="catalog-target-view-info" class="catalog-muted"></div></div>
      </div>
      <div id="catalog-category-info"></div>
    </section>
    <div class="catalog-pair catalog-object-cards">
      <article id="catalog-source-card" class="catalog-panel" aria-label="Source object details"></article>
      <article id="catalog-target-card" class="catalog-panel" aria-label="Target object details"></article>
    </div>
    <section class="catalog-panel" aria-labelledby="catalog-morphisms-title">
      <div class="catalog-section-heading"><h2 id="catalog-morphisms-title">Recorded collections of maps</h2><span id="catalog-coverage" class="catalog-badge"></span></div>
      <p id="catalog-query-label" class="catalog-muted"></p>
      <div id="catalog-morphisms" aria-live="polite"></div>
    </section>
    <section class="catalog-panel" aria-labelledby="catalog-relations-title">
      <h2 id="catalog-relations-title">Recorded relationships</h2>
      <p class="catalog-muted">Solid arrows are recorded maps in the selected category. Dashed arrows are constructions or structural relationships. Conditions and evidence appear below; an arrow is not a new proof.</p>
      <div id="catalog-diagram"></div>
      <p id="catalog-relations-status" class="catalog-muted"></p>
      <div id="catalog-relations"></div>
    </section>
  </div>
</main>'''
    page = html_document(
        "Object catalogue explorer · Knowlpedia",
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
