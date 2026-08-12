# Knowl concept-scope audit

This audit enforces the editorial rule that an ordinary knowl owns one
independently reusable definition, theorem, construction, example, or
convention. It was prompted by links labeled “local field” and
“nonarchimedean local field” that opened a page whose primary definition was
“global field.”

The audit is deliberately a two-stage process:

1. `scripts/audit_knowl_scope.py` reports structurally suspicious pages and
   exact-label target mismatches. It never edits content.
2. A reasoning review opens each candidate, decides whether its concepts are
   genuinely independent, and either makes a bounded correction or records a
   follow-up. A conjunction, comparison, theorem with equivalent forms, or a
   construction together with its defining data is not split merely because a
   string heuristic noticed two nouns.

## Resolved initiating case

The legacy ID
`langlands-letter/knowls/global-local-fields-completions` is retained so
existing URLs remain valid, but it now owns only the definition of a global
field. The previously bundled concepts have canonical knowls of their own:

- `algebra-fields-galois/number-field`
- `algebra-fields-galois/global-function-field`
- `algebra-fields-galois/place-of-global-field`
- `algebra-fields-galois/completion-at-place`
- `algebra-fields-galois/local-field`
- `algebra-fields-galois/archimedean-local-field`
- `algebra-fields-galois/nonarchimedean-local-field`

All 106 links that formerly targeted the umbrella page were reviewed by their
visible mathematical label, including labels split across Markdown lines.
Every use not solely denoting a global field was retargeted. The 29 links that
target the legacy ID after the split all say “global field” or “global
fields”; that total includes relationship links from the new atomic pages.
Local fields, number fields, places, completions, and function fields now open
their corresponding atomic knowls. The multi-topic convex-analysis lecture
notes were also reclassified from an ordinary `knowl` to a `document`.

Nine unrelated exact-label mistakes exposed by the same review were corrected:
representation theory, module homomorphism, exterior algebra, weight lattice,
bounded Hilbert-space operator, and four trace-class-operator links now open
their exact canonical targets.

## Running the audit

From the `knowlpedia` repository:

```bash
make audit-scope
```

That default pass reports stronger candidates: multiple explicit definienda,
or a section that begins by defining a term not supported by the page title.
It exits successfully because every result requires semantic review. For a
broader editorial inventory, including compound-title candidates:

```bash
.venv/bin/python scripts/audit_knowl_scope.py \
  ../knowlpedia-content/content --include-weak
```

Use `--format jsonl` for a review ledger and `--fail-on-findings` only after a
particular result set has been adjudicated. The latter is not a suitable
repository-wide CI gate while the historical backlog remains open.

The current corpus contains 3,397 knowls. The strong pass reports 136
concept-ownership candidates, and the optional compound-title pass expands
that to 262. It also reports 23 advisory exact-label mismatches. Every current
candidate was opened during this audit. Most are coherent theorem statements,
paired constructions, conventional variants, or auxiliary data and should be
retained. The script's output is evidence for review, not a verdict.

Examples retained after semantic review include the Poisson structure as the
defining data of a Poisson manifold, normalized and unnormalized variants of
the Jacquet module, Chern--Weil forms together with the classes they represent,
and paired existence/uniqueness or comparison theorems. The remaining
exact-label advisories are similarly context-sensitive links where a generic
visible phrase intentionally opens a more specific page.

## Confirmed follow-up ledger

These pages contain an independently reusable secondary concept, duplicate a
canonical definition, or are sufficiently broad that an atomic migration
should be designed. A checked box should mean the page was actually split,
consolidated, or intentionally reclassified after its incoming links were
reviewed; renaming alone is not sufficient.

### Existing canonical coverage to consolidate

- [ ] `functional-analysis/graph-norm` — move the duplicated definition of a
  core to `functional-analysis/core-of-closed-operator`.
- [ ] `functional-analysis/inductive-limit-locally-convex-spaces` — reconcile
  its LF-space definition with `functional-analysis/lf-space`.
- [ ] `lie-groups/center-of-universal-enveloping-algebra` — link rather than
  redefine infinitesimal character.
- [ ] `quantum-foundations/complex-hilbert-space-finite` — link rather than
  redefine the adjoint of a bounded operator.
- [ ] `quantum-foundations/positive-operator-valued-measure` — move its
  projection-valued-measure definition to the existing canonical page.
- [ ] `algebra-commutative/maximal-spectrum` — link rather than redefine a
  maximal ideal.
- [ ] `algebra-commutative/prime-spectrum` — link rather than redefine a prime
  ideal.
- [ ] `lie-groups/orbit-lie-group` — consolidate its orbit-map and stabilizer
  definitions with the existing atomic knowls.
- [ ] `real-analysis/regular-value-critical-value-multivariable` — consolidate
  its regular- and critical-value definitions with their canonical knowls.
