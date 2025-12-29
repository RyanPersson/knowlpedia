---
title: "Neighborhood"
description: "A set containing an open ball around a point in a metric space."
---

Let $(X,d)$ be a metric space and let $x\in X$. A set $N\subseteq X$ is a **neighborhood** of $x$ if there exists $r>0$ such that
$$B(x,r)\subseteq N.$$

Neighborhoods encode the local structure around a point. Many definitions in analysis can be phrased using neighborhoods (e.g., limit points, closure, continuity).

**Examples:**
- In $\mathbb{R}$, any interval of the form $(x-\varepsilon,x+\varepsilon)$ is a neighborhood of $x$.
- In $\mathbb{R}$, the set $[x-1,x+1]$ is a neighborhood of $x$ (it contains the open ball $(x-1,x+1)$).
- In a discrete metric space, $\{x\}$ is a neighborhood of $x$ (since $B(x,1)=\{x\}$).
