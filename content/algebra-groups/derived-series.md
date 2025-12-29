---
title: "Derived series"
description: "The descending series obtained by repeatedly taking commutator subgroups"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. The **derived series** of $G$ is the sequence of subgroups $(G^{(n)})_{n\ge 0}$ defined recursively by
$
G^{(0)}=G,\qquad G^{(n+1)}=[G^{(n)},G^{(n)}],
$
where $[G^{(n)},G^{(n)}]$ denotes the {{< knowl id="commutator-subgroup" text="commutator subgroup" >}} of $G^{(n)}$. Each $G^{(n)}$ is a normal subgroup of $G$, and the quotients $G^{(n)}/G^{(n+1)}$ are abelian.

A group $G$ is {{< knowl id="solvable-group" text="solvable" >}} if there exists $n$ such that $G^{(n)}$ is the {{< knowl id="trivial-subgroup" text="trivial subgroup" >}}. The derived series is a particular kind of {{< knowl id="subnormal-series" text="subnormal series" >}} that measures how far $G$ is from being abelian.

**Examples:**
- If $G$ is abelian, then $G^{(1)}=\{e\}$, so the derived series terminates after one step.
- For $S_3$, one has $S_3^{(1)}=A_3$ and $S_3^{(2)}=\{e\}$, so $S_3$ is solvable of derived length $2$.
- For a nonabelian simple group (e.g. $A_5$), the derived series does not reach $\{e\}$, hence such a group is not solvable.
