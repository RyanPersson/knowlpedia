---
title: "Properties of the Minkowski Gauge of a Convex Set"
description: "For absorbing convex Ω, pΩ is sublinear and its level sets describe core(Ω) and lin(Ω)."
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $\Omega\subset X$ be {{< knowl id="balanced-and-absorbing-sets" text="absorbing" >}} and {{< knowl id="convex-set" text="convex" >}}. Consider the {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski gauge" >}} $p_\Omega$.

**Theorem**:
1. $p_\Omega$ is real-valued and {{< knowl id="subadditive-positively-homogeneous-and-sublinear-functions" text="sublinear" >}}.
2. The strict sublevel set equals the {{< knowl id="algebraic-interior-core" text="algebraic interior (core)" >}}:
   $$
   \{x\in X\mid p_\Omega(x)<1\}=\operatorname{core}(\Omega).
   $$
3. The non-strict sublevel set equals the {{< knowl id="linear-closure" text="linear closure" >}}:
   $$
   \{x\in X\mid p_\Omega(x)\le 1\}=\operatorname{lin}(\Omega).
   $$

**Context:**
This theorem connects the algebraic geometry of $\Omega$ (core/lin) with a canonical sublinear functional. It is the key bridge to Hahn–Banach separation results such as {{< knowl id="separation-of-a-point-from-a-convex-set-via-the-core" text="separating a point from a convex set" >}}.
