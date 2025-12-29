---
title: "Baire space"
description: "A space where countable intersections of open dense sets are dense"
---

A topological space (in particular, a {{< knowl id="metric-space" text="metric space" >}}) $X$ is a **Baire space** if for every sequence of {{< knowl id="open-set" text="open" >}} {{< knowl id="dense-set" text="dense" >}} sets $U_1,U_2,\dots\subseteq X$, the intersection
$
\bigcap_{n=1}^\infty U_n
$
is dense in $X$.

Equivalently, $X$ is a Baire space if and only if:
- No nonempty open set in $X$ is {{< knowl id="meager-set" text="meager" >}} (i.e., every nonempty open set is of second category in itself).

In analysis, Baire spaces matter because they make "generic" ({{< knowl id="residual-set" text="residual" >}}) properties meaningful: residual sets are automatically dense.

**Examples:**
- Every {{< knowl id="complete-metric-space" text="complete metric space" >}} is a Baire space (Baire Category Theorem).
- $\mathbb{R}^k$ with the Euclidean metric is a Baire space.

**Non-example:**
- A metric space that is a countable union of {{< knowl id="nowhere-dense-set" text="nowhere dense" >}} sets is not a Baire space (by definition).
