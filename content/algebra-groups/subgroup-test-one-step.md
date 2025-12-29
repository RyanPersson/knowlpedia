---
title: "Subgroup Test (one-step)"
description: "A nonempty subset of a group is a subgroup iff it is closed under xy^{-1}"
---

**Subgroup Test (one-step)**: Let $G$ be a {{< knowl id="group" text="group" >}} and let $H$ be a nonempty {{< knowl id="subset" text="subset" >}} of $G$. Then $H$ is a {{< knowl id="subgroup" text="subgroup" >}} of $G$ if and only if for all $x,y\in H$ one has $xy^{-1}\in H$.

This is often the fastest criterion to check the subgroup property because it packages "closed under products" and "closed under inverses" into a single closure condition.

**Proof sketch**: If $H$ is a subgroup, then $y^{-1}\in H$ and hence $xy^{-1}\in H$. Conversely, assume $H\neq\varnothing$ and $xy^{-1}\in H$ for all $x,y\in H$. Fix $h\in H$. Taking $x=y=h$ gives $e=hh^{-1}\in H$. Taking $x=e$ shows $y^{-1}\in H$ for all $y\in H$, and then $xy=(x)( (y^{-1})^{-1})\in H$ shows closure under products.
