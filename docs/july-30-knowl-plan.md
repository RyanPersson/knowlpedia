# July 30 knowl expansion plan

This document is the canonical planning manifest for the July 30 expansion.
It follows the process in `docs/july-26-retrospective.md`: audit and deduplicate
against the production corpus before authorship, partition the accepted list by
mathematical neighborhood, then perform dependency closure, indexing,
interlinking, and layered validation.

No knowls were authored during this planning pass.

## Branch and baseline

- `knowlpedia` branch: `july-30`, based on `develop` at `cde6311`
  (`Render Markdown pipe tables`).
- `knowlpedia-content` branch: `july-30`, based on `develop` at `26de8df`
  (`Add development-only geometry testing content`).
- Production corpus audited: `knowlpedia-content/content`.
- Development-only material under `testing/` is not treated as production
  coverage.

## Status vocabulary

- **NEW**: no semantic equivalent was found; create the proposed canonical ID.
- **EXPAND**: preserve the existing ID and substantially extend it.
- **CORRECT**: preserve the existing ID and repair a focused error.
- **LINK**: the existing knowl is already adequate; add only integration links.
- **SECTION**: include the topic inside the named parent; do not create a file.
- **ALIAS**: add a genuine alternate name to the canonical existing or proposed
  record; do not create a file.
- **ENRICH**: a standard related structure that follows the core batch and
  brings its own required dependency closure.

The identifiers below are reserved by this plan. Authors should not invent
competing IDs without first updating this manifest.

## Scope corrections and deduplication decisions

1. The ordinary category of smooth manifolds has all smooth maps as morphisms.
   Restricting to diffeomorphisms gives its maximal subgroupoid
   \(\mathbf{Man}^{\simeq}\), while \(\operatorname{Diff}(M)\) is the
   automorphism group of one object.
2. “Holomorphic manifold” is an alias of **complex manifold**, not a separate
   object. Holomorphic charts define the objects; holomorphic maps are the
   morphisms.
3. The clean characteristic-zero equivalence is between finite-dimensional Lie
   algebras and formally smooth finite-dimensional **formal groups**. A formal
   group law is a coordinate presentation. The general theory must not be
   restricted to one-dimensional commutative formal group laws.
4. \(SL(2,\mathbb C)\to SO^+(1,3)\) is a double cover with kernel
   \(\{\pm I\}\), not an isomorphism. The induced statement is
   \[
   PSL(2,\mathbb C)_{\mathbb R}\cong SO^+(1,3)
   \]
   in the category of real Lie groups.
5. \(PGL_n\) is the quotient of \(GL_n\) by its scalar center; \(PSL_n\) is the
   quotient of \(SL_n\) by its center. They agree over \(\mathbb C\), but not
   over every field. In particular, \(PSL_2(\mathbb R)\) is the identity
   component of \(PGL_2(\mathbb R)\).
6. The Riemann sphere, extended complex plane, and analytic
   \(\mathbb P^1(\mathbb C)\) are one analytic object. The existing
   scheme-theoretic projective-space knowl remains distinct and should link to
   it.
7. “Clifford representation” remains an alias of the existing Clifford-module
   knowl. “Grassmann algebra” is an alias of exterior algebra. A Clifford
   algebra is naturally \(\mathbb Z/2\)-graded but is generally not
   supercommutative.
8. The existing Dirac-operator knowl is Riemannian and elliptic. The
   relativistic Minkowski/Lorentzian Dirac operator and Dirac equation require
   distinct IDs.
9. Hamiltonian diffeomorphisms are self-maps of a fixed symplectic manifold.
   There is no standard cross-object “category with Hamiltonian
   symplectomorphisms” parallel to the category with symplectic maps.
10. Serre–Swan is already present and correctly states a covariant equivalence
    for vector bundles over a fixed compact base. It should be linked, not
    regenerated.
11. Semirings and hyperrings are incomparable generalizations of rings.
    Ordered blueprints provide a common ambient category, not an equivalence
    between semirings and hyperrings.
12. There is no standard “Riemann sphere–Möbius group–Langlands conjecture.”
    The established links are that \(\mathbb P^1\) is a possible geometric
    Langlands base curve and a rank-one flag variety, while \(PGL_2\) is both
    \(\operatorname{Aut}_{\mathrm{hol}}(\mathbb P^1)\) and the Langlands dual
    group of \(SL_2\). These roles must not be conflated.

## Batch 0 — shared missing foundations

These records are shared by two or more later neighborhoods and should be
completed first.

| Ref | Status | Canonical ID | Kind | Direct role |
|---|---|---|---|---|
| F01 | NEW | `algebra-category-theory/monoidal-category` | definition | Parent for algebra objects and super tensor products. |
| F02 | NEW | `algebra-category-theory/symmetric-monoidal-category` | definition | Parent for super vector spaces and the Koszul braiding. |
| F03 | NEW | `algebra-category-theory/algebra-object` | definition | Categorical formulation of superalgebras. |
| F04 | NEW | `algebra-category-theory/group-object` | definition | Shared by formal groups and Lie supergroups. |
| F05 | NEW | `algebra-category-theory/groupoid` | definition | Required for diffeomorphism and structure-isomorphism cores. |
| F06 | NEW | `algebra-category-theory/core-of-a-category` | construction | Reusable maximal subgroupoid instead of redefining it for each geometry. |
| F07 | NEW | `linear-algebra/quadratic-form` | definition | Missing prerequisite of the existing Clifford algebra. |
| F08 | NEW | `linear-algebra/signature-of-symmetric-bilinear-form` | definition | Lorentz and indefinite spin conventions. |
| F09 | NEW | `linear-algebra/hermitian-matrix` | definition | Hermitian \(2\times2\) model of Minkowski space. |
| F10 | NEW | `linear-algebra/realification-of-a-complex-vector-space` | construction | Dimension-doubling scalar restriction. |
| F11 | NEW | `algebra-modules/tensor-algebra` | definition | Missing \(T(V)\) dependency for Clifford and enveloping algebras. |
| F12 | NEW | `algebra-modules/symmetric-algebra` | definition | Super symmetric/exterior comparison. |
| F13 | NEW | `algebra-modules/exterior-algebra` | definition | Alias “Grassmann algebra”; Clifford associated graded. |
| F14 | NEW | `topology/simply-connected-space` | definition | Cauchy theory, Riemann mapping, and covering arguments. |
| F15 | NEW | `topology/one-point-compactification` | construction | \(\mathbb C\cup\{\infty\}\). |
| F16 | NEW | `algebra-groups/commutative-monoid` | definition | Additive object underlying a semiring. |
| F17 | NEW | `algebra-groups/ordered-abelian-group` | definition | Value groups and tropical algebra. |

## Batch 1 — formal power series, formal groups, and Lie algebras

