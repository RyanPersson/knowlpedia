---
title: "Open ball"
description: "The set of points within a given radius of a center in a metric space."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}, let $x\in X$, and let $r>0$. The **open ball** of radius $r$ centered at $x$ is
$$
B_d(x,r)=\{y\in X : d(x,y)<r\}.
$$

Open balls are basic {{< knowl id="neighborhood" text="neighborhoods" >}} in the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}; in particular, each open ball is an {{< knowl id="open-set" text="open set" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual metric, $B(x,r)$ is the open interval $(x-r,x+r)$.
- In a discrete metric space, $B(x,1/2)=\{x\}$.
