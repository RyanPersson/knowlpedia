---
title: "Norm"
description: "A function assigning a nonnegative length to vectors."
---

A **norm** on a {{< knowl id="vector-space" text="vector space" >}} $V$ over $\mathbb{F}$ is a function $\|\cdot\|:V\to[0,\infty)$ such that for all $u,v\in V$ and $a\in\mathbb{F}$:
\[
\|v\|=0\iff v=0,\qquad \|a v\|=|a|\,\|v\|,\qquad \|u+v\|\le \|u\|+\|v\|.
\]
Here $|a|$ denotes the {{< knowl id="absolute-value" section="real-analysis" text="absolute value" >}} of the scalar $a$ (for $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$).

A norm induces a {{< knowl id="metric" section="topology" text="metric" >}} by $d(u,v)=\|u-v\|$, making $V$ into a {{< knowl id="metric-space" section="topology" text="metric space" >}} and thus giving notions of convergence and continuity.

**Examples:**
- On $\mathbb{R}^n$, the Euclidean norm $\|x\|_2=\sqrt{\sum_{i=1}^n x_i^2}$ is a norm.
- On $\mathbb{R}^n$, the $\ell^1$ norm $\|x\|_1=\sum_{i=1}^n |x_i|$ and the max norm $\|x\|_\infty=\max_i |x_i|$ are norms.
- On continuous functions on $[0,1]$, the sup norm $\|f\|_\infty=\sup_{t\in[0,1]} |f(t)|$ is a norm.
