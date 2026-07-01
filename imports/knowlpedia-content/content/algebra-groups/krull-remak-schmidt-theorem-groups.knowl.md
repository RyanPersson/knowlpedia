+++
id = "algebra-groups/krull-remak-schmidt-theorem-groups"
title = "Krull–Remak–Schmidt Theorem (Groups)"
kind = "knowl"
summary = "Under chain conditions, direct product decompositions into indecomposable normal factors are unique up to order"
aliases = ["krull-remak-schmidt-theorem-groups", "Krull–Remak–Schmidt Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/krull-remak-schmidt-theorem-groups.md"
+++

**Krull–Remak–Schmidt Theorem (Groups).**
Let $G$ be a [[algebra-groups/group|group]] that satisfies both the ascending and descending chain conditions on [[algebra-groups/normal-subgroup|normal subgroups]] (in particular, any finite group satisfies these conditions). Suppose
$$
G \cong G_1 \times \cdots \times G_n
$$

is a [[algebra-groups/direct-product-groups|direct product]] decomposition in which each $G_i$ is nontrivial, normal in $G$, and **directly indecomposable** (meaning $G_i$ is not isomorphic to $A\times B$ with $A,B$ both nontrivial). If also
$$
G \cong H_1 \times \cdots \times H_m
$$

is another such decomposition with directly indecomposable normal factors, then $n=m$ and, after permuting indices, there are [[algebra-groups/group-isomorphism|isomorphisms]] $G_i \cong H_i$ for all $i$.

Equivalently: the multiset of isomorphism types of directly indecomposable factors in an [[algebra-groups/internal-direct-product|internal direct product]] decomposition is an invariant of $G$ (under the stated chain hypotheses). This is the group analogue of [[algebra-modules/krull-schmidt-azumaya-theorem|Krull–Schmidt–Azumaya for modules]].
