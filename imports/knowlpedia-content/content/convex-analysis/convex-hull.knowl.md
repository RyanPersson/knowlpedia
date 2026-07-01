+++
id = "convex-analysis/convex-hull"
title = "Convex hull"
kind = "knowl"
summary = "The smallest convex set containing a given set"
aliases = ["convex-hull", "Convex hull"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-hull.md"
+++

Let $X$ be a real vector space and let $\Omega\subset X$. The **convex hull** of $\Omega$, denoted $\mathrm{co}(\Omega)$, is defined as the intersection of all [[convex-analysis/convex-set|convex]] sets containing $\Omega$:
$$
\mathrm{co}(\Omega):=\bigcap\{C\subset X:\ C\text{ is convex and }\Omega\subset C\}.
$$

**Context.** By [[convex-analysis/intersections-of-convex-sets-are-convex|stability under intersections]], this definition ensures $\mathrm{co}(\Omega)$ is convex. The convex hull is the basic "convexification" operator.

**Examples:**
- If $\Omega=\{x_1,x_2\}$, then $\mathrm{co}(\Omega)=[x_1,x_2]$ (the segment).
- If $\Omega$ is the unit circle in $\mathbb{R}^2$, then $\mathrm{co}(\Omega)$ is the closed unit disk.
- If $\Omega$ is already convex, then $\mathrm{co}(\Omega)=\Omega$.
