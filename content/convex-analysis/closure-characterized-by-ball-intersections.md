---
title: "Closure via balls"
description: "A point is in the closure iff every ball around it meets the set"
---

**Proposition.**
Let $(X,d)$ be a metric space, let $E\subset X$, and let $a\in X$. The following are equivalent:

1. $a\in \overline{E}$.
2. For every $r>0$, one has $B(a;r)\cap E\neq\emptyset$.

**Context.** This gives a local/topological interpretation of the {{< knowl id="closure-of-a-set" text="closure" >}} in terms of neighborhoods (open balls).

**Proof sketch.**
- If $a\in\overline{E}$ and some ball $B(a;r)$ missed $E$, then $E$ would lie in the closed complement of that ball, forcing $a$ to lie outside $\overline{E}$, a contradiction.
- Conversely, if every ball around $a$ meets $E$ and $a\notin\overline{E}$, then $\overline{E}^c$ is open and contains $a$, so some ball around $a$ lies in $\overline{E}^c$ and misses $E$, a contradiction.