House scope: a characteristic-zero field \(k\), especially
\(\mathbb R\) or \(\mathbb C\); finite-dimensional formally smooth formal
groups whose pointed formal scheme is a formal disc. A later generalization may
replace finite-dimensional vector spaces by finite projective modules over a
\(\mathbb Q\)-algebra.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| FG01 | EXPAND | `algebra-rings/formal-power-series-ring` | definition | Add augmentation ideal, units, coefficientwise equality, adic topology, and multivariable link. |
| FG02 | NEW | `algebra-rings/multivariable-formal-power-series-ring` | definition | FG01; define \(R[[X_1,\ldots,X_n]]\). |
| FG03 | NEW | `algebra-commutative/i-adic-topology` | definition | Ideals and topological rings. |
| FG04 | NEW | `algebra-commutative/i-adic-completion` | construction | FG03; \(\widehat A=\varprojlim A/I^n\). |
| FG05 | NEW | `algebra-rings/substitution-of-formal-power-series` | construction | FG02–FG04; tuples with vanishing constant term. |
| FG06 | NEW | `algebra-rings/formal-inverse-function-theorem` | theorem | FG05; invertible linear term criterion. |
| FG07 | NEW | `formal-groups/formal-group-law` | definition | General \(n\)-dimensional, possibly noncommutative law. |
| FG08 | NEW | `formal-groups/one-dimensional-formal-group-law` | definition | Classical commutative convention, explicitly narrower than FG07. |
| FG09 | NEW | `formal-groups/formal-group-law-morphism` | definition | Homomorphism, isomorphism, strict isomorphism, coordinate change. |
| FG10 | NEW | `formal-groups/additive-and-multiplicative-formal-group-laws` | example | Standard one-dimensional examples. |
| FG11 | NEW | `formal-groups/formal-group-logarithm` | theorem/construction | Commutative laws over a \(\mathbb Q\)-algebra. |
| FG12 | NEW | `algebraic-geometry-foundations/formal-spectrum` | definition | Adic affine formal geometry. |
| FG13 | NEW | `algebraic-geometry-foundations/formal-scheme` | definition | Intrinsic home for coordinate-independent formal groups. |
| FG14 | NEW | `formal-groups/formal-affine-space` | definition | \(\operatorname{Spf} k[[X_1,\ldots,X_n]]\), formal disc, tangent dimension. |
| FG15 | NEW | `formal-groups/formal-group` | definition | Group object in formal schemes; formally smooth finite-dimensional subcategory. |
| FG16 | NEW | `formal-groups/formal-group-laws-as-coordinates` | theorem | Equivalence between formal discs with chosen coordinates and formal group laws. |
| FG17 | EXPAND | `lie-groups/lie-algebra` | definition | State base field and finite-dimensional category conventions. |
| FG18 | LINK | `lie-groups/lie-algebra-homomorphism` | definition | Existing morphism record is adequate. |
| FG19 | EXPAND | `lie-groups/baker-campbell-hausdorff-formula` | theorem | Add a purely formal completed-Lie-series section; preserve analytic local statement. |
| FG20 | NEW | `formal-groups/tangent-lie-algebra` | construction | Tangent space, invariant derivations, functorial bracket. |
| FG21 | NEW | `formal-groups/lie-algebra-formal-group-equivalence` | theorem | Main tangent/BCH equivalence in characteristic zero. |
| FG22 | NEW | `formal-groups/formal-completion-at-identity` | construction | Bridge from Lie/algebraic groups; explain loss of global topology. |
| FG23 | NEW | `formal-groups/positive-characteristic-warning` | comparison | Heights and \(p\)-structure obstruct tangent classification. |
| FG24 | NEW | `formal-groups` | section/index | Subject navigation and convention record. |
| FG25 | ENRICH | `formal-groups/coordinate-hopf-algebra` | definition/equivalence | Continuous comultiplication and completed tensor product. |
| FG26 | ENRICH | `formal-groups/distribution-algebra` | theorem | Characteristic-zero comparison with \(U(\mathfrak g)\). |
| FG27 | ENRICH | `formal-groups/complete-filtered-lie-algebra-bch-group` | theorem | Pronilpotent generalization beyond the requested finite-dimensional case. |

## Batch 2 — one-variable complex analysis

The existing complex-geometry knowls remain canonical. In particular,
“holomorphic function” is the scalar-valued case of the existing holomorphic
map, not a competing foundation page.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| CA01 | NEW | `complex-analysis/complex-domain` | definition | Open connected subset of \(\mathbb C\); avoids collision with function domain. |
| CA02 | NEW | `complex-analysis/complex-derivative` | definition | Complex difference quotient. |
| CA03 | NEW | `complex-analysis/cauchy-riemann-equations` | definition | CA02 and real partial derivatives. |
| CA04 | NEW | `complex-analysis/cauchy-riemann-criterion` | theorem | State the necessary \(C^1\)/real differentiability hypothesis. |
| CA05 | EXPAND | `differential-geometry/holomorphic-map` | definition | Complex derivative, scalar-valued functions, chart invariance, analytic terminology. |
| CA06 | EXPAND | `real-analysis/power-series` | definition | Permit real or complex coefficients; preserve convergent/formal distinction. |
| CA07 | NEW | `complex-analysis/complex-contour-integral` | definition | \(\int_\gamma f(z)\,dz\). |
| CA08 | NEW | `complex-analysis/winding-number` | definition | Closed curves, index about a point. |
| CA09 | NEW | `complex-analysis/cauchy-integral-theorem` | theorem | Homotopy/simply-connected forms with hypotheses separated. |
| CA10 | NEW | `complex-analysis/cauchy-integral-formula` | theorem | CA08–CA09. |
| CA11 | NEW | `complex-analysis/holomorphic-functions-are-analytic` | theorem | Local convergent power-series expansion. |
| CA12 | NEW | `complex-analysis/identity-theorem` | theorem | Accumulation-point uniqueness on a domain. |
| CA13 | NEW | `complex-analysis/maximum-modulus-principle` | theorem | Local/global forms. |
| CA14 | NEW | `complex-analysis/open-mapping-theorem` | theorem | Explicitly disambiguate Banach–Schauder open mapping. |
| CA15 | NEW | `complex-analysis/liouville-theorem` | theorem | Bounded entire functions are constant. |
| CA16 | NEW | `complex-analysis/fundamental-theorem-of-algebra-complex-analysis` | theorem | Complex-analytic proof route; link algebraic formulations. |
| CA17 | NEW | `complex-analysis/analytic-continuation` | definition | Germ/overlap continuation and identity-theorem uniqueness. |
| CA18 | NEW | `complex-analysis/laurent-series` | definition/theorem | Annuli and coefficient formula. |
| CA19 | NEW | `complex-analysis/isolated-singularity-classification` | theorem | Removable singularities, poles, essential singularities. |
| CA20 | NEW | `complex-analysis/order-of-zero-or-pole` | definition | Local factorization. |
| CA21 | NEW | `complex-analysis/residue` | definition | Laurent coefficient. |
| CA22 | NEW | `complex-analysis/meromorphic-function` | definition | Functions with poles; later link to maps into the Riemann sphere. |
| CA23 | NEW | `complex-analysis/residue-theorem` | theorem | Winding-number form. |
| CA24 | NEW | `complex-analysis/argument-principle` | theorem | Zeros and poles with multiplicity. |
| CA25 | NEW | `differential-geometry/conformal-map` | definition | General Riemannian definition plus oriented Riemann-surface characterization. |
| CA26 | NEW | `complex-analysis/riemann-mapping-theorem` | theorem | Proper simply connected plane domains. |
| CA27 | NEW | `differential-geometry/category-of-complex-manifolds` | definition | Holomorphic maps; biholomorphisms are isomorphisms. |
| CA28 | NEW | `complex-analysis` | section/index | New subject index. |

## Batch 3 — projective geometry, the Riemann sphere, and Möbius geometry

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| PG01 | NEW | `linear-algebra/semilinear-map` | definition | Field automorphisms and semilinear maps. |
| PG02 | EXPAND | `algebraic-geometry-foundations/projective-space` | definition | \(P(V)\), charts, homogeneous coordinates, line/quotient convention warning. |
| PG03 | NEW | `algebraic-geometry-foundations/projective-line` | definition | \(\mathbb P^1(k)\), two affine charts, point at infinity. |
| PG04 | NEW | `algebraic-geometry-foundations/projective-geometry` | definition/index | Points, projective lines, incidence, projective subspaces. |
| PG05 | NEW | `algebraic-geometry-foundations/projective-transformation` | definition | Global maps induced by invertible linear maps. |
| PG06 | NEW | `algebra-groups/projective-general-linear-group` | definition | \(PGL(V)=GL(V)/(k^\times I)\). |
| PG07 | NEW | `algebra-groups/projective-special-linear-group` | definition | \(PSL_n(k)=SL_n(k)/Z(SL_n(k))\). |
| PG08 | NEW | `algebra-groups/pgl-psl-comparison` | theorem | Exact determinant-mod-\(n\)th-powers comparison. |
| PG09 | NEW | `algebraic-geometry-foundations/projective-semilinear-group` | definition | \(P\Gamma L(V)\). |
| PG10 | NEW | `algebraic-geometry-foundations/fundamental-theorem-of-projective-geometry` | theorem | Collineations in dimension at least two projectively. |
| PG11 | NEW | `lie-groups/projective-general-linear-lie-group` | definition | Real/complex Lie structures and dimensions. |
| PG12 | NEW | `lie-groups/projective-special-linear-lie-group` | definition | Finite-center quotient and component structure. |
| PG13 | NEW | `differential-geometry/real-projective-space` | definition | Smooth \(RP^n\), quotient and homogeneous descriptions. |
| PG14 | NEW | `differential-geometry/complex-projective-space` | definition | Smooth/complex \(CP^n\), Kähler and homogeneous descriptions. |
| PG15 | NEW | `complex-analysis/riemann-sphere` | definition | \(\widehat{\mathbb C}\cong CP^1\cong S^2\). |
| PG16 | NEW | `complex-analysis/mobius-transformation` | definition | Alias linear/fractional linear transformation. |
| PG17 | NEW | `complex-analysis/mobius-transformation-group` | definition | \(PGL_2(\mathbb C)\cong PSL_2(\mathbb C)\) action. |
| PG18 | NEW | `complex-analysis/automorphisms-of-riemann-sphere` | theorem | Every holomorphic automorphism is Möbius. |
| PG19 | NEW | `complex-analysis/cross-ratio` | definition | Ordering convention, infinity, permutation values. |
| PG20 | NEW | `complex-analysis/cross-ratio-characterization-of-mobius-transformations` | theorem | Invariance and sharp three-point action. |
| PG21 | NEW | `complex-analysis/schwarzian-derivative` | definition | Locally univalent maps. |
| PG22 | NEW | `complex-analysis/schwarzian-chain-rule-and-mobius-characterization` | theorem | Chain rule and \(S(f)=0\) characterization. |
| PG23 | SECTION | `complex-analysis/schwarzian-chain-rule-and-mobius-characterization` | section | Equal Schwarzians differ locally by postcomposition with Möbius maps. |
| PG24 | SECTION | `complex-analysis/mobius-transformation-group` | section | Orientation-preserving conformal group of the round sphere; anti-Möbius warning. |

