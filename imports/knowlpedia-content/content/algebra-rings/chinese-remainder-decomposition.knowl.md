+++
id = "algebra-rings/chinese-remainder-decomposition"
title = "Chinese remainder decomposition"
kind = "knowl"
summary = "For comaximal ideals, a quotient ring decomposes as a product of quotients."
aliases = ["chinese-remainder-decomposition", "Chinese remainder decomposition"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/chinese-remainder-decomposition.md"
+++

**Chinese remainder decomposition**: Let $R$ be a commutative ring and let $I_1,\dots,I_n$ be ideals that are pairwise comaximal. Then the natural homomorphism $R\to \prod_{i=1}^n R/I_i$ induces an isomorphism
\[
R\Big/\bigcap_{i=1}^n I_i \;\cong\; \prod_{i=1}^n R/I_i.
\]
In particular, if $I$ and $J$ are comaximal, then $R/(I\cap J)\cong R/I\times R/J$.

This is the standard [[algebra-rings/chinese-remainder-theorem|Chinese Remainder Theorem]] formulated as an explicit isomorphism of [[algebra-rings/quotient-ring|quotient rings]] when ideals are comaximal (i.e., their [[algebra-rings/sum-of-ideals|sum]] is the whole ring). It relates the [[algebra-rings/intersection-of-ideals|intersection]] of comaximal [[algebra-rings/ideal|ideals]] to a [[shared-foundations/cartesian-product|product]] ring and produces idempotents yielding the splitting in [[algebra-rings/idempotent-product-decomposition|idempotent decompositions]].
