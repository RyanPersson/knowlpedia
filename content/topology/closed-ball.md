---
title: "Closed ball"
description: "The set of points within a given radius of a center point in a metric space, using non-strict inequality."
---

A **closed ball** in a metric space $(X,d)$ is a set of the form
\[
\overline{B}_d(x,r)=\{y\in X : d(x,y)\le r\},
\]
where $x\in X$ and $r\ge 0$.

Closed balls are closely related to {{< knowl id="open-ball" text="open balls" >}} and are {{< knowl id="closed-set" text="closed sets" >}} in the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}.

**Examples:**
- In $(\mathbb{R},|\cdot|)$, $\overline{B}(x,r)=[x-r,x+r]$.
- In the discrete metric on $X$, $\overline{B}(x,0)=\{x\}$ and $\overline{B}(x,1)=X$.
