---
title: "Metric"
description: "A distance function on a set satisfying the metric axioms."
---

A **metric** on a {{{< knowl id="set" section="shared-foundations" text="set" >}}} $X$ is a {{{< knowl id="function" section="shared-foundations" text="function" >}}} $d:X\times X\to[0,\infty)$ on the {{{< knowl id="cartesian-product" section="shared-foundations" text="cartesian product" >}}} $X\times X$ such that for all $x,y,z\in X$:
1. $d(x,y)\ge 0$, and $d(x,y)=0$ if and only if $x=y$.
2. $d(x,y)=d(y,x)$.
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

A metric lets one define {{{< knowl id="open-ball" text="open balls" >}}}, talk about {{{< knowl id="convergent-sequence" text="convergence of sequences" >}}}, and build the {{{< knowl id="metric-induced-topology" text="metric-induced topology" >}}}.

**Examples:**
- On any set $X$, the **discrete metric** is $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise.
- On $\mathbb{R}^n$, the usual Euclidean distance defines a metric.
