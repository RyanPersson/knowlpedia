---
title: "Pure phase"
description: "A homogeneous equilibrium phase of an infinite lattice system, typically identified with a translation-ergodic (extremal) infinite-volume Gibbs measure."
---


Informally, a **pure phase** is a single, homogeneous thermodynamic state (no macroscopic coexistence of distinct phases). In the Gibbs/DLR framework for lattice systems, a standard rigorous identification is:

A **pure phase** at fixed interaction and parameters is an {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measure" >}} that is {{< knowl id="extremal-gibbs-measure" text="extremal" >}} in the Gibbs set and (in many applications) invariant and ergodic under lattice translations when the interaction is {{< knowl id="translation-invariant-interaction" text="translation-invariant" >}}.

This definition separates “indecomposable equilibrium states” (extremality) from mixtures (see {{< knowl id="mixture-gibbs-measures" text="mixtures of Gibbs measures" >}}).

## Key properties

- **No decomposition into other phases:** A pure phase cannot be expressed as a nontrivial convex mixture of other Gibbs states.

- **Sharp macroscopic observables:** Order parameters (see {{< knowl id="order-parameter" text="order parameter" >}}) typically take a definite value within a pure phase; fluctuations average out in large volumes (“self-averaging”).

- **Clustering inside a phase (typical):** Many pure phases satisfy a clustering/mixing property: connected {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}} decay with distance (away from criticality). This distinguishes a single homogeneous phase from a random mixture.

- **Phase multiplicity and transitions:** The existence of more than one pure phase at the same parameters is a hallmark of a {{< knowl id="phase-transition-gibbs" text="phase transition" >}}.

- **Symmetry breaking:** In models with global symmetries, distinct pure phases may be related by the symmetry and exhibit {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}. A classic diagnostic is nonzero {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}} in a ferromagnet.

## Physical interpretation

A pure phase is what one expects to observe in a large, well-equilibrated sample when boundary conditions or preparation select a definite macroscopic state. Different pure phases correspond to different stable macroscopic behaviors (e.g. magnetized “up” vs magnetized “down”), while a mixture Gibbs measure represents an ensemble that does not select a single phase and thus encodes phase coexistence or random phase selection.
