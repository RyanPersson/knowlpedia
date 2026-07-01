+++
id = "stat-mech-lattice/phase-transition-gibbs"
title = "Phase transition (Gibbsian viewpoint)"
kind = "knowl"
summary = "A qualitative change in infinite-volume equilibrium behavior, often detected by non-uniqueness of Gibbs measures and/or non-analyticity of the thermodynamic-limit pressure."
aliases = ["phase-transition-gibbs", "Phase transition (Gibbsian viewpoint)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/phase-transition-gibbs.md"
+++

Consider a lattice spin system with fixed interaction (e.g. via an [[stat-mech-lattice/interaction-potential-phi|interaction potential]]) and parameters such as [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$ and external field (see [[stat-mech-lattice/external-field-coupling|external field coupling]]). Let $\mathcal{G}(\gamma)$ be the set of [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] solving the [[stat-mech-lattice/dlr-equation|DLR equation]] for the associated [[stat-mech-lattice/gibbs-specification|Gibbs specification]] $\gamma$.

A **Gibbs phase transition** is commonly signaled by **non-uniqueness**:
- there exist at least two distinct measures $\mu,\nu \in \mathcal{G}(\gamma)$.

Equivalently (in many standard settings), different [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]] produce different infinite-volume limits of [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]].

A complementary thermodynamic signature is **non-analyticity** of the [[stat-mech-lattice/pressure-lattice|lattice pressure]] in the [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]] as a function of parameters. Both viewpoints are widely used; non-uniqueness corresponds most directly to phase coexistence, while non-analyticity captures both first-order and continuous critical phenomena.

## Key properties

- **Coexistence of pure phases:** When non-uniqueness holds, $\mathcal{G}(\gamma)$ contains multiple [[stat-mech-lattice/pure-phase|pure phases]], i.e. multiple [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]] distinguished by macroscopic observables (magnetization, density, etc.).

- **Order parameter behavior:** A phase transition is often accompanied by a qualitative change or discontinuity in an [[stat-mech-lattice/order-parameter|order parameter]]; for ferromagnets, this can be [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] and [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]].

- **Long-range correlations near criticality:** At or near a continuous transition, the [[stat-mech/correlation-length|correlation length]] may diverge and the [[stat-mech/susceptibility-stat-mech|susceptibility]] may become large, reflecting critical fluctuations even if the Gibbs measure is unique at the critical point.

- **Mixtures vs pure states:** In the coexistence region, symmetry-invariant equilibrium states can appear as [[stat-mech-lattice/mixture-gibbs-measures|mixtures of pure phases]], which are Gibbs but not extremal.

## Physical interpretation

A phase transition marks a change in the set and nature of equilibrium infinite-volume states: the system can support qualitatively different macroscopic behaviors under the same microscopic rules. In lattice spin systems, this includes transitions between disordered and ordered phases (e.g. paramagnet to ferromagnet), the onset of symmetry breaking, and critical points characterized by scale-free fluctuations and long-range correlations.
