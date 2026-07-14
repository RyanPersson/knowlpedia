---
title: "Baire Category Theorem"
description: "In a complete metric space, a countable intersection of dense open sets is dense"
---

**Baire Category Theorem:** Let $(X,d)$ be a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} that is {{< knowl id="complete-metric-space" section="topology-metric" text="complete" >}}. If $(U_n)_{n\in\mathbb{N}}$ is a sequence of subsets of $X$ that are {{< knowl id="open-set" section="topology-core" text="open" >}} and {{< knowl id="dense-set" section="topology-core" text="dense" >}}, then $\bigcap_{n\in\mathbb{N}} U_n$ is dense in $X$.

Equivalently, $X$ cannot be written as a {{< knowl id="countable-set" section="shared-foundations" text="countable" >}} {{< knowl id="union" section="shared-foundations" text="union" >}} of {{< knowl id="nowhere-dense-set" text="nowhere dense" >}} subsets; in particular, $X$ is not {{< knowl id="meager-set" text="meager" >}} in itself.

This theorem produces many {{< knowl id="baire-space" text="Baire spaces" >}} and underlies standard {{< knowl id="category-argument-template" text="category arguments" >}} that conclude a property holds on a {{< knowl id="residual-set" text="residual" >}} subset.
