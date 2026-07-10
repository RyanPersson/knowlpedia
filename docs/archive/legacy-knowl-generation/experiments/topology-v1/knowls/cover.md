---
title: "Cover"
description: "A family of sets whose union contains a given set."
---

Let $X$ be a {{< knowl id="set" text="set" >}} and let $A\subseteq X$. A **cover** of $A$ is a collection $\{U_i\}_{i\in I}$ of {{< knowl id="subset" text="subsets" >}} of $X$ such that
$$
A \subseteq \bigcup_{i\in I} U_i.
$$

Covers organize “local data” into global statements, especially when the $U_i$ have additional structure (for instance, an {{< knowl id="open-cover" text="open cover" >}} requires each $U_i$ to be {{< knowl id="open-set" text="open" >}}). Many compactness results are phrased in terms of selecting finite subcovers and comparing covers via {{< knowl id="refinement-of-an-open-cover" text="refinements" >}}.

**Examples:**
- The intervals $\{( -1,2)\}$ cover $[0,1]\subseteq \mathbb{R}$.
- The family $\{(n,n+2)\}_{n\in\mathbb{Z}}$ is an open cover of $\mathbb{R}$ in the usual topology.
- If $A=\varnothing$, then the empty family is a cover of $A$.
