---
title: "Partial order"
description: "A binary relation that is reflexive, antisymmetric, and transitive."
---

A **partial order** on a {{< knowl id="set" text="set" >}} $P$ is a {{< knowl id="relation" text="relation" >}} $\le\,\subseteq P\times P$ such that for all $a,b,c\in P$:
- (Reflexive) $a\le a$.
- (Antisymmetric) If $a\le b$ and $b\le a$, then $a=b$.
- (Transitive) If $a\le b$ and $b\le c$, then $a\le c$.

The pair $(P,\le)$ is called a partially ordered set (poset). Here $P\times P$ is the {{< knowl id="cartesian-product" text="Cartesian product" >}} of $P$ with itself.

A partial order does not require that every pair of elements be comparable; when comparability holds for all pairs, one has a {{< knowl id="total-order" text="total order" >}}. Many notions in order theory, such as {{< knowl id="upper-bound" text="upper bounds" >}} and {{< knowl id="lower-bound" text="lower bounds" >}}, are defined relative to a partial order.

**Examples:**
- On the {{< knowl id="power-set" text="power set" >}} $\mathcal P(X)$ of a set $X$, define $A\le B$ iff $A\subseteq B$ (the {{< knowl id="subset" text="subset" >}} relation).
- On $\mathbb{N}$ (the {{< knowl id="natural-numbers" text="natural numbers" >}}), define $a\preceq b$ iff $a\mid b$ (divisibility). This is a partial order but not a total order.
