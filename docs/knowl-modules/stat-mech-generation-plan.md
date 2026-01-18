# Statistical Mechanics Generation Plan

Phased generation plan based on prerequisite audit.

---

## Phase 1: Measure & Integration Extensions

**Target section:** `measure-theory` (extend existing)

**Dependencies:** `shared-foundations`, `real-analysis` (existing)

**Slugs (23 items):**

```
ae-equality
lebesgue-integrable-function
lebesgue-integral-nonnegative
lebesgue-integral
l1-function
l-infinity-function
essential-supremum
lp-norm
lp-space
convergence-almost-everywhere
convergence-in-measure
convergence-in-lp
uniform-integrability
product-measure
pushforward-measure
change-of-variables-pushforward
monotone-convergence-theorem
fatous-lemma
dominated-convergence-theorem
tonellis-theorem
fubinis-theorem
jensen-inequality-integral
minkowski-inequality-lp
```

---

## Phase 2: Probability Theory (New Section)

**Target section:** `probability` (new)

**Dependencies:** `measure-theory`, `shared-foundations`

**Slugs (37 items):**

```
probability-measure
probability-space
event-probability
random-variable
random-vector
distribution-law
expectation
expectation-function-of-rv
conditional-expectation
conditional-probability
independence-events
independence-sigma-algebras
independence-random-variables
identically-distributed
iid-sequence
variance
covariance
correlation-coefficient
moment
moment-generating-function
characteristic-function-probability
cumulant-generating-function
cumulant
markov-inequality
chebyshev-inequality
chernoff-bound
weak-law-large-numbers
strong-law-large-numbers
central-limit-theorem
shannon-entropy
differential-entropy
relative-entropy-kl-divergence
gibbs-inequality-kl
total-variation-distance
pinsker-inequality
maximum-entropy-principle
```

---

## Phase 3: Convex Duality Extensions

**Target section:** `convex-analysis` (extend existing)

**Dependencies:** `convex-analysis` (existing), `real-analysis`

**Slugs (11 items):**

```
convex-conjugate-fenchel
legendre-transform
legendre-fenchel-transform
biconjugate
closed-convex-function
subdifferential
subgradient
supporting-hyperplane-convex-function
fenchel-young-inequality
fenchel-moreau-theorem
convex-duality-primal-dual
```

---

## Phase 4: Large Deviations (New Section)

**Target section:** `large-deviations` (new)

**Dependencies:** `probability`, `convex-analysis`

**Slugs (12 items):**

```
large-deviation-principle
rate-function
good-rate-function
exponential-tightness
log-moment-generating-function
cramer-transform
laplace-principle
varadhans-lemma
cramers-theorem
sanovs-theorem
gartner-ellis-theorem
contraction-principle-ldp
```

---

## Phase 5: Asymptotics & Combinatorics

**Target section:** `asymptotics` (new) or inline with stat-mech

**Dependencies:** `real-analysis`

**Slugs (5 items):**

```
stirlings-approximation
entropy-multinomial-coefficients
laplaces-method
saddle-point-method
method-of-types
```

---

## Phase 6: Discrete Structures for Lattice Models

**Target section:** `stat-mech` or `graph-theory` (new)

**Dependencies:** `shared-foundations`

**Slugs (8 items):**

```
graph-vertex-edge
finite-graph
lattice-zd
finite-box-lattice
boundary-finite-region
nearest-neighbor-zd
finite-range-interaction-lattice
translation-invariant-interaction
```

---

## Phase 7: Quantum Structures Extensions

**Target section:** `quantum-foundations` (new) or extend `linear-algebra`

**Dependencies:** `linear-algebra` (existing)

**Slugs (12 items):**

```
complex-hilbert-space-finite
bounded-operator-hilbert
self-adjoint-operator-observable
spectrum-self-adjoint-finite
trace-operator
density-operator
pure-state-quantum
mixed-state-quantum
partial-trace
von-neumann-entropy
quantum-relative-entropy
golden-thompson-inequality
```

---

## Phase 8: Core Thermodynamics

**Target section:** `thermodynamics` (new)

**Dependencies:** Phases 1-7

**Estimated slugs:** ~80 items (systems, quantities, structure, axioms)

---

## Phase 9: Core Statistical Mechanics

**Target section:** `stat-mech` (new)

**Dependencies:** `thermodynamics`, `probability`, `measure-theory`

**Estimated slugs:** ~60 items (ensembles, partition functions, correlations)

---

## Phase 10: Lattice Models & Phase Transitions

**Target section:** `stat-mech-lattice` or part of `stat-mech`

**Dependencies:** `stat-mech`, discrete structures

**Estimated slugs:** ~50 items (Gibbs measures, Ising, DLR, phase transitions)

---

## Phase 11: Quantum Statistical Mechanics

**Target section:** `stat-mech-quantum` or part of `stat-mech`

**Dependencies:** `stat-mech`, quantum structures

**Estimated slugs:** ~15 items (quantum ensembles, KMS)

---

## Phase 12: Theorems, Lemmas, Propositions, Corollaries

**Target section:** distributed across above sections

**Dependencies:** All definitions

**Estimated slugs:** ~80 items

---

## Phase 13: TFAE Packages, Examples, Extensions

**Target section:** distributed

**Dependencies:** All above

**Estimated slugs:** ~40 items

---

## Summary

| Phase | Section | Items | Status |
|-------|---------|-------|--------|
| 1 | measure-theory (extend) | 23 | Ready |
| 2 | probability (new) | 37 | Ready |
| 3 | convex-analysis (extend) | 11 | Ready |
| 4 | large-deviations (new) | 12 | Ready |
| 5 | asymptotics | 5 | Ready |
| 6 | discrete structures | 8 | Ready |
| 7 | quantum-foundations | 12 | Ready |
| 8-13 | stat-mech core | ~245 | After prereqs |
| **Total** | | **~350** | |

---

## Rate Limit Testing Plan

Start with Phase 1 (23 slugs) split across 5 parallel agents (~5 slugs each).
If successful, increase to 10, 15, etc. for subsequent phases.
