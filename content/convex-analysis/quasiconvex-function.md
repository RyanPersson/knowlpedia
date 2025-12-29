---
title: "Quasiconvex function"
description: "A function with f(λx+(1−λ)y)≤max{f(x),f(y)}"
---

Let $X$ be a vector space and let $f:X\to\mathbb{R}$ be extended-real-valued. The function $f$ is **quasiconvex** if for all $x,y\in X$ and all $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)\le \max\{f(x),f(y)\}.
$$

**Context.** Quasiconvexity is weaker than convexity: every convex function is quasiconvex, but not conversely. It is important in economic modeling and level-set methods.

**Examples:**
- Any {{< knowl id="convex-function-via-epigraph" text="convex function" >}} is quasiconvex.
- The function $f(x)=\sqrt{|x|}$ on $\mathbb{R}$ is quasiconvex but not convex.
- Any constant function is quasiconvex.
