---
title: "Uniform convergence on compact sets"
description: "Convergence that is uniform when restricted to each compact subset of the domain."
---

Let $(X,d_X)$ be a metric space, let $(Y,d_Y)$ be a metric space, and let $f_n:E\to Y$ with $E\subseteq X$. The sequence $(f_n)$ **converges uniformly on compact sets** to $f:E\to Y$ if for every compact set $K\subseteq E$ (compact in the subspace metric),
$$\sup_{x\in K} d_Y\bigl(f_n(x),f(x)\bigr)\xrightarrow[n\to\infty]{}0.$$

This mode of convergence is weaker than uniform convergence on all of $E$ when $E$ is not compact. It is particularly important for power series and sequences of functions on noncompact domains.

**Examples:**
- $f_n(x)=x/n$ on $\mathbb{R}$ converges uniformly on compact sets to $0$ (and in fact uniformly on all of $\mathbb{R}$).
- $f_n(x)=x^n$ on $(0,1)$ converges pointwise to $0$ and uniformly on compact sets $K\subset(0,1)$, but not uniformly on $(0,1)$.
- For power series $\sum a_n x^n$ with radius $R>0$, the partial sums converge uniformly on compact subsets of $(-R,R)$.
