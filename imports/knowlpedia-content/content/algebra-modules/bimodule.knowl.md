+++
id = "algebra-modules/bimodule"
title = "Bimodule"
kind = "knowl"
summary = "A module with commuting left and right actions by (possibly different) rings."
aliases = ["bimodule"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/bimodule.md"
+++

Let $R,S$ be [[algebra-rings/ring|rings]]. An **$(R,S)$-bimodule** is an abelian group $M$ that is simultaneously a left [[algebra-modules/module|module]] over $R$ and a right module over $S$, such that the actions are compatible:
for all $r\in R$, $s\in S$, and $m\in M$, one has $(rm)s=r(ms)$.

Bimodules are the natural setting for many constructions (e.g. balanced products) and are the input for the [[algebra-modules/tensor-product|tensor product]], where compatibility of left/right actions is essential.

**Examples:**
- Any ring $R$ is an $(R,R)$-bimodule with actions given by multiplication on the left and right.
- If $M$ is a left $R$-module, then $M$ is an $(R,\mathbb Z)$-bimodule using the canonical right $\mathbb Z$-action coming from the abelian-group structure.
- If $A$ is an [[algebra-modules/algebra-over-ring|algebra over a ring]] $R$, then $A$ is naturally an $(R,A)$-bimodule: $r\cdot a$ uses the structure map $R\to A$, and $a\cdot a'$ is multiplication in $A$.
