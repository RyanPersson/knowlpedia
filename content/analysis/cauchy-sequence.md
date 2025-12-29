---
title: "Cauchy sequence"
description: "A sequence whose terms become arbitrarily close to each other."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. The sequence is **Cauchy** if
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall m,n\ge N,\ d(x_m,x_n)<\varepsilon.$$

A Cauchy sequence is one that has "intrinsic convergence" without reference to a candidate limit. {{< knowl id="complete-metric-space" text="Completeness" >}} of a metric space is the statement that every Cauchy sequence actually {{< knowl id="convergent-sequence" text="converges" >}} in the space.

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ is Cauchy (and converges to $0$).
- In $\mathbb{Q}$ with the usual metric, a rational sequence approximating $\sqrt{2}$ is Cauchy but does not converge in $\mathbb{Q}$.
- In a discrete metric space, a sequence is Cauchy iff it is eventually constant.
