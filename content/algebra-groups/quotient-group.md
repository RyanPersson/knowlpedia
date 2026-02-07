---
title: "Quotient Group"
description: "The group of cosets of a normal subgroup"
---

Let $N$ be a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of a {{< knowl id="group" text="group" >}} $G$. The **quotient group** $G/N$ is the set of (left) {{< knowl id="coset" text="cosets" >}} $\{gN : g\in G\}$ equipped with the operation
$$
(gN)(hN) := (gh)N.
$$

Normality of $N$ is exactly what makes this operation **well-defined**, meaning it does not depend on the choice of representatives $g,h$ of the cosets.

There is a canonical {{< knowl id="group-homomorphism" text="group homomorphism" >}} (the projection) $\pi:G\to G/N$, $\pi(g)=gN$, whose {{< knowl id="kernel-group" text="kernel" >}} is $N$. Quotient groups are the objects that appear in {{< knowl id="exact-sequence-groups" text="exact sequences" >}} and in the {{< knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" >}}, which identifies $G/\ker(\varphi)$ with $\operatorname{im}(\varphi)$ for any homomorphism $\varphi$.

**Examples:**
- $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the subgroup $n\mathbb{Z}$; its elements are the residue classes mod $n$.
- In $S_3$, the alternating subgroup $A_3$ is normal, and $S_3/A_3$ has order $2$ (isomorphic to $C_2$).
- If $G$ is abelian, every subgroup is normal, so quotients $G/H$ exist for all subgroups $H\le G$.
