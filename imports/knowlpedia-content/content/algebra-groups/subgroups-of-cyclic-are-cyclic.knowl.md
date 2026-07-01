+++
id = "algebra-groups/subgroups-of-cyclic-are-cyclic"
title = "Subgroups of cyclic groups are cyclic"
kind = "knowl"
summary = "Every subgroup of a cyclic group is cyclic, with an explicit generator"
aliases = ["subgroups-of-cyclic-are-cyclic", "Subgroups of cyclic groups are cyclic"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/subgroups-of-cyclic-are-cyclic.md"
+++

**Proposition (Subgroups of cyclic groups are cyclic).**
Let $G$ be a [[algebra-groups/group|group]] that is cyclic, meaning $G=\langle g\rangle$ for some $g\in G$ (so $G$ is a [[algebra-groups/cyclic-subgroup|cyclic group]]). Let $H\le G$ be a [[algebra-groups/subgroup|subgroup]].

1. If $G$ is infinite cyclic (isomorphic to $\mathbb Z$), then either $H=\{e\}$ or there exists a unique integer $m\ge 1$ such that $H=\langle g^m\rangle$.
2. If $|G|=n<\infty$, then there exists a divisor $d\mid n$ such that $|H|=d$, and moreover $H=\langle g^{n/d}\rangle$.

**Context.**
This result gives a complete classification of subgroups of cyclic groups: they are completely controlled by divisibility (finite case) or by a single positive integer (infinite case). It is frequently paired with [[algebra-groups/lagranges-theorem|Lagrange's theorem]] in finite group computations.
