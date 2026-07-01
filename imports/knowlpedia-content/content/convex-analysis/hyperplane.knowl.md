+++
id = "convex-analysis/hyperplane"
title = "Hyperplane"
kind = "knowl"
summary = "An affine set whose direction subspace has codimension one."
aliases = ["hyperplane"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/hyperplane.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]]. An [[convex-analysis/affine-set|affine set]] $\Omega\subset X$ is called a **hyperplane** if it has [[convex-analysis/codimension|codimension]] one.

More precisely: if $\Omega\neq\emptyset$, it is parallel to a unique subspace $L=\Omega-\Omega$ (see [[convex-analysis/parallel-subspace-to-an-affine-set-is|Ω−Ω characterization]]). Then $\Omega$ is a hyperplane iff $\operatorname{codim}(L)=1$.

In real vector spaces, hyperplanes are exactly level sets of nonzero linear functionals; see [[convex-analysis/hyperplanes-are-level-sets-of-nonzero-linear-functionals|the level-set characterization]].

**Examples:**
- In $\mathbb{R}^n$, the set $\{x\mid a^\top x=\alpha\}$ with $a\neq 0$ is a hyperplane.
