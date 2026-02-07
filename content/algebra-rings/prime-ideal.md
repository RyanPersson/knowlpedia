---
title: "Prime ideal"
description: "A proper ideal P such that ab in P forces a in P or b in P."
---

Let $R$ be a commutative ring. A **prime ideal** is a proper {{< knowl id="ideal" text="ideal" >}} $P\subsetneq R$ such that whenever $ab\in P$ (with $a,b\in R$), then $a\in P$ or $b\in P$.

Equivalently, $P$ is prime iff the {{< knowl id="quotient-ring" text="quotient ring" >}} $R/P$ is an {{< knowl id="integral-domain" text="integral domain" >}}. Prime ideals generalize prime numbers and underpin dimension theory, localization, and algebraic geometry.

**Examples:**
- In $\mathbb Z$, the ideal $(p)$ is prime iff $p$ is a prime integer.
- In $k[x,y]$, the ideal $(x)$ is prime, and so is $(x,y)$.
- In $\mathbb Z$, the ideal $(6)$ is not prime since $2\cdot 3\in (6)$ but neither $2$ nor $3$ lies in $(6)$.