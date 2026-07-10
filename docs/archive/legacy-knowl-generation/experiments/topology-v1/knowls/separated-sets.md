---
title: "Separated sets"
description: "Two sets that avoid each other's closure in a topological space."
---

Let $X$ be a {{< knowl id="topological-space" text="topological space" >}} and let $A,B\subseteq X$. The sets $A$ and $B$ are **separated** if
- $A\cap \overline{B}=\varnothing$, and
- $\overline{A}\cap B=\varnothing$,
where $\overline{A}$ and $\overline{B}$ denote {{< knowl id="closure" text="closures" >}}.

Separated sets need not have disjoint closures (they may share boundary points that lie in neither set). The notion is central to {{< knowl id="connected-set" text="connectedness" >}}: a space is disconnected exactly when it can be written as the union of two nonempty separated sets.

**Examples:**
- In $\mathbb{R}$, the sets $(0,1)$ and $(1,2)$ are separated.
- In $\mathbb{R}$, the sets $(0,2)$ and $(1,3)$ are not separated, since each intersects the closure of the other.
