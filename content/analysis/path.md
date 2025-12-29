---
title: "Path"
description: "A continuous map γ:[a,b]→X, used to connect points in a space."
---

Let $(X,d)$ be a metric space. A **path** in $X$ is a continuous function
$$\gamma:[a,b]\to X$$
for some real interval $[a,b]\subset\mathbb{R}$ (often $[0,1]$). The **endpoints** of the path are $\gamma(a)$ and $\gamma(b)$.

Paths model "continuous motion" inside a space. Path-connectedness is stronger than connectedness and is often easier to verify in geometric settings.

**Examples:**
- In $\mathbb{R}^k$, the map $\gamma(t)=(1-t)x+ty$ for $t\in[0,1]$ is a path from $x$ to $y$ (a line segment).
- On the unit circle $S^1\subset\mathbb{R}^2$, $\gamma(t)=(\cos t,\sin t)$ for $t\in[0,2\pi]$ is a path with $\gamma(0)=\gamma(2\pi)$.
- In the discrete metric space $X$ (with at least two points), any continuous map from a connected interval $[a,b]$ must be constant, so there are no nontrivial paths connecting distinct points.
