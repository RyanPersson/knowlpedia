# Finite-group catalogue and visual table

This follow-up stays on `catalog`, starting from application `f8f46ba` and
content `8ce039be`. Both worktrees were clean. It adds finite-group objects,
knowls and relationships plus a visual table within the existing Knowlpedia
application. The existing Tailscale preview on port 8015 will be reused.

## Mathematical and visual scope

Use finite simple groups as the primary classification: prime-order cyclic,
alternating, six classical Lie-type families, ten exceptional Lie-type families,
and 26 sporadic groups. Display the Tits group distinctly at the exceptional
Lie-type boundary; never count it as a 27th sporadic group. Add familiar finite
group families and small examples in a separate view. This is a map of simple
group classification, not a classification of all finite groups by their
composition factors.

Try classification blocks, sporadic grouping, and order-based browsing. Retain
views only when they make mathematical structure clearer. A tile is explicitly
an individual group or a constrained family, not an invented atomic number.

## Shared authoring contract

Canonical shards are `content/catalog/data/finite-sporadic.json`,
`finite-lie-type.json`, and `finite-elementary.json`. Retain schema_version 1
and the existing objects/categories/views/relationships/morphism_spaces model.
New IDs begin `fg-`. All finite-group records declare sets, groups, finite-groups;
finite simple records additionally declare finite-simple-groups. Add
abelian-groups only when true under all stated conditions. Dimensions may be an
empty dictionary; finite order is not vector-space dimension.

Object properties carry a `finite_group` dictionary:

- `table_role`: simple-family, sporadic, tits, family, or example.
- `section`: cyclic, alternating, classical, exceptional, sporadic, or familiar.
- `order_tex`: nonempty LaTeX formula, without delimiters.
- `order_decimal`: exact positive decimal string for a fixed known order,
  otherwise null. Never store huge orders as floating-point numbers.
- `simple`: true, false, or null when parameter-dependent.
- `simple_condition`: a precise nonempty sentence about simplicity.
- `parameter_summary`: a nonempty concise string (use a fixed-object statement
  for individual groups).
- `construction_summary`: a nonempty concise explanation of the object.
- optional `sporadic_cluster`: mathieu, leech, monster, or pariah, using the
  ATLAS v3 display grouping. This grouping does not assert direct containment.
- optional `order_factors`: list of [prime, positive exponent] integer pairs.
- optional `rank_label`: readable rank or dimension parameter description.
- optional `display_order`: nonnegative integer used only to arrange tiles
  within a region; it is not displayed and has no mathematical meaning.

Object notation is the displayed mathematical symbol. Existing constraints
remain the formal authoring scope, while the summaries support the table UI.
Family records must be simple for every admitted parameter if assigned to the
finite-simple-groups category. Small nonsimple cases are distinct examples or
explicitly excluded, never silently called simple. Low-rank isomorphisms are
recorded relationships, not deduplicated object labels.

Knowl namespaces: `catalog/finite-groups/sporadic/*`,
`catalog/finite-groups/lie-type/*`, `catalog/finite-groups/elementary/*`, and
`catalog/finite-groups/relationships/*`. Reuse existing canonical owners where
appropriate. Reviews/reservations/manifests go in `reviews/finite-groups/`.
Use targeted evidence with exact source locators and source hashes; no Lean
certification is claimed. Display references only in final References sections.

## Ownership

- Sporadic lane: 26 objects/definitions, ATLAS verified exact orders and
  grouping; selected genuinely supported relationships. Does not own Tits.
- Lie-type lane: 16 simple families, explicit rank/field constraints and
  low-parameter exceptions, Tits group, selected small examples and low-rank
  isomorphisms. No changes to existing real/complex Lie-group records.
- Elementary lane: cyclic, symmetric, alternating, dihedral, quaternion,
  elementary abelian, general/special linear, finite Heisenberg families and
  small examples, with selected relationships.
- Root: two finite categories, the finite-group definition and classification
  explanation, known morphism comparisons, navigation, integration and final
  review. Exact knowl reservations are in
  `reviews/finite-groups/core-reservations.json` in the content repository.
- Browser lane: periodic-table shell/runtime/CSS, meaningful alternate layouts,
  details/filter interaction, accessibility, screenshots and browser checks.
