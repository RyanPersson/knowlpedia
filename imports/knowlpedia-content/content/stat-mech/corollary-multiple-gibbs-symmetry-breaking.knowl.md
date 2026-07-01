+++
id = "stat-mech/corollary-multiple-gibbs-symmetry-breaking"
title = "Multiple Gibbs states and spontaneous symmetry breaking"
kind = "knowl"
summary = "In symmetric lattice models, coexistence of distinct Gibbs measures at zero field yields spontaneous symmetry breaking (e.g. plus/minus phases in the Ising model)."
aliases = ["corollary-multiple-gibbs-symmetry-breaking", "Multiple Gibbs states and spontaneous symmetry breaking"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-multiple-gibbs-symmetry-breaking.md"
+++

## Statement (symmetry breaking from phase coexistence)
Consider a lattice spin system with a global symmetry (e.g. spin-flip symmetry in the [[stat-mech-lattice/ising-model|Ising model]] at external field $h=0$). Suppose that at some parameter values (typically low temperature) there exist **at least two distinct** [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] for the same specification.

Then the symmetry is **spontaneously broken** in the sense that there exist distinct Gibbs measures $\mu^{(1)}\neq \mu^{(2)}$ such that a symmetry-related order parameter takes different values in these states (e.g. magnetization differs).

For the ferromagnetic Ising model in dimension $d\ge 2$, the [[stat-mech/peierls-argument|Peierls argument]] implies that for sufficiently large $\beta$ (low temperature) there are at least two distinct translation-invariant Gibbs measures $\mu^+$ and $\mu^-$ obtained as limits with $+$ and $-$ boundary conditions, and they satisfy
- $\mu^-(\sigma_0) = -\,\mu^+(\sigma_0)$ (spin-flip symmetry),
- $\mu^+(\sigma_0) > 0$ (nonzero spontaneous magnetization).

## Key hypotheses
- A symmetric specification (e.g. invariance under global spin flip when $h=0$).
- Existence of multiple Gibbs measures (phase coexistence), typically shown via [[stat-mech/peierls-argument|Peierls argument]] or other low-temperature methods.
- An order parameter odd under the symmetry (e.g. single-site spin $\sigma_0$).

## Conclusions
- **Nonuniqueness** of Gibbs states produces physically distinct macroscopic phases.
- The symmetry is not realized in each pure phase (each extremal state), but is restored by mixtures:
  the symmetric state can be formed as $\tfrac12(\mu^+ + \mu^-)$, which is Gibbs but not extremal.

## Cross-links (definitions and supporting results)
- [[stat-mech-lattice/ising-model|Ising model]]
- [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]], [[stat-mech-lattice/extremal-gibbs-measure|extremal (pure) Gibbs measures]]
- [[stat-mech-lattice/phase-transition-gibbs|phase transition via Gibbs nonuniqueness]]
- [[stat-mech/corollary-uniqueness-analyticity|uniqueness implies no phase transition]]
- [[stat-mech/corollary-multiple-gibbs-symmetry-breaking|this corollary]]
## significance
In symmetric models, if two distinct infinite-volume Gibbs measures exist and the symmetry maps Gibbs measures to Gibbs measures, then applying the symmetry to one state produces another. In the Ising case at $h=0$, spin flip maps a $+$-magnetized state to a $-$-magnetized state. The [[stat-mech/peierls-argument|Peierls argument]] constructs low-temperature stability of $+$ (and $-$) boundary conditions, producing distinct limiting Gibbs measures with opposite magnetizations. This is the canonical mechanism for spontaneous symmetry breaking in equilibrium statistical mechanics.