## Batch 4 — complex versus real \(SL(2,\mathbb C)\) and Lorentz geometry

Fix one signature convention across this batch. The Hermitian-matrix determinant
model, spin covering, wave operator, and gamma-matrix relations must use the
same convention.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| LG01 | NEW | `lie-groups/complex-lie-group` | definition | Holomorphic multiplication/inversion and complex dimension. |
| LG02 | NEW | `lie-groups/underlying-real-lie-group` | construction | Forget complex structure; double the real dimension. |
| LG03 | NEW | `lie-groups/underlying-real-lie-algebra` | construction | Same bracket under scalar restriction. |
| LG04 | NEW | `lie-groups/complexification-of-a-real-lie-algebra` | construction | Distinguish complexification from underlying-real algebra. |
| LG05 | NEW | `lie-groups/lie-functor-commutes-with-realification` | theorem | \(\operatorname{Lie}(G_{\mathbb R})\cong\operatorname{Lie}(G)_{\mathbb R}\). |
| LG06 | NEW | `lie-groups/sl2-complex-as-real-and-complex-lie-group` | example | Complex dimension \(3\), underlying real dimension \(6\). |
| LG07 | NEW | `lie-groups/psl2-complex` | example | Quotient by \(\{\pm I\}\), complex and underlying-real views. |
| LG08 | NEW | `linear-algebra/minkowski-vector-space` | definition | \(\mathbb R^{1,3}\), quadratic form, null/timelike/spacelike vectors. |
| LG09 | NEW | `differential-geometry/time-orientation` | definition | Future cone and orthochronous transformations. |
| LG10 | NEW | `lie-groups/proper-orthochronous-lorentz-group` | definition | Focused \(SO^+(1,3)\) node. |
| LG11 | NEW | `lie-groups/indefinite-spin-group` | definition | \(\operatorname{Pin}(p,q)\), \(\operatorname{Spin}(p,q)\), identity-component cautions. |
| LG12 | NEW | `lie-groups/hermitian-matrix-model-of-minkowski-space` | construction | \(X\mapsto AXA^\dagger\), determinant quadratic form. |
| LG13 | NEW | `lie-groups/sl2c-spin-cover-of-lorentz-group` | theorem | Surjection with kernel \(\{\pm I\}\); include real Lie-algebra isomorphism. |
| LG14 | NEW | `lie-groups/psl2c-proper-lorentz-isomorphism` | theorem | Exact requested real-Lie-group isomorphism. |
| LG15 | NEW | `differential-geometry/celestial-sphere` | construction | Projectivized future null cone \(S^2\cong CP^1\). |
| LG16 | NEW | `lie-groups/celestial-sphere-and-mobius-action` | theorem | Transport Lorentz action to Möbius action. |
| LG17 | CORRECT | `lie-groups/special-linear-group` | definition | Separate complex dimension from underlying real dimension. |
| LG18 | EXPAND | `lie-groups/special-linear-lie-algebra` | definition | Explicit \(\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\) dimensions. |
| LG19 | EXPAND | `lie-groups/lorentz-group` | definition | Link general group to \(SO^+(1,3)\), time orientation, and spin cover. |
| LG20 | EXPAND | `lie-groups/spin-group` | definition | Preserve positive-definite core; link rather than silently absorb indefinite groups. |
| LG21 | ENRICH | `algebraic-geometry-foundations/weil-restriction` | definition | Explain relation to, but difference from, forgetting complex structure. |
| LG22 | ENRICH | `differential-geometry/hyperbolic-three-space` | definition | Additional \(PSL_2(\mathbb C)\) action and automorphic context. |

## Batch 5 — super linear algebra, Clifford algebras, and spinors

Use even linear maps as the morphisms in \(\mathbf{SuperVect}\); odd maps live
in the internal Hom. Super sign statements require characteristic not equal to
\(2\), unless explicitly reformulated.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| SC01 | NEW | `supergeometry/super-vector-space` | definition | Alias \(\mathbb Z/2\)-graded vector space. |
| SC02 | NEW | `supergeometry/parity-shift` | construction | Parity reversal functor \(\Pi\). |
| SC03 | NEW | `supergeometry/category-of-super-vector-spaces` | definition | Tensor product, even maps, Koszul braiding. |
| SC04 | SECTION | `supergeometry/category-of-super-vector-spaces` | section | Koszul sign rule and odd internal maps. |
| SC05 | NEW | `supergeometry/superalgebra` | definition | Algebra object in SuperVect. |
| SC06 | NEW | `supergeometry/supercommutative-algebra` | definition | \(ab=(-1)^{|a||b|}ba\). |
| SC07 | NEW | `supergeometry/supermodule` | definition | Graded modules over a superalgebra. |
| SC08 | NEW | `supergeometry/symmetric-algebra-of-a-super-vector-space` | theorem/construction | \(\operatorname{Sym}(V_{\bar0})\otimes\Lambda(V_{\bar1})\). |
| SC09 | NEW | `supergeometry/lie-superalgebra` | definition | Graded skew symmetry and Jacobi identity. |
| SC10 | SECTION | `supergeometry/lie-superalgebra` | section | Morphisms, representations, and adjoint action. |
| SC11 | NEW | `supergeometry/universal-enveloping-algebra-of-lie-superalgebra` | definition | Tensor quotient with supercommutator relations. |
| SC12 | EXPAND | `differential-geometry/clifford-algebra` | definition | Link quadratic/tensor algebra; distinguish parity grading, filtration, supercommutativity. |
| SC13 | NEW | `differential-geometry/associated-graded-clifford-algebra` | theorem | \(\operatorname{gr}\operatorname{Cl}(V,q)\cong\Lambda V\). |
| SC14 | NEW | `differential-geometry/clifford-algebra-as-super-enveloping-quotient` | theorem | Central even generator and odd quadratic bracket. |
| SC15 | EXPAND | `differential-geometry/clifford-module` | definition | Relate graded Clifford modules to supermodules. |
| SC16 | NEW | `differential-geometry/spinor-module` | definition | Clifford spinor module and restricted spin representation. |
| SC17 | SECTION | `differential-geometry/spinor-module` | section | Dirac, Weyl, Majorana, and Majorana–Weyl convention table. |
| SC18 | NEW | `mathematical-physics/gamma-matrices` | definition | Basis-dependent Clifford representation matrices. |
| SC19 | EXPAND | `differential-geometry/spinor-bundle` | definition | Link missing spinor-module dependency; separate signatures. |
| SC20 | ALIAS | `differential-geometry/clifford-module` | alias | “Clifford representation.” |
| SC21 | ALIAS | `algebra-modules/exterior-algebra` | alias | “Grassmann algebra.” |

