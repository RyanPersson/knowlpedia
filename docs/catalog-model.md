# Category-aware mathematical catalogue

The catalogue separates an object's identity, the structure used to regard it
as an object of a category, and recorded information about its maps. For
example, real and complex special linear groups have different object IDs.
A complex algebra can additionally have a real algebra or real vector-space
view. Those views have different Hom, End and Aut queries.

Canonical data are the JSON shards in the content repository's
`content/catalog/data/`. Knowls supply mathematical definitions and evidence;
the JSON supplies stable identities and machine-readable relationships.
The compiler validates the entire catalogue before replacing the current
site, then emits `indexes/catalog.json`, `indexes/catalog.sqlite`, and the
browser explorer at `/catalog/explorer/`. No catalogue artifacts are created
when no shards exist. Selected-page builds validate data but do not replace
the complete catalogue exports.

## Explorer interaction

The explorer at `/catalog/explorer/` puts the object selection, map operation,
category, and result together. **Change** opens a searchable object picker with
keyboard navigation. Aut and End show one object; Hom shows both endpoints and
remembers its target when temporarily switching operations. Selection changes
update shareable URLs and participate in browser Back/Forward navigation.
In Hom mode, **Swap** exchanges the domain and codomain together with their
selected structures, retaining the category and querying maps in the new direction.

Categories with descriptions for the current objects and operation appear
first. Other common categories remain available. A structure selector appears
only when there is a choice; explicit structure parameters and constraints
remain visible. Missing descriptions offer available recorded alternatives
without interpreting an absent record as an empty collection of maps.

Object metadata, category axioms, evidence, and the pair diagram are expandable.
Related objects appear six relationships at a time, with statements, conditions,
source definitions, and explanation links inside each row. Conjectural labels
remain visible before expansion. Descriptions and conditions are taken from the
existing catalogue records; the UI does not create mathematical conclusions.

`node tests/catalog_browser_smoke.mjs` checks the interaction against a small
fixture. Set `PREVIEW_URL` to the existing HTTPS preview to also check every
exported morphism-space record, result links, object search pagination, related
objects, and the mobile layout. `CATALOG_DATA_PATH` can instead supply an exported
JSON index to test the current source without a running server.

## Authoring contract

Each shard has `schema_version: 1` and any of these arrays:

| Collection | Meaning |
| --- | --- |
| `objects` | Distinct objects or explicitly constrained symbolic families |
| `categories` | Object axioms, morphism axioms, scalar, regularity and unit policy |
| `views` | A named object with a specified categorical structure |
| `relationships` | Authored isomorphisms, embeddings, constructions and other relationships |
| `morphism_spaces` | Descriptions of Hom, End or Aut in one category |
| `magic_squares` | Ordered two-input construction tables with typed output references |

IDs are unique within each collection across all shards. Objects and
categories have stable lowercase IDs; view IDs can also contain `@`. The
validator rejects unknown top-level collection names, duplicate JSON keys,
nonfinite numbers, missing required fields, unresolved references and
malformed records. Arbitrary parameter metadata and dimension formulas are
never evaluated as executable code.

Objects require `id`, `name`, `notation`, `kind`, `family`, `parameters`,
`knowl`, `dimensions`, `category_ids`, `constraints`, `properties`, `status`
and `references`. Dimension values are nonnegative integers or nonempty
formula strings. A `status: "family"` record must state parameter domains in
`constraints`; individual objects have `status: "defined"`. A symbolic
family is not instantiated automatically. Distinct low-dimensional objects
therefore remain separate records even when a general family also exists.

Categories require `id`, `name`, `knowl`, `scalar`, `object_axioms`,
`morphism_axioms`, `unit_policy` and `regularity`. `scalar` may be null. Object
and morphism axioms are deliberately separate. In particular, unital objects
do not imply unit-preserving morphisms. The local conventions are:

| Convention | Objects | Morphisms |
| --- | --- | --- |
| Jord | Jordan algebras | Linear product-preserving maps |
| UJord | Unital Jordan algebras | Linear product-preserving maps |
| Jord1 | Unital Jordan algebras | Unit-preserving linear product-preserving maps |

Every declared object/category membership generates the default view
`OBJECT_ID@CATEGORY_ID`. Explicit views require `id`, `object_id` and
`category_id`; optional `scalar`, `parameters`, `constraints` and `description`
make a noncanonical structure or a scoped field extension explicit. They must
use a declared category membership. An explicit record can annotate a default
view, but cannot reuse its ID for another object or category. Multiple
structures on one carrier need distinct view IDs.

