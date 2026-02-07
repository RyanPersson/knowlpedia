---
title: "Paracompact topological space"
description: "A topological space in which every open cover has a locally finite open refinement."
---

Let $X$ be a topological space.

An open cover $\{U_i\}_{i\in I}$ of $X$ is **locally finite** if every point $x\in X$ has a neighborhood $V_x$ that meets only finitely many sets $U_i$.

The space $X$ is **paracompact** if every open cover of $X$ admits a locally finite open refinement (i.e., there is a locally finite open cover $\{V_j\}_{j\in J}$ such that each $V_j\subset U_{i(j)}$ for some $i(j)$).

Paracompactness is one of the key hypotheses that ensures the existence of {{< knowl id="partition-of-unity-subordinate-to-an-open-cover" text="partitions of unity subordinate to open covers" >}} and underlies many global constructions in differential geometry.

## Examples
1. **Metric spaces.**  
   Every metric space is paracompact. In particular, all smooth manifolds modeled on $\mathbb R^n$ with their usual topology are paracompact when they satisfy the standard countability hypotheses.

2. **Compact Hausdorff spaces.**  
   Every compact Hausdorff space is paracompact: open covers admit finite subcovers, hence are automatically locally finite.

3. **CW complexes.**  
   CW complexes are paracompact, which is one reason the {{< knowl id="classifying-space-bg" text="classifying space" >}} technology behaves well for bundles over CW-type bases.
