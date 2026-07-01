+++
id = "algebra-groups/automorphism-group"
title = "Automorphism Group"
kind = "knowl"
summary = "The group of all isomorphisms from a group to itself"
aliases = ["automorphism-group", "Automorphism Group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/automorphism-group.md"
+++

For a [[algebra-groups/group|group]] $G$, the **automorphism group** of $G$, denoted $\operatorname{Aut}(G)$, is the set of all [[algebra-groups/group-isomorphism|group isomorphisms]] $\varphi:G\to G$, with group operation given by [[shared-foundations/composition|composition]]
$$
(\varphi\psi)(x) := \varphi(\psi(x)).
$$

The identity element is $\mathrm{id}_G$, and inverses are given by inverse maps.

Automorphisms are "symmetries" of $G$ that preserve the group structure. Many constructions (e.g. [[algebra-groups/semidirect-product|semidirect products]]) are parametrized by homomorphisms into $\operatorname{Aut}(G)$.

**Examples:**
- $\operatorname{Aut}(\mathbb{Z})\cong C_2$, since an automorphism is determined by where it sends $1$, and it must send $1$ to $\pm 1$.
- If $G=C_n$ is cyclic of order $n$, then $\operatorname{Aut}(G)\cong (\mathbb{Z}/n\mathbb{Z})^\times$ (units mod $n$).
- For $G\times H$, there are automorphisms that swap factors when $G\cong H$, and more generally automorphisms can mix factors in nontrivial ways.
