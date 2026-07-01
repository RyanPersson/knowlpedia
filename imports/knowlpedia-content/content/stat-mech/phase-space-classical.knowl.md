+++
id = "stat-mech/phase-space-classical"
title = "Phase space (classical)"
kind = "knowl"
summary = "The space of all possible positions and momenta for a classical mechanical system, fundamental to statistical mechanics."
aliases = ["phase-space-classical", "Phase space (classical)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/phase-space-classical.md"
+++

For a classical mechanical system with $n$ degrees of freedom, the **phase space** is the $2n$-dimensional space
$$
\Gamma = \mathbb{R}^{2n}
$$

(or, more generally, a $2n$-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]]) whose points are pairs $(q, p) = (q_1, \ldots, q_n, p_1, \ldots, p_n)$ of generalized positions $q_i$ and conjugate momenta $p_i$.

A single point in phase space specifies the complete instantaneous [[stat-mech/microstate-classical|microstate]] of the system.

## Examples

- **Single particle in 3D:** Phase space is $\mathbb{R}^6$ with coordinates $(x, y, z, p_x, p_y, p_z)$.
- **$N$ particles in 3D:** Phase space is $\mathbb{R}^{6N}$ with coordinates $(q_1, \ldots, q_{3N}, p_1, \ldots, p_{3N})$.

## Role in statistical mechanics

In the [[stat-mech/microcanonical-ensemble|microcanonical]], [[stat-mech/canonical-ensemble|canonical]], and [[stat-mech/grand-canonical-ensemble|grand canonical]] ensembles, equilibrium distributions are probability measures on phase space. The [[stat-mech/phase-space-volume-element|phase space volume element]] $d^nq\,d^np$ (or $d\Gamma$) is the natural measure for integration.
