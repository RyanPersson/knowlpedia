---
title: "Phase coexistence implies nondifferentiability of the pressure"
description: "If multiple Gibbs phases exist at the same parameters with different order-parameter expectations, the thermodynamic pressure is not differentiable in the conjugate field."
---

Consider a lattice system in finite volume $\Lambda$ with an external field $h$ coupled linearly to an extensive order parameter $A_\Lambda$:
$H_{\Lambda,h}=H_{\Lambda,0}-h\,A_\Lambda$.
Let $Z_\Lambda(\beta,h)$ be the {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}} and
$p_\Lambda(\beta,h)=\frac{1}{|\Lambda|}\log Z_\Lambda(\beta,h)$ the finite-volume {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}}.

Assume the thermodynamic limit pressure exists:
$$
p(\beta,h)=\lim_{\Lambda\uparrow\mathbb{Z}^d} p_\Lambda(\beta,h),
$$
with the limit taken along a standard van Hove sequence.

## Statement
The function $h\mapsto p(\beta,h)$ is convex. Moreover:

- If $p(\beta,h)$ is differentiable at a given $h$, then every {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}} $\mu$ at parameters $(\beta,h)$ has the same order-parameter density
  $$
  a(\mu)=\lim_{\Lambda\uparrow\mathbb{Z}^d}\frac{1}{|\Lambda|}\,\mathbb{E}_\mu[A_\Lambda],
  $$
  and it is fixed by the derivative:
  $$
  a(\mu)=\frac{1}{\beta}\,\partial_h p(\beta,h).
  $$

- Conversely, if there exist two Gibbs measures $\mu_1,\mu_2$ at the same $(\beta,h)$ with
  $$
  a(\mu_1)\neq a(\mu_2),
  $$

  then $p(\beta,h)$ is **not** differentiable at $h$; equivalently, the left and right derivatives satisfy
  $$
  \partial_h^- p(\beta,h) < \partial_h^+ p(\beta,h).
  $$
  This is a first-order transition / phase coexistence signature in the sense of {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="Gibbs-phase transitions" >}}.

In the important special case $A_\Lambda=M_\Lambda$ (magnetization), this connects coexistence of distinct magnetized phases to a cusp in $h\mapsto p(\beta,h)$.

## Key hypotheses
- Linear field coupling $-hA_\Lambda$.
- Existence of the thermodynamic limit pressure $p(\beta,h)$.
- Existence of at least two infinite-volume Gibbs measures at the same $(\beta,h)$ with different $a(\mu)$ (for the “coexistence $\Rightarrow$ nondifferentiability” direction).

## Conclusions
- Differentiability of $p(\beta,h)$ at $h$ rules out coexistence of Gibbs states with different densities of the conjugate order parameter.
- Coexistence forces a non-single-valued “slope” at $h$ (a nontrivial subgradient), hence nondifferentiability.
- In convex-analysis language (see {{< knowl id="convex-function-via-epigraph" section="convex-analysis" text="convex functions" >}}), multiple coexisting values of $a(\mu)$ correspond to a nontrivial subdifferential of $p(\beta,\cdot)$ at $h$.

