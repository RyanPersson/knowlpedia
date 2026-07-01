+++
id = "fiber-bundles/local-frame-of-a-vector-bundle"
title = "Local frame of a vector bundle"
kind = "knowl"
summary = "A choice of smooth local sections that form a basis of each fiber over an open set."
aliases = ["local-frame-of-a-vector-bundle", "Local frame of a vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/local-frame-of-a-vector-bundle.md"
+++

Let $\pi:E\to M$ be a smooth vector bundle of rank $r$ over a [[fiber-bundles/smooth-manifold|smooth manifold]]. Let $U\subseteq M$ be open. A **local frame** of $E$ over $U$ is an ordered $r$-tuple of smooth sections
\[
e_1,\dots,e_r:U\to E
\]
such that for every $x\in U$, the vectors $(e_1(x),\dots,e_r(x))$ form a basis of the fiber $E_x$.

Equivalently, a local frame over $U$ is the same data as a local trivialization $E|_U\cong U\times \mathbb F^r$, by sending $(x,v)$ to $\sum_i v^i e_i(x)$ and conversely by taking the images of the standard basis vectors in $\mathbb F^r$.

When $E=TM$, a local frame is the same thing as a collection of $r=\dim M$ linearly independent [[fiber-bundles/vector-field|vector fields]] on $U$.

On overlaps of two framed open sets, the change-of-frame is encoded by a [[fiber-bundles/transition-matrix-of-a-local-frame|transition matrix]].

## Examples
1. **Coordinate frame for the tangent bundle.** On a coordinate chart $(U;x^1,\dots,x^n)$, the coordinate vector fields $\partial/\partial x^1,\dots,\partial/\partial x^n$ form a local frame of $TM|_U$.

2. **Standard frame for a trivial bundle.** For $E=M\times \mathbb F^r$, the constant sections $e_i(x)=(x,\mathbf e_i)$ (where $\mathbf e_i$ is the $i$th standard basis vector) form a global frame.

3. **Orthonormal local frame.** If $E$ has a [[fiber-bundles/bundle-metric|bundle metric]], one can choose (after shrinking $U$) a local frame that is orthonormal in each fiber.
