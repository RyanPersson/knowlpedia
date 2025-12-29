---
title: "Convex hull"
description: "The smallest convex set containing a given set"
---

Let $X$ be a real vector space and let $\Omega\subset X$. The **convex hull** of $\Omega$, denoted $\mathrm{co}(\Omega)$, is defined as the intersection of all {{< knowl id="convex-set" text="convex" >}} sets containing $\Omega$:
$$
\mathrm{co}(\Omega):=\bigcap\{C\subset X:\ C\text{ is convex and }\Omega\subset C\}.
$$

**Context.** By {{< knowl id="intersections-of-convex-sets-are-convex" text="stability under intersections" >}}, this definition ensures $\mathrm{co}(\Omega)$ is convex. The convex hull is the basic "convexification" operator.

**Examples:**
- If $\Omega=\{x_1,x_2\}$, then $\mathrm{co}(\Omega)=[x_1,x_2]$ (the segment).
- If $\Omega$ is the unit circle in $\mathbb{R}^2$, then $\mathrm{co}(\Omega)$ is the closed unit disk.
- If $\Omega$ is already convex, then $\mathrm{co}(\Omega)=\Omega$.
