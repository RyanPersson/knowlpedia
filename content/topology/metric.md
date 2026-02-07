---
title: "Metric"
description: "A distance function on a set satisfying positivity, symmetry, and the triangle inequality."
---

A **metric** on a {{< knowl id="set" section="shared-foundations" text="set" >}} $X$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $d\colon X\times X\to[0,\infty)$ such that for all $x,y,z\in X$:

1. (Identity of indiscernibles) $d(x,y)=0$ if and only if $x=y$.
2. (Symmetry) $d(x,y)=d(y,x)$.
3. (Triangle inequality) $d(x,z)\le d(x,y)+d(y,z)$.

A metric is the basic structure underlying a {{< knowl id="metric-space" text="metric space" >}}; it determines {{< knowl id="open-ball" text="open balls" >}} and hence the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}.

**Examples:**
- On $\mathbb{R}^n$, the Euclidean metric $d(x,y)=\|x-y\|_2$.
- On any set $X$, the discrete metric $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise.
