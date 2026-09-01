# Fractal uncertainty and quantum chaos knowl plan

This document is the review manifest for the axiomatic knowl batch supporting
Alex Cohen's *Fractal uncertainty in higher dimensions*
([arXiv:2305.05022](https://arxiv.org/abs/2305.05022)).

## Verified baseline

- Knowlpedia branch: “quantum-chaos,” based on develop at 82de626.
- Content branch: “quantum-chaos,” based on develop at 68b9e61.
- Both develop branches were fetched from GitHub and had divergence 0 0 from
  origin/develop before the feature branches were created.
- Source audited: arXiv v2, dated October 5, 2024; the supplied PDF has SHA-256
  a82654cb491020c46b51c2e97e36f9b2425eeb71fe1bc3f1caecc1e3089c1317.

## Editorial and deduplication decisions

The batch follows the content editorial guide and the July 26 retrospective:
one reusable concept or theorem per ordinary knowl, a self-contained core
before the first level-two heading, progressive detail, internal links for
genuine prerequisites, and external citations only in final reference
sections.

Semantic deduplication was performed before and after authorship against all
source IDs, titles, and aliases. Existing canonical records are reused for:

- Fourier transformation and inversion on Schwartz space, Plancherel theory,
  Schwartz space, and Hilbert space;
- Lebesgue measure and integration, indicator functions, support, almost
  everywhere, null sets, and distributions;
- weak and distributional derivatives, Hessians, Lipschitz continuity, bump
  functions, and partitions of unity;
- vector spaces, Euclidean spaces, linear maps, orthogonal complements,
  positive-semidefinite matrices, and Cauchy–Schwarz;
- holomorphic maps, Dolbeault operators, tangent bundles, Riemannian manifolds,
  and the Laplace–Beltrami operator.

Rejected automatic matches include Euclidean affine lines to the algebraic
affine line, an Ahlfors regular set to an operator resolvent set, the word
“unit” to a ring unit, and Levi-form positivity to a quantum positive operator.

## New production knowls (56)

### Quantitative geometry and reusable notation

- porosity on balls, porosity on lines, and box porosity;
- Ahlfors–David regularity, porous-set volume decay, and line-section decay;
- Minkowski sum and thickening, finitely overlapping families, and dyadic
  annuli;
- quantitative unique continuation and unique ergodicity;
- Cauchy principal value, Japanese brackets, and multi-index notation.

### Fourier, potential theory, and several complex variables

- bounded Fourier support and the bounded-support Paley–Wiener theorem;
- Hilbert transform, upper-half-plane Poisson kernel and extension,
  Dirichlet-to-Neumann operator, X-ray transform, and oscillatory integrals;
- harmonic functions and their maximum principle;
- upper semicontinuity, subharmonic functions, and logarithmic-modulus
  subharmonicity;
- entire functions of several variables, Levi forms, plurisubharmonic and
  strictly plurisubharmonic functions;
- Hörmander's weighted \(L^2\) theorem for the d-bar equation and the
  holomorphic \(L^2\)-to-pointwise estimate.

### Beurling–Malliavin and fractal uncertainty

- classical and higher-dimensional Beurling–Malliavin multiplier theorems;
- the radial-line growth functional and linewise Poisson extension;
- exact PSH-BM, PSH-BM, and analytic BM propositions;
- damping functions, the damping-function FUP theorem, and production of
  damping functions from line porosity;
- the general FUP concept and the higher-dimensional line-porous FUP theorem.

### Quantum-chaos application and navigation

- compact hyperbolic surfaces, geodesic flow, Anosov flow, and horocycle flow;
- the hyperbolic Poisson kernel and hyperbolic plane waves;
- Laplace–Beltrami eigenfunctions, semiclassical measures, and the uniform
  eigenfunction mass lower bound;
- one dependency-ordered batch index.

## Integration

The durable entry point is “knowlification/quantum-chaos-index.” It lists each
new record once in dependency order and describes the reused prerequisite
layer. The analysis, complex-analysis, differential-geometry,
harmonic-analysis, and mathematical-physics subject indexes also link the new
neighborhoods.

## Validation protocol

The batch is accepted only after all of the following complete:

1. exact compiler build without allowing validation errors;
2. source section-order audit;
3. external-link placement audit;
4. semantic scope and exact-label mismatch audit;
5. conservative and single-word interlink reports with manual acceptance;
6. full compiler tests and browser runtime smoke tests;
7. development and production builds;
8. generated HTML rendering-error scans;
9. representative browser inspection of the batch index, theorem, and
   several-complex-variables pages;
10. generated side-by-side review site against develop.

