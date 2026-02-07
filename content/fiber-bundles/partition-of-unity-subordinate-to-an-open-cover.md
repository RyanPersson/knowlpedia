---
title: "Partition of unity subordinate to an open cover"
description: "A locally finite family of smooth functions that sum to one and have supports contained in prescribed open sets."
---

Let $M$ be a smooth manifold and let $\{U_i\}_{i\in I}$ be an open cover of $M$.

A **smooth partition of unity subordinate to** $\{U_i\}$ is a family of smooth functions $\{\varphi_i:M\to[0,1]\}_{i\in I}$ such that:

1. (**Support condition**) For each $i$, the support $\mathrm{supp}(\varphi_i)$ is contained in $U_i$.
2. (**Local finiteness**) The family $\{\mathrm{supp}(\varphi_i)\}$ is locally finite: every point of $M$ has a neighborhood meeting only finitely many supports.
3. (**Sum to one**) For all $x\in M$,
   \[
   \sum_{i\in I}\varphi_i(x)=1,
   \]
   where the sum is well-defined because of local finiteness.

A fundamental theorem states that if $M$ is a {{< knowl id="paracompact-manifold" text="paracompact manifold" >}}, then every open cover admits such a partition of unity.

## Examples
1. **Three-arc cover of the circle.**  
   Cover $S^1$ by three open arcs with pairwise overlaps. One can build smooth bump functions supported in each arc and normalize their sum to obtain a partition of unity.

2. **Cover of $\mathbb R^n$ by balls.**  
   For an open cover of $\mathbb R^n$ by (possibly overlapping) balls, choose a locally finite refinement and bump functions supported in the refined sets; normalizing yields a subordinate partition of unity.

3. **Gluing local data.**  
   If $\alpha_i$ are differential forms defined on $U_i$, then $\sum_i \varphi_i\,\alpha_i$ defines a global form when the $\alpha_i$ agree on overlaps in the appropriate sense; local finiteness ensures the sum is pointwise finite.
