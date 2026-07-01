+++
id = "algebra-rings/chinese-remainder-theorem"
title = "Chinese remainder theorem"
kind = "knowl"
summary = "For pairwise comaximal ideals, the quotient by their intersection splits as a product of quotients."
aliases = ["chinese-remainder-theorem", "Chinese remainder theorem"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/chinese-remainder-theorem.md"
+++

**Chinese remainder theorem**: Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] with \(1\), and let \(I_1,\dots,I_n\triangleleft R\) be [[algebra-rings/ideal|ideals]] such that \(I_i+I_j=R\) for all \(i\neq j\) (pairwise comaximal, expressed via the [[algebra-rings/sum-of-ideals|sum of ideals]]). Then the natural map
\[
R \longrightarrow \prod_{i=1}^n R/I_i,\qquad r\longmapsto (r\bmod I_1,\dots,r\bmod I_n)
\]
is surjective with kernel \(\bigcap_{i=1}^n I_i\) (the [[algebra-rings/intersection-of-ideals|intersection of ideals]]), hence induces an isomorphism
\[
R/\bigcap_{i=1}^n I_i \ \cong\ \prod_{i=1}^n R/I_i
\]
of [[algebra-rings/quotient-ring|quotient rings]]. The right-hand side is the ring structure on the [[shared-foundations/cartesian-product|cartesian product]] given componentwise.
