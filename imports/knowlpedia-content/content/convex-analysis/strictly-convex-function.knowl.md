+++
id = "convex-analysis/strictly-convex-function"
title = "Strictly convex function"
kind = "knowl"
summary = "A convex function with strict inequality for distinct points"
aliases = ["strictly-convex-function", "Strictly convex function"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/strictly-convex-function.md"
+++

Let $X$ be a vector space and let $f:X\to\mathbb{R}$ be extended-real-valued. The function $f$ is **strictly convex** if for all $x,y\in \mathrm{dom}(f)$ with $x\neq y$ and all $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)<\lambda f(x)+(1-\lambda)f(y).
$$

**Context.** Strict convexity strengthens [[convex-analysis/convex-function-via-epigraph|convexity]] and typically yields uniqueness of minimizers in optimization problems.

**Examples:**
- On $\mathbb{R}$, $f(x)=x^2$ is strictly convex.
- On a normed space, $f(x)=\|x\|^2$ is strictly convex in many settings (e.g., Hilbert spaces).
- $f(x)=|x|$ on $\mathbb{R}$ is convex but not strictly convex (equality holds on rays with the same sign).
