+++
id = "algebra-groups/second-isomorphism-theorem-groups"
title = "Second Isomorphism Theorem (Groups)"
kind = "knowl"
summary = "For H ≤ G and K ⊲ G, there is a natural isomorphism H/(H∩K) ≅ HK/K"
aliases = ["second-isomorphism-theorem-groups", "Second Isomorphism Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/second-isomorphism-theorem-groups.md"
+++

**Second Isomorphism Theorem (Groups).**
Let $G$ be a [[algebra-groups/group|group]], let $H \le G$ be a [[algebra-groups/subgroup|subgroup]], and let $K \trianglelefteq G$ be a [[algebra-groups/normal-subgroup|normal subgroup]]. Define the subset
$$
HK = \{hk : h \in H,\ k \in K\}.
$$

Then $HK \le G$, $K \trianglelefteq HK$, and $H \cap K \trianglelefteq H$. Moreover, the map
$$
\phi: H \to HK/K, \qquad \phi(h) = hK,
$$

is a [[algebra-groups/group-homomorphism|homomorphism]] with kernel $H \cap K$, hence induces an isomorphism of [[algebra-groups/quotient-group|quotient groups]]
$$
H/(H \cap K) \cong HK/K.
$$

This theorem compares a subgroup with its image in a quotient and is frequently used to compute or identify quotients inside a larger group. It is most efficiently proved by applying [[algebra-groups/first-isomorphism-theorem-groups|the first isomorphism theorem]] to the restriction of the quotient map $HK \to HK/K$.
