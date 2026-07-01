+++
id = "convex-analysis/separation-of-two-convex-sets-via-the-core-condition"
title = "Separation of Two Convex Sets via the Core Condition"
kind = "knowl"
summary = "If core(Ω1)≠∅ and core(Ω1) is disjoint from Ω2, then Ω1 and Ω2 are separable by a hyperplane."
aliases = ["separation-of-two-convex-sets-via-the-core-condition", "Separation of Two Convex Sets via the Core Condition"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-of-two-convex-sets-via-the-core-condition.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]]. Assume [[convex-analysis/algebraic-interior-core|core(Ω₁)]]$\neq\emptyset$ and
$$
\operatorname{core}(\Omega_1)\cap \Omega_2=\emptyset.
$$

**Theorem**: The sets $\Omega_1$ and $\Omega_2$ can be [[convex-analysis/separation-by-a-hyperplane|separated by a hyperplane]].

**Context:**
This strengthens the disjointness condition by requiring only that $\Omega_2$ avoid the core of $\Omega_1$. The argument uses [[convex-analysis/idempotence-of-the-core-operator|idempotence of core]] and the [[convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core|auxiliary separation lemma]].