Relationships require `id`, `source`, `target`, `kind`, `category_id`,
`statement`, `knowl`, `conditions` and `evidence`. Endpoints are object IDs.
A non-null category must contain both endpoints. A null category records a
construction or structural relationship without asserting that it is a
morphism in one of the listed categories. An arrow's orientation is authored;
the exporter does not infer inverse arrows, composition, category inheritance,
or membership from isomorphism claims.

Isomorphisms, embeddings, quotients and coverings require a category.
Constructions, scalar restrictions, complexifications, associated Lie or
derivation algebras, and automorphism-group constructions require a null
category. Representations may be categorized maps or structural constructions;
their statements must identify which interpretation is intended.

Morphism-space records require `id`, `source_view`, `target_view`, `operation`,
`description`, `knowl`, `conditions` and `evidence`. `operation` is `hom`, `end`
or `aut`. Hom endpoints must have the same category, and End/Aut require the
identical view at both endpoints. Equal underlying carriers are insufficient.
Optional `coverage` is `partial` by default; `complete` asserts a full
description **under that record's conditions**. Multiple records can describe
one query with different hypotheses or methods. Their coverage is preserved
individually and is not merged into an unconditional completeness claim.
Optional `result_object_ids` link to objects that describe the result, such as
a matrix algebra describing an endomorphism algebra. Their IDs are validated
and reverse-indexed. The description must specify the structure and conditions
of that identification; an object reference alone does not assert an
isomorphism in an unspecified category.

A missing record means **not catalogued**, never an empty Hom-set. A result
with records means only that information has been recorded, not that a proof
assistant has checked it. Hom(A,A), End(A) and Aut(A) are separately queried
operations; the exporter does not synthesize one from another. To assert that
a Hom-set is empty, an author must provide an explicit complete description
with its conditions and evidence.

Knowl references resolve through the compiler's canonical registry, including
explicit redirects. Public catalogue records cannot reference private or
development-only knowls. References are `{url, title, locator}` objects with
absolute HTTP(S) URLs. Evidence is `{status, method, references, lean}` where
status is `definition`, `proved-in-text`, `literature` or `conjectural`.
`lean` is null until a proof reference is available. Future references have
`module`, `declaration` and `revision` fields. Storing a proof reference does
not verify it; a future Lean checking stage must pin the toolchain/library
revision and check that the declaration establishes the intended statement.

## Two-input constructions

A magic square has `id`, `name`, `knowl`, `field`, `form`, `row_object_ids`,
`column_object_ids`, `cells` and `evidence`. Each cell records
`row_object_id`, `column_object_id`, `output_object_id` and
`construction_relationship_ids`. Validation requires unique, complete
rectangular coverage and verifies the cited construction outputs. The same
output may occur in multiple cells without duplicating its object identity.

A construction relationship may carry `parameters.other_input_id`,
`parameters.square_id`, zero-based `parameters.cell: [row, column]`, and
`parameters.transposed_relationship_id`. These references are checked. Both
inputs appear in a dedicated construction adjacency index, so searching the
column input finds the construction as well as searching the row input.
Construction participation does not create a Hom-space record. The full
multi-input table is preserved in both exports.

## Finite-group table metadata

Finite-group records may additionally include `properties.finite_group`.
The ordinary catalogue remains valid without this optional metadata. When
any object includes it, a full build adds `/catalog/finite-groups/table/` and
its browser assets. The table reads the existing `indexes/catalog.json`;
it does not maintain another mathematical dataset. Object tiles link to
their knowls and can be compared through the existing category explorer.
The simple-group classification view distinguishes constrained families,
the sporadic groups, and the Tits group. The familiar-family view includes
groups that are not simple or whose simplicity depends on parameters.

The metadata requires these fields:

| Field | Contract |
| --- | --- |
| `table_role` | `simple-family`, `sporadic`, `tits`, `family`, or `example` |
| `section` | `cyclic`, `alternating`, `classical`, `exceptional`, `sporadic`, or `familiar` |
| `order_tex` | Nonempty LaTeX formula without math delimiters |
| `order_decimal` | Exact positive decimal string without leading zeroes, or null |
| `simple` | Boolean, or null for a parameter-dependent entry |
| `simple_condition` | Nonempty statement of simplicity and its conditions |
| `parameter_summary` | Nonempty parameter scope or fixed-object description |
| `construction_summary` | Nonempty description of the construction |

