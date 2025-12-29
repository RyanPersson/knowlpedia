---
title: "Convergent sequence"
description: "A sequence whose terms eventually become arbitrarily close to a single limit point."
---

Let $(X,d)$ be a metric space and let $(x_n)_{n\in\mathbb{N}}$ be a sequence in $X$. The sequence is **convergent** if there exists $x\in X$ such that
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall n\ge N,\ d(x_n,x)<\varepsilon.$$
In that case, one writes $x_n\to x$ and calls $x$ the limit.

Convergence is the basic notion underlying limits of functions, continuity, series, and completeness. In a metric space, limits (if they exist) are unique.

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ converges to $0$.
- In $\mathbb{R}^2$, $x_n=(1/n,(-1)^n/n)$ converges to $(0,0)$.
- In a discrete metric space, a sequence converges iff it is eventually constant.
