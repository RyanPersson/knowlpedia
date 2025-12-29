---
title: "Convergent sequence"
description: "A sequence whose terms eventually become arbitrarily close to a single limit point."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)_{n\in\mathbb{N}}$ be a sequence in $X$. The sequence is **convergent** if there exists $x\in X$ such that
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall n\ge N,\ d(x_n,x)<\varepsilon.$$
In that case, one writes $x_n\to x$ and calls $x$ the {{< knowl id="limit-of-a-sequence" text="limit" >}}.

Convergence is the basic notion underlying {{< knowl id="limit-of-a-function-at-a-point" text="limits of functions" >}}, {{< knowl id="continuity-at-a-point" text="continuity" >}}, {{< knowl id="series" text="series" >}}, and {{< knowl id="complete-metric-space" text="completeness" >}}. In a metric space, limits (if they exist) are unique.

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ converges to $0$.
- In $\mathbb{R}^2$, $x_n=(1/n,(-1)^n/n)$ converges to $(0,0)$.
- In a discrete metric space, a sequence converges iff it is eventually constant.
