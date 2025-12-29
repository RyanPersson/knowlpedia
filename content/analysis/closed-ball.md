---
title: "Closed ball"
description: "The set of points within distance ≤ r of a center point in a metric space."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}, let $x\in X$, and let $r\ge 0$. The **closed ball** of radius $r$ centered at $x$ is
$$\overline{B}(x,r):=\{y\in X : d(x,y)\le r\}.$$

Closed balls are typically {{< knowl id="closed-set" text="closed sets" >}} in metric spaces and are used to describe {{< knowl id="bounded-set" text="boundedness" >}} and {{< knowl id="compact-set" text="compactness" >}} phenomena (e.g., bounded sets lie inside some closed ball). Compare with {{< knowl id="open-ball" text="open ball" >}}.

**Examples:**
- In $\mathbb{R}$, $\overline{B}(a,r)=[a-r,a+r]$.
- In $\mathbb{R}^2$, $\overline{B}(0,1)$ is the closed unit disk.
- In a discrete metric space, $\overline{B}(x,1)=X$ if the metric is $0/1$ (since $d(x,y)\le 1$ for all $y$).
