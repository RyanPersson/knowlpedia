---
title: "Existence of partitions of unity on paracompact manifolds"
description: "On a paracompact smooth manifold, every open cover admits a smooth partition of unity subordinate to it."
---

Partitions of unity are the main technical tool that lets local constructions on charts be assembled into global geometric objects.

## Theorem (Smooth partitions of unity)
Let $M$ be a paracompact {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $\{U_i\}_{i\in I}$ be an open cover of $M$. Then there exists a family of smooth functions $\{\rho_i\}_{i\in I}$ on $M$ such that:

1. $0\le \rho_i\le 1$ for all $i$,
2. the family is locally finite (every point has a neighborhood where all but finitely many $\rho_i$ vanish),
3. $\mathrm{supp}(\rho_i)\subset U_i$ for all $i$ (subordinate to the cover), and
4. $\sum_{i\in I}\rho_i = 1$ everywhere on $M$.

In particular, any collection of local data defined over the $U_i$ that is affine or convex (e.g. local connection 1-forms, local metrics, local differential forms) can be glued into a global object by weighting with the $\rho_i$ and summing.

## Examples
1. **Bump functions on Euclidean space.** On $\mathbb{R}^n$, for a cover by balls one can choose smooth bump functions supported in slightly smaller balls and normalize their sum to obtain a partition of unity.
2. **Gluing differential forms.** If $\alpha_i$ are local differential forms on $U_i$ agreeing on overlaps, then $\sum_i \rho_i \alpha_i$ defines a global form; smoothness follows from local finiteness.
3. **Building global connections.** Local connection 1-forms on a trivializing cover can be combined using a partition of unity to produce a global {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} (or a principal connection after ensuring the correct transformation behavior).
