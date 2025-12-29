---
title: "Closure via sequences"
description: "In metric spaces, a point is in the closure iff it is a limit of a sequence from the set"
---

**Proposition.**
Let $(X,d)$ be a metric space and let $A\subset X$. Then for $a\in X$,
$$
a\in \overline{A}\quad\Longleftrightarrow\quad \exists\ (a_n)\subset A \text{ with } a_n\to a.
$$

**Context.** This is a specifically metric phenomenon (first-countability): the topological notion of {{< knowl id="closure-of-a-set" text="closure" >}} can be detected by sequences.

**Proof sketch.**
- If $a\in\overline{A}$, then by {{< knowl id="closure-characterized-by-ball-intersections" text="ball intersections" >}} each ball $B(a;1/n)$ meets $A$; pick $a_n\in A\cap B(a;1/n)$ to get $a_n\to a$.
- Conversely, if $a_n\in A$ and $a_n\to a$, then every ball around $a$ contains some $a_n$, hence meets $A$, so $a\in\overline{A}$.
