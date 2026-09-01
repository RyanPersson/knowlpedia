# Quaternionic plurisubharmonicity knowl plan

This is the canonical manifest for the expansion centered on Semyon Alesker's
survey *Quaternionic plurisubharmonic functions and their applications to
convexity* (arXiv:math/0606756). It follows the process recorded in
`docs/july-26-retrospective.md`: semantic deduplication precedes authorship,
accepted IDs are reserved here, and index closure and reviewed interlinking
follow the content pass.

The neighboring octonionic branch is based on Alesker's later paper
arXiv:0707.4385. It is kept separate because octonionic plurisubharmonicity is
developed on the plane \(\mathbb O^2\), not as a routine theory on arbitrary
\(\mathbb O^n\).

## Baseline

- `knowlpedia`: `develop` at `f358146`.
- `knowlpedia-content`: `develop` at `a2ea3b7`.
- Production corpus audited: 3,453 knowls under `knowlpedia-content/content`.
- Working branch in both repositories: `add-quaternionic-psh-convexity-knowls`.

## Deduplication decisions

- Preserve and expand the existing harmonic, subharmonic, plurisubharmonic,
  strictly plurisubharmonic, and Levi-form knowls. The new pluriharmonic knowl
  and a comparison theorem will own the four-way H/SH/PSH/PH relationship.
- Preserve the existing quaternion, quaternionic-vector-space, hypercomplex,
  hyper-Hermitian, hyperkähler, octonion, and spin-group knowls as canonical
  prerequisites.
- A hyperhermitian form and its representing matrix are two presentations of
  one object after a basis is chosen; one knowl will own both rather than
  creating competing form and matrix pages.
- A valuation on convex bodies will own the continuity, translation-invariance,
  and group-invariance predicates. These predicates do not receive nearly
  empty standalone knowls.
- The Moore determinant is quaternionic and distinct from the ordinary
  determinant. The determinant of a \(2\times2\) octonionic Hermitian matrix is
  another dimension-sensitive construction and receives its own knowl.
- Quaternionic PSH functions on flat \(\mathbb H^n\) and on hypercomplex
  manifolds have materially different definitions, so they remain separate
  knowls connected by a flat-model section.
- HKT means hyperkähler with torsion; it is weaker than hyperkähler and is not
  an alias for the existing hyper-Hermitian knowl.
- `SL_2(\mathbb O)` is convention-sensitive because octonionic matrices do not
  form an associative matrix group. Its knowl will use the transformation/Lie
  group convention and state the identification with \(\operatorname{Spin}(9,1)\).

## Batch 1 — classical potential theory

| Status | Canonical ID | Kind | Action |
|---|---|---|---|
| EXPAND | `complex-analysis/harmonic-function` | definition | Add sphere/ball mean-value forms and links. |
| EXPAND | `complex-analysis/subharmonic-function` | definition | Generalize the core from \(\mathbb C\) to \(\mathbb R^m\). |
| EXPAND | `complex-analysis/plurisubharmonic-function` | definition | Add ordinary subharmonic comparison. |
| NEW | `complex-analysis/pluriharmonic-function` | definition | Linewise harmonicity, vanishing Levi form, local real parts. |
| NEW | `complex-analysis/harmonic-subharmonic-pluriharmonic-relations` | theorem | Exact H/SH/PSH/PH inclusion and intersection diagram. |
| NEW | `complex-analysis/complex-monge-ampere-operator` | definition | Complex Hessian determinant and Bedford–Taylor measure. |

## Batch 2 — quaternionic linear and potential theory

| Status | Canonical ID | Kind | Action |
|---|---|---|---|
| NEW | `linear-algebra/hyperhermitian-form` | definition | Forms, matrices, positivity, spectral theorem. |
| NEW | `linear-algebra/moore-determinant` | definition | Quaternionic determinant on hyperhermitian matrices. |
| NEW | `linear-algebra/mixed-discriminant` | definition | Polarization of determinant, including Moore determinant. |
| NEW | `complex-analysis/cauchy-fueter-operators` | definition | Quaternionic Dirac operators and convention warning. |
| NEW | `complex-analysis/quaternionic-hessian` | definition | Hyperhermitian matrix of mixed quaternionic derivatives. |
| NEW | `complex-analysis/quaternionic-plurisubharmonic-function` | definition | Upper semicontinuity plus right-line subharmonicity. |
| NEW | `complex-analysis/strictly-quaternionic-plurisubharmonic-function` | definition | Strict linewise/Hessian positivity. |
| NEW | `complex-analysis/quaternionic-monge-ampere-measure` | definition | Moore determinant measure for continuous quaternionic PSH functions. |
| NEW | `complex-analysis/mixed-quaternionic-monge-ampere-measure` | definition | Polarized Hessian measure. |
| NEW | `complex-analysis/quaternionic-monge-ampere-continuity-theorem` | theorem | Aleksandrov–Chern–Levine–Nirenberg analogue. |
| NEW | `complex-analysis/quaternionic-blocki-formula` | theorem | Max/min identity used for valuations. |
| NEW | `complex-analysis/quaternionic-monge-ampere-equation` | definition | Nonlinear PDE and its Dirichlet data. |
| NEW | `complex-analysis/strictly-quaternionically-pseudoconvex-domain` | definition | Local strictly PSH defining functions. |
| NEW | `complex-analysis/quaternionic-monge-ampere-dirichlet-theorem` | theorem | Existence and uniqueness on bounded strictly pseudoconvex domains. |

