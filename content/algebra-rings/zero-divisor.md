---
title: "Zero divisor"
description: "A nonzero element that multiplies with some nonzero element to give zero."
---

Let $R$ be a ring. A nonzero element $a\in R$ is a **left zero divisor** if there exists $b\ne 0$ with $ab=0$, and a **right zero divisor** if there exists $c\ne 0$ with $ca=0$. In a {{< knowl id="commutative-ring" text="commutative ring" >}}, these notions coincide and one simply says *zero divisor*.

A ring has no nonzero zero divisors precisely when it is an {{< knowl id="integral-domain" text="integral domain" >}} (in the commutative, unital convention). Zero divisors are detected by nontrivial annihilators and obstruct cancellation.

**Examples:**
- In $\mathbb Z/6\mathbb Z$, the class of $2$ is a zero divisor since $2\cdot 3=0$.
- In $k[x,y]/(xy)$, the classes of $x$ and $y$ are nonzero zero divisors.
- In $\mathbb Z$, no nonzero element is a zero divisor.