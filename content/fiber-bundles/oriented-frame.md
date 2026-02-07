---
title: "Oriented frame"
description: "An ordered basis of a real vector space or fiber that is compatible with a chosen orientation."
---

Let $\pi:E\to M$ be a smooth real vector bundle of rank $r$ equipped with an {{< knowl id="orientation-of-a-real-vector-bundle" text="orientation" >}}. For a point $x\in M$, an **oriented frame** of $E$ at $x$ is an ordered basis $(e_1,\dots,e_r)$ of the vector space $E_x$ that lies in the chosen positive component of the set of all ordered bases of $E_x$.

Equivalently, $(e_1,\dots,e_r)$ is oriented if and only if, for some (hence any) local trivialization compatible with the chosen orientation, the change-of-basis matrix from the standard basis to $(e_1,\dots,e_r)$ has positive determinant.

The set of oriented frames in $E_x$ is a torsor under the special linear group $\mathrm{GL}^+(r,\mathbb R)$, and collecting these over all $x\in M$ gives a principal bundle often called the oriented frame bundle (a reduction of the full {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}}).

## Examples
1. **Standard oriented frame in Euclidean space.** In $\mathbb R^r$ with its standard orientation, the standard basis $(\mathbf e_1,\dots,\mathbf e_r)$ is an oriented frame; any basis obtained by applying a matrix with positive determinant is oriented.

2. **Oriented coordinate frames on a manifold.** On an oriented $n$-manifold, a coordinate chart $(U;x^1,\dots,x^n)$ is called orientation-preserving when $(\partial/\partial x^1,\dots,\partial/\partial x^n)$ is an oriented frame of $TM$ at each point of $U$.

3. **Rank-one case.** For a rank-one oriented bundle, an oriented frame at $x$ is simply a nonzero vector in $E_x$ that points in the chosen “positive direction”; there are exactly two possible choices of orientation in each fiber.
