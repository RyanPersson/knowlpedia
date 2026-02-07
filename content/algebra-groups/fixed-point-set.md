---
title: "Fixed-Point Set"
description: "The subset of points fixed by all group elements in an action"
---

Let a {{< knowl id="group-action" text="group action" >}} of a group $G$ on a set $X$ be given. The **fixed-point set** of the action is
$$
X^G := \{x\in X : g\cdot x = x \text{ for all } g\in G\}.
$$

Equivalently, $x\in X^G$ iff its {{< knowl id="stabilizer" text="stabilizer" >}} is all of $G$, i.e. $G_x=G$. Fixed points often detect "invariants" of the action; for example, fixed points of conjugation encode central elements.

**Examples:**
- For the trivial action $g\cdot x=x$ for all $g,x$, one has $X^G=X$.
- For the conjugation action of $G$ on itself, the fixed-point set is the {{< knowl id="center-of-group" text="center" >}} $Z(G)$.
- For the action of $C_n$ on the vertices of a regular $n$-gon by rotation, the fixed-point set is empty if $n>1$ (no vertex is fixed by all rotations).
