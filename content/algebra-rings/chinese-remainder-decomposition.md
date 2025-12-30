---
title: "Chinese remainder decomposition"
description: "For comaximal ideals, a quotient ring decomposes as a product of quotients."
---

**Chinese remainder decomposition**: Let $R$ be a commutative ring and let $I_1,\dots,I_n$ be ideals that are pairwise comaximal. Then the natural homomorphism $R\to \prod_{i=1}^n R/I_i$ induces an isomorphism
\[
R\Big/\bigcap_{i=1}^n I_i \;\cong\; \prod_{i=1}^n R/I_i.
\]
In particular, if $I$ and $J$ are comaximal, then $R/(I\cap J)\cong R/I\times R/J$.

This is the standard {{< knowl id="chinese-remainder-theorem" text="Chinese Remainder Theorem" >}} formulated as an explicit isomorphism of {{< knowl id="quotient-ring" text="quotient rings" >}} when ideals are comaximal (i.e., their {{< knowl id="sum-of-ideals" text="sum" >}} is the whole ring). It relates the {{< knowl id="intersection-of-ideals" text="intersection" >}} of comaximal {{< knowl id="ideal" text="ideals" >}} to a {{< knowl id="cartesian-product" text="product" >}} ring and produces idempotents yielding the splitting in {{< knowl id="idempotent-product-decomposition" text="idempotent decompositions" >}}.