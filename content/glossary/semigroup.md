---
title: "Semigroup"
description: "A set with an associative binary operation"
---

A **semigroup** is a set $S$ together with an associative binary operation $\cdot : S \times S \to S$:
$$(ab)c = a(bc) \quad \text{for all } a, b, c \in S$$

A semigroup is a {{< knowl id="magma" text="magma" >}} with associativity. If it also has an identity element, it becomes a {{< knowl id="monoid" text="monoid" >}}.

**Examples:**
- $(\mathbb{Z}^+, +)$ — positive integers under addition (no identity)
- $(2\mathbb{Z} \setminus \{0\}, \cdot)$ — nonzero even integers under multiplication
- Non-empty strings under concatenation
- $(\mathbb{N}, \max)$ — natural numbers with maximum operation
