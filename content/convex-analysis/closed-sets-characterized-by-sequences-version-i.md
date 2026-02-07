---
title: "Closed sets via sequences (proof I)"
description: "A set is closed iff it contains limits of all convergent sequences from it"
---

**Proposition (Sequential characterization of closed sets, proof I).**
Let $(X,d)$ be a metric space and let $A\subset X$. Then $A$ is {{< knowl id="closed-subset" text="closed" >}} if and only if whenever $(a_n)$ is a sequence in $A$ and $a_n\to a$, we have $a\in A$.

**Proof sketch (using closure).**
- If $A$ is closed, then $\overline{A}=A$. If $a_n\in A$ and $a_n\to a$, then by {{< knowl id="closure-characterized-by-convergent-sequences" text="closure via sequences" >}} we have $a\in\overline{A}=A$.
- Conversely, assume the "contains limits" property. Take any $x\in\overline{A}$. By the same closure-via-sequences proposition, there exists $a_n\in A$ with $a_n\to x$. By hypothesis $x\in A$. Hence $\overline{A}\subset A$, so $\overline{A}=A$ and $A$ is closed.
