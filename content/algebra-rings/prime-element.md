---
title: "Prime element"
description: "A nonzero nonunit p such that p | ab implies p | a or p | b."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}}. An element $p\in R$ is a **prime element** if $p\neq 0$, $p$ is not a unit, and whenever $p$ divides a product $ab$, then $p$ divides $a$ or $p$ divides $b$.

Prime elements correspond to prime ideals: $p$ is prime if and only if the {{< knowl id="principal-ideal" text="principal ideal" >}} $(p)$ is a {{< knowl id="prime-ideal" text="prime ideal" >}}. Prime elements are always {{< knowl id="irreducible-element" text="irreducible" >}}, and in a UFD the converse holds.

**Examples:**
- In $\mathbb{Z}$, an integer is prime (in the usual number-theoretic sense) exactly when it is a prime element.
- In $k[x]$ for a field $k$, the polynomial $x$ is a prime element.
- In $\mathbb{Z}$, the element $6$ is not prime since $6\mid 2\cdot 3$ but $6\nmid 2$ and $6\nmid 3$.