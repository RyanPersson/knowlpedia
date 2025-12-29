---
title: "Sums and scalar multiples of convex sets are convex"
description: "Minkowski sums and dilations preserve convexity"
---

**Proposition.**
Let $\Omega_1,\Omega_2$ be {{< knowl id="convex-set" text="convex" >}} subsets of a real vector space $X$ and let $\lambda\in\mathbb{R}$. Define the {{< knowl id="set-operations-sum-scalar-multiple-difference" text="Minkowski sum and scalar multiple" >}}
$$
\Omega_1+\Omega_2:=\{x_1+x_2:x_1\in\Omega_1,\ x_2\in\Omega_2\},\qquad
\lambda\Omega_1:=\{\lambda x:x\in\Omega_1\}.
$$
Then $\Omega_1+\Omega_2$ and $\lambda\Omega_1$ are convex.

**Context.** This is a key stability property: adding convex "uncertainty sets" or scaling constraints preserves convexity.

**Proof sketch.** For sums, take $u_i=x_i+y_i\in\Omega_1+\Omega_2$ and use convexity of each set to show $\lambda u_1+(1-\lambda)u_2$ decomposes as a sum of two points in $\Omega_1$ and $\Omega_2$. For scalar multiples, note $\lambda(\theta x+(1-\theta)y)=\theta(\lambda x)+(1-\theta)(\lambda y)$.
