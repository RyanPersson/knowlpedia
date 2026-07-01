+++
id = "stat-mech/universality-class"
title = "Universality class"
kind = "knowl"
summary = "The equivalence class of microscopic models that share the same long-distance critical behavior, typically controlled by the same RG fixed point."
aliases = ["universality-class", "Universality class"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/universality-class.md"
+++

## Definition (universality class)
Two families of models (lattice or continuum) are in the same **universality class** if, after appropriate identification of macroscopic observables and rescalings, they share the same asymptotic long-distance behavior near criticality. Concretely, this is reflected in agreement of:
- critical exponents (e.g., $\alpha,\beta,\gamma,\nu,\eta,\delta$),
- scaling forms (equation-of-state scaling functions, finite-size scaling functions),
- operator content/relevant perturbations around the controlling fixed point.

## RG characterization
In RG terms, a universality class is associated with an (infrared) stable fixed point $g^\star$ and its spectrum of relevant directions.
- Different microscopic Hamiltonians flow under RG to the same $g^\star$.
- Microscopic differences correspond to irrelevant operators (they do not affect the scaling limit).
- Relevant perturbations correspond to the few parameters that must be tuned to reach criticality (typically temperature-like and field-like).

## What data typically determine the class
While details depend on the setting, the following features often control the universality class:
- spatial dimension $d$,
- symmetry of the order parameter (e.g., $\mathbb{Z}_2$, $O(N)$),
- range of interactions (short-range vs long-range),
- nature of the order parameter and constraints (scalar vs vector, conserved vs nonconserved dynamics in dynamical settings).

## Example contrasts (informal)
- The 2D Ising model and many other $\mathbb{Z}_2$-symmetric short-range models share the same critical exponents and scaling functions (same class).
- Systems with continuous symmetry in 2D may avoid conventional symmetry-breaking transitions and instead exhibit topological transitions (different class), as in the [[stat-mech/kosterlitz-thouless-transition|Kosterlitz–Thouless transition]].

## Prerequisites / cross-links
- [[stat-mech/rg-fixed-point|RG fixed point]]
- [[stat-mech/renormalization-group-transformation|renormalization-group (RG) transformation]]
- [[stat-mech/critical-exponent|critical exponents]]
- [[stat-mech/scaling-relation-exponents|scaling relations among exponents]]
- [[stat-mech-lattice/ising-model|Ising model]]
- [[stat-mech/continuous-symmetry-on-spins|continuous symmetries on spin systems]]
