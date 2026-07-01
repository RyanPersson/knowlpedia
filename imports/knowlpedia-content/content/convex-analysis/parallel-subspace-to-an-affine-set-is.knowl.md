+++
id = "convex-analysis/parallel-subspace-to-an-affine-set-is"
title = "Parallel Subspace to an Affine Set is Ω−Ω"
kind = "knowl"
summary = "Every nonempty affine set is parallel to a unique subspace L=Ω−Ω."
aliases = ["parallel-subspace-to-an-affine-set-is", "Parallel Subspace to an Affine Set is Ω−Ω"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/parallel-subspace-to-an-affine-set-is.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$ be a nonempty [[convex-analysis/affine-set|affine set]].

**Proposition**: The set $\Omega$ is parallel to a unique [[convex-analysis/linear-subspace|linear subspace]] $L\subset X$, and this subspace is
$$
L=\Omega-\Omega:=\{u-v\mid u,v\in\Omega\}.
$$

**Context:**
The subspace $\Omega-\Omega$ captures the "direction" of the affine set. It is the appropriate linear object used to define [[convex-analysis/hyperplane|hyperplanes]] as affine sets of [[convex-analysis/codimension|codimension]] one.
