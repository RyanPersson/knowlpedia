---
title: "Mermin–Wagner theorem (no continuous symmetry breaking in d ≤ 2)"
description: "For short-range systems with a continuous symmetry, spontaneous symmetry breaking and conventional long-range order are impossible in one and two dimensions at positive temperature."
---

## Context
In lattice statistical mechanics, a {{< knowl id="spontaneous-symmetry-breaking-group" section="stat-mech-lattice" text="spontaneous symmetry breaking" >}} phase is detected by a nonzero {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}} (e.g. magnetization) or by multiple {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs states" >}}.

For models with a *continuous* symmetry (see {{< knowl id="continuous-symmetry-on-spins" text="continuous symmetry on spins" >}}), low-dimensional fluctuations can destroy long-range order even when interactions are ferromagnetic and short-range.

## Theorem (Mermin–Wagner; lattice spin systems, informal standard form)
Consider a translation-invariant, finite-range (or sufficiently fast decaying) lattice spin system in dimension $d\le 2$ whose Hamiltonian is invariant under a nontrivial continuous compact Lie group (e.g. $O(n)$ rotations with $n\ge 2$). Then at any positive temperature:
1. There is **no spontaneous breaking** of that continuous symmetry.
2. In particular, any symmetry-breaking magnetization order parameter vanishes:
   $$
   \langle \mathbf{S}_0\rangle = 0
   $$
   in every translation-invariant {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="Gibbs measure" >}}.

A common corollary is the absence of conventional ferromagnetic long-range order:
$$
\lim_{|x|\to\infty}\langle \mathbf{S}_0\cdot \mathbf{S}_x\rangle = 0
\quad (d\le 2,\ T>0),
$$
where the bracket denotes an {{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}} and the left-hand side is a {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}} limit.

## Why it matters (examples and contrasts)
- **2D XY / 2D Heisenberg:** no nonzero magnetization at $T>0$, but the 2D XY model can still have a {{< knowl id="kosterlitz-thouless-transition" text="Kosterlitz–Thouless transition" >}} with quasi-long-range order (power-law correlations) rather than true long-range order.
- **Discrete symmetry is different:** the theorem does *not* apply to discrete symmetries like the $\mathbb{Z}_2$ symmetry of the {{< knowl id="ising-model" section="stat-mech-lattice" text="2D Ising model" >}}, which *does* exhibit spontaneous magnetization below $T_c$ (see {{< knowl id="onsager-2d-ising-solution" section="stat-mech-lattice" text="Onsager’s solution" >}}).

## Technical conditions (typical hypotheses)
Precise statements depend on the setting, but usually assume:
- finite-range or summable interactions (a condition on the {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}),
- continuous symmetry acting nontrivially on the single-site spin space,
- finite temperature Gibbs equilibrium described via the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equations" >}}.

## Prerequisites and connections (cross-links)
- Equilibrium notion: {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}, {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR condition" >}}.
- Order and correlations: {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}, {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}.