## Batch 6 — superspaces, supermanifolds, and Lie supergroups

The first pass uses finite-dimensional smooth real Berezin–Leites/Kostant
supermanifolds. Complex-analytic, algebraic, DeWitt, and Rogers models should be
identified but not merged.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| SG01 | NEW | `supergeometry/superspace` | definition | Locally superringed space and morphisms. |
| SG02 | NEW | `supergeometry/superdomain` | definition | \(C^\infty(U)\otimes\Lambda(\mathbb R^q)^*\). |
| SG03 | NEW | `supergeometry/supermanifold` | definition | Locally modeled on superdomains. |
| SG04 | NEW | `supergeometry/split-supermanifold` | definition | Exterior algebra of a vector bundle. |
| SG05 | NEW | `supergeometry/batchelor-theorem` | theorem | Smooth real supermanifolds split noncanonically. |
| SG06 | NEW | `supergeometry/functor-of-points-of-supermanifold` | definition | Relate functorial and ringed-space viewpoints. |
| SG07 | NEW | `supergeometry/lie-supergroup` | definition | Group object in the chosen supermanifold category. |
| SG08 | NEW | `supergeometry/lie-superalgebra-of-lie-supergroup` | construction | Tangent Lie superalgebra. |
| SG09 | NEW | `supergeometry/super-harish-chandra-pair` | definition | Lie group, Lie superalgebra, compatible action. |
| SG10 | NEW | `supergeometry/lie-supergroups-and-super-harish-chandra-pairs` | theorem | State the exact smooth/analytic category. |
| SG11 | NEW | `supergeometry` | section/index | Subject navigation and model conventions. |
| SG12 | ENRICH | `mathematical-physics/supertranslation-algebra` | definition | Spinor bilinear as odd-odd bracket. |
| SG13 | ENRICH | `mathematical-physics/super-poincare-algebra` | definition | Supersymmetry extension of the Poincaré algebra. |
| SG14 | ENRICH | `supergeometry/super-minkowski-space` | definition | Physics superspace, distinct from a general superspace. |

## Batch 7 — Lorentzian operators and relativistic field equations

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| PDE01 | NEW | `differential-geometry/pseudo-riemannian-manifold` | definition | Smooth nondegenerate symmetric metric of fixed signature. |
| PDE02 | NEW | `differential-geometry/lorentzian-manifold` | definition | Index-one pseudo-Riemannian manifold; separate time orientation. |
| PDE03 | NEW | `mathematical-physics/minkowski-spacetime` | definition | Affine/Lorentzian realization of LG08. |
| PDE04 | NEW | `differential-geometry/laplace-beltrami-operator` | definition | Riemannian and pseudo-Riemannian metric operator. |
| PDE05 | NEW | `mathematical-physics/dalembert-operator` | definition | \(\Box_g\), d’Alembertian, scalar wave operator. |
| PDE06 | NEW | `mathematical-physics/normally-hyperbolic-operator` | definition | Principal-symbol characterization. |
| PDE07 | NEW | `mathematical-physics/wave-equation` | definition | Massless scalar equation. |
| PDE08 | NEW | `mathematical-physics/klein-gordon-operator` | definition | \(\Box_g+m^2\) with declared sign convention. |
| PDE09 | NEW | `mathematical-physics/klein-gordon-equation` | definition | Correct spelling “Gordon”; massive/massless cases. |
| PDE10 | NEW | `differential-geometry/lorentzian-spin-structure` | definition | Signature-sensitive spin lift. |
| PDE11 | NEW | `differential-geometry/lorentzian-spinor-bundle` | definition | Pseudo-Riemannian Clifford module bundle. |
| PDE12 | NEW | `mathematical-physics/minkowski-dirac-operator` | definition | Flat relativistic operator; distinct from Riemannian Dirac. |
| PDE13 | NEW | `mathematical-physics/dirac-equation` | definition | Massive/massless classical spinor equation. |
| PDE14 | NEW | `mathematical-physics/dirac-klein-gordon-factorization` | theorem | Flat free factorization; warn about curvature/gauge terms. |
| PDE15 | EXPAND | `noncommutative-geometry/dirac-operator` | definition | Add explicit Riemannian-versus-Lorentzian cross-link. |
| PDE16 | NEW | `mathematical-physics` | section/index | Physics convention and navigation index. |

## Batch 8 — manifold categories, \(C^\infty\)-rings, and Serre–Swan

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| CAT01 | EXPAND | `differential-geometry/category-of-smooth-manifolds` | definition | Contrast all smooth maps with the maximal diffeomorphism subgroupoid. |
| CAT02 | NEW | `differential-geometry/diffeomorphism-groupoid-of-smooth-manifolds` | definition | \(\mathbf{Man}^{\simeq}\). |
| CAT03 | NEW | `differential-geometry/c-infinity-ring` | definition | Operations induced by all smooth maps \(\mathbb R^n\to\mathbb R\). |
| CAT04 | NEW | `differential-geometry/smooth-maps-from-smooth-function-algebras` | theorem | \(C^\infty(-)\) is contravariant and fully faithful onto its image. |
| CAT05 | NEW | `algebraic-geometry-foundations/ringed-space` | definition | Missing base for module sheaves. |
| CAT06 | NEW | `differential-geometry/locally-c-infinity-ringed-space` | definition | Structure-preserving refinement of locally ringed spaces. |
| CAT07 | EXPAND | `differential-geometry/algebra-of-smooth-functions` | definition | Canonical \(C^\infty\)-ring structure and pullback. |
| CAT08 | EXPAND | `differential-geometry/sheaf-of-smooth-functions` | definition | Locally \(C^\infty\)-ringed interpretation. |
| CAT09 | NEW | `algebraic-geometry-foundations/sheaf-of-modules` | definition | Modules over a sheaf of rings. |
| CAT10 | NEW | `algebraic-geometry-foundations/locally-free-sheaf` | definition | Finite-rank locally free module sheaf. |
| CAT11 | NEW | `fiber-bundles/sheaf-of-smooth-sections` | definition | Distinguish section sheaf from global section module. |
| CAT12 | NEW | `fiber-bundles/category-of-vector-bundles-over-a-manifold` | definition | Fixed-base maps covering \(\operatorname{id}_M\). |
| CAT13 | NEW | `algebra-modules/category-of-finitely-generated-projective-modules` | definition | \(\mathbf{Proj}(A)\). |
| CAT14 | NEW | `fiber-bundles/vector-bundles-and-locally-free-sheaves` | theorem | Sheaf-level equivalence, independent of compact global sections. |
| CAT15 | EXPAND | `fiber-bundles/vector-bundle-morphism` | definition | Distinguish fixed-base and varying-base categories. |
| CAT16 | EXPAND | `fiber-bundles/module-of-smooth-sections` | definition | Global module versus sheaf of sections. |
| CAT17 | CORRECT | `fiber-bundles/section-module-is-finitely-generated-projective` | theorem | Change erroneous front-matter kind from definition to theorem. |
| CAT18 | LINK | `fiber-bundles/serre-swan-theorem` | theorem | Already correct; link CAT12–CAT14 only. |

## Batch 9 — symplectic, Hamiltonian, Kähler, and hyperkähler morphisms

