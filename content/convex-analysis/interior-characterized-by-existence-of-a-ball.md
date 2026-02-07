---
title: "Interior via balls"
description: "A point lies in the interior iff a ball around it is contained in the set"
---

**Proposition.**
Let $(X,d)$ be a metric space, let $a\in X$, and let $E\subset X$. Then
$$
a\in \operatorname{int}(E)\quad\Longleftrightarrow\quad \exists\,\delta>0 \text{ such that } B(a;\delta)\subset E.
$$

**Context.** This equivalence connects the "union of all open subsets" definition of {{< knowl id="interior-of-a-set" text="interior" >}} to the ball-based definition of openness in metric spaces.

**Proof sketch.**
- If $a\in\operatorname{int}(E)$, then $a$ lies in some open set $G\subset E$, so by openness there is a ball around $a$ contained in $G\subset E$.
- If $B(a;\delta)\subset E$, then $B(a;\delta)$ is open and contained in $E$, hence lies in the union defining $\operatorname{int}(E)$, so $a\in\operatorname{int}(E)$.
