+++
id = "convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core"
title = "Auxiliary Separation Lemma"
kind = "knowl"
summary = "Disjoint convex sets are separable if one has nonempty core and the sets are disjoint."
aliases = ["auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core", "Auxiliary Separation Lemma"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]] and let $\Omega_1,\Omega_2\subset X$ be nonempty [[convex-analysis/convex-set|convex sets]]. Assume that [[convex-analysis/algebraic-interior-core|core(Ω₁)]]$\neq\emptyset$ and $\Omega_1\cap\Omega_2=\emptyset$.

**Lemma**: The sets $\Omega_1$ and $\Omega_2$ can be [[convex-analysis/separation-by-a-hyperplane|separated by a hyperplane]].

**Context:**
The proof reduces separation of two sets to separation of a point from a convex set by applying [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|point-vs-set separation]] to the Minkowski difference $\Omega_1-\Omega_2$.
