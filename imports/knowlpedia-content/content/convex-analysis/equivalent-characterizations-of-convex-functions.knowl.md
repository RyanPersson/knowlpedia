+++
id = "convex-analysis/equivalent-characterizations-of-convex-functions"
title = "Equivalent characterizations of convex functions"
kind = "knowl"
summary = "Convexity via epigraph is equivalent to Jensen and extended Jensen inequalities"
aliases = ["equivalent-characterizations-of-convex-functions", "Equivalent characterizations of convex functions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/equivalent-characterizations-of-convex-functions.md"
+++

**Theorem.**
Let $f:X\to\mathbb{R}$ be an extended-real-valued function on a vector space $X$. The following are equivalent:

1. $f$ is [[convex-analysis/convex-function-via-epigraph|convex]] (i.e., $\mathrm{epi}(f)$ is convex).
2. (**Jensen inequality**) For all $x,y\in X$ and $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y).
$$

3. (**Extended Jensen inequality**) For all $m\in\mathbb{N}$, all $x_1,\dots,x_m\in X$, and all $\lambda_i\ge 0$ with $\sum_{i=1}^m\lambda_i=1$,
$$
f\!\left(\sum_{i=1}^m \lambda_i x_i\right)\le \sum_{i=1}^m \lambda_i f(x_i).
$$

**Context.** Item (3) says that convexity is equivalent to "subadditivity under" [[convex-analysis/convex-combination|convex combinations]] of finitely many points.

**Proof sketch.** (2) ⇒ (1): show any convex combination of points in the epigraph stays in the epigraph using the inequality. (1) ⇒ (2): apply convexity of the epigraph to $(x,f(x))$ and $(y,f(y))$. (2) ⇔ (3): (3) implies (2) by taking $m=2$; (2) implies (3) by induction and the convex-combination characterization.
