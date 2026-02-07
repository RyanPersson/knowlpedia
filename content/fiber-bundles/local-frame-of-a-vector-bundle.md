---
title: "Local frame of a vector bundle"
description: "A choice of smooth local sections that form a basis of each fiber over an open set."
---

Let $\pi:E\to M$ be a smooth vector bundle of rank $r$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. Let $U\subseteq M$ be open. A **local frame** of $E$ over $U$ is an ordered $r$-tuple of smooth sections
\[
e_1,\dots,e_r:U\to E
\]
such that for every $x\in U$, the vectors $(e_1(x),\dots,e_r(x))$ form a basis of the fiber $E_x$.

Equivalently, a local frame over $U$ is the same data as a local trivialization $E|_U\cong U\times \mathbb F^r$, by sending $(x,v)$ to $\sum_i v^i e_i(x)$ and conversely by taking the images of the standard basis vectors in $\mathbb F^r$.

When $E=TM$, a local frame is the same thing as a collection of $r=\dim M$ linearly independent {{< knowl id="vector-field" text="vector fields" >}} on $U$.

On overlaps of two framed open sets, the change-of-frame is encoded by a {{< knowl id="transition-matrix-of-a-local-frame" text="transition matrix" >}}.

## Examples
1. **Coordinate frame for the tangent bundle.** On a coordinate chart $(U;x^1,\dots,x^n)$, the coordinate vector fields $\partial/\partial x^1,\dots,\partial/\partial x^n$ form a local frame of $TM|_U$.

2. **Standard frame for a trivial bundle.** For $E=M\times \mathbb F^r$, the constant sections $e_i(x)=(x,\mathbf e_i)$ (where $\mathbf e_i$ is the $i$th standard basis vector) form a global frame.

3. **Orthonormal local frame.** If $E$ has a {{< knowl id="bundle-metric" text="bundle metric" >}}, one can choose (after shrinking $U$) a local frame that is orthonormal in each fiber.
