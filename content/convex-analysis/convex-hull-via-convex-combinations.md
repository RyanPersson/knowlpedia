---
title: "Convex hull via convex combinations"
description: "The convex hull equals the set of all finite convex combinations of points in Ω"
---

**Theorem.**
Let $\Omega\subset X$ be a nonempty subset of a real vector space $X$. Then the {{< knowl id="convex-hull" text="convex hull" >}} can be described as
$$
\mathrm{co}(\Omega)=\left\{\sum_{i=1}^m \lambda_i x_i:\ m\in\mathbb{N},\ x_i\in\Omega,\ \lambda_i\ge 0,\ \sum_{i=1}^m\lambda_i=1\right\}.
$$

**Context.** This gives a constructive description of convex hulls: start from points in $\Omega$ and take all possible {{< knowl id="convex-combination" text="convex combinations" >}}.

**Proof sketch.** Let $C$ be the set of all finite convex combinations of points in $\Omega$. By {{< knowl id="convex-sets-characterized-by-closure-under-convex-combinations" text="closure under convex combinations" >}}, $C$ is convex and contains $\Omega$, hence $\mathrm{co}(\Omega)\subset C$ by minimality. Conversely, any convex set containing $\Omega$ must contain all convex combinations of points in $\Omega$, so $C\subset \mathrm{co}(\Omega)$.