Optional `sporadic_cluster` is `mathieu`, `leech`, `monster`, or `pariah` on
a sporadic record. These are display groups, not asserted containment
relations. Optional `rank_label` is a nonempty string. Optional
`display_order` is a nonnegative integer (booleans are rejected) for
conventional family ordering within a table region. It is only a sorting
hint and is never displayed as an atomic number. Optional
`order_factors` contains distinct integer factor bases at least two paired
with positive integer exponents. The validator checks their structure and,
when an exact order is supplied, their exact product. It does not prove the
bases prime or verify that the displayed group actually has that order.
An empty factor list represents the product one.

Exact orders stay decimal strings in both JSON and SQLite so large orders
never pass through a floating-point number. A browser can use `BigInt` for
order comparisons; unknown or symbolic orders remain null and cannot be
placed in a numerical order by treating a formula as executable code.
Finite order is separate from vector-space dimension.

Finite metadata requires explicit `sets`, `groups`, and `finite-groups`
memberships. `simple: true` must agree with `finite-simple-groups` membership,
and order one cannot be marked simple. A `simple-family` entry has family
status and simplicity throughout its stated constraints. Sporadic and Tits
entries have defined status, a fixed exact order, and simplicity; the Tits
entry belongs in the exceptional section rather than the sporadic section.
These checks catch inconsistent metadata, not incorrect mathematical claims.
The validator accepts partial catalogues and does not hard-code global
classification counts as a schema requirement.

The navigation generator recognizes `finite-sporadic.json`,
`finite-lie-type.json`, and `finite-elementary.json`. It adds an order-based
index for each present object-bearing shard, links the table from the main
catalogue, and retains the existing generated-file overwrite guard. The
default new-knowl baseline remains `d1ad541e`, so the existing created-knowl
list continues to cover the whole catalogue branch.

## Lie-group table metadata

Lie-group records may include `properties.lie_group`. This metadata is valid
only on objects with `kind: "lie-group"` and explicit `real-lie-groups`
membership, including complex Lie groups viewed as real Lie groups. When
present, a full build adds `/catalog/lie-groups/table/` and its assets. The
page reads `indexes/catalog.json`; its scripts contain no mathematical
records. The navigation generator links the table from the main catalogue
and the Lie-group index when their records include this metadata.

The required fields are:

| Field | Contract |
| --- | --- |
| `section` | `classical`, `exceptional`, `abelian`, `nilpotent`, `geometric`, or `product` |
| `form` | `compact`, `complex`, `real`, or `mixed` |
| `parameter_summary` | Nonempty parameter scope or fixed-object description |
| `construction_summary` | Nonempty description of the construction |
| `global_form_summary` | Nonempty statement identifying the chosen global group |

Optional `display_order` is a nonnegative integer, with booleans rejected.
It controls presentation only. The existing object `dimensions`,
`properties.compact`, `properties.connected`, and category memberships
remain the source for these facts; a display section or form does not imply
them. Parameter-dependent and unknown values must remain explicit.

Optional `classification_cells` is a nonempty array of selections of the
owning object or family. Each cell requires these fields:

| Field | Contract |
| --- | --- |
| `series` | `A`, `B`, `C`, `D`, `G2`, `F4`, `E6`, `E7`, or `E8` |
| `form` | `compact`, `split`, or `complex` |
| `notation` | Nonempty LaTeX for the selected group, without math delimiters |
| `dimension_tex` | Nonempty LaTeX dimension formula, without math delimiters |
| `dimension_field` | `real` for compact/split columns; `complex` for the complex column |
| `parameter_summary` | Nonempty, exact rank range or fixed-group scope |
| `specialization` | Nonempty explanation of substitution into the owner, or the whole fixed group |
| `global_form` | Nonempty identification of the selected global group |

No two cells across any objects or shards may occupy the same `(series,
form)` position. A partial table is valid; the schema does not demand a
fixed number of cells. Unknown metadata and cell fields are rejected.
The owning object must declare the cell's real or complex dimension field;
complex cells also require `complex-lie-groups` membership. A real Lie group
defined using complex matrices is not thereby a complex Lie group.
Validation checks structure and internal consistency, not mathematical
truth or equivalence of symbolic formulas.

