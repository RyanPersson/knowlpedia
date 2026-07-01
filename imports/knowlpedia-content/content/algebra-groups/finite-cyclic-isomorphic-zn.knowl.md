+++
id = "algebra-groups/finite-cyclic-isomorphic-zn"
title = "Finite cyclic group is isomorphic to ℤ/nℤ"
kind = "knowl"
summary = "A cyclic group of order n is (canonically) isomorphic to ℤ/nℤ"
aliases = ["finite-cyclic-isomorphic-zn", "Finite cyclic group is isomorphic to ℤ/nℤ"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/finite-cyclic-isomorphic-zn.md"
+++

**Proposition (Finite cyclic groups).**
Let $G$ be a [[algebra-groups/group|group]]. Suppose $G$ is cyclic of finite order $n$, i.e. $G=\langle g\rangle$ and $|G|=n$. Then $G$ is [[algebra-groups/group-isomorphism|isomorphic]] to the additive group $\mathbb Z/n\mathbb Z$. Concretely, the map
$$
\varphi:\mathbb Z/n\mathbb Z \longrightarrow G,\qquad \varphi(\overline{k})=g^k
$$
is a well-defined isomorphism.

**Context.**
This identifies finite cyclic groups up to unique isomorphism by their order. Many computations about cyclic groups can therefore be reduced to modular arithmetic in $\mathbb Z/n\mathbb Z$.
