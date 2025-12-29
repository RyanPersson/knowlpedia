---
title: "Groups of order p^2 are abelian"
description: "Every group of order p^2 (p prime) is abelian"
---

**Proposition (Order $p^2$ implies abelian).**
Let $G$ be a finite {{</* knowl id="group" text="group" */>}} with $|G|=p^2$ for a prime $p$. Then $G$ is {{</* knowl id="abelian-group" text="abelian" */>}}, i.e. $xy=yx$ for all $x,y\in G$.

**Context.**
A common strategy for small-order classification is: show the center is nontrivial, then pass to a quotient. The key input is that finite {{</* knowl id="p-group" text="p-groups" */>}} have nontrivial center.

**Proof sketch.**
Since $|G|=p^2$ is a power of $p$, $G$ is a $p$-group. By the lemma {{</* knowl id="p-group-nontrivial-center" text="a p-group has nontrivial center" */>}}, $Z(G)\neq \{e\}$. Thus $|Z(G)|$ is $p$ or $p^2$.

- If $|Z(G)|=p^2$, then $Z(G)=G$, so $G$ is abelian.
- If $|Z(G)|=p$, then the quotient $G/Z(G)$ has order $p$ and hence is cyclic by {{</* knowl id="prime-order-cyclic" text="prime-order implies cyclic" */>}}. If $G/Z(G)$ is cyclic, then $G$ is abelian: for any $x,y\in G$, their images commute in the quotient, so $x^{-1}y^{-1}xy\in Z(G)$; but commutators landing in the center and a cyclic quotient force all commutators to be trivial in this order-$p$ situation, yielding $xy=yx$.
