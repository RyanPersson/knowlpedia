+++
id = "convex-analysis/metric-metric-space"
title = "Metric and metric space"
kind = "knowl"
summary = "A distance function satisfying positivity, symmetry, and the triangle inequality"
aliases = ["metric-metric-space", "Metric and metric space"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/metric-metric-space.md"
+++

Let $X$ be a nonempty set. A function $d:X\times X\to\mathbb{R}$ is a **metric** on $X$ if for all $x,y,z\in X$:

1. $d(x,y)\ge 0$, and $d(x,y)=0$ if and only if $x=y$.
2. $d(x,y)=d(y,x)$.
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

The pair $(X,d)$ is called a **metric space**.

Metrics allow one to define [[convex-analysis/open-and-closed-balls-in-a-metric-space|balls]], [[convex-analysis/open-subset|open sets]], and notions of [[convex-analysis/convergence-of-a-sequence|convergence]] and completeness.

**Examples:**
- On $\mathbb{R}^n$, the Euclidean metric $d(x,y)=\|x-y\|_2$.
- The discrete metric: $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise.
- On a normed vector space $(X,\|\cdot\|)$, $d(x,y)=\|x-y\|$ is a metric.
