---
title: "Peierls argument"
description: "A contour estimate showing phase coexistence for the ferromagnetic Ising model on Z^d (d≥2) at sufficiently low temperature."
---

## Statement

Consider the nearest-neighbor ferromagnetic {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} on $\mathbb{Z}^d$ with $d\ge 2$, coupling $J>0$, and zero external field. Let $\mu_{\Lambda}^{+}$ denote the {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}} in a finite region $\Lambda$ with **plus** boundary condition.

Then there exists $\beta_0<\infty$ such that for all inverse temperatures $\beta>\beta_0$:

1. The probability (under plus boundary condition) that the origin is negative is small:
   $\mu_{\Lambda}^{+}(\sigma_0=-1)$ can be bounded by a convergent contour sum uniformly in large $\Lambda$.

2. Consequently, the infinite-volume plus state $\mu^{+}$ (any weak limit of $\mu_{\Lambda}^{+}$ as $\Lambda\uparrow\mathbb{Z}^d$) has **strictly positive magnetization**:
   $\mu^{+}(\sigma_0)>0$.

3. The plus and minus infinite-volume Gibbs states are distinct, so there are **at least two** {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} at low temperature:
   $\mu^{+}\neq \mu^{-}$.

In particular, the model exhibits {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase coexistence / a phase transition" >}} for sufficiently large $\beta$.

## Key hypotheses

- **Dimension:** $d\ge 2$ (so domain walls form nontrivial closed contours/surfaces).
- **Ferromagnetic coupling:** $J>0$ (aligning spins lowers energy).
- **Zero field:** $h=0$ (symmetry between $+$ and $-$ phases).
- **Low temperature:** $\beta$ large.

## Key conclusions

- **Peierls estimate:** configurations with a “droplet” of $-$ spins inside $+$ boundary conditions pay an energy cost proportional to the size of the droplet boundary (a contour/surface).
- **Spontaneous magnetization:** $\mu^{+}(\sigma_0)>0$ (and similarly $\mu^{-}(\sigma_0)<0$).
- **Non-uniqueness of Gibbs measures:** there are multiple infinite-volume Gibbs states, typically extremal ones {{< knowl id="extremal-gibbs-measure" section="stat-mech-lattice" text="extremal Gibbs measures" >}} corresponding to $+$ and $-$ phases.

