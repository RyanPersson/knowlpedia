+++
id = "algebra-modules/chinese-remainder-modules"
title = "Chinese remainder for modules"
kind = "knowl"
summary = "Module quotients by comaximal ideal multiples split as a direct sum of smaller quotients."
aliases = ["chinese-remainder-modules", "Chinese remainder for modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/chinese-remainder-modules.md"
+++

**Chinese remainder for modules**: Let $R$ be a commutative ring, let $M$ be an $R$-module, and let $I_1,\dots,I_n\subset R$ be pairwise comaximal ideals. Then the canonical map
\[
M\Big/\Bigl(\bigcap_{j=1}^n I_j M\Bigr)\longrightarrow \bigoplus_{j=1}^n M/I_j M
\]
is an isomorphism of $R$-modules. In particular, if $I+J=R$ then $M/(IM\cap JM)\cong M/IM\oplus M/JM$.

This is the module-level consequence of the [[algebra-rings/chinese-remainder-theorem|Chinese remainder theorem]] for pairwise comaximal [[algebra-rings/ideal|ideals]] in a [[algebra-rings/commutative-ring|commutative ring]], expressed as an isomorphism of [[algebra-modules/quotient-module|quotient modules]] into a [[algebra-modules/direct-sum-modules|direct sum]].
