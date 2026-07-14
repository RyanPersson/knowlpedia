---
title: "Nowhere dense set"
description: "A subset whose closure has empty interior in a topological space."
---

A subset $A\subseteq X$ of a {{{< knowl id="topological-space" section="topology-core" text="topological space" >}}} $X$ is **nowhere dense** in $X$ if the {{{< knowl id="interior" section="topology-core" text="interior" >}}} of its {{{< knowl id="closure" section="topology-core" text="closure" >}}} is empty:
$$\operatorname{int}(\overline{A})=\varnothing.$$

Equivalently, for every nonempty {{{< knowl id="open-set" section="topology-core" text="open set" >}}} $U\subseteq X$, there exists a nonempty open set $V\subseteq U$ with $V\cap A=\varnothing$. Nowhere dense sets are the basic pieces used to build {{{< knowl id="meager-set" text="meager sets" >}}} and are central in the definition of a {{{< knowl id="baire-space" text="Baire space" >}}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, any singleton $\{x\}$ (and hence any finite subset) is nowhere dense.
- The Cantor set in $\mathbb{R}$ is nowhere dense.
