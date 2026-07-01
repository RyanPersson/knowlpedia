+++
id = "algebra-groups/semigroup"
title = "Semigroup"
kind = "knowl"
summary = "A set equipped with an associative binary operation"
aliases = ["semigroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/semigroup.md"
+++

A **semigroup** is a [[shared-foundations/set|set]] $S$ together with an associative [[shared-foundations/binary-operation|binary operation]] $\cdot : S \times S \to S$, meaning that for all $a,b,c \in S$,
$
(a\cdot b)\cdot c \;=\; a\cdot(b\cdot c).
$

Semigroups are the weakest common algebraic setting in which repeated products are unambiguous (associativity lets you omit parentheses). A [[algebra-groups/monoid|monoid]] is a semigroup with an identity element, and a [[algebra-groups/group|group]] is a monoid in which every element has an inverse.

**Examples:**
- $(\mathbb{N},+)$ is a semigroup (addition is associative).
- $(\mathbb{N}_{\ge 1},\times)$ is a semigroup (multiplication is associative).
- The set of all $n\times n$ real matrices under matrix multiplication is a semigroup.
- *(Edge case)* If one allows empty algebraic structures, the empty set has a unique binary operation $\,\emptyset\times\emptyset\to\emptyset\,$ and is a semigroup, but it cannot be a monoid (no identity element exists).
