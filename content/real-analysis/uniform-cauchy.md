---
title: "Uniform Cauchy sequence"
description: "A Cauchy condition for function sequences with a uniform bound over the domain."
---

A sequence of functions $(f_n):X\to Y$ into a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(Y,d)$ is **uniform Cauchy** on $X$ if for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$ and all $x\in X$,
\[
d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon.
\]
Equivalently,
\[
\sup_{x\in X} d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon \quad \text{for all } m,n\ge N.
\]

This is the Cauchy formulation of {{< knowl id="uniform-convergence" text="uniform convergence" >}}; their relationship is summarized by {{< knowl id="uniform-cauchy-iff-uniform-convergence" text="uniform Cauchy if and only if uniform convergence" >}} (under the standard completeness hypotheses on the codomain). In the real-valued bounded setting, this is exactly the {{< knowl id="cauchy-sequence" section="topology" text="Cauchy condition" >}} in the {{< knowl id="uniform-metric" text="uniform metric" >}}.

**Examples:**
- On $[0,1]$, $f_n(x)=x/n$ is uniform Cauchy because $\sup_{x\in[0,1]}|f_m(x)-f_n(x)|\le |1/m-1/n|$.
- On $[0,1]$, $f_n(x)=x^n$ is not uniform Cauchy (the functions separate near $x=1$ for large indices).
