+++
id = "fiber-bundles/convention-manifolds-are-smooth-hausdorff-and-second-countable"
title = "Convention: manifolds are smooth, Hausdorff, and second countable"
kind = "knowl"
summary = "Throughout, a manifold means a smooth Hausdorff second-countable manifold (unless explicitly stated otherwise)."
aliases = ["convention-manifolds-are-smooth-hausdorff-and-second-countable", "Convention: manifolds are smooth, Hausdorff, and second countable"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/convention-manifolds-are-smooth-hausdorff-and-second-countable.md"
+++

## Convention
Unless explicitly stated otherwise, the word **manifold** means a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$ satisfying:

1. **Smoothness:** $M$ is a $C^\infty$ manifold (all atlases, transition maps, and structure maps are smooth).
2. **Hausdorff:** For any distinct points $p\neq q$ in $M$, there exist disjoint open sets separating them.
3. **Second countable:** The topology of $M$ has a countable basis.

This convention ensures standard foundational results used throughout differential geometry, including existence of partitions of unity, paracompactness, and well-behaved constructions of vector bundles and [[fiber-bundles/principal-g-bundle|principal bundles]].

## Examples
1. **Why Hausdorff matters.** The “line with two origins” is a classical example of a non-Hausdorff topological manifold; many standard arguments in analysis and geometry (e.g., uniqueness of limits) fail there.

2. **Why second countable matters.** A long line is Hausdorff and locally Euclidean but not second countable; it is not paracompact, and partitions of unity can fail to exist.

3. **Typical spaces covered by the convention.** Open subsets of $\mathbb R^n$, tori $T^n$, spheres $S^n$, and smooth quotients arising from free proper group actions (see [[fiber-bundles/construction-quotient-manifold-pg-for-a-free-proper-g-action|quotient manifold construction]]) all satisfy these hypotheses.
