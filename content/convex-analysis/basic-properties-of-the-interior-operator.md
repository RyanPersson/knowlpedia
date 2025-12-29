---
title: "Basic properties of interior"
description: "Monotonicity, idempotence, and compatibility with finite intersections"
---

**Proposition.**
Let $(X,d)$ be a metric space and let $A,B\subset X$. Then:

1. If $A\subset B$, then $A^\circ\subset B^\circ$.
2. $A^\circ=A$ if and only if $A$ is {{< knowl id="open-subset" text="open" >}}.
3. $(A^\circ)^\circ=A^\circ$ (idempotence).
4. $(A\cap B)^\circ=A^\circ\cap B^\circ$.

**Proof sketch.**
1. Any open set contained in $A$ is contained in $B$, so its union is contained in $B^\circ$.
2. By definition, $A^\circ\subset A$ always; equality holds exactly when $A$ is already open.
3. $A^\circ$ is open, so its interior is itself.
4. Use that a set is contained in $A\cap B$ iff it is contained in both $A$ and $B$.
