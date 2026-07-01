+++
id = "algebra-groups/quotient-group"
title = "Quotient Group"
kind = "knowl"
summary = "The group of cosets of a normal subgroup"
aliases = ["quotient-group", "Quotient Group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/quotient-group.md"
+++

Let $N$ be a [[algebra-groups/normal-subgroup|normal subgroup]] of a [[algebra-groups/group|group]] $G$. The **quotient group** $G/N$ is the set of (left) [[algebra-groups/coset|cosets]] $\{gN : g\in G\}$ equipped with the operation
$$
(gN)(hN) := (gh)N.
$$

Normality of $N$ is exactly what makes this operation **well-defined**, meaning it does not depend on the choice of representatives $g,h$ of the cosets.

There is a canonical [[algebra-groups/group-homomorphism|group homomorphism]] (the projection) $\pi:G\to G/N$, $\pi(g)=gN$, whose [[algebra-groups/kernel-group|kernel]] is $N$. Quotient groups are the objects that appear in [[algebra-groups/exact-sequence-groups|exact sequences]] and in the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]], which identifies $G/\ker(\varphi)$ with $\operatorname{im}(\varphi)$ for any homomorphism $\varphi$.

**Examples:**
- $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the subgroup $n\mathbb{Z}$; its elements are the residue classes mod $n$.
- In $S_3$, the alternating subgroup $A_3$ is normal, and $S_3/A_3$ has order $2$ (isomorphic to $C_2$).
- If $G$ is abelian, every subgroup is normal, so quotients $G/H$ exist for all subgroups $H\le G$.
