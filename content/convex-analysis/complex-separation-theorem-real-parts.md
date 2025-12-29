---
title: "Complex Separation Theorem (Real Parts)"
description: "In complex vector spaces, separation holds via the real part of a complex linear functional."
---

Let $X$ be a complex {{< knowl id="vector-space" text="vector space" >}} and let $\Omega_1,\Omega_2\subset X$ be nonempty {{< knowl id="convex-set" text="convex sets" >}}. Assume {{< knowl id="algebraic-interior-core-and-linear-closure" text="core(Ω₁)" >}}$\neq\emptyset$ and $\operatorname{core}(\Omega_1)\cap\Omega_2=\emptyset$.

**Theorem**: There exists a nonzero complex-linear functional $F$ on $X$ such that
$$
\operatorname{Re}F(x)\le \operatorname{Re}F(y)\quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

**Context:**
View $X$ as a real vector space and apply {{< knowl id="separation-of-two-convex-sets-via-the-core-condition" text="the real separation theorem" >}} to obtain a real linear functional $f$. Then form a complex functional $F$ whose real part is $f$.
