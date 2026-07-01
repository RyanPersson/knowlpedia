+++
id = "algebra-groups/jordan-holder-theorem-groups"
title = "Jordan–Hölder Theorem (Groups)"
kind = "knowl"
summary = "Any two composition series have the same length and the same composition factors up to order"
aliases = ["jordan-holder-theorem-groups", "Jordan–Hölder Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/jordan-holder-theorem-groups.md"
+++

**Jordan–Hölder Theorem (Groups).**
Let $G$ be a [[algebra-groups/group|group]] that admits a [[algebra-groups/composition-series-group|composition series]], i.e. a finite chain
$$
G = G_0 \triangleright G_1 \triangleright \cdots \triangleright G_n = \{e\}
$$

such that each $G_{i+1}\trianglelefteq G_i$ and each factor $G_i/G_{i+1}$ is a [[algebra-groups/simple-group|simple group]]. Then for any two composition series of $G$,
- the lengths are equal, and
- the multisets of factor groups $\{G_i/G_{i+1}\}$ agree up to [[algebra-groups/group-isomorphism|isomorphism]] and permutation.

Jordan–Hölder gives a well-defined notion of the "composition factors" of a group (up to order and isomorphism). The standard proof combines [[algebra-groups/schreier-refinement-theorem|the Schreier refinement theorem]] with the fact that a simple factor admits no nontrivial refinement.
