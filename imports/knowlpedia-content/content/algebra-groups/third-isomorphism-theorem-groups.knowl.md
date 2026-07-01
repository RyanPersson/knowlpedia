+++
id = "algebra-groups/third-isomorphism-theorem-groups"
title = "Third Isomorphism Theorem (Groups)"
kind = "knowl"
summary = "If N ⊆ K ⊲ G with N ⊲ G, then (G/N)/(K/N) ≅ G/K"
aliases = ["third-isomorphism-theorem-groups", "Third Isomorphism Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/third-isomorphism-theorem-groups.md"
+++

**Third Isomorphism Theorem (Groups).**
Let $G$ be a [[algebra-groups/group|group]] and let $N \trianglelefteq G$ and $K \trianglelefteq G$ be [[algebra-groups/normal-subgroup|normal subgroups]] with $N \subseteq K$. Then $K/N$ is a normal subgroup of $G/N$, and there is a canonical isomorphism of [[algebra-groups/quotient-group|quotient groups]]
$$
(G/N)/(K/N) \cong G/K,
$$

induced by the map $gN \mapsto gK$.

This theorem formalizes the idea that "quotienting by $N$ and then by $K/N$" is the same as quotienting directly by $K$. It can be viewed as a special case of [[algebra-groups/correspondence-theorem-groups|the correspondence theorem]], or proved directly using [[algebra-groups/first-isomorphism-theorem-groups|the first isomorphism theorem]].
