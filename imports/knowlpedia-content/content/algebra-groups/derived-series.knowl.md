+++
id = "algebra-groups/derived-series"
title = "Derived series"
kind = "knowl"
summary = "The descending series obtained by repeatedly taking commutator subgroups"
aliases = ["derived-series", "Derived series"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/derived-series.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. The **derived series** of $G$ is the sequence of subgroups $(G^{(n)})_{n\ge 0}$ defined recursively by
$
G^{(0)}=G,\qquad G^{(n+1)}=[G^{(n)},G^{(n)}],
$
where $[G^{(n)},G^{(n)}]$ denotes the [[algebra-groups/commutator-subgroup|commutator subgroup]] of $G^{(n)}$. Each $G^{(n)}$ is a normal subgroup of $G$, and the quotients $G^{(n)}/G^{(n+1)}$ are abelian.

A group $G$ is [[algebra-groups/solvable-group|solvable]] if there exists $n$ such that $G^{(n)}$ is the [[algebra-groups/trivial-subgroup|trivial subgroup]]. The derived series is a particular kind of [[algebra-groups/subnormal-series|subnormal series]] that measures how far $G$ is from being abelian.

**Examples:**
- If $G$ is abelian, then $G^{(1)}=\{e\}$, so the derived series terminates after one step.
- For $S_3$, one has $S_3^{(1)}=A_3$ and $S_3^{(2)}=\{e\}$, so $S_3$ is solvable of derived length $2$.
- For a nonabelian simple group (e.g. $A_5$), the derived series does not reach $\{e\}$, hence such a group is not solvable.
