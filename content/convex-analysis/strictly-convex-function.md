---
title: "Strictly convex function"
description: "A convex function with strict inequality for distinct points"
---

Let $X$ be a vector space and let $f:X\to\mathbb{R}$ be extended-real-valued. The function $f$ is **strictly convex** if for all $x,y\in \mathrm{dom}(f)$ with $x\neq y$ and all $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)<\lambda f(x)+(1-\lambda)f(y).
$$

**Context.** Strict convexity strengthens {{< knowl id="convex-function-via-epigraph" text="convexity" >}} and typically yields uniqueness of minimizers in optimization problems.

**Examples:**
- On $\mathbb{R}$, $f(x)=x^2$ is strictly convex.
- On a normed space, $f(x)=\|x\|^2$ is strictly convex in many settings (e.g., Hilbert spaces).
- $f(x)=|x|$ on $\mathbb{R}$ is convex but not strictly convex (equality holds on rays with the same sign).