## Batch 3 — convex bodies and valuations

| Status | Canonical ID | Kind | Action |
|---|---|---|---|
| NEW | `convex-analysis/convex-body` | definition | Nonempty compact convex subset convention. |
| NEW | `topology/hausdorff-distance` | definition | Metric on nonempty compact subsets. |
| NEW | `convex-analysis/support-function` | definition | Dual support function of a convex body. |
| NEW | `convex-analysis/valuation-on-convex-bodies` | definition | Inclusion–exclusion, continuity, invariance. |
| NEW | `convex-analysis/mixed-volume` | definition | Polarization of Euclidean volume. |
| NEW | `convex-analysis/pluripotential-valuation-construction` | theorem | Complex/quaternionic Hessian measures of support functions. |

## Batch 4 — hypercomplex and HKT geometry

| Status | Canonical ID | Kind | Action |
|---|---|---|---|
| NEW | `differential-geometry/del-j-operator` | definition | \(\partial_J=J^{-1}\bar\partial J\). |
| NEW | `differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex` | definition | Positivity of \(\partial\partial_Ju\). |
| NEW | `differential-geometry/hkt-metric` | definition | Hyper-Hermitian metric with \(\partial\Omega=0\). |
| NEW | `differential-geometry/local-hkt-potential` | theorem | Strict quaternionic PSH functions are local HKT potentials. |

## Batch 5 — octonionic plane and Spin geometry

| Status | Canonical ID | Kind | Action |
|---|---|---|---|
| REUSE | `nonassociative-algebra/octonionic-spin-factor` | definition | Existing owner of \(H_2(\mathbb O)\); reuse rather than duplicate under a Hermitian-matrix title. |
| NEW | `nonassociative-algebra/octonionic-two-by-two-determinant` | definition | Quadratic determinant and polarization on \(H_2(\mathbb O)\). |
| NEW | `differential-geometry/octonionic-projective-line` | definition | \(\mathbb OP^1\cong S^8\), used to parametrize directions. |
| NEW | `lie-groups/octonionic-special-linear-group` | definition | Transformation convention and \(\operatorname{Spin}(9,1)\). |
| NEW | `lie-groups/spin9-spin-representation` | definition | The real 16-dimensional spin action on \(\mathbb O^2\). |
| NEW | `complex-analysis/octonionic-affine-line` | definition | Affine copies of \(\mathbb O\) in \(\mathbb O^2\). |
| NEW | `complex-analysis/octonionic-radon-transform` | definition/theorem | Integration over affine octonionic lines and injectivity. |
| NEW | `complex-analysis/octonionic-hessian` | definition | Hermitian \(2\times2\) Hessian and dimension warning. |
| NEW | `complex-analysis/octonionic-plurisubharmonic-function` | definition | Linewise subharmonicity on \(\mathbb O^2\). |
| NEW | `complex-analysis/octonionic-monge-ampere-measure` | definition | Determinant Hessian measure. |
| NEW | `convex-analysis/octonionic-pseudovolume` | construction | Spin(9)-invariant valuation from support functions. |

## Integration

- Add a permanent expansion index at
  `knowlification/quaternionic-psh-convexity-expansion`.
- Update complex analysis, linear algebra, topology, convex analysis,
  differential geometry, Lie groups, nonassociative algebra, and
  knowlification indexes.
- Run the interlinker in report-only mode over new files, review candidates
  semantically, and apply only accepted links.
- Run compiler tests, section/link/scope audits, development and production
  builds, rendering checks, and representative browser inspection.

## Completion record

- Added 38 atomic or navigational knowls and expanded 12 existing corpus
  pages, including all affected subject indexes.
- The semantic interlink report began with 84 candidates. Reviewed additions
  reduced the residual report to 34 candidates; the remainder are deliberate
  rejections or already-linked substrings. Recurring false matches included
  algebraic-geometric affine lines for octonionic affine lines, complex PSH
  targets for quaternionic or octonionic PSH terms, and a quantum-operator
  target for positive-semidefinite forms and matrices.
- The scope audit exposed a near-duplicate that exact-title matching missed:
  the proposed octonionic Hermitian \(2\times2\) matrix page was another
  presentation of the existing octonionic spin factor. It was replaced by the
  genuinely separate quadratic-determinant knowl.
- The isolated production corpus contains 3,491 knowls. All 80 compiler tests,
  the section audit, the external-link audit, the targeted scope audit, the
  production build, and the production rendering check passed. The separately
  composed conjectures catalog is outside this project and outside the live
  production build.

## Deferred research map

The first batch should link, but not prematurely collapse, later developments:
pluripotential theory on general quaternionic manifolds via Baston operators;
the quaternionic Calabi problem on compact HKT manifolds; finite-energy and
quaternionic \(m\)-subharmonic classes; calibrated plurisubharmonicity; and the
classification of invariant valuations for groups transitive on spheres. These
are candidates for later source-guided expansions after the foundational graph
is stable.
