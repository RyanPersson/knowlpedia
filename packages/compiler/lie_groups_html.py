"""Site-native shell for the data-backed Lie-group table."""

from __future__ import annotations

from html import escape
from typing import Any, Callable


def render_lie_groups_table(
    html_document: Callable[..., str],
    profile: Any,
    data_url: str = "/indexes/catalog.json",
    asset_version: str = "1",
) -> str:
    body = f'''<main id="main-content" class="lg-shell" data-lie-groups
  data-catalog-url="{escape(data_url, quote=True)}">
  <header class="lg-hero">
    <p class="kind">The Lie-group catalogue</p>
    <h1>A table of Lie groups</h1>
    <p class="lg-intro">Compare compact, split-real, and complex forms.</p>
    <nav class="lg-page-links" aria-label="Lie-group pages">
      <a href="/catalog/lie-groups-table-guide/">How to read the table</a>
      <a href="/catalog/lie-groups-index/">Definitions</a>
      <a href="/catalog/finite-groups/table/">Finite-group table</a>
    </nav>
    <p id="lg-status" class="lg-status" role="status">Loading the table…</p>
  </header>
  <noscript><p>JavaScript displays this interactive table. You can still <a href="/catalog/lie-groups-index/">read the Lie-group catalogue</a>.</p></noscript>
  <div id="lg-loaded" hidden>
    <section class="lg-controls" aria-label="Table controls">
      <div class="lg-control-top">
        <div class="lg-layout" role="group" aria-label="Table layout">
          <button type="button" id="lg-classification" aria-pressed="true">Dynkin table</button>
          <button type="button" id="lg-all" aria-pressed="false">All groups</button>
        </div>
        <p id="lg-view-description" class="lg-control-caption"></p>
      </div>
      <div class="lg-search-row">
        <label class="lg-search-control" for="lg-search">Find a group or family<input id="lg-search" type="search" placeholder="Name, symbol, type, or construction…" autocomplete="off" spellcheck="false"></label>
        <details id="lg-filters" class="lg-filters"><summary>Filters <span id="lg-filter-count"></span></summary>
          <div class="lg-filter-grid">
            <label for="lg-section">Group family<select id="lg-section"><option value="all">All families</option><option value="classical">Classical</option><option value="exceptional">Exceptional</option><option value="abelian">Abelian</option><option value="nilpotent">Nilpotent</option><option value="geometric">Geometric</option><option value="product">Products</option></select></label>
            <label for="lg-field">Lie-group field<select id="lg-field"><option value="all">Real and complex</option><option value="real">Real only</option><option value="complex">Complex structure</option></select></label>
            <label for="lg-compact">Compactness<select id="lg-compact"><option value="all">All compactness values</option><option value="yes">Compact</option><option value="no">Noncompact</option><option value="parameter">Parameter-dependent</option><option value="unknown">Not recorded</option></select></label>
            <label for="lg-family">Named family<select id="lg-family"><option value="all">Every named family</option></select></label>
          </div>
        </details>
      </div>
      <div class="lg-control-bottom"><p id="lg-results" role="status"></p><button id="lg-reset" type="button" class="lg-text-button" hidden>Clear filters</button></div>
    </section>
    <p id="lg-scope" class="lg-scope">Selected global groups, not all real forms. Dimensions are real except in the complex column.</p>
    <div class="lg-mobile-series"><label for="lg-series">Dynkin series</label><select id="lg-series"></select><span id="lg-series-position"></span></div>
    <div id="lg-board"></div>
    <nav id="lg-pagination" class="lg-pagination" aria-label="Catalogue pages" hidden><button id="lg-page-previous" type="button">← Previous</button><span id="lg-page-label" role="status"></span><button id="lg-page-next" type="button">Next →</button></nav>
    <p class="lg-footnote">A family tile includes its stated parameters. Equal Lie algebras do not identify global groups. Open a tile for global forms, low-rank coincidences, and recorded covering or quotient maps. Arrow keys move between tiles; Enter opens details.</p>
  </div>
  <dialog id="lg-detail" class="lg-detail" aria-labelledby="lg-detail-title">
    <div class="lg-detail-toolbar"><span id="lg-detail-position"></span><div>
      <button type="button" id="lg-previous" aria-label="Previous group">←</button><button type="button" id="lg-next" aria-label="Next group">→</button><button type="button" id="lg-close" aria-label="Close group details">×</button>
    </div></div>
    <div id="lg-detail-body"></div>
  </dialog>
</main>'''
    page = html_document(
        "A table of Lie groups · Knowlpedia", body,
        preload_mode="none", profile=profile, page_script="lie-groups.js",
    )
    version = escape(str(asset_version), quote=True)
    return page.replace(
        "</head>", f'<link rel="stylesheet" href="/assets/lie-groups.css?v={version}">\n</head>',
    ).replace(
        '<script defer src="/assets/lie-groups.js',
        f'<script defer src="/assets/katex.min.js?v={version}"></script>\n  <script defer src="/assets/lie-groups.js',
    )
