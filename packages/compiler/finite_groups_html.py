"""Site-native shell for the data-backed finite-group table."""

from __future__ import annotations

from html import escape
from typing import Any, Callable


def render_finite_groups_table(
    html_document: Callable[..., str],
    profile: Any,
    data_url: str = "/indexes/catalog.json",
    asset_version: str = "1",
) -> str:
    body = f'''<main id="main-content" class="fg-shell" data-finite-groups
  data-catalog-url="{escape(data_url, quote=True)}">
  <header class="fg-hero">
    <p class="kind">The finite-group catalogue</p>
    <h1>A table of finite groups</h1>
    <p class="fg-intro">A map of the simple families, the sporadic exceptions, and familiar finite groups.</p>
    <nav class="fg-page-links" aria-label="Finite-group pages">
      <a href="/catalog/finite-groups/">Read the finite-group catalogue</a>
      <a href="/catalog/explorer/">Explore homomorphisms</a>
      <a href="/catalog/">All mathematical objects</a>
    </nav>
    <p id="fg-status" class="fg-status" role="status">Loading the table…</p>
  </header>
  <noscript><p>JavaScript displays the interactive table. You can still <a href="/catalog/finite-groups/">read the finite-group catalogue</a>.</p></noscript>
  <div id="fg-loaded" hidden>
    <section class="fg-controls" aria-label="Table controls">
      <div class="fg-control-top">
        <div class="fg-layout" role="group" aria-label="Table layout">
          <button type="button" id="fg-classification" aria-pressed="true">Classification map</button>
          <button type="button" id="fg-all" aria-pressed="false">All groups</button>
        </div>
        <p id="fg-view-description" class="fg-control-caption"></p>
      </div>
      <div class="fg-filter-row">
        <div class="fg-search-control"><label for="fg-search">Find a group or family</label><input id="fg-search" type="search" placeholder="Name, symbol, family, or exact order…" autocomplete="off" spellcheck="false"></div>
        <div><label for="fg-region">Region</label><select id="fg-region">
          <option value="all">All regions</option><option value="cyclic">Cyclic</option><option value="alternating">Alternating</option>
          <option value="classical">Classical Lie type</option><option value="exceptional">Exceptional Lie type</option>
          <option value="sporadic">Sporadic</option><option value="familiar">Familiar families and examples</option>
        </select></div>
      </div>
      <div class="fg-control-bottom"><p id="fg-results" role="status"></p><button id="fg-reset" type="button" class="fg-text-button" hidden>Clear filters</button></div>
    </section>
    <div id="fg-board"></div>
    <p class="fg-footnote">The arrangement shows mathematical families and relationships, not a periodic law. A family tile stands for every group in its stated parameter range; distinct tiles may have recorded low-dimensional isomorphisms. Use arrow keys to move between tiles and Enter to open a definition card.</p>
  </div>
  <dialog id="fg-detail" class="fg-detail" aria-labelledby="fg-detail-title">
    <div class="fg-detail-toolbar"><span id="fg-detail-position"></span><div>
      <button type="button" id="fg-previous" aria-label="Previous group">←</button><button type="button" id="fg-next" aria-label="Next group">→</button><button type="button" id="fg-close" aria-label="Close group details">×</button>
    </div></div>
    <div id="fg-detail-body"></div>
  </dialog>
</main>'''
    page = html_document(
        "A table of finite groups · Knowlpedia",
        body,
        preload_mode="none",
        profile=profile,
        page_script="finite-groups.js",
    )
    version = escape(str(asset_version), quote=True)
    return page.replace(
        "</head>",
        f'<link rel="stylesheet" href="/assets/finite-groups.css?v={version}">\n</head>',
    ).replace(
        '<script defer src="/assets/finite-groups.js',
        f'<script defer src="/assets/katex.min.js?v={version}"></script>\n  <script defer src="/assets/finite-groups.js',
    )
