---
title: "Equivalent characterizations of convex functions"
description: "Convexity via epigraph is equivalent to Jensen and extended Jensen inequalities"
---

**Theorem.**
Let $f:X\to\mathbb{R}$ be an extended-real-valued function on a vector space $X$. The following are equivalent:

1. $f$ is {{< knowl id="convex-function-via-epigraph" text="convex" >}} (i.e., $\mathrm{epi}(f)$ is convex).
2. (**Jensen inequality**) For all $x,y\in X$ and $\lambda\in(0,1)$,
$$
f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y).
$$
3. (**Extended Jensen inequality**) For all $m\in\mathbb{N}$, all $x_1,\dots,x_m\in X$, and all $\lambda_i\ge 0$ with $\sum_{i=1}^m\lambda_i=1$,
$$
f\!\left(\sum_{i=1}^m \lambda_i x_i\right)\le \sum_{i=1}^m \lambda_i f(x_i).
$$

**Context.** Item (3) says that convexity is equivalent to "subadditivity under" {{< knowl id="convex-combination" text="convex combinations" >}} of finitely many points.

**Proof sketch.** (2) ⇒ (1): show any convex combination of points in the epigraph stays in the epigraph using the inequality. (1) ⇒ (2): apply convexity of the epigraph to $(x,f(x))$ and $(y,f(y))$. (2) ⇔ (3): (3) implies (2) by taking $m=2$; (2) implies (3) by induction and the convex-combination characterization.