Most object-level definitions are already strong. This batch supplies
categorical organization and convention-sensitive morphisms.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| GEO01 | EXPAND | `differential-geometry/almost-complex-structure` | definition | Add the \(df\circ J_M=J_N\circ df\) morphism equation. |
| GEO02 | EXPAND | `differential-geometry/integrable-almost-complex-structure` | definition/theorem | Newlander–Nirenberg and regularity scope. |
| GEO03 | EXPAND | `differential-geometry/complex-manifold` | definition | Progressive treatment; add “holomorphic manifold” alias. |
| GEO04 | EXPAND | `differential-geometry/symplectic-manifold` | definition | Progressive treatment and neighborhood links. |
| GEO05 | CORRECT | `differential-geometry/symplectomorphism` | definition | Fix Darboux link to the symplectic theorem. |
| GEO06 | NEW | `differential-geometry/category-of-symplectic-manifolds` | definition | Symplectic maps; isomorphisms are symplectomorphisms. |
| GEO07 | SECTION | `differential-geometry/category-of-symplectic-manifolds` | section | Maximal symplectomorphism subgroupoid; do not call it a symplectic groupoid. |
| GEO08 | NEW | `differential-geometry/symplectomorphism-group` | definition | \(\operatorname{Symp}(M,\omega)\) and identity component. |
| GEO09 | NEW | `differential-geometry/symplectic-isotopy` | definition | Closed contraction one-forms. |
| GEO10 | NEW | `differential-geometry/hamiltonian-isotopy` | definition | Exact contraction one-forms and support convention. |
| GEO11 | EXPAND | `differential-geometry/hamiltonian-diffeomorphism` | definition | Link isotopies, flux, and \(\operatorname{Ham}(M,\omega)\). |
| GEO12 | NEW | `differential-geometry/flux-homomorphism` | definition | Define on path classes/universal cover. |
| GEO13 | NEW | `differential-geometry/flux-group` | definition | Endpoint obstruction in \(H^1/\Gamma_\omega\). |
| GEO14 | NEW | `differential-geometry/biholomorphism-group` | definition | \(\operatorname{Aut}_{\mathrm{hol}}(X)\). |
| GEO15 | NEW | `differential-geometry/riemannian-isometric-immersion` | definition | Pullback metric; diffeomorphic case as isometry. |
| GEO16 | NEW | `differential-geometry/holomorphic-isometric-immersion` | definition | Strict Hermitian/Kähler structure preservation. |
| GEO17 | NEW | `differential-geometry/morphisms-between-kahler-manifolds` | convention/overview | Separate holomorphic maps, strict immersions, and isomorphisms. |
| GEO18 | NEW | `differential-geometry/triholomorphic-map` | definition | Preserve ordered \(I,J,K\). |
| GEO19 | NEW | `differential-geometry/hyperkahler-isometry` | definition | Strict versus \(SO(3)\)-rotating convention. |
| GEO20 | NEW | `differential-geometry/morphisms-between-hyperkahler-manifolds` | convention/overview | Separate hypercomplex, metric, and groupoid choices. |
| GEO21 | LINK | `differential-geometry/kahler-manifold` | definition | Strong existing object record; add morphism links only. |
| GEO22 | LINK | `differential-geometry/hyperkahler-manifold` | definition | Strong existing object record; add morphism links only. |

## Batch 10 — semirings, hyperrings, hyperfields, and tropical algebra

House conventions: commutative unital semirings; a semifield is a nontrivial
commutative semiring whose nonzero elements form a multiplicative group; a
Krasner hyperring has a canonical commutative additive hypergroup and
single-valued multiplication.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| H01 | NEW | `algebra-rings/semiring` | definition | Additive commutative monoid and multiplicative monoid. |
| H02 | NEW | `algebra-rings/commutative-semiring` | definition | Commutative multiplication convention. |
| H03 | NEW | `algebra-rings/semiring-homomorphism` | definition | Unit-preserving house convention. |
| H04 | NEW | `algebra-rings/semifield` | definition | Nonzero multiplicative group; additive inverses not required. |
| H05 | NEW | `algebra-rings/idempotent-semiring` | definition | \(a+a=a\). |
| H06 | NEW | `algebra-rings/natural-order-of-idempotent-semiring` | proposition | \(a\le b\iff a+b=b\). |
| H07 | NEW | `algebra-rings/idempotent-semifield` | definition | Idempotent semifield. |
| H08 | NEW | `algebra-rings/boolean-semifield` | example | Two-element idempotent semifield. |
| H09 | NEW | `algebra-rings/tropical-semifield` | example | Max-plus house convention; min-plus/order warning. |
| H10 | NEW | `algebra-hyperstructures/hyperoperation` | definition | Nonempty-valued operation into a power set. |
| H11 | NEW | `algebra-hyperstructures/canonical-hypergroup` | definition | Identity, unique inverse, associativity, reversibility. |
| H12 | NEW | `algebra-hyperstructures/hyperring` | definition | Krasner convention and equality distributivity. |
| H13 | NEW | `algebra-hyperstructures/hyperfield` | definition | Hyperring with nonzero multiplicative group. |
| H14 | NEW | `algebra-hyperstructures/hyperring-homomorphism` | definition | Weak inclusion convention; identify strong morphisms. |
| H15 | NEW | `algebra-hyperstructures/quotient-hyperring` | construction | \(R/G\) for a multiplicative subgroup. |
| H16 | NEW | `algebra-hyperstructures/krasner-hyperfield` | example | Field quotient and two-element comparison. |
| H17 | NEW | `algebra-hyperstructures/sign-hyperfield` | example | Signs and quotient construction. |
| H18 | NEW | `algebra-hyperstructures/tropical-hyperfield` | example | Multivalued tropical addition. |
| H19 | NEW | `algebra-fields-galois/valuation-on-a-field` | definition | Krull valuation and valued field. |
| H20 | NEW | `algebra-hyperstructures/valuation-as-tropical-hyperfield-morphism` | proposition | Non-Archimedean valuation as hyperfield morphism. |
| H21 | NEW | `algebra-hyperstructures/fields-semifields-and-hyperfields` | comparison | Precise inclusions and non-inclusions. |
| H22 | NEW | `algebra-hyperstructures/tropical-hyperfield-versus-semifield` | comparison | Same carrier/multiplication, different addition. |

## Batch 11 — blueprints and ordered blueprints

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| B01 | NEW | `algebra-rings/ordered-semiring` | definition | Semiring with compatible partial order. |
| B02 | NEW | `algebraic-geometry-foundations/blueprint` | definition | Multiplicative monoid with formal additive relations. |
| B03 | NEW | `algebraic-geometry-foundations/ordered-blueprint` | definition | Ordered-semiring and monoid presentation. |
| B04 | NEW | `algebraic-geometry-foundations/semirings-and-monoids-as-blueprints` | construction | Canonical embeddings. |
| B05 | NEW | `algebraic-geometry-foundations/hyperrings-as-ordered-blueprints` | construction | Fully faithful hyperring embedding. |
| B06 | NEW | `algebraic-geometry-foundations/ordered-blueprint-with-unique-weak-inverses` | definition | Current title; legacy alias “pasteurized ordered blueprint.” |
| B07 | NEW | `algebra-hyperstructures/comparison-map` | comparison/guide | Semirings, hyperrings, hyperfields, tropical objects, ordered blueprints. |
| B08 | NEW | `algebra-hyperstructures` | section/index | Requested durable section and convention map. |
| B09 | ENRICH | `algebraic-geometry-foundations/pasteurization-of-ordered-blueprint` | construction | Reflection into unique-weak-inverse objects. |
| B10 | ENRICH | `algebra-hyperstructures/tract` | definition | Needed for matroids over partial hyperstructures. |
| B11 | ENRICH | `algebra-hyperstructures/pasture` | definition | Version-sensitive; do not identify with every ordered blue field. |
| B12 | ENRICH | `algebraic-geometry-foundations/blue-scheme` | definition | Scheme-theoretic layer built from blueprint spectra. |

## Batch 12 — rank-one Langlands context

This batch records established context, not a conjectural identification.
General geometric Langlands has a much larger dependency closure and should be
undertaken only as its own expansion.

