+++
id = "convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set"
title = "Properties of the Minkowski Gauge of a Convex Set"
kind = "knowl"
summary = "For absorbing convex Ω, pΩ is sublinear and its level sets describe core(Ω) and lin(Ω)."
aliases = ["properties-of-the-minkowski-functional-of-a-convex-set", "Properties of the Minkowski Gauge of a Convex Set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$ be [[convex-analysis/balanced-and-absorbing-sets|absorbing]] and [[convex-analysis/convex-set|convex]]. Consider the [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski gauge]] $p_\Omega$.

**Theorem**:
1. $p_\Omega$ is real-valued and [[convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions|sublinear]].
2. The strict sublevel set equals the [[convex-analysis/algebraic-interior-core|algebraic interior (core)]]:
   $$
   \{x\in X\mid p_\Omega(x)<1\}=\operatorname{core}(\Omega).
   $$
3. The non-strict sublevel set equals the [[convex-analysis/linear-closure|linear closure]]:
   $$
   \{x\in X\mid p_\Omega(x)\le 1\}=\operatorname{lin}(\Omega).
   $$

**Context:**
This theorem connects the algebraic geometry of $\Omega$ (core/lin) with a canonical sublinear functional. It is the key bridge to Hahn–Banach separation results such as [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|separating a point from a convex set]].
