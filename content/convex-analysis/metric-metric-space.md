---
title: "Metric and metric space"
description: "A distance function satisfying positivity, symmetry, and the triangle inequality"
---

Let $X$ be a nonempty set. A function $d:X\times X\to\mathbb{R}$ is a **metric** on $X$ if for all $x,y,z\in X$:

1. $d(x,y)\ge 0$, and $d(x,y)=0$ if and only if $x=y$.
2. $d(x,y)=d(y,x)$.
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

The pair $(X,d)$ is called a **metric space**.

Metrics allow one to define {{< knowl id="open-and-closed-balls-in-a-metric-space" text="balls" >}}, {{< knowl id="open-subset" text="open sets" >}}, and notions of {{< knowl id="convergence-of-a-sequence" text="convergence" >}} and completeness.

**Examples:**
- On $\mathbb{R}^n$, the Euclidean metric $d(x,y)=\|x-y\|_2$.
- The discrete metric: $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise.
- On a normed vector space $(X,\|\cdot\|)$, $d(x,y)=\|x-y\|$ is a metric.
