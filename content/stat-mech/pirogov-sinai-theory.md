---
title: "Pirogov–Sinai theory (low-temperature phase diagrams with multiple ground states)"
description: "A contour-based framework proving existence and stability of multiple Gibbs phases and first-order transitions for low-temperature lattice systems with finitely many competing ground states."
---

## Context
Many lattice models (see {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonians" >}}) have several distinct ground states at zero temperature. Pirogov–Sinai theory provides a systematic way to analyze the corresponding low-temperature equilibrium structure: existence of multiple {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="Gibbs measures" >}}, stability under perturbations, and precise first-order transition lines.

It builds on contour representations and convergent expansions (see {{< knowl id="cluster-expansion-theorem" text="cluster expansion" >}}).

## Theorem (Pirogov–Sinai; standard qualitative form)
Consider a finite-range lattice spin system with:
- a finite set of periodic ground states $\mathcal{G}=\{g_1,\dots,g_m\}$ at zero temperature,
- a Peierls-type condition: excitations above each ground state have energy cost proportional to the size of their boundary (contour cost).

Then there exists $\beta_0<\infty$ such that for all $\beta\ge \beta_0$:

1. **Phase coexistence and pure phases:** for each *stable* ground state $g_k$ there exists a corresponding translation-invariant *pure* infinite-volume Gibbs state $\mu_k$ solving the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equations" >}}.

2. **Uniqueness away from coexistence:** in regions of parameter space where a single ground state is stable, the infinite-volume Gibbs measure is unique and correlations decay exponentially (finite {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}).

3. **First-order transitions:** coexistence surfaces (where two or more ground states have equal free-energy competition) correspond to first-order transitions: multiple Gibbs states exist and macroscopic observables (e.g. an {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}) exhibit discontinuities across the surface.

4. **Interfaces and surface tension:** at coexistence, mixed boundary conditions generate stable interfaces with positive {{< knowl id="surface-tension-interface" text="surface tension" >}}, giving control of droplet formation and providing a rigorous foundation for {{< knowl id="metastable-state" text="metastability" >}} at low temperature.

## What you can do with it
- Prove low-temperature phase diagrams for models like Potts-type systems, Ising models with fields or competing interactions, lattice gases, and small perturbations of exactly solvable ground-state structures.
- Establish sharp statements about stable phases, coexistence lines, and interface costs in terms of contour weights and convergent expansions.

## Prerequisites and connections (cross-links)
- Gibbs formalism on lattices: {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}, {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equations" >}}, {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}.
- Thermodynamic potentials: {{< knowl id="free-energy-statistical" section="stat-mech" text="free energy" >}}, {{< knowl id="pressure-log-partition-density" text="pressure (log-partition density)" >}}.
- Phase-transition diagnostics: {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions in Gibbs measures" >}}, {{< knowl id="tfae-gibbs-measure-characterizations" text="equivalent Gibbs characterizations" >}}.
- Expansion technology: {{< knowl id="cluster-expansion-theorem" text="cluster expansion theorem" >}}.
