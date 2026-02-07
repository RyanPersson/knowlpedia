---
title: "Chinese remainder theorem"
description: "For pairwise comaximal ideals, the quotient by their intersection splits as a product of quotients."
---

**Chinese remainder theorem**: Let \(R\) be a {{< knowl id="commutative-ring" text="commutative ring" >}} with \(1\), and let \(I_1,\dots,I_n\triangleleft R\) be {{< knowl id="ideal" text="ideals" >}} such that \(I_i+I_j=R\) for all \(i\neq j\) (pairwise comaximal, expressed via the {{< knowl id="sum-of-ideals" text="sum of ideals" >}}). Then the natural map
\[
R \longrightarrow \prod_{i=1}^n R/I_i,\qquad r\longmapsto (r\bmod I_1,\dots,r\bmod I_n)
\]
is surjective with kernel \(\bigcap_{i=1}^n I_i\) (the {{< knowl id="intersection-of-ideals" text="intersection of ideals" >}}), hence induces an isomorphism
\[
R/\bigcap_{i=1}^n I_i \ \cong\ \prod_{i=1}^n R/I_i
\]
of {{< knowl id="quotient-ring" text="quotient rings" >}}. The right-hand side is the ring structure on the {{< knowl id="cartesian-product" section="shared-foundations" text="cartesian product" >}} given componentwise.
