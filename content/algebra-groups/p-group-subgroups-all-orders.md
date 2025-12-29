---
title: "Finite p-groups have subgroups of all p-power orders"
description: "If |G|=p^n then for each k there is a subgroup of order p^k"
---

**Proposition (Subgroups of all orders in a finite p-group).**
Let $p$ be a prime and let $G$ be a finite {{</* knowl id="p-group" text="p-group" */>}} with $|G|=p^n$. Then for every integer $k$ with $0\le k\le n$ there exists a {{</* knowl id="subgroup" text="subgroup" */>}} $H\le G$ such that $|H|=p^k$.

**Context.**
This is a structural strengthening of Lagrange's theorem for $p$-groups: not only do subgroup orders divide $|G|$, all intermediate $p$-powers actually occur. It is proved by induction using the existence of nontrivial center.

**Proof sketch.**
Induct on $n$. The cases $n=0,1$ are immediate. For $n\ge 1$, by {{</* knowl id="p-group-nontrivial-center" text="nontrivial center of a p-group" */>}} pick an element $z\in Z(G)$ of order $p$ (existence also follows from {{</* knowl id="cauchys-theorem-groups" text="Cauchy's theorem" */>}}). Let $Z=\langle z\rangle\le Z(G)$, so $|Z|=p$ and $Z\lhd G$. Then $G/Z$ is a $p$-group of order $p^{n-1}$. By the induction hypothesis, for each $0\le j\le n-1$ there is a subgroup $\overline H\le G/Z$ with $|\overline H|=p^j$. Let $H$ be the full preimage of $\overline H$ under the quotient map $G\to G/Z$; then $H$ has order $p^{j+1}$. Together with the trivial subgroup (order $p^0$), this yields all orders $p^k$.
