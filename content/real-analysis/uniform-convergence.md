---
title: "Uniform convergence"
description: "Convergence of functions with an error bound that is uniform in the domain variable."
---

A sequence of functions $(f_n)$ from a set $X$ into a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(Y,d)$ **converges uniformly** to a function $f:X\to Y$ if for every $\varepsilon>0$ there exists $N$ such that for all $n\ge N$ and all $x\in X$,
\[
d\bigl(f_n(x),f(x)\bigr)<\varepsilon.
\]
Equivalently,
\[
\sup_{x\in X} d\bigl(f_n(x),f(x)\bigr)\to 0 \quad \text{as } n\to\infty.
\]

Uniform convergence implies {{< knowl id="pointwise-convergence" text="pointwise convergence" >}} and can be expressed as convergence in the {{< knowl id="uniform-metric" text="uniform metric" >}} (for real-valued bounded functions, this is the metric induced by the {{< knowl id="supremum-norm" text="supremum norm" >}}). It is the mode of convergence used in results like {{< knowl id="uniform-limit-of-continuous-is-continuous" text="uniform limit of continuous functions is continuous" >}}.

**Examples:**
- On any set $X\subseteq\mathbb{R}$, the functions $f_n(x)=x/n$ converge uniformly to $0$ on every bounded interval, e.g. on $[0,1]$.
- On $[0,1]$, the sequence $f_n(x)=x^n$ does not converge uniformly (even though it converges pointwise).
