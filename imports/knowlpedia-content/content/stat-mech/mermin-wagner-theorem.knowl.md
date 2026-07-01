+++
id = "stat-mech/mermin-wagner-theorem"
title = "Mermin–Wagner theorem (no continuous symmetry breaking in d ≤ 2)"
kind = "knowl"
summary = "For short-range systems with a continuous symmetry, spontaneous symmetry breaking and conventional long-range order are impossible in one and two dimensions at positive temperature."
aliases = ["mermin-wagner-theorem", "Mermin–Wagner theorem (no continuous symmetry breaking in d ≤ 2)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/mermin-wagner-theorem.md"
+++

## Context
In lattice statistical mechanics, a [[stat-mech-lattice/spontaneous-symmetry-breaking-group|spontaneous symmetry breaking]] phase is detected by a nonzero [[stat-mech-lattice/order-parameter|order parameter]] (e.g. magnetization) or by multiple [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs states]].

For models with a *continuous* symmetry (see [[stat-mech/continuous-symmetry-on-spins|continuous symmetry on spins]]), low-dimensional fluctuations can destroy long-range order even when interactions are ferromagnetic and short-range.

## Theorem (Mermin–Wagner; lattice spin systems, informal standard form)
Consider a translation-invariant, finite-range (or sufficiently fast decaying) lattice spin system in dimension $d\le 2$ whose Hamiltonian is invariant under a nontrivial continuous compact Lie group (e.g. $O(n)$ rotations with $n\ge 2$). Then at any positive temperature:
1. There is **no spontaneous breaking** of that continuous symmetry.
2. In particular, any symmetry-breaking magnetization order parameter vanishes:
   $$
   \langle \mathbf{S}_0\rangle = 0
   $$
   in every translation-invariant [[stat-mech-lattice/infinite-volume-gibbs-measure|Gibbs measure]].

A common corollary is the absence of conventional ferromagnetic long-range order:
$$
\lim_{|x|\to\infty}\langle \mathbf{S}_0\cdot \mathbf{S}_x\rangle = 0
\quad (d\le 2,\ T>0),
$$
where the bracket denotes an [[stat-mech/ensemble-average|ensemble average]] and the left-hand side is a [[stat-mech/correlation-function-two-point|two-point correlation function]] limit.

## Why it matters (examples and contrasts)
- **2D XY / 2D Heisenberg:** no nonzero magnetization at $T>0$, but the 2D XY model can still have a [[stat-mech/kosterlitz-thouless-transition|Kosterlitz–Thouless transition]] with quasi-long-range order (power-law correlations) rather than true long-range order.
- **Discrete symmetry is different:** the theorem does *not* apply to discrete symmetries like the $\mathbb{Z}_2$ symmetry of the [[stat-mech-lattice/ising-model|2D Ising model]], which *does* exhibit spontaneous magnetization below $T_c$ (see [[stat-mech-lattice/onsager-2d-ising-solution|Onsager’s solution]]).

## Technical conditions (typical hypotheses)
Precise statements depend on the setting, but usually assume:
- finite-range or summable interactions (a condition on the [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]]),
- continuous symmetry acting nontrivially on the single-site spin space,
- finite temperature Gibbs equilibrium described via the [[stat-mech-lattice/dlr-equation|DLR equations]].

## Prerequisites and connections (cross-links)
- Equilibrium notion: [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]], [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]], [[stat-mech-lattice/dlr-equation|DLR condition]].
- Order and correlations: [[stat-mech-lattice/order-parameter|order parameter]], [[stat-mech/correlation-length|correlation length]].
