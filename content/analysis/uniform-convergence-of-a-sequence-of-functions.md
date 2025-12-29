---
title: "Uniform convergence (sequence of functions)"
description: "Convergence f_n→f with a single N(ε) working for all x in the domain."
---

Let $X$ be a set and let $(Y,d_Y)$ be a metric space. A sequence of functions $f_n:X\to Y$ **converges uniformly** to $f:X\to Y$ if
$$\forall \varepsilon>0,\ \exists N\in\mathbb{N}\ \text{such that}\ \forall n\ge N,\ \forall x\in X,\ d_Y\bigl(f_n(x),f(x)\bigr)<\varepsilon.$$
Equivalently,
$$\sup_{x\in X} d_Y\bigl(f_n(x),f(x)\bigr)\xrightarrow[n\to\infty]{}0,$$
where the supremum is taken in $[0,\infty]$.

Uniform convergence is strong enough to pass many properties to the limit (e.g., continuity, under standard hypotheses). It is a central tool in analysis and approximation theory.

**Examples:**
- $f_n(x)=\frac{1}{n}\sin x$ converges uniformly to $0$ on $\mathbb{R}$.
- On $[0,1]$, $f_n(x)=x^n$ converges pointwise to $f$ (as above) but not uniformly (since $\sup_{x\in[0,1]}|x^n-f(x)|=1$ for all $n$).
- If $f_n$ are continuous on a compact set and converge uniformly, then the limit is continuous (uniform limit theorem).
