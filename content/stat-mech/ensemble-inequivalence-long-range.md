---
title: "Ensemble inequivalence for long-range (nonadditive) systems"
description: "When interactions are nonadditive, the microcanonical entropy can be nonconcave, causing the canonical ensemble to realize only the concave envelope—leading to inequivalent thermodynamics (e.g., temperature jumps, negative heat capacity)."
---

## Prerequisites and notation

- Microcanonical entropy density: {{< knowl id="microcanonical-entropy-density" text="microcanonical entropy density" >}}
- Canonical and free energy: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}
- Legendre/Fenchel duality: {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}, {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}}, {{< knowl id="tfae-legendre-duality-entropy-free-energy" text="Legendre duality: entropy ↔ free energy" >}}
- Large-deviation viewpoint: {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}}, {{< knowl id="rate-function" section="large-deviations" text="rate function" >}}
- A common symptom: {{< knowl id="microcanonical-negative-heat-capacity" text="negative microcanonical heat capacity" >}}

## Extension: why long-range forces can break ensemble equivalence

### Additivity vs nonadditivity
For short-range interactions, the energy is (approximately) additive over distant subsystems, which underpins equivalence between microcanonical and canonical ensembles in the thermodynamic limit. For long-range interactions (e.g., potentials decaying like $r^{-d}$ or slower in $d$ dimensions, or mean-field couplings), the energy can be **nonadditive**: splitting the system into macroscopic parts leaves an interaction energy of the same order as the parts themselves.

Nonadditivity allows the microcanonical entropy to develop nonconcave regions, which are forbidden in canonical equilibrium.

### Entropy–free energy relation as a convex-analytic envelope
Let $s(u)$ be the microcanonical entropy density as a function of energy density $u$ (see {{< knowl id="microcanonical-entropy-density" text="microcanonical entropy density" >}}). The canonical free energy density $f(\beta)$ can be written as a Legendre–Fenchel transform:
$$
-\beta f(\beta)=\sup_{u}\,\bigl(s(u)-\beta u\bigr).
$$

Equivalently, the canonical ensemble selects supporting lines of slope $\beta$ to the graph of $s(u)$. If $s(u)$ is strictly concave, this is an invertible Legendre duality. If $s(u)$ is not concave, the transform replaces $s(u)$ by its **concave envelope**, meaning that some microcanonical energies are never realized canonically.

### Practical indicators of inequivalence
Ensemble inequivalence may manifest as:
- **Temperature jumps** in microcanonical caloric curves $T(u)$ when $s(u)$ has affine/convex segments.
- **First-order transitions** appearing differently: microcanonical can show continuous traversal through energies where canonical shows phase coexistence at fixed $\beta$.
- **Negative microcanonical heat capacity**, which cannot occur canonically (see {{< knowl id="microcanonical-negative-heat-capacity" text="negative microcanonical heat capacity" >}}).

### Typical models and where it connects
Common settings include mean-field spin models (e.g., {{< knowl id="curie-weiss-model" text="Curie–Weiss model" >}}), self-gravitating systems, and other nonadditive Hamiltonians. In lattice systems, inequivalence is often discussed alongside {{< knowl id="ensemble-equivalence-breakdown" text="ensemble equivalence breakdown" >}} and can be formulated using large deviations: the canonical equilibrium concentrates on minimizers of a rate function that corresponds to the convex/concave regularization of microcanonical variational principles.
