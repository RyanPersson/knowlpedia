---
title: "Intersection of dense open sets is dense"
description: "In a Baire space, countable intersections of open dense sets are dense"
---

**Intersection of dense open sets is dense**: Let $X$ be a {{< knowl id="baire-space" text="Baire space" >}} and let $U_1,U_2,\dots$ be a {{< knowl id="countable-set" text="countable" >}} family of subsets of $X$ such that each $U_n$ is {{< knowl id="open-set" text="open" >}} and {{< knowl id="dense-set" text="dense" >}}. Then their {{< knowl id="intersection" text="intersection" >}} $\bigcap_{n\ge 1} U_n$ is dense in $X$.

Equivalently, the complement of such an intersection is {{< knowl id="meager-set" text="meager" >}}. When $X$ is a {{< knowl id="complete-metric-space" text="complete metric space" >}}, this property is guaranteed by the {{< knowl id="baire-category-theorem" text="Baire category theorem" >}}.

**Proof sketch**: This is exactly the defining property of a Baire space. In complete metric spaces, it follows from the nested-balls argument in the Baire category theorem.
