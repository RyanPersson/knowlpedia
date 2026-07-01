+++
id = "convex-analysis/cartesian-product-of-convex-sets-is-convex"
title = "Cartesian product of convex sets is convex"
kind = "knowl"
summary = "The product Ω1×Ω2 is convex when each factor is convex"
aliases = ["cartesian-product-of-convex-sets-is-convex", "Cartesian product of convex sets is convex"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/cartesian-product-of-convex-sets-is-convex.md"
+++

**Proposition.**
Let $\Omega_1\subset X$ and $\Omega_2\subset Y$ be [[convex-analysis/convex-set|convex]] sets in vector spaces $X$ and $Y$. Then the Cartesian product $\Omega_1\times \Omega_2$ is convex in the [[convex-analysis/product-space-cartesian-product|product space]] $X\times Y$.

**Context.** Convexity is stable under forming product constraints, a basic fact used in multi-variable convex analysis.

**Proof sketch.** If $(x_1,y_1),(x_2,y_2)\in\Omega_1\times\Omega_2$ and $\lambda\in[0,1]$, then
$$
\lambda(x_1,y_1)+(1-\lambda)(x_2,y_2)=(\lambda x_1+(1-\lambda)x_2,\ \lambda y_1+(1-\lambda)y_2),
$$
and each component lies in the appropriate convex set.
