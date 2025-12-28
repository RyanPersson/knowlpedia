---
title: "Monoid"
description: "A semigroup with an identity element"
---

A **monoid** is a set $M$ together with an associative binary operation and an identity element:

1. **Associativity:** $(ab)c = a(bc)$ for all $a, b, c \in M$
2. **Identity:** There exists $e \in M$ such that $ea = ae = a$ for all $a \in M$

A monoid is a {{< knowl id="semigroup" text="semigroup" >}} with identity. If every element also has an inverse, it becomes a {{< knowl id="group" text="group" >}}.

**Examples:**
- $(\mathbb{N}, +, 0)$ — natural numbers under addition
- $(\mathbb{N}, \cdot, 1)$ — natural numbers under multiplication
- $(M_n(\mathbb{R}), \cdot, I)$ — $n \times n$ matrices under multiplication
- $(\Sigma^*, \cdot, \varepsilon)$ — strings over alphabet $\Sigma$ with concatenation
