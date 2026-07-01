+++
id = "stat-mech/pirogov-sinai-theory"
title = "Pirogov–Sinai theory (low-temperature phase diagrams with multiple ground states)"
kind = "knowl"
summary = "A contour-based framework proving existence and stability of multiple Gibbs phases and first-order transitions for low-temperature lattice systems with finitely many competing ground states."
aliases = ["pirogov-sinai-theory", "Pirogov–Sinai theory (low-temperature phase diagrams with multiple ground states)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/pirogov-sinai-theory.md"
+++

## Context
Many lattice models (see [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonians]]) have several distinct ground states at zero temperature. Pirogov–Sinai theory provides a systematic way to analyze the corresponding low-temperature equilibrium structure: existence of multiple [[stat-mech-lattice/infinite-volume-gibbs-measure|Gibbs measures]], stability under perturbations, and precise first-order transition lines.

It builds on contour representations and convergent expansions (see [[stat-mech/cluster-expansion-theorem|cluster expansion]]).

## Theorem (Pirogov–Sinai; standard qualitative form)
Consider a finite-range lattice spin system with:
- a finite set of periodic ground states $\mathcal{G}=\{g_1,\dots,g_m\}$ at zero temperature,
- a Peierls-type condition: excitations above each ground state have energy cost proportional to the size of their boundary (contour cost).

Then there exists $\beta_0<\infty$ such that for all $\beta\ge \beta_0$:

1. **Phase coexistence and pure phases:** for each *stable* ground state $g_k$ there exists a corresponding translation-invariant *pure* infinite-volume Gibbs state $\mu_k$ solving the [[stat-mech-lattice/dlr-equation|DLR equations]].

2. **Uniqueness away from coexistence:** in regions of parameter space where a single ground state is stable, the infinite-volume Gibbs measure is unique and correlations decay exponentially (finite [[stat-mech/correlation-length|correlation length]]).

3. **First-order transitions:** coexistence surfaces (where two or more ground states have equal free-energy competition) correspond to first-order transitions: multiple Gibbs states exist and macroscopic observables (e.g. an [[stat-mech-lattice/order-parameter|order parameter]]) exhibit discontinuities across the surface.

4. **Interfaces and surface tension:** at coexistence, mixed boundary conditions generate stable interfaces with positive [[stat-mech/surface-tension-interface|surface tension]], giving control of droplet formation and providing a rigorous foundation for [[stat-mech/metastable-state|metastability]] at low temperature.

## What you can do with it
- Prove low-temperature phase diagrams for models like Potts-type systems, Ising models with fields or competing interactions, lattice gases, and small perturbations of exactly solvable ground-state structures.
- Establish sharp statements about stable phases, coexistence lines, and interface costs in terms of contour weights and convergent expansions.

## Prerequisites and connections (cross-links)
- Gibbs formalism on lattices: [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]], [[stat-mech-lattice/dlr-equation|DLR equations]], [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]].
- Thermodynamic potentials: [[stat-mech/free-energy-statistical|free energy]], [[stat-mech/pressure-log-partition-density|pressure (log-partition density)]].
- Phase-transition diagnostics: [[stat-mech-lattice/phase-transition-gibbs|phase transitions in Gibbs measures]], [[stat-mech/tfae-gibbs-measure-characterizations|equivalent Gibbs characterizations]].
- Expansion technology: [[stat-mech/cluster-expansion-theorem|cluster expansion theorem]].