- Infrastructure lane: validate finite metadata, generator navigation support,
  compiler wiring for /catalog/finite-groups/table/, focused tests.

The visual page reads the exported catalogue; it must not maintain a second
independent mathematical dataset. Simple-family tiles total 18 including cyclic
and alternating; sporadic tiles total 26; Tits is a separate special case.

## Delivered content

Content commit `f01eb0a8` adds 144 finite-group records: 18 simple families,
26 sporadics, the Tits group, and 99 further families or specified examples.
There are 157 new knowls and two updated catalogue navigation pages. The
three object lanes contain 50 elementary, 68 Lie-type, and 26 sporadic records;
the new core shard supplies two categories and 22 cyclic Hom/End/Aut records.
The complete catalogue now has 658 objects, 42 categories, 3,284 views,
688 relationships, 175 morphism-space records, and the existing magic square.

Knowl definitions give actual constructions: small permutation models,
specified matrix models, presentations, central quotients, fixed points, and
derived groups. Literature evidence for group order and simplicity remains
distinct from the bounded arithmetic/model checks and from formal proofs.
All 157 new knowls have a current content-review record. The canonical ledger
preserves targeted and dependency scopes; the original refactor baseline is
unchanged. Separate independent reviews cover the seven root knowls and all
sporadic definitions plus their Leech-lattice prerequisite.

## Visual comparisons and revisions

Compared classification blocks against equal-size all-group grids at 1440px
and 390px, first with a synthetic fixture and then the complete dataset.
Classification is the default because it keeps the six classical and ten
exceptional families visibly distinct. The all-groups layout remains available:
it places constrained families together and sorts individual groups by exact
integer order. Sporadics offer ATLAS display grouping or increasing order;
the cluster view is the default because it better communicates their context.

The second iteration reduced mobile space before the first tiles from about
725px to 497px in the fixture, moved long order products into details, corrected
fixture encoding, and aligned symbols below multiline rank labels. Authored
presentation ranks put the simple families in conventional order. These ranks
are not shown as mathematical invariants. Final compiled pages also fit below
the site's existing mobile header.

The reader pass found a 399.25px inline orthogonal-group formula overflowing
a 370px phone column. Moving it to a display preserved the definition and
made the formula scroll within the page. Integration also made the helper's
finite-dimensional vector-space hypothesis explicit. The corrected live page
is exactly 390px wide. No global reader CSS was changed.

Screenshots are under `tmp/finite-groups-layouts/`; durable comparison and
validation results are in the content repository's
`reviews/finite-groups/browser-layout-review.json`. The page is
`https://optiplex.taildb538a.ts.net:8443/catalog/finite-groups/table/`, served by
the existing `knowlpedia-astra-benchmark` service on backend port 8015.

## Integration checks

- All 219 Python tests pass, including finite metadata and conditional-page
  compiler tests. Browser tests cover all 144 detail panels, both layouts,
  both sporadic arrangements, exact large-order sorting, keyboard interaction,
  filters, dark theme, and 16 representative reader pages at phone/desktop widths.
- The catalogue validates. Ninety-seven additional exact arithmetic checks
  cover prime factor bases/products and order consistency of fixed-group
  isomorphisms and embeddings; these do not certify the asserted groups/maps.
- The production dependency graph has no cycles, missing targets, or invalid
  edges. All 159 new/changed knowls preserve their complete section contents.
- The external-reference audit passes. Two new scope-audit findings were
  reviewed and retained with reasons in `integration-scope-review.json`.
  The sole section-audit failure is the unchanged baseline fibre-bundle
  connection-splitting page, verified byte-identical to `8ce039be`.
- The development build contains 4,896 knowls and passed the full rendering
  scan; the final corrected orthogonal page and all its fragments were checked
  again. HTTPS table, overview, sporadic index, and exported catalogue bytes
  match the current local build. The service was reused without a restart.
- The final production build contains 4,884 knowls; its complete rendering,
  production-profile, and prebuilt-diagram checks pass after the orthogonal
  correction. The finite-group review export contains 159 comparisons at
  `/review/finite-groups/`. Previous catalogue and transcript review pages
  were restored at their existing URLs after rebuilding the site.
