---
title: "Intersections of convex sets are convex"
description: "Any intersection of convex sets is convex"
---

**Proposition.**
Let $\{\Omega_i\}_{i\in I}$ be a family of {{< knowl id="convex-set" text="convex" >}} subsets of a vector space $X$. Then the intersection $\bigcap_{i\in I}\Omega_i$ is convex.

**Context.** This is fundamental for defining the {{< knowl id="convex-hull" text="convex hull" >}} as an intersection of all convex supersets and for building convex feasible regions from many convex constraints.

**Proof sketch.** If $x,y$ lie in every $\Omega_i$, then for each $i$ and each $\lambda\in[0,1]$ the point $\lambda x+(1-\lambda)y$ lies in $\Omega_i$ by convexity. Hence it lies in the intersection.
