---
title: "Closed ball"
description: "The set of points within distance at most r of a center point."
---

A **closed ball** in a metric space $(X,d)$ is a set of the form
\[
\overline{B}(x,r)=\{\,y\in X : d(x,y)\le r\,\},
\]
where $x\in X$ and $r\ge 0$.

Closed balls are {{{< knowl id="closed-set" section="topology-core" text="closed sets" >}}} in the {{{< knowl id="metric-induced-topology" text="metric-induced topology" >}}}. The boundary of a ball is described by the {{{< knowl id="sphere-metric-sphere" text="metric sphere" >}}}.

**Examples:**
- In $\mathbb{R}$ with the usual metric, $\overline{B}(a,r)$ is the closed interval $[a-r,a+r]$.
- In the discrete metric on a set $X$, $\overline{B}(x,1)=X$ while $B(x,1)=\{x\}$, so a closed ball need not be the closure of the corresponding open ball.
