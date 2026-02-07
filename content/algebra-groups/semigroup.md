---
title: "Semigroup"
description: "A set equipped with an associative binary operation"
---

A **semigroup** is a {{< knowl id="set" section="shared-foundations" text="set" >}} $S$ together with an associative {{< knowl id="binary-operation" section="shared-foundations" text="binary operation" >}} $\cdot : S \times S \to S$, meaning that for all $a,b,c \in S$,
$
(a\cdot b)\cdot c \;=\; a\cdot(b\cdot c).
$

Semigroups are the weakest common algebraic setting in which repeated products are unambiguous (associativity lets you omit parentheses). A {{< knowl id="monoid" text="monoid" >}} is a semigroup with an identity element, and a {{< knowl id="group" text="group" >}} is a monoid in which every element has an inverse.

**Examples:**
- $(\mathbb{N},+)$ is a semigroup (addition is associative).
- $(\mathbb{N}_{\ge 1},\times)$ is a semigroup (multiplication is associative).
- The set of all $n\times n$ real matrices under matrix multiplication is a semigroup.
- *(Edge case)* If one allows empty algebraic structures, the empty set has a unique binary operation $\,\emptyset\times\emptyset\to\emptyset\,$ and is a semigroup, but it cannot be a monoid (no identity element exists).