| Ref | Status | Canonical ID | Kind | Direct prerequisites or action |
|---|---|---|---|---|
| LAN01 | NEW | `algebraic-geometry-foundations/borel-subgroup` | definition | Rank-one flag variety dependency. |
| LAN02 | NEW | `algebraic-geometry-foundations/flag-variety` | definition | \(G/B\). |
| LAN03 | NEW | `algebraic-geometry-foundations/projective-line-as-rank-one-flag-variety` | theorem/example | \(\mathbb P^1\cong SL_2/B\cong PGL_2/B\). |
| LAN04 | EXPAND | `langlands-letter/knowls/langlands-dual-group` | definition | Add \(\widehat{SL_2}=PGL_2\) and \(\widehat{PGL_2}=SL_2\). |
| LAN05 | EXPAND | `langlands-letter/knowls/root-vs-weight-lattice-isogeny` | definition | Add the type-\(A_1\) central isogeny. |
| LAN06 | SECTION | `lie-groups/psl2-complex` | context section | Distinguish Möbius automorphism group, reductive group, and Langlands-dual roles. |
| LAN07 | NEW | `algebraic-geometry-foundations/algebraic-curve` | definition | First dependency of a future general geometric-Langlands batch. |
| LAN08 | NEW | `algebraic-geometry-foundations/smooth-projective-curve` | definition | Base curve \(X\). |
| LAN09 | ENRICH | `fiber-bundles/local-system` | definition | Dual-side local systems. |
| LAN10 | ENRICH | `algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve` | definition | Automorphic-side \(\operatorname{Bun}_G(X)\). |
| LAN11 | ENRICH | `algebraic-geometry-foundations/d-module` | definition | Sheaf-theoretic automorphic side. |
| LAN12 | ENRICH | `langlands/hecke-eigensheaf` | definition | Requires Hecke correspondences. |
| LAN13 | ENRICH | `langlands/geometric-langlands-correspondence` | conjecture/theorem family | State categorical form after LAN07–LAN12. |
| LAN14 | ENRICH | `langlands/projective-line-in-geometric-langlands` | context | Unramified sparsity and marked/ramified examples. |
| LAN15 | ENRICH | `langlands/ramified-geometric-langlands` | definition/program | Marked-point enrichment. |

## Authored enrichment and dependency closure

All 19 records originally marked **ENRICH** in Batches 1, 4, 6, 11, and 12
are part of the July 30 authored corpus; none remains deferred. During
authorship, semantic deduplication and outbound-link review identified the
following additional records. These are required parts of the expansion rather
than an informal backlog.

### Formal-group closure

| Canonical ID | Title |
|---|---|
| `algebra-coalgebras/coalgebra` | Coalgebra |
| `algebra-coalgebras/bialgebra` | Bialgebra |
| `algebra-coalgebras/hopf-algebra` | Hopf algebra |
| `algebra-topological/completed-tensor-product` | Completed tensor product |
| `lie-groups/complete-filtered-lie-algebra` | Complete filtered Lie algebra |

### Complex-analysis and Lorentz closure

| Canonical ID | Title |
|---|---|
| `complex-analysis/entire-function` | Entire function |
| `complex-analysis/holomorphic-germ` | Holomorphic germ |
| `complex-analysis/monodromy-theorem` | Monodromy theorem |
| `complex-analysis/normal-family` | Normal family |
| `complex-analysis/rouche-theorem` | Rouché's theorem |
| `complex-analysis/casorati-weierstrass-theorem` | Casorati–Weierstrass theorem |
| `complex-analysis/great-picard-theorem` | Great Picard theorem |
| `complex-analysis/rational-function` | Rational function |
| `complex-analysis/generalized-circle` | Generalized circle |
| `complex-analysis/anti-mobius-transformation` | Anti-Möbius transformation |
| `complex-analysis/projective-connection` | Holomorphic projective connection |
| `complex-analysis/logarithmic-derivative` | Logarithmic derivative |
| `algebraic-geometry-foundations/finite-locally-free-morphism` | Finite locally free morphism |
| `lie-groups/psl2c-action-on-hyperbolic-three-space` | \(PSL(2,\mathbb C)\) action on hyperbolic three-space |

### Supergeometry and field-equation closure

| Canonical ID | Title |
|---|---|
| `mathematical-physics/poincare-algebra` | Poincaré algebra |
| `differential-geometry/globally-hyperbolic-spacetime` | Globally hyperbolic spacetime |

### Hyperstructure enrichment and closure

| Canonical ID | Title |
|---|---|
| `algebra-rings/idempotent-semifields-and-lattice-ordered-groups` | Idempotent semifields and lattice-ordered groups |
| `algebra-hyperstructures/valuative-hyperfield` | Valuative hyperfield |
| `algebra-hyperstructures/hyperfield-of-a-field-quotient` | Hyperfield of a field quotient |
| `algebra-hyperstructures/stringent-hyperfield` | Stringent hyperfield |
| `algebra-hyperstructures/partial-field` | Partial field |
| `algebra-hyperstructures/partial-hyperfield` | Partial hyperfield |
| `shared-foundations/lattice` | Lattice |
| `algebra-groups/lattice-ordered-abelian-group` | Lattice-ordered abelian group |
| `algebra-hyperstructures/integral-hyperring` | Integral hyperring |

The proposed standalone “field as semifield and hyperfield” record was
deduplicated into `algebra-hyperstructures/fields-semifields-and-hyperfields`
as an alias and a categorical comparison section.

### Blueprint closure

| Canonical ID | Title |
|---|---|
| `algebraic-geometry-foundations/localization-of-blueprint` | Localization of a blueprint |
| `algebraic-geometry-foundations/spectrum-of-blueprint` | Spectrum of a blueprint |
| `algebraic-geometry-foundations/affine-blue-scheme` | Affine blue scheme |
| `algebraic-geometry-foundations/ordered-blue-scheme` | Ordered blue scheme |
| `algebraic-geometry-foundations/ordered-blue-field` | Ordered blue field |
| `algebra-hyperstructures/idyll` | Idyll |

### Geometric-Langlands closure

| Canonical ID | Title |
|---|---|
| `algebraic-geometry-foundations/algebraic-stack` | Algebraic stack |
| `algebraic-geometry-foundations/principal-g-bundle-on-scheme` | Principal \(G\)-bundle on a scheme |
| `algebraic-geometry-foundations/quasi-coherent-sheaf` | Quasi-coherent sheaf |
| `algebraic-geometry-foundations/sheaf-of-differential-operators` | Sheaf of differential operators |
| `algebraic-geometry-foundations/pointed-algebraic-curve` | Pointed algebraic curve |
| `langlands/g-local-system` | \(G\)-local system |
| `langlands/moduli-stack-of-g-local-systems` | Moduli stack of \(G\)-local systems |
| `langlands/ind-coherent-sheaves-with-nilpotent-singular-support` | Ind-coherent sheaves with nilpotent singular support |
| `langlands/affine-grassmannian` | Affine Grassmannian |
| `langlands/geometric-satake-equivalence` | Geometric Satake equivalence |
| `langlands/hecke-modification` | Hecke modification |
| `langlands/hecke-correspondence` | Hecke correspondence |
| `langlands/hecke-functor` | Geometric Hecke functor |
| `langlands/level-structure-on-g-bundle` | Level structure on a \(G\)-bundle |
| `langlands/ramification-of-g-local-system` | Ramification of a \(G\)-local system |
| `langlands` | Geometric Langlands subject index |

## Atomicity follow-up after rendered review

A rendered-page review found two distinct problems after the first integration
pass: top-level knowl IDs were not recognized by the wikilink parser, and a
small number of authored pages bundled several independently named
definitions, constructions, or theorems into one overview-style record. The
follow-up re-audited every July 30 addition against established atomic knowls.
Its house rule is that a knowl has one axiomatic, clickable mathematical
nucleus; independently named results or structures receive their own IDs,
while subject navigation belongs in an index.

At the close of this follow-up, the `knowlpedia-content` working tree differs
from `develop` by **373 added knowls** and **64 modified pre-existing knowls**.
The 373 additions include **109 atomic dependencies and results extracted
during this follow-up**. Six proposed July 30 overview records were folded into
atomic children or subject indexes and therefore do not appear in the final
added count.

### Folded proposed records

These IDs were introduced by the first July 30 pass and then removed before
final integration; no pre-July canonical ID was deleted.

| Folded ID | Final disposition |
|---|---|
| `algebra-hyperstructures/comparison-map` | Navigation moved to `algebra-hyperstructures`; mathematical assertions moved to the separate embedding, tract, band, blueprint, and tropical-comparison knowls. |
| `complex-analysis/cross-ratio-characterization-of-mobius-transformations` | Split into cross-ratio invariance, sharp three-transitivity, and the cross-ratio-preserving-bijection characterization. |
| `complex-analysis/schwarzian-chain-rule-and-mobius-characterization` | Split into the Schwarzian chain rule, Möbius characterization, equal-Schwarzian theorem, and the second-order-ODE relation. |
| `differential-geometry/morphisms-between-kahler-manifolds` | Folded into the atomic holomorphic/isometric morphism definitions and the differential-geometry index. |
| `differential-geometry/morphisms-between-hyperkahler-manifolds` | Replaced by triholomorphic maps, strict and rotating hyperkähler isometries, and hyperkähler isometric immersions. |
| `langlands/projective-line-in-geometric-langlands` | The precise marked/ramified example moved to `langlands/ramified-geometric-langlands`; rank-one group roles remain in their atomic projective, Möbius, and dual-group records. |

