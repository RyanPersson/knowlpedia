---
title: "Convergence of a sequence in a metric space"
description: "A sequence converges if points eventually lie arbitrarily close to the limit"
---

Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}. A sequence $(x_n)$ in $X$ **converges** to a point $a\in X$ if
$$
(\forall \varepsilon>0)(\exists N\in\mathbb{N})(\forall n\ge N):\ d(x_n,a)<\varepsilon.
$$
We write $\lim_{n\to\infty}x_n=a$ or $x_n\to a$.

Convergence in metric spaces is the foundation for defining {{< knowl id="closure-characterized-by-convergent-sequences" text="closure via sequences" >}} and for studying {{< knowl id="cauchy-sequence" text="Cauchy sequences" >}}.

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ converges to $0$.
- In any metric space, a constant sequence $x_n=x$ converges to $x$.
- In the discrete metric, $x_n\to a$ iff $x_n=a$ for all sufficiently large $n$.
