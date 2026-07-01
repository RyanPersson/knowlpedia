+++
id = "convex-analysis/complex-separation-theorem-real-parts"
title = "Complex Separation Theorem (Real Parts)"
kind = "knowl"
summary = "In complex vector spaces, separation holds via the real part of a complex linear functional."
aliases = ["complex-separation-theorem-real-parts", "Complex Separation Theorem (Real Parts)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/complex-separation-theorem-real-parts.md"
+++

Let $X$ be a complex [[linear-algebra/vector-space|vector space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]]. Assume [[convex-analysis/algebraic-interior-core|core(Ω₁)]]$\neq\emptyset$ and $\operatorname{core}(\Omega_1)\cap\Omega_2=\emptyset$.

**Theorem**: There exists a nonzero complex-linear functional $F$ on $X$ such that
$$
\operatorname{Re}F(x)\le \operatorname{Re}F(y)\quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
$$

**Context:**
View $X$ as a real vector space and apply [[convex-analysis/separation-of-two-convex-sets-via-the-core-condition|the real separation theorem]] to obtain a real linear functional $f$. Then form a complex functional $F$ whose real part is $f$.
