---
title: "Subgroups of cyclic groups are cyclic"
description: "Every subgroup of a cyclic group is cyclic, with an explicit generator"
---

**Proposition (Subgroups of cyclic groups are cyclic).**
Let $G$ be a {{< knowl id="group" text="group" >}} that is cyclic, meaning $G=\langle g\rangle$ for some $g\in G$ (so $G$ is a {{< knowl id="cyclic-subgroup" text="cyclic group" >}}). Let $H\le G$ be a {{< knowl id="subgroup" text="subgroup" >}}.

1. If $G$ is infinite cyclic (isomorphic to $\mathbb Z$), then either $H=\{e\}$ or there exists a unique integer $m\ge 1$ such that $H=\langle g^m\rangle$.
2. If $|G|=n<\infty$, then there exists a divisor $d\mid n$ such that $|H|=d$, and moreover $H=\langle g^{n/d}\rangle$.

**Context.**
This result gives a complete classification of subgroups of cyclic groups: they are completely controlled by divisibility (finite case) or by a single positive integer (infinite case). It is frequently paired with {{< knowl id="lagranges-theorem" text="Lagrange's theorem" >}} in finite group computations.

**Proof sketch.**
(1) Consider the set $S=\{k\in\mathbb Z_{\ge 0}: g^k\in H\}$. If $H\neq\{e\}$ then $S$ contains a positive integer; let $m$ be the least positive element. Show $H=\langle g^m\rangle$ by Euclidean division: write $k=qm+r$ with $0\le r<m$, and use $g^k\in H$ to force $g^r\in H$, hence $r=0$.
(2) Reduce to (1) in the finite cyclic group of order $n$ by working with exponents modulo $n$, and use Lagrange to identify $|H|$ as a divisor of $n$.
