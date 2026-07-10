---
title: "Category argument template"
description: "A standard strategy in a Baire space to prove a property holds on a residual set"
---

A **category argument** is a proof strategy in a {{< knowl id="baire-space" text="Baire space" >}} showing that a desired property holds on a {{< knowl id="residual-set" text="residual" >}} (hence dense) subset by expressing that subset as a countable intersection of {{< knowl id="dense-set" section="topology-core" text="dense" >}} {{< knowl id="open-set" section="topology-core" text="open" >}} sets.

A common template is:
- Define sets $U_n\subseteq X$ encoding an “approximate” version of the property (often at accuracy $1/n$).
- Prove each $U_n$ is open.
- Prove each $U_n$ is dense (typically by working inside an arbitrary nonempty open set and making a small modification to land in $U_n$).
- Conclude that $\bigcap_{n\in\mathbb{N}} U_n$ is dense (by {{< knowl id="intersection-of-dense-open-is-dense" text="intersection of dense open sets is dense" >}}), hence the property holds on a residual set.

**Examples:**
- In $\mathbb{R}$, since $\mathbb{Q}=\{q_1,q_2,\dots\}$ is countable, each set $U_n=\mathbb{R}\setminus\{q_n\}$ is open and dense, and $\bigcap_{n\in\mathbb{N}} U_n=\mathbb{R}\setminus\mathbb{Q}$ is residual.
- In a {{< knowl id="complete-metric-space" section="topology-metric" text="complete metric space" >}}, verifying “open and dense” for the sets $U_n$ is often enough to show the target property is generic via the {{< knowl id="baire-category-theorem" text="Baire Category Theorem" >}}.
