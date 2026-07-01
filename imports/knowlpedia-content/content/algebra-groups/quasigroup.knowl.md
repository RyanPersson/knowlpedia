+++
id = "algebra-groups/quasigroup"
title = "Quasigroup"
kind = "knowl"
summary = "A magma where division is always possible"
aliases = ["quasigroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/quasigroup.md"
+++

A **quasigroup** is a set $Q$ with a binary operation $\cdot$ such that for all $a, b \in Q$, the equations
$$ax = b \quad \text{and} \quad ya = b$$

each have unique solutions $x, y \in Q$.

Equivalently, a quasigroup is a [[algebra-groups/magma|magma]] whose Cayley table forms a Latin square—each element appears exactly once in each row and column.

A quasigroup with an identity element is called a [[algebra-groups/loop|loop]].

**Examples:**
- $(\mathbb{Z}, -)$ — integers under subtraction
- $(\mathbb{R}^+, \div)$ — positive reals under division
- Any Latin square defines a quasigroup
