---
title: "Closed sets via sequences (proof II)"
description: "A set is closed iff it contains limits of all convergent sequences from it"
---

**Proposition (Sequential characterization of closed sets, proof II).**
Let $(X,d)$ be a metric space and let $A\subset X$. Then $A$ is closed if and only if whenever $(a_n)$ is a sequence in $A$ and $a_n\to a$, we have $a\in A$.

**Proof sketch (using openness of the complement).**
- If $A$ is closed and $a_n\in A$ with $a_n\to a$, suppose $a\notin A$. Then $a\in A^c$, and $A^c$ is open, so some ball $B(a;\varepsilon)\subset A^c$. For large $n$, $a_n\in B(a;\varepsilon)$, contradicting $a_n\in A$.
- Conversely, assume the "contains limits" property and suppose $A^c$ is not open. Then there exists $a\in A^c$ such that every ball around $a$ meets $A$. Choose $a_n\in A\cap B(a;1/n)$, so $a_n\to a$ but $a\notin A$, a contradiction. Hence $A^c$ is open and $A$ is closed.
