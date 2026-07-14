---
title: "Closed ball"
description: "The set of points at distance at most a given radius from a center."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}, let $x\in X$, and let $r>0$. The **closed ball** of radius $r$ centered at $x$ is
$$
\overline{B}_d(x,r)=\{y\in X : d(x,y)\le r\}.
$$

In the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}, every closed ball is a {{< knowl id="closed-set" text="closed set" >}} (though it need not be open, unlike an {{< knowl id="open-ball" text="open ball" >}}).

**Examples:**
- In $\mathbb{R}$ with the usual metric, $\overline{B}(x,r)$ is the closed interval $[x-r,x+r]$.
- In a discrete metric space, $\overline{B}(x,1/2)=\{x\}$, while $\overline{B}(x,2)=X$.
