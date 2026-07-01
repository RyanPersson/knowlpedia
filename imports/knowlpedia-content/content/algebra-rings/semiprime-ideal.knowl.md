+++
id = "algebra-rings/semiprime-ideal"
title = "Semiprime ideal"
kind = "knowl"
summary = "An ideal containing no nonzero nilpotent ideal modulo it; in commutative rings, the same as a radical ideal."
aliases = ["semiprime-ideal", "Semiprime ideal"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/semiprime-ideal.md"
+++

Let $R$ be a ring and let $I$ be a [[algebra-rings/two-sided-ideal|two-sided ideal]]. The ideal $I$ is **semiprime** if for every two-sided ideal $J\subseteq R$, the condition $J^2\subseteq I$ implies $J\subseteq I$.

Equivalently, the quotient $R/I$ has no nonzero nilpotent ideals, i.e. it contains no nonzero ideal all of whose elements are [[algebra-rings/nilpotent-element|nilpotent]]. In a commutative ring, semiprime ideals are exactly [[algebra-rings/radical-of-ideal|radical ideals]].

**Examples:**
- In $k[x,y]$, the ideal $(x)\cap (y)$ is semiprime (it is an intersection of prime ideals).
- In $\mathbb{Z}$, the ideal $(6)$ is semiprime (it is radical because $6$ is squarefree).
- In $\mathbb{Z}$, the ideal $(4)$ is not semiprime since $(2)^2\subseteq (4)$ but $(2)\nsubseteq (4)$.
