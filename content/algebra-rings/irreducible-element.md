---
title: "Irreducible element"
description: "A nonzero nonunit that cannot be written as a product of two nonunits."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}}. An element $a\in R$ is **irreducible** if $a\neq 0$, $a$ is not a {{< knowl id="unit" text="unit" >}}, and whenever $a=bc$, then $b$ or $c$ is a unit.

Irreducibles are the basic “atoms” of factorization. In general domains, irreducible need not imply {{< knowl id="prime-element" text="prime" >}}, but they coincide in a {{< knowl id="ufd" text="UFD" >}}.

**Examples:**
- In $\mathbb{Z}$, $2$ is irreducible.
- In $k[x,y]$ (for a field $k$), the polynomial $x$ is irreducible.
- In $\mathbb{Z}$, $6$ is not irreducible since $6=2\cdot 3$ with neither factor a unit.