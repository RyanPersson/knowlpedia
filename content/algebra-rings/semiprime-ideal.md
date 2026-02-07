---
title: "Semiprime ideal"
description: "An ideal containing no nonzero nilpotent ideal modulo it; in commutative rings, the same as a radical ideal."
---

Let $R$ be a ring and let $I$ be a {{< knowl id="two-sided-ideal" text="two-sided ideal" >}}. The ideal $I$ is **semiprime** if for every two-sided ideal $J\subseteq R$, the condition $J^2\subseteq I$ implies $J\subseteq I$.

Equivalently, the quotient $R/I$ has no nonzero nilpotent ideals, i.e. it contains no nonzero ideal all of whose elements are {{< knowl id="nilpotent-element" text="nilpotent" >}}. In a commutative ring, semiprime ideals are exactly {{< knowl id="radical-of-ideal" text="radical ideals" >}}.

**Examples:**
- In $k[x,y]$, the ideal $(x)\cap (y)$ is semiprime (it is an intersection of prime ideals).
- In $\mathbb{Z}$, the ideal $(6)$ is semiprime (it is radical because $6$ is squarefree).
- In $\mathbb{Z}$, the ideal $(4)$ is not semiprime since $(2)^2\subseteq (4)$ but $(2)\nsubseteq (4)$.