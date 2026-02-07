---
title: "Phase transition (Gibbsian viewpoint)"
description: "A qualitative change in infinite-volume equilibrium behavior, often detected by non-uniqueness of Gibbs measures and/or non-analyticity of the thermodynamic-limit pressure."
---


Consider a lattice spin system with fixed interaction (e.g. via an {{< knowl id="interaction-potential-phi" text="interaction potential" >}}) and parameters such as {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta$ and external field (see {{< knowl id="external-field-coupling" text="external field coupling" >}}). Let $\mathcal{G}(\gamma)$ be the set of {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} solving the {{< knowl id="dlr-equation" text="DLR equation" >}} for the associated {{< knowl id="gibbs-specification" text="Gibbs specification" >}} $\gamma$.

A **Gibbs phase transition** is commonly signaled by **non-uniqueness**:
- there exist at least two distinct measures $\mu,\nu \in \mathcal{G}(\gamma)$.

Equivalently (in many standard settings), different {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}} produce different infinite-volume limits of {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measures" >}}.

A complementary thermodynamic signature is **non-analyticity** of the {{< knowl id="pressure-lattice" text="lattice pressure" >}} in the {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}} as a function of parameters. Both viewpoints are widely used; non-uniqueness corresponds most directly to phase coexistence, while non-analyticity captures both first-order and continuous critical phenomena.

## Key properties

- **Coexistence of pure phases:** When non-uniqueness holds, $\mathcal{G}(\gamma)$ contains multiple {{< knowl id="pure-phase" text="pure phases" >}}, i.e. multiple {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}} distinguished by macroscopic observables (magnetization, density, etc.).

- **Order parameter behavior:** A phase transition is often accompanied by a qualitative change or discontinuity in an {{< knowl id="order-parameter" text="order parameter" >}}; for ferromagnets, this can be {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}} and {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}.

- **Long-range correlations near criticality:** At or near a continuous transition, the {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} may diverge and the {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}} may become large, reflecting critical fluctuations even if the Gibbs measure is unique at the critical point.

- **Mixtures vs pure states:** In the coexistence region, symmetry-invariant equilibrium states can appear as {{< knowl id="mixture-gibbs-measures" text="mixtures of pure phases" >}}, which are Gibbs but not extremal.

## Physical interpretation

A phase transition marks a change in the set and nature of equilibrium infinite-volume states: the system can support qualitatively different macroscopic behaviors under the same microscopic rules. In lattice spin systems, this includes transitions between disordered and ordered phases (e.g. paramagnet to ferromagnet), the onset of symmetry breaking, and critical points characterized by scale-free fluctuations and long-range correlations.
