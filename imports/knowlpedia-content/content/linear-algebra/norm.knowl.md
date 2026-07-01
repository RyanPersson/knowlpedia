+++
id = "linear-algebra/norm"
title = "Norm"
kind = "knowl"
summary = "A function assigning a nonnegative length to vectors."
aliases = ["norm"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/norm.md"
+++

A **norm** on a [[linear-algebra/vector-space|vector space]] $V$ over $\mathbb{F}$ is a function $\|\cdot\|:V\to[0,\infty)$ such that for all $u,v\in V$ and $a\in\mathbb{F}$:
\[
\|v\|=0\iff v=0,\qquad \|a v\|=|a|\,\|v\|,\qquad \|u+v\|\le \|u\|+\|v\|.
\]
Here $|a|$ denotes the [[real-analysis/absolute-value|absolute value]] of the scalar $a$ (for $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$).

A norm induces a [[topology/metric|metric]] by $d(u,v)=\|u-v\|$, making $V$ into a [[topology/metric-space|metric space]] and thus giving notions of convergence and continuity.

**Examples:**
- On $\mathbb{R}^n$, the Euclidean norm $\|x\|_2=\sqrt{\sum_{i=1}^n x_i^2}$ is a norm.
- On $\mathbb{R}^n$, the $\ell^1$ norm $\|x\|_1=\sum_{i=1}^n |x_i|$ and the max norm $\|x\|_\infty=\max_i |x_i|$ are norms.
- On continuous functions on $[0,1]$, the sup norm $\|f\|_\infty=\sup_{t\in[0,1]} |f(t)|$ is a norm.
