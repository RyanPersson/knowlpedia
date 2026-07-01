+++
id = "stat-mech/ensemble-inequivalence-long-range"
title = "Ensemble inequivalence for long-range (nonadditive) systems"
kind = "knowl"
summary = "When interactions are nonadditive, the microcanonical entropy can be nonconcave, causing the canonical ensemble to realize only the concave envelope—leading to inequivalent thermodynamics (e.g., temperature jumps, negative heat capacity)."
aliases = ["ensemble-inequivalence-long-range", "Ensemble inequivalence for long-range (nonadditive) systems"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/ensemble-inequivalence-long-range.md"
+++

## Prerequisites and notation

- Microcanonical entropy density: [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]]
- Canonical and free energy: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/free-energy-statistical|statistical free energy]]
- Legendre/Fenchel duality: [[convex-analysis/legendre-transform|Legendre transform]], [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]], [[stat-mech/tfae-legendre-duality-entropy-free-energy|Legendre duality: entropy ↔ free energy]]
- Large-deviation viewpoint: [[large-deviations/large-deviation-principle|large deviation principle]], [[large-deviations/rate-function|rate function]]
- A common symptom: [[stat-mech/microcanonical-negative-heat-capacity|negative microcanonical heat capacity]]

## Extension: why long-range forces can break ensemble equivalence

### Additivity vs nonadditivity
For short-range interactions, the energy is (approximately) additive over distant subsystems, which underpins equivalence between microcanonical and canonical ensembles in the thermodynamic limit. For long-range interactions (e.g., potentials decaying like $r^{-d}$ or slower in $d$ dimensions, or mean-field couplings), the energy can be **nonadditive**: splitting the system into macroscopic parts leaves an interaction energy of the same order as the parts themselves.

Nonadditivity allows the microcanonical entropy to develop nonconcave regions, which are forbidden in canonical equilibrium.

### Entropy–free energy relation as a convex-analytic envelope
Let $s(u)$ be the microcanonical entropy density as a function of energy density $u$ (see [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]]). The canonical free energy density $f(\beta)$ can be written as a Legendre–Fenchel transform:
$$
-\beta f(\beta)=\sup_{u}\,\bigl(s(u)-\beta u\bigr).
$$

Equivalently, the canonical ensemble selects supporting lines of slope $\beta$ to the graph of $s(u)$. If $s(u)$ is strictly concave, this is an invertible Legendre duality. If $s(u)$ is not concave, the transform replaces $s(u)$ by its **concave envelope**, meaning that some microcanonical energies are never realized canonically.

### Practical indicators of inequivalence
Ensemble inequivalence may manifest as:
- **Temperature jumps** in microcanonical caloric curves $T(u)$ when $s(u)$ has affine/convex segments.
- **First-order transitions** appearing differently: microcanonical can show continuous traversal through energies where canonical shows phase coexistence at fixed $\beta$.
- **Negative microcanonical heat capacity**, which cannot occur canonically (see [[stat-mech/microcanonical-negative-heat-capacity|negative microcanonical heat capacity]]).

### Typical models and where it connects
Common settings include mean-field spin models (e.g., [[stat-mech/curie-weiss-model|Curie–Weiss model]]), self-gravitating systems, and other nonadditive Hamiltonians. In lattice systems, inequivalence is often discussed alongside [[stat-mech/ensemble-equivalence-breakdown|ensemble equivalence breakdown]] and can be formulated using large deviations: the canonical equilibrium concentrates on minimizers of a rate function that corresponds to the convex/concave regularization of microcanonical variational principles.
