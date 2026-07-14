---
title: "Metric"
description: "A distance function on a set satisfying the standard metric axioms."
---

A **metric** on a {{< knowl id="set" text="set" >}} $X$ is a {{< knowl id="function" text="function" >}} $d : X \times X \to [0,\infty)$ whose domain is the {{< knowl id="cartesian-product" text="Cartesian product" >}} $X\times X$ and such that for all $x,y,z \in X$:

1. **Nonnegativity and definiteness:** $d(x,y)\ge 0$, and $d(x,y)=0$ if and only if $x=y$.
2. **Symmetry:** $d(x,y)=d(y,x)$.
3. **Triangle inequality:** $d(x,z)\le d(x,y)+d(y,z)$.

A metric lets you talk about “distance,” and it turns $X$ into a {{< knowl id="metric-space" text="metric space" >}}; from this you get notions like {{< knowl id="open-ball" text="open balls" >}}, convergence, and continuity.

**Examples:**
- On Euclidean space, the usual distance is $d(x,y)=\|x-y\|_2$, where $\|\cdot\|_2$ is the {{< knowl id="euclidean-norm" text="Euclidean norm" >}}.
- (**Discrete metric**) On any set $X$, define $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise. This satisfies all metric axioms.
