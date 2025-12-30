---
title: "Bimodule"
description: "A module with commuting left and right actions by (possibly different) rings."
---

Let $R,S$ be {{< knowl id="ring" text="rings" >}}. An **$(R,S)$-bimodule** is an abelian group $M$ that is simultaneously a left {{< knowl id="module" text="module" >}} over $R$ and a right module over $S$, such that the actions are compatible:
for all $r\in R$, $s\in S$, and $m\in M$, one has $(rm)s=r(ms)$.

Bimodules are the natural setting for many constructions (e.g. balanced products) and are the input for the {{< knowl id="tensor-product" text="tensor product" >}}, where compatibility of left/right actions is essential.

**Examples:**
- Any ring $R$ is an $(R,R)$-bimodule with actions given by multiplication on the left and right.
- If $M$ is a left $R$-module, then $M$ is an $(R,\mathbb Z)$-bimodule using the canonical right $\mathbb Z$-action coming from the abelian-group structure.
- If $A$ is an {{< knowl id="algebra-over-ring" text="algebra over a ring" >}} $R$, then $A$ is naturally an $(R,A)$-bimodule: $r\cdot a$ uses the structure map $R\to A$, and $a\cdot a'$ is multiplication in $A$.
