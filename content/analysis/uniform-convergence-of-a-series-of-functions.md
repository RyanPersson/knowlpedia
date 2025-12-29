---
title: "Uniform convergence (series of functions)"
description: "A series ∑ f_n converges uniformly if its partial sums converge uniformly."
---

Let $X$ be a set and let $(Y,d_Y)$ be a metric space. A series of functions $\sum_{n=1}^\infty f_n$ **converges uniformly** on $X$ if the sequence of partial sums
$$S_N(x):=\sum_{n=1}^N f_n(x)$$
converges uniformly to a limit function $S:X\to Y$.

Uniform convergence of a series is the main hypothesis under which one can justify term-by-term operations (e.g., continuity passes to the sum; with additional hypotheses, differentiation or integration can be interchanged with summation).

**Examples:**
- On any set $X$, if $|f_n(x)|\le M_n$ for all $x$ and $\sum M_n$ converges, then $\sum f_n$ converges uniformly (Weierstrass M-test).
- The geometric series $\sum_{n=0}^\infty x^n$ converges uniformly on $[-r,r]$ for every $0\le r<1$.
- The series $\sum_{n=1}^\infty x^n$ does not converge uniformly on $(0,1)$ (partial sums blow up near $x=1$).
