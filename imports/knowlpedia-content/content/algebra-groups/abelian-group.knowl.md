+++
id = "algebra-groups/abelian-group"
title = "Abelian Group"
kind = "knowl"
summary = "A group whose operation is commutative"
aliases = ["abelian-group", "Abelian Group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/abelian-group.md"
+++

An **abelian group** is a [[algebra-groups/group|group]] $(G,\cdot)$ such that for all $a,b\in G$,
$
a\cdot b = b\cdot a.
$
(That is, the group operation is commutative.)

Abelian groups are often written in additive notation, replacing $\cdot$ by $+$, the identity element by $0$, and inverses by negatives. They form the algebraic backbone of linear structures (e.g. every [[linear-algebra/vector-space|vector space]] is an abelian group under addition).

**Examples:**
- $(\mathbb{Z},+)$ and $(\mathbb{R},+)$ are abelian groups.
- $(\mathbb{Z}/n\mathbb{Z},+)$ is an abelian group for each $n\ge 1$.
- The nonzero complex numbers $(\mathbb{C}^{\times},\times)$ form an abelian group.
- *(Non-example)* The symmetric group $S_3$ is not abelian.
