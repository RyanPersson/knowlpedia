---
title: "Cover"
description: "A family of sets whose union contains a given set."
---

A **cover** of a subset $A\subseteq X$ is a family of subsets $\{U_i\}_{i\in I}$ of $X$ such that
\[
A \subseteq \bigcup_{i\in I} U_i.
\]

In other words, the {{< knowl id="union" section="shared-foundations" text="union" >}} of the sets $U_i$ contains $A$. If each $U_i$ is an {{< knowl id="open-set" text="open set" >}}, the family is an {{< knowl id="open-cover" section="topology-compactness" text="open cover" >}}.

**Examples:**
- The intervals $\{( -1,2 )\}$ cover $[0,1]$, and so do $\{( -1,1/2 ), (1/2,2)\}$.
- $\{X\}$ is a (trivial) cover of every subset $A\subseteq X$.
- The empty family covers $\varnothing$, since $\varnothing\subseteq\bigcup\varnothing=\varnothing$.
