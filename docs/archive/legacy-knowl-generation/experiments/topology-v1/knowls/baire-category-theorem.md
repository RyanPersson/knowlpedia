---
title: "Baire category theorem"
description: "A completeness principle implying countable intersections of dense open sets are dense"
---

**Baire category theorem**: Let $(X,d)$ be a {{< knowl id="complete-metric-space" text="complete metric space" >}}. If $U_1,U_2,\dots$ are {{< knowl id="open-set" text="open" >}} and {{< knowl id="dense-set" text="dense" >}} subsets of $X$, then $\bigcap_{n\ge 1} U_n$ is dense in $X$. Equivalently, $X$ is a {{< knowl id="baire-space" text="Baire space" >}}.

A common reformulation is that $X$ cannot be written as a {{< knowl id="countable-set" text="countable" >}} {{< knowl id="union" text="union" >}} of {{< knowl id="nowhere-dense-set" text="nowhere dense" >}} sets (so “small” sets in the sense of category cannot exhaust a complete metric space). This theorem underlies many {{< knowl id="category-argument-template" text="category arguments" >}}.

**Proof sketch** *(idea)*: To show $\bigcap_n U_n$ meets an arbitrary nonempty open set, start inside a nonempty {{< knowl id="open-ball" text="open ball" >}} and use density of $U_1$ to choose a point of $U_1$ within it. Then choose a smaller nested {{< knowl id="closed-ball" text="closed ball" >}} contained in that open ball and still meeting $U_1$. Iterate, producing nested closed balls with radii going to zero and contained successively in $U_1,U_2,\dots$. By completeness (often packaged via the {{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}}), the intersection of these nested closed balls is nonempty, and any point in it lies in every $U_n$, forcing $\bigcap_n U_n$ to be dense.
