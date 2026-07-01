+++
id = "stat-mech-lattice/spin-space"
title = "Spin space"
kind = "knowl"
summary = "The single-site state space of a lattice spin system, together with its natural measurable structure (and often an a priori measure)."
aliases = ["spin-space", "Spin space"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/spin-space.md"
+++

A **spin space** is the set $S$ of allowed values for a single spin variable at one lattice site. In a lattice model on the integer lattice (see [[discrete-structures/lattice-zd|integer lattice]]), each site $i$ carries a spin $\sigma_i \in S$.

For probabilistic and Gibbsian formulations, one typically equips $S$ with a $\sigma$-algebra $\mathcal{S}$ (see [[measure-theory/sigma-algebra|sigma-algebra]]) so that local observables are [[measure-theory/measurable-function|measurable functions]] of $\sigma_i$. Often one also fixes an **a priori measure** $\rho$ on $(S,\mathcal{S})$ (see [[measure-theory/measure|measure]]), which is counting measure for discrete spins and a reference (e.g. Haar/surface) measure for continuous spins.

The spin space determines what a [[stat-mech-lattice/spin-configuration|spin configuration]] is and underlies the full [[stat-mech-lattice/configuration-space-lattice|configuration space]].

## Common examples
- **Ising spins:** $S=\{-1,+1\}$ (see [[stat-mech-lattice/ising-model|Ising model]]).
- **Potts spins:** $S=\{1,2,\dots,q\}$ (see [[stat-mech-lattice/potts-model|Potts model]]).
- **Lattice gas/occupancy:** $S=\{0,1\}$ (see [[stat-mech-lattice/lattice-gas|lattice gas]]).
- **XY spins:** $S$ is the unit circle (see [[stat-mech-lattice/xy-model|XY model]]).
- **Heisenberg spins:** $S$ is a unit sphere in $\mathbb{R}^n$ (see [[stat-mech-lattice/heisenberg-model|Heisenberg model]]).

## Key properties
- **Discrete vs continuous:** If $S$ is finite/countable, sums replace integrals in the [[stat-mech-lattice/partition-function-lattice|partition function]]; if $S$ is continuous, the choice of a priori measure $\rho$ is part of the model.
- **Compactness/topology (often used):** When $S$ is finite or compact, the product configuration space can inherit useful compactness properties (see [[stat-mech-lattice/configuration-space-lattice|configuration space]]).
- **Symmetries:** Many models have a symmetry group acting on $S$ (e.g. spin-flip for Ising, rotations for XY/Heisenberg). Symmetries on $S$ induce symmetries of the Hamiltonian and Gibbs measures, relevant for [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]].

## Physical interpretation
The spin space represents the **local microscopic degrees of freedom**:
- orientations of a magnetic moment (continuous $S$),
- discrete “up/down” magnetic moments (Ising),
- internal states/colors (Potts),
- presence/absence of a particle (lattice gas).

Changing the choice of $S$ changes the nature of fluctuations and possible ordered phases (e.g. continuous symmetries vs discrete symmetries), influencing whether and how [[stat-mech-lattice/phase-transition-gibbs|phase transitions]] can occur.
