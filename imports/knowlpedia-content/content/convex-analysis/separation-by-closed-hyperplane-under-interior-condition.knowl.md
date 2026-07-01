+++
id = "convex-analysis/separation-by-closed-hyperplane-under-interior-condition"
title = "Separation by Closed Hyperplane Under an Interior Condition"
kind = "knowl"
summary = "If int(Ω1)≠∅ and int(Ω1)∩Ω2=∅, then Ω1 and Ω2 are separable by a continuous functional."
aliases = ["separation-by-closed-hyperplane-under-interior-condition", "Separation by Closed Hyperplane Under an Interior Condition"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-by-closed-hyperplane-under-interior-condition.md"
+++

Let $X$ be a real [[convex-analysis/norm-normed-vector-space|normed space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]]. Assume that [[convex-analysis/interior-of-a-set|int(Ω₁)]]$\neq\emptyset$ and
$$
\operatorname{int}(\Omega_1)\cap\Omega_2=\emptyset.
$$

**Theorem**: The sets $\Omega_1$ and $\Omega_2$ can be [[convex-analysis/separation-by-a-closed-hyperplane|separated by a closed hyperplane]]; i.e., there exists $x^\ast \in X^\ast \setminus\{0\}$ such that
$$
\langle x^\ast ,x\rangle \le \langle x^\ast ,y\rangle\quad \text{for all }x\in\Omega_1,\ y\in\Omega_2.
$$

**Context:**
In vector spaces, the analogous separation uses possibly discontinuous linear functionals (see [[convex-analysis/separation-of-two-convex-sets-via-the-core-condition|core-based separation]]). The interior assumption ensures the separating functional is continuous, using [[convex-analysis/continuity-of-linear-functionals-via-closed-level-sets|closed level-set continuity]].
