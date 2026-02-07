---
title: "Second Isomorphism Theorem (Groups)"
description: "For H ≤ G and K ⊲ G, there is a natural isomorphism H/(H∩K) ≅ HK/K"
---

**Second Isomorphism Theorem (Groups).**
Let $G$ be a {{< knowl id="group" text="group" >}}, let $H \le G$ be a {{< knowl id="subgroup" text="subgroup" >}}, and let $K \trianglelefteq G$ be a {{< knowl id="normal-subgroup" text="normal subgroup" >}}. Define the subset
$$
HK = \{hk : h \in H,\ k \in K\}.
$$

Then $HK \le G$, $K \trianglelefteq HK$, and $H \cap K \trianglelefteq H$. Moreover, the map
$$
\phi: H \to HK/K, \qquad \phi(h) = hK,
$$

is a {{< knowl id="group-homomorphism" text="homomorphism" >}} with kernel $H \cap K$, hence induces an isomorphism of {{< knowl id="quotient-group" text="quotient groups" >}}
$$
H/(H \cap K) \cong HK/K.
$$

This theorem compares a subgroup with its image in a quotient and is frequently used to compute or identify quotients inside a larger group. It is most efficiently proved by applying {{< knowl id="first-isomorphism-theorem-groups" text="the first isomorphism theorem" >}} to the restriction of the quotient map $HK \to HK/K$.
