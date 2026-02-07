---
title: "Solvable Group"
description: "A group whose derived series terminates at the trivial subgroup"
---

A **solvable group** is a {{< knowl id="group" text="group" >}} $G$ whose {{< knowl id="derived-series" text="derived series" >}} reaches the {{< knowl id="trivial-subgroup" text="trivial subgroup" >}} after finitely many steps; explicitly, there exists $n\ge 0$ such that $G^{(n)}=\{e\}$, where
- $G^{(0)}=G$, and
- $G^{(k+1)}=[G^{(k)},G^{(k)}]$ is the {{< knowl id="commutator-subgroup" text="commutator subgroup" >}} of $G^{(k)}$.

Equivalently, $G$ is solvable iff it has a finite {{< knowl id="subnormal-series" text="subnormal series" >}} whose successive quotients are {{< knowl id="abelian-group" text="abelian" >}}.

**Examples:**
- Every abelian group is solvable (the derived series hits $\{e\}$ in at most two steps).
- $S_3$ is solvable.
- *(Non-example)* $A_5$ is not solvable.
