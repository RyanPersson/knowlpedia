# Smooth and distribution vectors: follow-up batch

The complete pasted number-field message was already covered by the previous
ergodic-theory batch. In particular, the arithmetic reading path includes the
Archimedean torus, its torsion subgroup, the codifferent and all Fourier
characters, the single-translation trace criterion, the joint additive
ring-of-integers criterion, and the Gaussian-integer counterexample.

The smooth-vector message overlaps substantial earlier representation-theory
content: strong and weak continuity, smooth vectors, the derived action,
Gårding density, Stone generators, essential skew-adjointness, operator cores,
and distribution vectors already had canonical entries. This follow-up adds
15 ordinary knowls and one reading-path index to cover the missing statements
and examples, with focused updates to related entries and navigation.

The [coverage inventory](smooth-vectors-knowl-coverage.json) maps each topic in
both pasted messages to existing and new entries. It records input hashes,
the baseline commits, all changed source hashes, and 340 reused prerequisite
knowls. Its scope is the two supplied messages; it does not assert access to
other unprovided messages or recover unrelated truncated replies.

## Additions

- Differentiable vectors of finite order, the explicit smooth-vector Fréchet
  norms and continuity estimate, and the iterated-generator-domain theorem.
- Banach manifolds, Banach–Lie groups, and the operator-norm unitary group,
  clarifying why operator-norm smoothness is stronger than smooth orbit maps.
- Continuous anti-duals, trace-class representations, and the equivalence of
  trace class with nuclear smooth vectors, including a type I counterexample.
- A noncompact nonabelian type I group with a two-dimensional irreducible
  representation; the strongly continuous but not norm-continuous modulation
  group; Schwartz smooth vectors and the derived Heisenberg representation.
- Left-action fundamental vector fields and the inverse-pullback derivative.

## Existing entries improved

The smooth-vector entry no longer treats first-order differentiability as an
alias for smoothness. Its topology has a dedicated canonical entry. The
derived representation states real-linearity in the Lie-algebra variable and
complex-linearity on the vector space. Distribution vectors now specify the
Hilbert embedding, point evaluation, and the nuclearity qualification.

Algebraic irreducibility and subrepresentations now allow infinite-dimensional
vector spaces; the finite-dimensional restriction remains explicit in the
complete-reducibility consequence. The Schrödinger entry connects its existing
Weyl convention to the Heisenberg group. No review counts were incremented.

## Conventions and evidence

The repository takes the inner product linear in its first variable. Hence
the linear embedding into the anti-dual is `j(v)(w) = <v,w>`, with the order
reversed from the pasted message's opposite inner-product convention. The
rigged-Hilbert example consistently uses the anti-dual rather than silently
identifying it linearly with the usual linear distribution dual.

The Stone convention remains `pi(exp(tX)) = exp(it A_X)`. The maximal
skew-adjoint generator is `K_X = i A_X`, and the derived operator is its
restriction to smooth vectors. Symmetric Heisenberg coordinates remain in
place; the conversion `c = z + ab/2` gives the pasted group law. Positive
left-action fundamental fields reverse brackets, and inverse pullback gives
minus the Lie derivative.

Primary mathematical sources checked include Neeb's
[differentiable-vector paper](https://arxiv.org/abs/1002.1602), §§2–5 and
Theorem 9.4; van Dijk–Neeb–Salmasian–Zellner's
[trace-class characterization](https://arxiv.org/abs/1512.02451), §1 and
Proposition 1.11; Deitmar–van Dijk's
[trace-class groups](https://arxiv.org/abs/1501.02375), Examples 1.5,
Theorem 1.7 and Propositions 1.9–1.10; and Garg–Thangavelu's
[Schrödinger-vector paper](https://arxiv.org/abs/1006.3265), §2.
Each entry cites the locator actually checked or supplies its direct
calculation. These are authorship checks, not a completed formal full review.

## Reading paths and validation

The new path is
[Smooth and distribution vectors](https://optiplex.taildb538a.ts.net:8443/lie-groups/smooth-unitary-representations-index/).
The number-field material remains in
[Number-field translations](https://optiplex.taildb538a.ts.net:8443/ergodic-theory/arithmetic-index/).
Both are linked from the ergodic-theory entry point. Five subject indexes also
link the additions.

The coverage inventory records final source, dependency, build, and browser
validation. The existing persistent service on backend port 8015 serves the
rebuilt `public-imported` directory through Tailscale HTTPS on port 8443, with
the feedback server enabled. Inline knowl expansion splits the prose at the
clicked link and rejoins it on close, including nested expansions.

- Development build: 5,346 knowls, passed. Production build: 4,158 knowls,
  passed; the complete primary production rendering scan also passed.
- Prerequisites: 4,168 nodes and 13,905 edges, with no cycles, invalid sources,
  or missing targets.
- All 34 changed source files preserve their section content in order and
  keep external references in the required location. All inventory hashes match.
- All 34 changed pages and 16 new core fragments load. All 16 new pages were
  checked on desktop and at 390px; rendered mathematics, nested inline
  expansion, optional sections, and search passed, with no page overflow or
  JavaScript errors.
- The scope audit flags the anti-dual together with its strong topology; this
  is one dual-space construction reusing the existing strong-dual definition.
  No changed entry has an exact-label mismatch.

The unchanged imported conjectures catalog retains the rendering findings
documented in the earlier batch; it is outside this collection.
