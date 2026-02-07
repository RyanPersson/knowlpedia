---
title: "Equicontinuous family"
description: "A family of functions that satisfies the equicontinuity condition at every point."
---

A family $\mathcal{F}$ of functions from a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(X,d_X)$ to a {{< knowl id="metric-space" section="topology" text="metric space" >}} $(Y,d_Y)$ is an **equicontinuous family** (or is **equicontinuous on $X$**) if it is {{< knowl id="equicontinuity" text="equicontinuous at each point" >}}: for every $x_0\in X$ and every $\varepsilon>0$ there exists $\delta>0$ such that for all $f\in\mathcal{F}$ and all $x\in X$,
\[
d_X(x,x_0)<\delta \implies d_Y\bigl(f(x),f(x_0)\bigr)<\varepsilon.
\]

Equicontinuity provides uniform control of continuity across the family and is a key hypothesis (together with {{< knowl id="pointwise-bounded-family" text="pointwise boundedness" >}}) in the {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli theorem" >}} for subsets of {{< knowl id="space-of-continuous-functions" text="spaces of continuous functions" >}} equipped with the {{< knowl id="uniform-metric" text="uniform metric" >}}.

**Examples:**
- Any family of Lipschitz functions with a common Lipschitz constant is equicontinuous; for instance, $f_a(x)=\sin(x+a)$ for $a\in\mathbb{R}$ is equicontinuous on $\mathbb{R}$.
- On $[0,1]$, the sequence $f_n(x)=x^n$ is not an equicontinuous family (the behavior near $x=1$ prevents a uniform choice of $\delta$).