- [ ] `fiber-bundles/reproduction-property-x` — link rather than redefine the
  fundamental vector field.
- [ ] `lie-groups/dynkin-diagram` — link rather than redefine the Cartan
  matrix.
- [ ] `lie-groups/weights-in-dual-cartan` — link rather than redefine the
  weight lattice.
- [ ] `algebra-homological/ext-tor-derived-functors` — use the atomic Ext and
  Tor pages for the two definitions.
- [ ] `algebra-homological/hom-tensor-exactness` — use the atomic Hom and
  tensor-functor exactness pages.
- [ ] `convex-analysis/bounded-set-and-bounded-sequence` — consolidate the
  duplicated bounded-set and bounded-sequence definitions.
- [ ] `convex-analysis/uniqueness-of-limits-and-boundedness-in-normed-spaces`
  — link its results to the existing atomic theorem pages.
- [ ] `langlands-letter/knowls/roots-weights-weyl` — keep the historical bridge
  but replace embedded definitions with links to modern canonical pages.

### Missing atomic targets

- [ ] `langlands-letter/knowls/galois-extension-and-group` — separate the
  Galois group from the extension it acts on.
- [ ] `convex-analysis/image-and-kernel-linear-isomorphism` — separate image,
  kernel, and linear isomorphism.
- [ ] `langlands-letter/knowls/galois-descent-forms` — separate forms and inner
  forms from their descent context.
- [ ] `convex-analysis/domain-and-epigraph-proper-function` — separate domain,
  epigraph, and proper function.
- [ ] `convex-analysis/set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping`
  — separate multifunction, domain, graph, and convexity.
- [ ] `nonassociative-algebra/derivation-of-a-jordan-algebra` — add an atomic
  inner Jordan derivation rather than overloading the ordinary inner-derivation
  page.
- [ ] `algebra-commutative/dvr` — add an atomic uniformizer knowl.
- [ ] `langlands-letter/knowls/ideles-artin-reciprocity-hecke-character` —
  separate ideles, Hecke characters, and global Artin reciprocity.
- [ ] `convex-analysis/dual-space-and-duality-pairing` — separate the dual
  space from a duality pairing.
- [ ] `discrete-structures/boundary-finite-region` — separate the boundary
  variants used by the page.
- [ ] `algebraic-geometry-foundations/adic-space` — add atomic Huber-pair and
  `Spa` construction pages before narrowing the adic-space page.
- [ ] `algebraic-geometry-foundations/v-stack` — add atomic v-topology,
  v-sheaf, and diamond pages before narrowing the v-stack page.
- [ ] `fiber-bundles/parallel-section-along-a-curve` — distinguish a parallel
  section from a section parallel only along a curve.
- [ ] `fiber-bundles/right-principal-action` — separate the right-principal
  convention from the general smooth action it currently defines.
- [ ] `harmonic-analysis/bernstein-decomposition` — add atomic cuspidal-pair
  and inertial-equivalence knowls.
- [ ] `lie-groups/k-type` — add an atomic isotypic-component knowl.
- [ ] `langlands-letter/knowls/euler-product-and-local-factor` — separate the
  local L-factor from the Euler product built from those factors.
- [ ] `operator-algebras/graded-operator` — separate the graded commutator from
  even and odd operators.
- [ ] `algebraic-geometry-foundations/fundamental-theorem-of-projective-geometry`
  — add an atomic collineation knowl.
- [ ] `linear-algebra/positive-semidefinite-matrix` — add atomic positive
  definite matrix and Loewner-order knowls.
- [ ] `langlands/tamagawa-measure` — add an atomic Tamagawa-number knowl.
- [ ] `algebraic-geometry-foundations/harder-narasimhan-filtration` — separate
  the Harder--Narasimhan polygon and moduli-truncation construction from the
  filtration theorem.

### Compound pages requiring a bounded semantic split

- [ ] `convex-analysis/affine-hull-affine-combination`
- [ ] `convex-analysis/balanced-and-absorbing-sets`
- [ ] `convex-analysis/basis-hamel-basis-and-dimension`
- [ ] `convex-analysis/bounded-linear-functional-norm-of-a-functional`
- [ ] `convex-analysis/quotient-vector-space-codimension`
- [ ] `convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions`
- [ ] `langlands-letter/knowls/chevalley-lattice-integral-model`
- [ ] `langlands-letter/knowls/spherical-hecke-algebra-satake`
- [ ] `real-analysis/additivity-linearity-riemann-integral`
- [ ] `real-analysis/m-test-continuity-integration-corollary`
- [ ] `topology/cup-product-and-cohomology-ring`

The next remediation pass should work one row or tightly related family at a
time: inspect all incoming labels, identify existing semantic equivalents,
add only missing canonical knowls, retarget links by meaning, and then rebuild
the site. The audit script must remain report-only so a lexical guess cannot
silently change mathematical ownership.
