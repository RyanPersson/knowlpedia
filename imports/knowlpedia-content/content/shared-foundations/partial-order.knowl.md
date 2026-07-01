+++
id = "shared-foundations/partial-order"
title = "Partial order"
kind = "knowl"
summary = "A binary relation that is reflexive, antisymmetric, and transitive."
aliases = ["partial-order", "Partial order"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/partial-order.md"
+++

A **partial order** on a [[shared-foundations/set|set]] $P$ is a [[shared-foundations/relation|relation]] $\le\,\subseteq P\times P$ such that for all $a,b,c\in P$:
- (Reflexive) $a\le a$.
- (Antisymmetric) If $a\le b$ and $b\le a$, then $a=b$.
- (Transitive) If $a\le b$ and $b\le c$, then $a\le c$.

The pair $(P,\le)$ is called a partially ordered set (poset). Here $P\times P$ is the [[shared-foundations/cartesian-product|Cartesian product]] of $P$ with itself.

A partial order does not require that every pair of elements be comparable; when comparability holds for all pairs, one has a [[shared-foundations/total-order|total order]]. Many notions in order theory, such as [[shared-foundations/upper-bound|upper bounds]] and [[shared-foundations/lower-bound|lower bounds]], are defined relative to a partial order.

**Examples:**
- On the [[shared-foundations/power-set|power set]] $\mathcal P(X)$ of a set $X$, define $A\le B$ iff $A\subseteq B$ (the [[shared-foundations/subset|subset]] relation).
- On $\mathbb{N}$ (the [[shared-foundations/natural-numbers|natural numbers]]), define $a\preceq b$ iff $a\mid b$ (divisibility). This is a partial order but not a total order.
