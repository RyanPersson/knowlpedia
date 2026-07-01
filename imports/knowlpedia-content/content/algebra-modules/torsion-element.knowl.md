+++
id = "algebra-modules/torsion-element"
title = "Torsion element"
kind = "knowl"
summary = "An element killed by a nonzero scalar in a module over an integral domain."
aliases = ["torsion-element", "Torsion element"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/torsion-element.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]] and $M$ a (left) $R$-[[algebra-modules/module|module]]. An element $m\in M$ is a **torsion element** if there exists a nonzero $r\in R$ such that $rm=0$. Equivalently, the [[algebra-modules/annihilator-element|annihilator]]
$\operatorname{ann}(m)$ is a nonzero ideal of $R$.

Torsion detects “failure of cancellation” under scalar multiplication and is a central invariant in structure theorems over PIDs and Dedekind domains.

**Examples:**
- In the $\mathbb Z$-module $\mathbb Z/n\mathbb Z$, every element is torsion (killed by $n$).
- In the $\mathbb Z$-module $\mathbb Z$, the only torsion element is $0$.
- (Edge case) Over a field, every nonzero scalar is invertible, so the only torsion element in a vector space is $0$.
