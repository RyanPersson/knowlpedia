---
title: "Compactness criteria in metric spaces"
description: "Equivalent ways to check compactness for subsets of metric spaces"
---

**Compactness criteria (metric spaces)**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$. The following conditions are equivalent:

1. $K$ is {{< knowl id="compact-set" text="compact" >}} (open-cover definition).
2. $K$ is {{< knowl id="sequentially-compact-set" text="sequentially compact" >}}.
3. $K$ is complete and {{< knowl id="totally-bounded-set" text="totally bounded" >}}.
4. Every sequence in $K$ has a {{< knowl id="totally-bounded-cauchy-subsequence" text="Cauchy subsequence" >}}, and $K$ is complete.

These equivalences let you switch between topological and analytic viewpoints. For example, in $\mathbb{R}^n$ one often combines them with the {{< knowl id="heine-borel-theorem" text="Heine–Borel theorem" >}}.

**Proof sketch**: (1)$\Leftrightarrow$(2) is {{< knowl id="sequential-compactness-equals-compactness" text="sequential compactness equals compactness" >}}. (1)$\Leftrightarrow$(3) is {{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}}. The step (3)$\Rightarrow$(4) uses that total boundedness yields Cauchy subsequences, while (4)$\Rightarrow$(2) follows by completing Cauchy subsequences to convergent subsequences.

**Examples:**
- To show a set in $\mathbb{R}^n$ is compact, it often suffices to show it is closed and bounded (then apply Heine–Borel).
- In an infinite discrete metric space, completeness holds but total boundedness fails, so compactness fails by these criteria.
