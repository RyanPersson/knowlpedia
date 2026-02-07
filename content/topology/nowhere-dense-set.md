---
title: "Nowhere dense set"
description: "A set whose closure has empty interior"
---

A **nowhere dense set** in a {{< knowl id="topological-space" text="topological space" >}} $X$ is a {{< knowl id="subset" section="shared-foundations" text="subset" >}} $A\subseteq X$ such that the {{< knowl id="interior" text="interior" >}} of its {{< knowl id="closure" text="closure" >}} is {{< knowl id="empty-set" section="shared-foundations" text="empty" >}}, i.e. $\operatorname{int}(\overline{A})=\varnothing$.

Equivalently, $A$ is nowhere dense if $\overline{A}$ contains no nonempty {{< knowl id="open-set" text="open set" >}}. Nowhere dense sets are the basic building blocks of {{< knowl id="meager-set" text="meager sets" >}} in the {{< knowl id="baire-space" text="Baire category" >}} viewpoint.

**Examples:**
- The set of integers $\mathbb{Z}\subseteq \mathbb{R}$ (with the usual topology) is nowhere dense: it is {{< knowl id="closed-set" text="closed" >}} and has empty interior.
- The set $\{1/n : n\in\mathbb{N}\}\subseteq \mathbb{R}$ is nowhere dense: its closure is $\{1/n:n\in\mathbb{N}\}\cup\{0\}$, which has empty interior.
