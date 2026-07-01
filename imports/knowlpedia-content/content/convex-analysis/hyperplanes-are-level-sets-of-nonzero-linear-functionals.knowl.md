+++
id = "convex-analysis/hyperplanes-are-level-sets-of-nonzero-linear-functionals"
title = "Hyperplanes as Level Sets of Linear Functionals"
kind = "knowl"
summary = "In real vector spaces, Ω is a hyperplane iff Ω={x : f(x)=α} for some f≠0."
aliases = ["hyperplanes-are-level-sets-of-nonzero-linear-functionals", "Hyperplanes as Level Sets of Linear Functionals"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hyperplanes-are-level-sets-of-nonzero-linear-functionals.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]].

**Proposition**: A subset $\Omega\subset X$ is a [[convex-analysis/hyperplane|hyperplane]] if and only if there exist a nonzero linear functional $f:X\to\mathbb{R}$ and a scalar $\alpha\in\mathbb{R}$ such that
$$
\Omega=\{x\in X\mid f(x)=\alpha\}.
$$

**Context:**
One direction uses the decomposition of codimension-one subspaces (see [[convex-analysis/codimension-one-subspaces-yield-direct-sum-decompositions|codimension-one decomposition]]). The other direction uses that $\ker f$ has codimension one (see [[convex-analysis/kernel-of-a-nonzero-linear-functional-has-codimension-one|codimension of kernels]]).
