+++
id = "algebra-modules/torsion-module"
title = "Torsion module"
kind = "knowl"
summary = "A module in which every element is torsion (over an integral domain)."
aliases = ["torsion-module", "Torsion module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/torsion-module.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and $M$ an $R$-[[algebra-modules/module|module]]. The module $M$ is a **torsion module** if every element of $M$ is a [[algebra-modules/torsion-element|torsion element]]; equivalently, for each $m\in M$ there exists $0\ne r\in R$ with $rm=0$.

Torsion modules sit opposite to [[algebra-modules/torsion-free-module|torsion-free modules]] and often decompose into primary pieces over suitable rings.

**Examples:**
- Any finite abelian group, viewed as a $\mathbb Z$-module, is torsion.
- For $R=k[x]$ and nonzero $f\in R$, the module $R/(f)$ is torsion as an $R$-module (every class is killed by $f$).
- (Nonexample) $\mathbb Z$ is not a torsion $\mathbb Z$-module.
