---
title: "Universality class"
description: "The equivalence class of microscopic models that share the same long-distance critical behavior, typically controlled by the same RG fixed point."
---

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
- Systems with continuous symmetry in 2D may avoid conventional symmetry-breaking transitions and instead exhibit topological transitions (different class), as in the {{< knowl id="kosterlitz-thouless-transition" text="Kosterlitz–Thouless transition" >}}.

## Prerequisites / cross-links
- {{< knowl id="rg-fixed-point" text="RG fixed point" >}}
- {{< knowl id="renormalization-group-transformation" text="renormalization-group (RG) transformation" >}}
- {{< knowl id="critical-exponent" text="critical exponents" >}}
- {{< knowl id="scaling-relation-exponents" text="scaling relations among exponents" >}}
- {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}
- {{< knowl id="continuous-symmetry-on-spins" text="continuous symmetries on spin systems" >}}
