---
title: "Closed ball"
description: "The set of points at distance at most a radius from a center in a metric space"
---

A **closed ball** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a set of the form
\[
\overline{B}_d(x,r)=\{y\in X : d(x,y)\le r\},
\]
where $x\in X$ and $r\ge 0$.

In the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, closed balls are {{< knowl id="closed-set" section="topology-core" text="closed sets" >}}. Their “boundary at radius $r$” is the {{< knowl id="sphere-metric-sphere" text="metric sphere" >}} $S_d(x,r)$.

**Examples:**
- In $(\mathbb{R},|x-y|)$, $\overline{B}_d(x,r)=[x-r,x+r]$.
- In the discrete metric on $X$, if $0\le r<1$ then $\overline{B}_d(x,r)=\{x\}$, and if $r\ge 1$ then $\overline{B}_d(x,r)=X$.
