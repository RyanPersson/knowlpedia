---
title: "Spin space"
description: "The single-site state space of a lattice spin system, together with its natural measurable structure (and often an a priori measure)."
---

A **spin space** is the set $S$ of allowed values for a single spin variable at one lattice site. In a lattice model on the integer lattice (see {{< knowl id="lattice-zd" section="discrete-structures" text="integer lattice" >}}), each site $i$ carries a spin $\sigma_i \in S$.

For probabilistic and Gibbsian formulations, one typically equips $S$ with a $\sigma$-algebra $\mathcal{S}$ (see {{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}}) so that local observables are {{< knowl id="measurable-function" section="measure-theory" text="measurable functions" >}} of $\sigma_i$. Often one also fixes an **a priori measure** $\rho$ on $(S,\mathcal{S})$ (see {{< knowl id="measure" section="measure-theory" text="measure" >}}), which is counting measure for discrete spins and a reference (e.g. Haar/surface) measure for continuous spins.

The spin space determines what a {{< knowl id="spin-configuration" text="spin configuration" >}} is and underlies the full {{< knowl id="configuration-space-lattice" text="configuration space" >}}.

## Common examples
- **Ising spins:** $S=\{-1,+1\}$ (see {{< knowl id="ising-model" text="Ising model" >}}).
- **Potts spins:** $S=\{1,2,\dots,q\}$ (see {{< knowl id="potts-model" text="Potts model" >}}).
- **Lattice gas/occupancy:** $S=\{0,1\}$ (see {{< knowl id="lattice-gas" text="lattice gas" >}}).
- **XY spins:** $S$ is the unit circle (see {{< knowl id="xy-model" text="XY model" >}}).
- **Heisenberg spins:** $S$ is a unit sphere in $\mathbb{R}^n$ (see {{< knowl id="heisenberg-model" text="Heisenberg model" >}}).

## Key properties
- **Discrete vs continuous:** If $S$ is finite/countable, sums replace integrals in the {{< knowl id="partition-function-lattice" text="partition function" >}}; if $S$ is continuous, the choice of a priori measure $\rho$ is part of the model.
- **Compactness/topology (often used):** When $S$ is finite or compact, the product configuration space can inherit useful compactness properties (see {{< knowl id="configuration-space-lattice" text="configuration space" >}}).
- **Symmetries:** Many models have a symmetry group acting on $S$ (e.g. spin-flip for Ising, rotations for XY/Heisenberg). Symmetries on $S$ induce symmetries of the Hamiltonian and Gibbs measures, relevant for {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}.

## Physical interpretation
The spin space represents the **local microscopic degrees of freedom**:
- orientations of a magnetic moment (continuous $S$),
- discrete “up/down” magnetic moments (Ising),
- internal states/colors (Potts),
- presence/absence of a particle (lattice gas).

Changing the choice of $S$ changes the nature of fluctuations and possible ordered phases (e.g. continuous symmetries vs discrete symmetries), influencing whether and how {{< knowl id="phase-transition-gibbs" text="phase transitions" >}} can occur.
