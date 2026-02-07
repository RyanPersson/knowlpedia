---
title: "Krull–Remak–Schmidt Theorem (Groups)"
description: "Under chain conditions, direct product decompositions into indecomposable normal factors are unique up to order"
---

**Krull–Remak–Schmidt Theorem (Groups).**
Let $G$ be a {{< knowl id="group" text="group" >}} that satisfies both the ascending and descending chain conditions on {{< knowl id="normal-subgroup" text="normal subgroups" >}} (in particular, any finite group satisfies these conditions). Suppose
$$
G \cong G_1 \times \cdots \times G_n
$$

is a {{< knowl id="direct-product-groups" text="direct product" >}} decomposition in which each $G_i$ is nontrivial, normal in $G$, and **directly indecomposable** (meaning $G_i$ is not isomorphic to $A\times B$ with $A,B$ both nontrivial). If also
$$
G \cong H_1 \times \cdots \times H_m
$$

is another such decomposition with directly indecomposable normal factors, then $n=m$ and, after permuting indices, there are {{< knowl id="group-isomorphism" text="isomorphisms" >}} $G_i \cong H_i$ for all $i$.

Equivalently: the multiset of isomorphism types of directly indecomposable factors in an {{< knowl id="internal-direct-product" text="internal direct product" >}} decomposition is an invariant of $G$ (under the stated chain hypotheses). This is the group analogue of {{< knowl id="krull-schmidt-azumaya-theorem" section="algebra-modules" text="Krull–Schmidt–Azumaya for modules" >}}.
