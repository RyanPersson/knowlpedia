---
title: "Interior and closure of a convex set are convex"
description: "In a normed space, convexity is preserved under interior and closure"
---

**Proposition.**
Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}}. Then:

- the {{< knowl id="interior-of-a-set" text="interior" >}} $\mathrm{int}(\Omega)$ is convex (possibly empty),
- the {{< knowl id="closure-of-a-set" text="closure" >}} $\overline{\Omega}$ is convex.

**Context.** Convexity is stable under two basic topological operations in normed spaces, which is essential for analyzing convex feasible regions.

**Proof sketch.** For $\overline{\Omega}$, approximate points by sequences in $\Omega$ and use convexity plus limit arguments. For $\mathrm{int}(\Omega)$, if $x,y\in\mathrm{int}(\Omega)$ then small balls around $x$ and $y$ lie in $\Omega$; convex combinations of these balls give a neighborhood of $\lambda x+(1-\lambda)y$ contained in $\Omega$, so the combination lies in $\mathrm{int}(\Omega)$.
