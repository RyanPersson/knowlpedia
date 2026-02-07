---
title: "Good cover"
description: "An open cover whose nonempty finite intersections are contractible."
---

Let $X$ be a topological space (often a smooth manifold).

An open cover $\{U_i\}_{i\in I}$ of $X$ is a **good cover** if every nonempty finite intersection
\[
U_{i_0}\cap \cdots \cap U_{i_k}
\]
is contractible.

Good covers are especially useful because many global invariants can be computed from the combinatorics of the cover, and because they behave well with constructions built from local trivializations (for example, principal bundles and their transition functions).

On a {{< knowl id="paracompact-manifold" text="paracompact manifold" >}}, one can often refine a given cover to a good cover by taking sufficiently small coordinate neighborhoods (or sufficiently small geodesically convex balls when a Riemannian metric is available).

## Examples
1. **Convex covers of $\mathbb R^n$.**  
   Any cover of $\mathbb R^n$ by sufficiently small convex open sets (for instance, small Euclidean balls) is a good cover, since finite intersections of convex open sets are convex and hence contractible.

2. **A good cover of the circle.**  
   $S^1$ admits a good cover by three open arcs arranged so that all nonempty intersections are (possibly smaller) open arcs, hence contractible.

3. **A concrete nonexample.**  
   Cover $S^2$ by the north and south open hemispheres. Their intersection is an open neighborhood of the equator, homotopy equivalent to $S^1$, so it is not contractible; this two-set cover is not good.
