+++
id = "convex-analysis/affine-set"
title = "Affine Set"
kind = "knowl"
summary = "A set containing the entire line through any two of its points."
aliases = ["affine-set", "Affine Set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/affine-set.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]]. A subset $\Omega\subset X$ is **affine** if for all $a,b\in\Omega$ we have
$$
L[a,b]\subset \Omega,
$$

where $L[a,b]$ is the [[convex-analysis/line-connecting-two-points|line connecting a and b]].

Equivalently, $\Omega$ is affine if it is a translate of a [[convex-analysis/linear-subspace|linear subspace]] (see [[convex-analysis/affine-sets-are-translates-of-subspaces|the translate characterization]]).

**Examples:**
- Any linear subspace is affine.
- In $\mathbb{R}^n$, a set of the form $x_0+L$ with $L$ a subspace is affine (an "affine subspace").
- A [[convex-analysis/convex-set|convex set]] need not be affine; affine sets are "flat," while convex sets may be curved.
