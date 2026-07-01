+++
id = "algebra-modules/rank-module"
title = "Rank of a free module"
kind = "knowl"
summary = "The cardinality of a basis of a free module."
aliases = ["rank-module", "Rank of a free module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/rank-module.md"
+++

Let $F$ be a [[algebra-modules/free-module|free module]]. The **rank** of $F$ is the [[shared-foundations/cardinality|cardinality]] of a [[algebra-modules/basis-module|basis]], denoted $\operatorname{rank}(F)$. This is well-defined: any two bases of a free module have the same cardinality.

When the rank is finite, it plays the role of [[convex-analysis/basis-hamel-basis-and-dimension|dimension]], but over a general ring one typically speaks of rank only for free (or locally free) modules.

**Examples:**
- $\operatorname{rank}(R^n)=n$.
- The zero module has rank $0$ (its basis is the empty set).
- If $F\cong \bigoplus_{i\in I} R$, then $\operatorname{rank}(F)=|I|$.
