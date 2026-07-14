---
title: "Sphere (metric sphere)"
description: "The set of points at exactly a fixed distance from a center."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}, let $x\in X$, and let $r>0$. The **sphere** (or **metric sphere**) of radius $r$ centered at $x$ is
$$
S_d(x,r)=\{y\in X : d(x,y)=r\}.
$$

A sphere can be viewed as the “boundary” between the {{< knowl id="open-ball" text="open ball" >}} and the {{< knowl id="closed-ball" text="closed ball" >}}: in words, it is the set difference of the closed ball minus the open ball of the same center and radius (using {{< knowl id="set-difference" text="set difference" >}}).

**Examples:**
- In Euclidean space, $S(x,r)$ is the usual geometric sphere of radius $r$.
- In a discrete metric space, for $r=1$ the sphere $S(x,1)$ is $X\setminus\{x\}$, while for $0<r<1$ the sphere is empty.
