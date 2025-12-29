---
title: "Schreier Refinement Theorem"
description: "Any two subnormal series admit equivalent refinements with isomorphic factors"
---

**Schreier Refinement Theorem.**
Let $G$ be a {{< knowl id="group" text="group" >}}. Consider two finite {{< knowl id="subnormal-series" text="subnormal series" >}} (normal series)
$$
G = G_0 \triangleright G_1 \triangleright \cdots \triangleright G_n,
\qquad
G = H_0 \triangleright H_1 \triangleright \cdots \triangleright H_m,
$$
where each inclusion is normal in the previous term. Then there exist refinements of these series (obtained by inserting additional intermediate subgroups) such that the refined series have the same length and their successive factor groups are pairwise {{< knowl id="group-isomorphism" text="isomorphic" >}} up to a permutation. Each factor group is a {{< knowl id="quotient-group" text="quotient group" >}} of the form $A/B$ with $B \trianglelefteq A$.

Schreier refinement is the main structural comparison tool for normal series. It is the standard input for {{< knowl id="jordan-holder-theorem-groups" text="the Jordan–Hölder theorem" >}}.

**Proof sketch.**
One constructs a common refinement by inserting the subgroups $G_i\cap H_j$ (and related products) into both chains. The key identifications of successive quotients come from repeated applications of {{< knowl id="second-isomorphism-theorem-groups" text="the second isomorphism theorem" >}} to compare quotients built from intersections and products.
