---
title: "Metric space"
description: "A set equipped with a metric."
---

A **metric space** is a pair $(X,d)$ where $X$ is a {{< knowl id="set" text="set" >}} and $d$ is a {{< knowl id="metric" text="metric" >}} on $X$.

Every metric space carries a natural {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, so it can also be viewed as a {{< knowl id="topological-space" text="topological space" >}}.

**Examples:**
- {{< knowl id="euclidean-space" text="Euclidean space" >}} $\mathbb{R}^n$ with distance $d(x,y)=\|x-y\|_2$.
- Any set $X$ with the discrete metric (distance $1$ between distinct points).
- A subset $A\subseteq X$ with the restricted distance $d|_{A\times A}$ is again a metric space.
