---
title: "Ideal"
description: "An additive subgroup closed under multiplication by ring elements on one side (left or right)."
---

An **ideal** in a {{< knowl id="ring" text="ring" >}} $R$ is an additive subgroup $I\le (R,+)$ such that it is stable under multiplication by elements of $R$ on one side:
- $I$ is a **left ideal** if $rI\subseteq I$ for all $r\in R$,
- $I$ is a **right ideal** if $Ir\subseteq I$ for all $r\in R$.

Ideals are exactly the kernels of ring homomorphisms, and they are the congruence data needed to form a {{< knowl id="quotient-ring" text="quotient ring" >}}. In commutative rings the left/right distinction disappears, but in noncommutative rings it is essential.

**Examples:**
- In $\mathbb Z$, every ideal has the form $n\mathbb Z$ for some $n\ge 0$.
- In $k[x,y]$, the set $(x,y)$ of polynomials with zero constant term is an ideal.
- In $M_2(k)$, the set of matrices whose second column is zero is a left ideal but not a right ideal.