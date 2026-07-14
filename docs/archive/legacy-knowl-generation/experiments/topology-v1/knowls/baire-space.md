---
title: "Baire space"
description: "A topological space where countable intersections of dense open sets are dense"
---

A **Baire space** is a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for every {{< knowl id="countable-set" text="countable" >}} family of {{< knowl id="open-set" text="open sets" >}} $U_1,U_2,\dots$ that are each {{< knowl id="dense-set" text="dense" >}} in $X$, the {{< knowl id="intersection" text="intersection" >}} $\bigcap_{n\ge 1} U_n$ is dense in $X$.

Equivalently, $X$ is Baire if and only if no nonempty open set is {{< knowl id="meager-set" text="meager" >}}. A major source of examples is the {{< knowl id="baire-category-theorem" text="Baire category theorem" >}}, which implies that every {{< knowl id="complete-metric-space" text="complete metric space" >}} is Baire.

**Examples:**
- The real line $\mathbb{R}$ with its usual topology is a Baire space.
- Any discrete topological space is a Baire space (every nonempty open set is already “large” in the category sense).
- The rationals $\mathbb{Q}$ with the subspace topology inherited from $\mathbb{R}$ are not a Baire space (they are meager in themselves).
