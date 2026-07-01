+++
id = "algebra-groups/p-squared-abelian"
title = "Groups of order p^2 are abelian"
kind = "knowl"
summary = "Every group of order p^2 (p prime) is abelian"
aliases = ["p-squared-abelian", "Groups of order p^2 are abelian"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/p-squared-abelian.md"
+++

**Proposition (Order $p^2$ implies abelian).**
Let $G$ be a finite [[algebra-groups/group|group]] with $|G|=p^2$ for a prime $p$. Then $G$ is [[algebra-groups/abelian-group|abelian]], i.e. $xy=yx$ for all $x,y\in G$.

**Context.**
A common strategy for small-order classification is: show the center is nontrivial, then pass to a quotient. The key input is that finite [[algebra-groups/p-group|p-groups]] have nontrivial center.


- If $|Z(G)|=p^2$, then $Z(G)=G$, so $G$ is abelian.
- If $|Z(G)|=p$, then the quotient $G/Z(G)$ has order $p$ and hence is cyclic by [[algebra-groups/prime-order-cyclic|prime-order implies cyclic]]. If $G/Z(G)$ is cyclic, then $G$ is abelian: for any $x,y\in G$, their images commute in the quotient, so $x^{-1}y^{-1}xy\in Z(G)$; but commutators landing in the center and a cyclic quotient force all commutators to be trivial in this order-$p$ situation, yielding $xy=yx$.
