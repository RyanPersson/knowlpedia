---
title: "Topology axioms"
description: "The three closure properties that characterize when a family of subsets is a topology."
---

The **topology axioms** say that a collection $\tau$ of subsets of a set $X$ is a {{< knowl id="topology" text="topology" >}} if and only if:

1. $\varnothing\in\tau$ and $X\in\tau$.
2. If $\{U_i\}_{i\in I}\subseteq\tau$, then $\bigcup_{i\in I} U_i \in \tau$.
3. If $U_1,\dots,U_n\in\tau$, then $\bigcap_{k=1}^n U_k \in \tau$.

Here $\bigcup$ and $\bigcap$ are the {{< knowl id="union" section="shared-foundations" text="union" >}} and {{< knowl id="intersection" section="shared-foundations" text="intersection" >}} operations; these axioms ensure {{< knowl id="open-set" text="open sets" >}} are stable under arbitrary unions and finite intersections.

**Examples:**
- $\{\varnothing,X\}$ satisfies the axioms (the indiscrete topology).
- The collection of all open intervals $(a,b)\subseteq\mathbb{R}$ does *not* form a topology, because unions of open intervals need not be a single open interval; it is instead a {{< knowl id="basis-of-a-topology" text="basis" >}} for the usual topology.
