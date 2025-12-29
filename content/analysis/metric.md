---
title: "Distance (metric)"
description: "A function d(x,y) satisfying positivity, symmetry, and the triangle inequality."
---

Let $X$ be a set. A **metric** (or **distance function**) on $X$ is a function
$$d:X\times X\to[0,\infty)$$
such that for all $x,y,z\in X$:
- (**Positive definiteness**) $d(x,y)=0$ iff $x=y$.
- (**Symmetry**) $d(x,y)=d(y,x)$.
- (**Triangle inequality**) $d(x,z)\le d(x,y)+d(y,z)$.

Metrics quantify "closeness" abstractly. Most of analysis can be formulated in terms of a metric, including convergence, continuity, compactness, and completeness.

**Examples:**
- On $\mathbb{R}$, $d(x,y)=|x-y|$ is a metric.
- On $\mathbb{R}^k$, $d(x,y)=\|x-y\|_2$ (Euclidean distance) is a metric.
- On any set $X$, the discrete metric $d(x,y)=0$ if $x=y$ and $1$ otherwise is a metric.
