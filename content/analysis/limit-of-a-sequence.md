---
title: "Limit of a sequence"
description: "A point x such that x_n becomes arbitrarily close to x as n→∞."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. A point $x\in X$ is the **limit** of $(x_n)$ if
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall n\ge N,\ d(x_n,x)<\varepsilon.$$
One writes $x=\lim_{n\to\infty}x_n$ or $x_n\to x$.

The limit (when it exists) summarizes the eventual behavior of a sequence. In metric spaces, a sequence has at most one limit (see {{< knowl id="convergent-sequence" text="convergent sequence" >}}).

**Examples:**
- $\lim_{n\to\infty} (1/n)=0$ in $\mathbb{R}$.
- If $x_n=2$ for all $n$, then $\lim_{n\to\infty}x_n=2$.
- The sequence $(-1)^n$ has no limit in $\mathbb{R}$.
