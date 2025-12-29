---
title: "Uniform Cauchy sequence of functions"
description: "A sequence (f_n) such that sup_x d(f_m(x),f_n(x))→0 as m,n→∞."
---

Let $X$ be a set and let $(Y,d_Y)$ be a metric space. A sequence of functions $f_n:X\to Y$ is **uniformly Cauchy** if
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall m,n\ge N,\ \forall x\in X,\ d_Y\bigl(f_m(x),f_n(x)\bigr)<\varepsilon.$$
Equivalently,
$$\sup_{x\in X} d_Y\bigl(f_m(x),f_n(x)\bigr)\xrightarrow[m,n\to\infty]{}0.$$

Uniform Cauchy-ness is the Cauchy criterion for uniform convergence: in complete codomains (e.g., $Y=\mathbb{R}$), uniformly Cauchy sequences converge uniformly.

**Examples:**
- If $f_n\to f$ uniformly, then $(f_n)$ is uniformly Cauchy.
- On $X=[0,1]$, define $f_n(x)=\sum_{k=1}^n \frac{x^k}{2^k}$. Then $(f_n)$ is uniformly Cauchy since the tail is bounded by a geometric series.
- Pointwise Cauchy need not be uniformly Cauchy: $f_n(x)=x^n$ is pointwise Cauchy on $[0,1]$ but not uniformly Cauchy.
