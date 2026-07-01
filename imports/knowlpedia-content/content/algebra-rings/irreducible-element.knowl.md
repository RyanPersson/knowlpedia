+++
id = "algebra-rings/irreducible-element"
title = "Irreducible element"
kind = "knowl"
summary = "A nonzero nonunit that cannot be written as a product of two nonunits."
aliases = ["irreducible-element", "Irreducible element"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/irreducible-element.md"
+++

Let $R$ be an [[algebra-rings/integral-domain|integral domain]]. An element $a\in R$ is **irreducible** if $a\neq 0$, $a$ is not a [[algebra-rings/unit|unit]], and whenever $a=bc$, then $b$ or $c$ is a unit.

Irreducibles are the basic “atoms” of factorization. In general domains, irreducible need not imply [[algebra-rings/prime-element|prime]], but they coincide in a [[algebra-rings/ufd|UFD]].

**Examples:**
- In $\mathbb{Z}$, $2$ is irreducible.
- In $k[x,y]$ (for a field $k$), the polynomial $x$ is irreducible.
- In $\mathbb{Z}$, $6$ is not irreducible since $6=2\cdot 3$ with neither factor a unit.
