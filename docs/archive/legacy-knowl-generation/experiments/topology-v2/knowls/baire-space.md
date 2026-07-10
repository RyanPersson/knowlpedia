---
title: "Baire space"
description: "A topological space in which countable intersections of dense open sets remain dense"
---

A **Baire space** is a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ such that for every sequence $(U_n)_{n\in\mathbb{N}}$ of subsets of $X$ that are {{< knowl id="open-set" section="topology-core" text="open" >}} and {{< knowl id="dense-set" section="topology-core" text="dense" >}} in $X$, the intersection $\bigcap_{n\in\mathbb{N}} U_n$ is dense in $X$.

Baire spaces are the basic setting for {{< knowl id="category-argument-template" text="category arguments" >}} and for interpreting {{< knowl id="residual-set" text="residual" >}} (generic) subsets.

**Examples:**
- Every {{< knowl id="complete-metric-space" section="topology-metric" text="complete metric space" >}} is a Baire space (see {{< knowl id="complete-metric-space-is-baire" text="complete metric space is Baire" >}}).
- $\mathbb{R}$ with its usual metric topology is a Baire space.
- $\mathbb{Q}$ with the {{< knowl id="subspace-topology" section="topology-core" text="subspace topology" >}} inherited from $\mathbb{R}$ is not a Baire space; it is {{< knowl id="meager-set" text="meager" >}} in itself.
