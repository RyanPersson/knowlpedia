---
title: "Jordan–Hölder Theorem (Groups)"
description: "Any two composition series have the same length and the same composition factors up to order"
---

**Jordan–Hölder Theorem (Groups).**
Let $G$ be a {{< knowl id="group" text="group" >}} that admits a {{< knowl id="composition-series-group" text="composition series" >}}, i.e. a finite chain
$$
G = G_0 \triangleright G_1 \triangleright \cdots \triangleright G_n = \{e\}
$$
such that each $G_{i+1}\trianglelefteq G_i$ and each factor $G_i/G_{i+1}$ is a {{< knowl id="simple-group" text="simple group" >}}. Then for any two composition series of $G$,
- the lengths are equal, and
- the multisets of factor groups $\{G_i/G_{i+1}\}$ agree up to {{< knowl id="group-isomorphism" text="isomorphism" >}} and permutation.

Jordan–Hölder gives a well-defined notion of the "composition factors" of a group (up to order and isomorphism). The standard proof combines {{< knowl id="schreier-refinement-theorem" text="the Schreier refinement theorem" >}} with the fact that a simple factor admits no nontrivial refinement.

**Proof sketch.**
Apply Schreier refinement to two composition series to obtain equivalent refinements. Since factors in a composition series are simple, any refinement must repeat the same factors (there is no proper intermediate normal subgroup), forcing the original series to have the same factors up to order.
