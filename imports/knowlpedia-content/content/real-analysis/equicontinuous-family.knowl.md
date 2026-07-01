+++
id = "real-analysis/equicontinuous-family"
title = "Equicontinuous family"
kind = "knowl"
summary = "A family of functions that satisfies the equicontinuity condition at every point."
aliases = ["equicontinuous-family", "Equicontinuous family"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/equicontinuous-family.md"
+++

A family $\mathcal{F}$ of functions from a [[topology/metric-space|metric space]] $(X,d_X)$ to a [[topology/metric-space|metric space]] $(Y,d_Y)$ is an **equicontinuous family** (or is **equicontinuous on $X$**) if it is [[real-analysis/equicontinuity|equicontinuous at each point]]: for every $x_0\in X$ and every $\varepsilon>0$ there exists $\delta>0$ such that for all $f\in\mathcal{F}$ and all $x\in X$,
\[
d_X(x,x_0)<\delta \implies d_Y\bigl(f(x),f(x_0)\bigr)<\varepsilon.
\]

Equicontinuity provides uniform control of continuity across the family and is a key hypothesis (together with [[real-analysis/pointwise-bounded-family|pointwise boundedness]]) in the [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli theorem]] for subsets of [[real-analysis/space-of-continuous-functions|spaces of continuous functions]] equipped with the [[real-analysis/uniform-metric|uniform metric]].

**Examples:**
- Any family of Lipschitz functions with a common Lipschitz constant is equicontinuous; for instance, $f_a(x)=\sin(x+a)$ for $a\in\mathbb{R}$ is equicontinuous on $\mathbb{R}$.
- On $[0,1]$, the sequence $f_n(x)=x^n$ is not an equicontinuous family (the behavior near $x=1$ prevents a uniform choice of $\delta$).