### Newly extracted atomic dependencies and results

The following 109 records were not in the first authored manifest. They arose
from dependency closure and from splitting independently named concepts out of
bundled records.

#### Formal groups and indefinite spin — 5

- `formal-groups/affine-formal-groups-and-complete-hopf-algebras`
- `formal-groups/distribution-algebra-and-universal-enveloping-algebra`
- `formal-groups/height-of-one-dimensional-formal-group-law`
- `lie-groups/indefinite-pin-group`
- `lie-groups/restricted-spin-group`

#### Complex analysis and projective structures — 11

- `complex-analysis/complex-projective-structure`
- `complex-analysis/cross-ratio-invariance-under-mobius-transformations`
- `complex-analysis/cross-ratio-preserving-bijections-are-mobius`
- `complex-analysis/sharp-three-transitivity-of-mobius-group`
- `complex-analysis/little-picard-theorem`
- `complex-analysis/montel-theorem`
- `complex-analysis/projective-connections-form-an-affine-space`
- `complex-analysis/schwarzian-chain-rule`
- `complex-analysis/mobius-characterization-by-schwarzian`
- `complex-analysis/equal-schwarzians-differ-by-mobius`
- `complex-analysis/schwarzian-and-second-order-linear-odes`

#### Almost-complex, Kähler, and hyperkähler geometry — 5

- `differential-geometry/almost-complex-map`
- `differential-geometry/nijenhuis-tensor`
- `differential-geometry/newlander-nirenberg-theorem`
- `differential-geometry/hyperkahler-isometric-immersion`
- `differential-geometry/rotating-hyperkahler-isometry`

#### Valuations, hyperstructures, bands, and blueprints — 26

- `algebra-fields-galois/non-archimedean-absolute-value`
- `algebra-fields-galois/valuation-ring`
- `algebra-fields-galois/value-group`
- `algebra-rings/parasemifield`
- `algebra-hyperstructures/band`
- `algebra-hyperstructures/null-set-of-a-band`
- `algebra-hyperstructures/fusion-rule-for-bands`
- `algebra-hyperstructures/fusion-band`
- `algebra-hyperstructures/phase-hyperfield`
- `algebra-hyperstructures/doubly-distributive-hyperfield`
- `algebra-hyperstructures/doubly-distributive-hyperfields-are-stringent`
- `algebra-hyperstructures/classification-of-stringent-hyperfields`
- `algebra-hyperstructures/hyperfield-as-a-tract`
- `algebra-hyperstructures/partial-field-as-a-tract`
- `algebra-hyperstructures/partial-hyperfield-as-a-tract`
- `algebra-hyperstructures/tract-as-an-ordered-blueprint`
- `algebraic-geometry-foundations/pre-addition-on-a-monoid`
- `algebraic-geometry-foundations/semiring-completion-of-a-blueprint`
- `algebraic-geometry-foundations/k-ideal-of-a-blueprint`
- `algebraic-geometry-foundations/locally-blueprinted-space`
- `algebraic-geometry-foundations/ordered-blueprinted-space`
- `algebraic-geometry-foundations/semiring-as-a-blueprint`
- `algebraic-geometry-foundations/commutative-monoid-with-zero-as-a-blueprint`
- `algebraic-geometry-foundations/blueprint-as-an-ordered-blueprint`
- `algebraic-geometry-foundations/band-as-an-ordered-blueprint`
- `algebraic-geometry-foundations/idyll-as-ordered-blue-field`

#### Algebraic geometry and geometric Langlands — 33

- `algebra-topological/adic-ring`
- `algebra-topological/ideal-of-definition`
- `algebraic-geometry-foundations/locally-topologically-ringed-space`
- `algebraic-geometry-foundations/algebraic-group`
- `algebraic-geometry-foundations/algebraic-space`
- `algebraic-geometry-foundations/coherent-sheaf`
- `algebraic-geometry-foundations/derived-algebraic-stack`
- `algebraic-geometry-foundations/integrable-connection`
- `algebraic-geometry-foundations/parabolic-subgroup`
- `algebraic-geometry-foundations/projective-morphism`
- `algebraic-geometry-foundations/punctured-algebraic-curve`
- `algebraic-geometry-foundations/reductive-algebraic-group`
- `algebraic-geometry-foundations/smooth-morphism`
- `algebraic-geometry-foundations/tangent-sheaf`
- `langlands/affine-schubert-variety`
- `langlands/convolution-of-sheaves`
- `langlands/dominant-coweight`
- `langlands/global-nilpotent-cone`
- `langlands/ind-coherent-sheaf`
- `langlands/ind-scheme`
- `langlands/intersection-cohomology-complex`
- `langlands/irregular-singular-connection`
- `langlands/iwahori-level-structure`
- `langlands/loop-group`
- `langlands/parahoric-level-structure`
- `langlands/perverse-sheaf`
- `langlands/positive-loop-group`
- `langlands/regular-singular-connection`
- `langlands/riemann-hilbert-correspondence`
- `langlands/singular-support-of-coherent-sheaf`
- `langlands/stokes-data`
- `langlands/tame-ramification`
- `langlands/wild-ramification`

#### Supergeometry, Clifford theory, causality, and field equations — 29

- `supergeometry/koszul-sign-rule`
- `supergeometry/representation-of-a-lie-superalgebra`
- `supergeometry/super-internal-hom`
- `supergeometry/super-pbw-theorem`
- `supergeometry/supercommutator`
- `supergeometry/supertranslation-distribution`
- `differential-geometry/complex-clifford-module-classification`
- `differential-geometry/dirac-spinor`
- `differential-geometry/weyl-spinor`
- `differential-geometry/majorana-spinor`
- `differential-geometry/majorana-weyl-spinor`
- `differential-geometry/chirality-operator`
- `differential-geometry/lorentzian-dirac-operator`
- `mathematical-physics/clifford-slash-notation`
- `differential-geometry/causal-curve`
- `differential-geometry/chronological-and-causal-future`
- `differential-geometry/strong-causality`
- `differential-geometry/causal-diamond`
- `differential-geometry/cauchy-hypersurface`
- `differential-geometry/global-hyperbolicity-and-cauchy-hypersurfaces`
- `differential-geometry/smooth-splitting-of-globally-hyperbolic-spacetimes`
- `differential-geometry/connection-laplacian`
- `differential-geometry/scalar-curvature`
- `mathematical-physics/conformal-coupling-of-a-scalar-field`
- `mathematical-physics/connection-form-of-a-normally-hyperbolic-operator`
- `mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators`
- `mathematical-physics/advanced-and-retarded-green-operators`
- `mathematical-physics/existence-of-advanced-and-retarded-green-operators`
- `mathematical-physics/cauchy-problem-for-the-lorentzian-dirac-operator`

### Parser, rendered-link checking, and preservation audit

The broken raw links in the rendered screenshots were a compiler defect rather
than missing knowls. The wikilink parser previously required at least one `/`
in every target, so valid top-level IDs such as `formal-groups`,
`supergeometry`, `langlands`, and `algebra-hyperstructures` remained literal
text. The parser now accepts top-level IDs, multiline labels, and labels
containing brackets. Link extraction protects mathematics first so expressions
such as \(R[[x]]\) are not mistaken for links. Regression tests cover each
case.

The rendered-output checker now flags every visible raw `[[` or `]]` marker,
including lone markers and markup-split links, while continuing to ignore
mathematics and code. This closes the gap through which the screenshot defects
passed the earlier build.

Finally, the pre-existing-content comparison was repeated side by side against
`develop`. The original 41 modified canonical records were audited for lost
definitions, hypotheses, consequences, aliases, and links; displaced material
was restored or moved to a more precise atomic child. The final preservation
review passed with no unintended mathematical content loss. In particular, it
retains the symplectic Stokes consequence, the projective-space `Proj` link,
the “proper orthochronous” terminology, the formal-power-series
completion/deformation context, and consistent real/complex scalar fields in
smooth-section and Serre–Swan statements.

