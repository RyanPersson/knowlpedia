# Lie-group visual table

This follow-up stays on `catalog`, beginning with application `72e7f66` and
content `f01eb0a8`, both clean. Reuse the existing preview service on port 8015.
The user requests a Lie-group table following the finite-group process,
including actual visual comparison and iteration.

## Scope and mathematical interpretation

Compare a nine-row Dynkin-series matrix with compact, split-real, and complex
columns against a broader family-board layout. The matrix shows selected
global groups whose Lie algebras have the indicated type. It does not classify
all Lie groups, identify distinct global forms, or list all real forms.
Use the existing 179 Lie-group records, their dimensions and relationships.
Add the identity-component SO0(p,q) family only where necessary to populate
the split B/D cells correctly. Reuse existing definitions and type-classification
theorems. Tori, additive, Heisenberg, affine, Euclidean and product groups belong
in the broader catalogue. Low-rank coincidences and covering/quotient maps
must remain visible and retain their actual map kinds.

## Metadata contract

Add optional `properties.lie_group` on Lie-group objects. Required strings:
`section` in classical/exceptional/abelian/nilpotent/geometric/product;
`form` in compact/complex/real/mixed; `parameter_summary`,
`construction_summary`, `global_form_summary`. `display_order` is an optional
nonnegative integer with no mathematical meaning. Existing `dimensions`,
`properties.compact`, `properties.connected`, and category membership remain
the data source; unknown or parameter-dependent values must stay explicit.

Optional `classification_cells` is a nonempty list of dictionaries:

- `series`: A, B, C, D, G2, F4, E6, E7, E8.
- `form`: compact, split, complex.
- `notation`: LaTeX without delimiters for this parameterized slice.
- `dimension_tex`: LaTeX formula without delimiters.
- `dimension_field`: real or complex (complex column uses complex dimension).
- `parameter_summary`: exact allowed rank range; use A r>=1, B r>=2,
  C r>=3, D r>=4 to avoid repeated types, with low-rank overlaps explained.
- `specialization`: how the displayed rank substitutes into the owning object,
  or a statement that this is the whole fixed group.
- `global_form`: precise group choice; never infer topological simple connectivity
  of a split matrix group from algebraic simple connectivity.

Cells live on their owning object, are selections of that object/family, and
open details that show both the slice and the complete family. The full catalogue
contains each object once. There must be at most one cell per (series,form).
The UI reads exported catalogue data, with no mathematical records in JS.
Compact B/D use Spin; split B/D use SO0; complex B/D use Spin.
Compact A/C use SU/Sp; split A/C use SL/Sp; complex A/C use SL/Sp.

## Ownership and verification

- Metadata/content lane: lie-groups.json, new SO0 definition (reserve exact ID),
  all 179 existing objects' display metadata and 27 cells, per-record review
  evidence under reviews/lie-groups-table/. Do not edit application code or ledger.
- Browser lane: compiler/lie_groups_html.py, static-runtime/lie-groups.js/css,
  browser smoke script, actual screenshot layout comparisons and iterations.
- Infrastructure lane: catalogue validation, compiler/assets/conditional page,
  index-generator navigation, tests and catalog-model.md extension.
- Root: explanation page catalog/lie-groups-table-guide, integration, source review,
  adversarial review coordination, shared ledger and final builds/commits.

Route: /catalog/lie-groups/table/. Preserve finite-group and explorer pages.
Validate source data, all new links and dimensions, production rendering,
desktop/phone layouts, keyboard details, search/filter state, and relation kinds.
Commit application and content separately, without merging or pushing.

## Content integration

Content commit: `396b5778` (31 files, including two new knowls, seven changed
knowls, the data shard, and review records).

The resulting data has 180 Lie-group entries and 27 classification cells on
24 owning records. The only new group family is SO0(p,q), together with its
inclusion into full SO(p,q). The complete catalogue has 659 objects, 689
relationships, 3,288 views, 42 categories, 175 morphism records and one magic
square. The 179 existing Lie-group records keep every prior mathematical
field; the 82 preexisting relationships are unchanged. Missing compactness
values on 28 records remain unknown.

The new guide explains dimension fields, rank substitutions, global forms,
low-rank coincidences and the scope of the comparison. Three directly relevant
source corrections were made during review: C2 no longer duplicates B2 in a
uniqueness statement; compact Sp(n) and split Sp(2n,R) have equal real dimensions
and the complex matrix-size notation is explicit; SL(1,R) is correctly separated
as the compact trivial group. Full SO(p,q) links to the newly defined identity
component. The generated main, Lie-group and created-knowl indexes were updated.

Independent mathematical review checks every cell's rank range, dimension,
field, specialization and global form, plus all new display summaries. It
records current source/data hashes and exact source locators in
`reviews/lie-groups-table/independent-review.json`. The review is targeted;
it does not claim a fresh proof of classification or a full audit of all old
definition pages.

## Visual iterations and delivered interface

Compared the Dynkin matrix and a broader family board using actual catalogue
data at 1440px and 390px, including the compiled site's header. The matrix
is the default: the compact, split-real and complex choices stay adjacent.
The alternate board includes all 180 entries, with families before fixed
examples, filters, and 36 entries per desktop page or 12 per phone page.
Phones use a series selector to keep the three form cards legible.

The first compiled matrix placed its first tile at 631px on desktop and
665px on phones. Condensing the framing and controls moved those positions
to 458px and 473px. The mobile family board shortened from 4,624px to 2,048px.
Screenshots and measurements are under `tmp/lie-groups-layouts/`; the durable
comparison is `reviews/lie-groups-table/browser-layout-review.json` in content.

Details distinguish the selected rank slice from its complete owning family,
show the dimension field and chosen global form, and preserve the catalogue's
relationship kinds and categories. Family details include bounded lists of
existing fixed low-rank examples. In particular, the Lorentz isomorphism of
PSL(2,C) is labelled as a map in real Lie groups. Type searches and cell links
work across desktop and phone views. Unknown compactness remains distinct from
false or parameter-dependent compactness.

## Final verification

- All 226 Python tests pass. Catalogue schema validation and the independent
  mathematical review pass. All 216 new canonical review records match their
  current source hashes; nine new or changed knowls preserve section contents.
- The final HTTPS browser checks open all 180 entries and all 27 cells at both
  widths, verify typed/category-labelled relationships and pagination, and
  inspect 14 reader pages. Keyboard interaction, filters, type search, phone
  permalinks, dark theme, math rendering and page containment pass.
- The development build contains 4,898 knowls and passes the full rendering
  scan. The production build contains 4,886 knowls and passes full rendering,
  production-profile and prebuilt-diagram checks. After the final JS interaction
  changes, the table and its two assets were refreshed through the same renderer
  in both outputs, with targeted rendering/profile checks and the final browser
  pass. No mathematical content changed during those UI refinements.
- Existing finite-group and explorer browser regressions pass, including the
  new SO0 inclusion. HTTPS table, assets, data and prior review pages match the
  local output. The existing service on port 8015 was reused without restarting.
- External-reference and dependency-graph audits pass. The only global section
  audit finding is the unchanged connection-splitting page, verified identical
  to `f01eb0a8`; all nine scoped sources pass.
- Previous catalogue, transcript and finite-group review pages were restored
  at their existing URLs, with exact-source evidence on all 521, 51 and 159
  comparisons respectively. This batch's review is at `/review/lie-groups/`.
