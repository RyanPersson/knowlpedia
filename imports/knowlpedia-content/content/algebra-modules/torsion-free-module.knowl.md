+++
id = "algebra-modules/torsion-free-module"
title = "Torsion-free module"
kind = "knowl"
summary = "A module over an integral domain with no nonzero torsion elements."
aliases = ["torsion-free-module", "Torsion-free module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/torsion-free-module.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and $M$ an $R$-[[algebra-modules/module|module]]. The module $M$ is **torsion-free** if its only [[algebra-modules/torsion-element|torsion element]] is $0$, i.e. if $rm=0$ with $0\ne r\in R$ forces $m=0$.

Torsion-freeness is weaker than freeness but is a key hypothesis in many classification results over PIDs and in the theory of lattices.

**Examples:**
- $\mathbb Z^n$ is torsion-free as a $\mathbb Z$-module.
- Any ideal $I$ in an integral domain $R$, viewed as an $R$-module, is torsion-free.
- (Nonexample) $\mathbb Z/n\mathbb Z$ is not torsion-free for $n>1$.
