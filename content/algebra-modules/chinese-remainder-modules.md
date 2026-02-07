---
title: "Chinese remainder for modules"
description: "Module quotients by comaximal ideal multiples split as a direct sum of smaller quotients."
---

**Chinese remainder for modules**: Let $R$ be a commutative ring, let $M$ be an $R$-module, and let $I_1,\dots,I_n\subset R$ be pairwise comaximal ideals. Then the canonical map
\[
M\Big/\Bigl(\bigcap_{j=1}^n I_j M\Bigr)\longrightarrow \bigoplus_{j=1}^n M/I_j M
\]
is an isomorphism of $R$-modules. In particular, if $I+J=R$ then $M/(IM\cap JM)\cong M/IM\oplus M/JM$.

This is the module-level consequence of the {{< knowl id="chinese-remainder-theorem" section="algebra-rings" text="Chinese remainder theorem" >}} for pairwise comaximal {{< knowl id="ideal" section="algebra-rings" text="ideals" >}} in a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}, expressed as an isomorphism of {{< knowl id="quotient-module" text="quotient modules" >}} into a {{< knowl id="direct-sum-modules" text="direct sum" >}}.
