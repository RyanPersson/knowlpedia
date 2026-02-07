---
title: "Multiple Gibbs states and spontaneous symmetry breaking"
description: "In symmetric lattice models, coexistence of distinct Gibbs measures at zero field yields spontaneous symmetry breaking (e.g. plus/minus phases in the Ising model)."
---

## Statement (symmetry breaking from phase coexistence)
Consider a lattice spin system with a global symmetry (e.g. spin-flip symmetry in the {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} at external field $h=0$). Suppose that at some parameter values (typically low temperature) there exist **at least two distinct** {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} for the same specification.

Then the symmetry is **spontaneously broken** in the sense that there exist distinct Gibbs measures $\mu^{(1)}\neq \mu^{(2)}$ such that a symmetry-related order parameter takes different values in these states (e.g. magnetization differs).

For the ferromagnetic Ising model in dimension $d\ge 2$, the {{< knowl id="peierls-argument" text="Peierls argument" >}} implies that for sufficiently large $\beta$ (low temperature) there are at least two distinct translation-invariant Gibbs measures $\mu^+$ and $\mu^-$ obtained as limits with $+$ and $-$ boundary conditions, and they satisfy
- $\mu^-(\sigma_0) = -\,\mu^+(\sigma_0)$ (spin-flip symmetry),
- $\mu^+(\sigma_0) > 0$ (nonzero spontaneous magnetization).

## Key hypotheses
- A symmetric specification (e.g. invariance under global spin flip when $h=0$).
- Existence of multiple Gibbs measures (phase coexistence), typically shown via {{< knowl id="peierls-argument" text="Peierls argument" >}} or other low-temperature methods.
- An order parameter odd under the symmetry (e.g. single-site spin $\sigma_0$).

## Conclusions
- **Nonuniqueness** of Gibbs states produces physically distinct macroscopic phases.
- The symmetry is not realized in each pure phase (each extremal state), but is restored by mixtures:
  the symmetric state can be formed as $\tfrac12(\mu^+ + \mu^-)$, which is Gibbs but not extremal.

## Cross-links (definitions and supporting results)
- {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}
- {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}, {{< knowl id="extremal-gibbs-measure" section="stat-mech-lattice" text="extremal (pure) Gibbs measures" >}}
- {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition via Gibbs nonuniqueness" >}}
- {{< knowl id="corollary-uniqueness-analyticity" text="uniqueness implies no phase transition" >}}
- {{< knowl id="corollary-multiple-gibbs-symmetry-breaking" text="this corollary" >}}
## significance
In symmetric models, if two distinct infinite-volume Gibbs measures exist and the symmetry maps Gibbs measures to Gibbs measures, then applying the symmetry to one state produces another. In the Ising case at $h=0$, spin flip maps a $+$-magnetized state to a $-$-magnetized state. The {{< knowl id="peierls-argument" text="Peierls argument" >}} constructs low-temperature stability of $+$ (and $-$) boundary conditions, producing distinct limiting Gibbs measures with opposite magnetizations. This is the canonical mechanism for spontaneous symmetry breaking in equilibrium statistical mechanics.

