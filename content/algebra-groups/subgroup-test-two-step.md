---
title: "Subgroup Test (two-step)"
description: "A nonempty subset of a group is a subgroup iff it is closed under products and inverses"
---

**Subgroup Test (two-step)**: Let $G$ be a {{< knowl id="group" text="group" >}} and let $H$ be a nonempty {{< knowl id="subset" text="subset" >}} of $G$. Then $H$ is a {{< knowl id="subgroup" text="subgroup" >}} of $G$ if and only if:

1. for all $x,y\in H$ one has $xy\in H$ (closure under the group operation), and
2. for all $x\in H$ one has $x^{-1}\in H$ (closure under inverses).

This criterion is equivalent to the {{< knowl id="subgroup-test-one-step" text="one-step subgroup test" >}}; use whichever closure condition is easier to verify in a given situation.

**Proof sketch**: A subgroup satisfies both closure properties by definition. Conversely, if $H$ is nonempty and closed under products and inverses, then $H$ contains the identity (take $xx^{-1}$ for any $x\in H$) and satisfies the subgroup axioms inside $G$.
