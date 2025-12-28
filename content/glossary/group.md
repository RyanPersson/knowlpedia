---
title: "Group"
description: "A set with an associative binary operation, identity element, and inverses"
---

A **group** is a set $G$ together with a binary operation $\cdot : G \times G \to G$ satisfying:

1. **Associativity:** $(ab)c = a(bc)$ for all $a, b, c \in G$
2. **Identity:** There exists $e \in G$ such that $ea = ae = a$ for all $a \in G$
3. **Inverses:** For each $a \in G$, there exists $a^{-1} \in G$ such that $aa^{-1} = a^{-1}a = e$

Equivalently, a group is a {{< knowl id="monoid" text="monoid" >}} in which every element is invertible, or a {{< knowl id="loop" text="loop" >}} that is associative.

**Examples:**
- $(\mathbb{Z}, +)$ — integers under addition
- $(\mathbb{Q} \setminus \{0\}, \cdot)$ — nonzero rationals under multiplication
- $S_n$ — symmetric group on $n$ elements
- $\text{GL}(n, \mathbb{R})$ — invertible $n \times n$ matrices