## Batch 13 — integration, indexing, and validation

| Ref | Status | Canonical ID or target | Kind | Action |
|---|---|---|---|---|
| INT01 | NEW | `knowlification/july-30-additions-index` | index | Permanent provenance/review index for every accepted authored item. |
| INT02 | LINK | `differential-geometry` | subject index | Add complex, symplectic, Kähler, hyperkähler, Lorentzian, and spin links. |
| INT03 | LINK | `lie-groups` | subject index | Add formal, projective, complex/real, Lorentz, spin, and super links. |
| INT04 | LINK | `algebra-rings` | subject index | Add formal-series, semiring, and idempotent links. |
| INT05 | LINK | `algebra-category-theory` | subject index | Add groupoid, monoidal, algebra-object, and group-object links. |
| INT06 | LINK | `fiber-bundles` | subject index | Add Serre–Swan categorical and Lorentzian spin links. |
| INT07 | LINK | new subject indexes | index closure | Ensure every new record is reachable from a subject index and INT01. |
| INT08 | LINK | complete authored corpus | interlink pass | Run conservative scripted interlinking only after content stabilizes. |
| INT09 | LINK | compiler and content checks | validation | Front matter, duplicate IDs, links, tests, section audit, development build, rendering scan, production build. |
| INT10 | LINK | representative rendered pages | visual review | Inspect at least one page from every mathematical neighborhood. |

## Existing-content TODO

The following canonical records should not be duplicated. They need correction,
expansion, or possible future regeneration in place.

### Correct during the relevant batch

| Priority | Existing ID | Problem | Required action |
|---|---|---|---|
| P0 | `lie-groups/special-linear-group` | States dimension \(n^2-1\) after allowing both \(\mathbb R\) and \(\mathbb C\), without distinguishing real and complex dimension. | Correct in LG17 before authoring dependent \(SL_2(\mathbb C)\) pages. |
| P0 | `lie-groups/example-sl2c` | Generic title and alias “Example:” and content only about the Lie algebra. | Preserve ID; retitle to “The complex Lie algebra \(\mathfrak{sl}_2(\mathbb C)\)” and distinguish its underlying real algebra. |
| P1 | `differential-geometry/symplectomorphism` | Darboux context links to the real-analysis theorem rather than the symplectic Darboux theorem. | Correct the target during GEO05. |
| P1 | `fiber-bundles/section-module-is-finitely-generated-projective` | Front matter says `kind = "definition"` although the record is a theorem. | Correct metadata during CAT17. |
| P1 | `shared-foundations/total-order` and `shared-foundations/total-order-linear-order` | Two canonical-looking records cover the same concept. | Defer consolidation to a focused cleanup; depend on `shared-foundations/total-order` meanwhile. |

### Future-regeneration candidates

These are low-depth or legacy records whose IDs should be retained. Regeneration
means rewriting the canonical file in place after reviewing incoming links,
not creating another knowl.

| Priority | Existing ID | Evidence | Future action |
|---|---|---|---|
| R1 | `differential-geometry/complex-manifold` | Short non-progressive legacy core; missing categorical and integrability context. | Regenerate progressively under GEO03, preserving title/aliases and incoming links. |
| R1 | `differential-geometry/holomorphic-map` | Only a short Euclidean/manifold summary; it asserts analytic equivalence without its theorem dependency. | Regenerate progressively under CA05 after CA02–CA11 exist. |
| R1 | `differential-geometry/almost-complex-structure` | Very short legacy entry with no morphism convention. | Regenerate or substantially expand under GEO01. |
| R1 | `differential-geometry/integrable-almost-complex-structure` | Very short entry; Newlander–Nirenberg hypotheses and Nijenhuis relation are absent. | Regenerate or substantially expand under GEO02. |
| R1 | `differential-geometry/symplectic-manifold` | Legacy generic kind and little progressive structure despite a large downstream neighborhood. | Regenerate progressively under GEO04. |
| R1 | `lie-groups/example-sl2c` | Unusable generic presentation metadata in addition to the correctness ambiguity above. | Treat the P0 repair as an in-place regeneration, not a new \(\mathfrak{sl}_2(\mathbb C)\) file. |
| R2 | `lie-groups/lorentz-group` | Concise legacy entry; \(SO^+(1,3)\), components, signature choices, and spin relation are only sketched. | Regenerate progressively after LG08–LG14 are available. |
| R2 | `algebra-rings/formal-power-series-ring` | One-variable only and lacks topology, substitution, and completion context. | Expand in place under FG01; regenerate only if the expanded core becomes structurally awkward. |
| R2 | `real-analysis/power-series` | Real-coefficient framing conflicts with downstream complex examples. | Expand in place under CA06; retain analytic, not formal, scope. |
| R3 | `lie-groups/spin-group` | Positive-definite scope is legitimate but easy to overread as \(\operatorname{Spin}(p,q)\). | Preserve core; add an explicit scope warning and indefinite-spin link rather than replacing it. |

The following existing records were inspected and should **not** be regenerated
for this expansion: `fiber-bundles/serre-swan-theorem`,
`differential-geometry/clifford-algebra`,
`differential-geometry/clifford-module`,
`differential-geometry/kahler-manifold`, and
`differential-geometry/hyperkahler-manifold`. They need only the expansions or
links listed above.

## Recommended session boundaries

The manifest is intentionally larger than one safe authoring session. A
practical sequence is:

1. Batch 0 plus Batch 1 (formal groups), including the central equivalence.
2. Batches 2–3 (complex analysis, projective and Möbius geometry).
3. Batch 4 (real/complex \(SL_2\), Lorentz, and the celestial sphere).
4. Batch 5 (super linear algebra, Clifford, and spinors).
5. Batch 6 (supergeometry).
6. Batch 7 (Lorentzian PDE and field equations).
7. Batch 8 (smooth categories, \(C^\infty\)-rings, sheaves, Serre–Swan).
8. Batch 9 (symplectic, Hamiltonian, Kähler, and hyperkähler morphisms).
9. Batch 10 (semirings, hyperrings, hyperfields, tropical algebra).
10. Batch 11 (ordered blueprints and comparison map).
11. Batch 12a (rank-one flag/Langlands context), followed by Batch 12b
    (local systems, \(D\)-modules, \(\operatorname{Bun}_G\), Hecke
    eigensheaves, and unramified/ramified geometric Langlands).
12. Enrichment closure for coordinate Hopf algebras, distribution algebras,
    filtered BCH groups, Weil restriction, hyperbolic \(3\)-space,
    supersymmetry, tracts, pastures, pasteurization, and blue schemes.
13. Batch 13 (index closure, interlinking, layered validation, visual review).

Each session should end with its exact completed ID list and any newly
discovered dependency IDs added to the July 30 expansion index and to this
plan. Newly discovered dependencies are deduplicated against the complete
corpus before authorship and become required manifest entries rather than
informal omissions.

## Authoring references to resolve conventions

Use standard texts for ordinary material and primary literature for
version-sensitive structures. In particular:

- Formal groups and the BCH/Lie correspondence: Hazewinkel, *Formal Groups and
  Applications*, together with standard Lie-theory treatments of the formal
  BCH series.
- Supergeometry and spin: Deligne–Morgan, Varadarajan, and
  Lawson–Michelsohn, with the chosen smooth-real supermanifold model stated
  explicitly.
- Lorentzian equations: a single source/convention set should govern metric
  signature, Clifford signs, \(\Box\), gamma matrices, and Dirac factorization.
- Hyperfields: Baker–Bowler,
  [Matroids over Hyperfields](https://arxiv.org/abs/1601.01204).
- Blueprints and tropicalization: Lorscheid,
  [Geometry of Blueprints, Part I](https://arxiv.org/abs/1103.1745) and
  [A Unifying Approach to Tropicalization](https://arxiv.org/abs/1508.07949).
- Projective-line geometric Langlands examples should be labeled as ramified
  or marked when appropriate; for example Nadler–Yun,
  [Geometric Langlands correspondence for \(SL(2)\), \(PGL(2)\) over the pair
  of pants](https://arxiv.org/abs/1610.08398).
