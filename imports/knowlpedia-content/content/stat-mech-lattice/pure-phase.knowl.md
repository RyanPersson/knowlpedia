+++
id = "stat-mech-lattice/pure-phase"
title = "Pure phase"
kind = "knowl"
summary = "A homogeneous equilibrium phase of an infinite lattice system, typically identified with a translation-ergodic (extremal) infinite-volume Gibbs measure."
aliases = ["pure-phase", "Pure phase"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/pure-phase.md"
+++

Informally, a **pure phase** is a single, homogeneous thermodynamic state (no macroscopic coexistence of distinct phases). In the Gibbs/DLR framework for lattice systems, a standard rigorous identification is:

A **pure phase** at fixed interaction and parameters is an [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] that is [[stat-mech-lattice/extremal-gibbs-measure|extremal]] in the Gibbs set and (in many applications) invariant and ergodic under lattice translations when the interaction is [[stat-mech-lattice/translation-invariant-interaction|translation-invariant]].

This definition separates “indecomposable equilibrium states” (extremality) from mixtures (see [[stat-mech-lattice/mixture-gibbs-measures|mixtures of Gibbs measures]]).

## Key properties

- **No decomposition into other phases:** A pure phase cannot be expressed as a nontrivial convex mixture of other Gibbs states.

- **Sharp macroscopic observables:** Order parameters (see [[stat-mech-lattice/order-parameter|order parameter]]) typically take a definite value within a pure phase; fluctuations average out in large volumes (“self-averaging”).

- **Clustering inside a phase (typical):** Many pure phases satisfy a clustering/mixing property: connected [[stat-mech/correlation-function-two-point|two-point correlations]] decay with distance (away from criticality). This distinguishes a single homogeneous phase from a random mixture.

- **Phase multiplicity and transitions:** The existence of more than one pure phase at the same parameters is a hallmark of a [[stat-mech-lattice/phase-transition-gibbs|phase transition]].

- **Symmetry breaking:** In models with global symmetries, distinct pure phases may be related by the symmetry and exhibit [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]]. A classic diagnostic is nonzero [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] in a ferromagnet.

## Physical interpretation

A pure phase is what one expects to observe in a large, well-equilibrated sample when boundary conditions or preparation select a definite macroscopic state. Different pure phases correspond to different stable macroscopic behaviors (e.g. magnetized “up” vs magnetized “down”), while a mixture Gibbs measure represents an ensemble that does not select a single phase and thus encodes phase coexistence or random phase selection.
