+++
id = "convex-analysis/intersections-of-convex-sets-are-convex"
title = "Intersections of convex sets are convex"
kind = "knowl"
summary = "Any intersection of convex sets is convex"
aliases = ["intersections-of-convex-sets-are-convex", "Intersections of convex sets are convex"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/intersections-of-convex-sets-are-convex.md"
+++

**Proposition.**
Let $\{\Omega_i\}_{i\in I}$ be a family of [[convex-analysis/convex-set|convex]] subsets of a vector space $X$. Then the intersection $\bigcap_{i\in I}\Omega_i$ is convex.

**Context.** This is fundamental for defining the [[convex-analysis/convex-hull|convex hull]] as an intersection of all convex supersets and for building convex feasible regions from many convex constraints.

**Proof sketch.** If $x,y$ lie in every $\Omega_i$, then for each $i$ and each $\lambda\in[0,1]$ the point $\lambda x+(1-\lambda)y$ lies in $\Omega_i$ by convexity. Hence it lies in the intersection.