The table shows chosen global groups with the indicated Lie-algebra type;
it does not classify all Lie groups, all global forms, or all real forms.
The classical rank conventions are A with rank at least 1, B at least 2,
C at least 3, and D at least 4, avoiding repeated low-rank types. Authors
must explain the overlaps and preserve the actual covering, quotient, and
isomorphism relationship kinds. In particular, algebraic simple connectivity
does not imply topological simple connectivity of a split matrix group.
Cell details identify the selected slice and the complete owning family;
the full catalogue includes each owning object once.

## Querying

Normal builds export the catalogue automatically. Standalone commands from
the application repository use the same validator:

```bash
make catalog-validate
.venv/bin/python scripts/catalog.py export --output-dir tmp/catalog-export
.venv/bin/python scripts/catalog.py counts
.venv/bin/python scripts/catalog.py common scalar-c scalar-r
.venv/bin/python scripts/catalog.py views scalar-c
.venv/bin/python scripts/catalog.py neighbors scalar-split-o
.venv/bin/python scripts/catalog.py hom scalar-c@real-vector-spaces scalar-r@real-vector-spaces
.venv/bin/python scripts/catalog.py aut scalar-c@complex-associative-algebras
```

Use `--database PATH` **before** the command to select a different export.
`objects` supports category, kind and family filters; `neighbors` supports
direction, category and relationship-kind filters. All database queries are
read-only. An unknown object/view/category ID is an error, while a valid
unrecorded Hom query returns `status: "not-catalogued"` and `records: []`.
The Python interface in `packages/compiler/catalog.py` is:

```python
from pathlib import Path
from catalog import CatalogQuery

with CatalogQuery(Path("public-imported/indexes/catalog.sqlite")) as query:
    categories = query.common_categories("scalar-c", "scalar-r")
    information = query.morphisms(
        "scalar-c@real-vector-spaces", "scalar-r@real-vector-spaces", "hom"
    )
```

The database has normalized object/category memberships and named views,
indexed relationship endpoints and construction inputs, and composite
source/target/category/operation indexes for morphism spaces. Full JSON
payloads preserve evidence and extensible metadata alongside those indexed
columns. `PRAGMA user_version` identifies the export schema. Consumers should
rebuild exports from source after a schema change.

## Browser indexes and cost

JSON collection arrays are sorted by ID. `indexes.by_id[collection][id]`
gives the array position. Other indexes map IDs to lists of matching record
IDs: `objects_by_category`, `objects_by_kind`, `objects_by_family`,
`views_by_object`, `views_by_category`, `relationships_from`,
`relationships_to`, `relationships_by_category`, `construction_inputs`,
`morphisms_by_source`, `morphisms_by_target` and `morphism_results_by_object`. The nested sparse
`morphism_lookup[source_view][target_view][operation]` contains only recorded
queries. Categories are already determined by those views. No Cartesian
product of object pairs is allocated.

Let V count objects, categories, memberships and views; E count relationship
and construction participation records; and M count morphism records. Graph
validation and index assembly use O(V + E + M) space and work, excluding the
length of authored text and exact-integer factor arithmetic. Deterministic ID ordering adds O(S log S) sorting
for S total records, and SQLite B-tree insertion also has logarithmic costs.
The build therefore makes no claim of a strictly linear total export time.
Two-input table coverage checks scale with the explicitly authored cells.

Browser hash-map lookups take expected O(1) time plus returned records.
Indexed SQLite ID, category, pair and adjacency queries take O(log S + R)
for R matched records, apart from optional result sorting and parsing returned
payloads. Intersecting category lists additionally depends on their lengths;
combining both directions of adjacency includes result deduplication. Neither
the browser nor SQLite query interface scans all possible object pairs.

Tests cover scalar/category mismatches, distinct structures on one carrier,
unit policy separation, unresolved references, schema errors, public-content
isolation, sparse unknown results, read-only queries, query-index selection,
construction cells and deterministic JSON/SQLite exports. Mathematical truth
still requires the knowl reviews and future proof checking; schema validation
alone cannot certify a claimed isomorphism.

An October 2, 2026 measurement on the development host used 514 objects,
40 categories, 2,740 views, 622 relationships, 153 morphism records and one
magic square. Loading, validating and indexing its shards took 48.8 ms after
the knowl registry was available; writing both exports took 75.6 ms. JSON
occupied 1,520,220 bytes and SQLite 2,686,976 bytes. Over 1,000 warm queries,
mean times were 44 microseconds for a Hom lookup, 111 microseconds for common
categories, and 227 microseconds for octonion adjacency including two-input
constructions. These are a corpus snapshot and local timings, not performance
guarantees; ordinary knowl discovery/rendering is outside this measurement.
