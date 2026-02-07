---
title: "Phase space (classical)"
description: "The space of all possible positions and momenta for a classical mechanical system, fundamental to statistical mechanics."
---

For a classical mechanical system with $n$ degrees of freedom, the **phase space** is the $2n$-dimensional space
$$
\Gamma = \mathbb{R}^{2n}
$$

(or, more generally, a $2n$-dimensional {{< knowl id="symplectic-manifold" section="differential-geometry" text="symplectic manifold" >}}) whose points are pairs $(q, p) = (q_1, \ldots, q_n, p_1, \ldots, p_n)$ of generalized positions $q_i$ and conjugate momenta $p_i$.

A single point in phase space specifies the complete instantaneous {{< knowl id="microstate-classical" text="microstate" >}} of the system.

## Examples

- **Single particle in 3D:** Phase space is $\mathbb{R}^6$ with coordinates $(x, y, z, p_x, p_y, p_z)$.
- **$N$ particles in 3D:** Phase space is $\mathbb{R}^{6N}$ with coordinates $(q_1, \ldots, q_{3N}, p_1, \ldots, p_{3N})$.

## Role in statistical mechanics

In the {{< knowl id="microcanonical-ensemble" text="microcanonical" >}}, {{< knowl id="canonical-ensemble" text="canonical" >}}, and {{< knowl id="grand-canonical-ensemble" text="grand canonical" >}} ensembles, equilibrium distributions are probability measures on phase space. The {{< knowl id="phase-space-volume-element" text="phase space volume element" >}} $d^nq\,d^np$ (or $d\Gamma$) is the natural measure for integration.
