+++
id = "real-analysis/uniform-cauchy"
title = "Uniform Cauchy sequence"
kind = "knowl"
summary = "A Cauchy condition for function sequences with a uniform bound over the domain."
aliases = ["uniform-cauchy", "Uniform Cauchy sequence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-cauchy.md"
+++

A sequence of functions $(f_n):X\to Y$ into a [[topology/metric-space|metric space]] $(Y,d)$ is **uniform Cauchy** on $X$ if for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$ and all $x\in X$,
\[
d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon.
\]
Equivalently,
\[
\sup_{x\in X} d\bigl(f_m(x),f_n(x)\bigr)<\varepsilon \quad \text{for all } m,n\ge N.
\]

This is the Cauchy formulation of [[real-analysis/uniform-convergence|uniform convergence]]; their relationship is summarized by [[real-analysis/uniform-cauchy-iff-uniform-convergence|uniform Cauchy if and only if uniform convergence]] (under the standard completeness hypotheses on the codomain). In the real-valued bounded setting, this is exactly the [[topology/cauchy-sequence|Cauchy condition]] in the [[real-analysis/uniform-metric|uniform metric]].

**Examples:**
- On $[0,1]$, $f_n(x)=x/n$ is uniform Cauchy because $\sup_{x\in[0,1]}|f_m(x)-f_n(x)|\le |1/m-1/n|$.
- On $[0,1]$, $f_n(x)=x^n$ is not uniform Cauchy (the functions separate near $x=1$ for large indices).
