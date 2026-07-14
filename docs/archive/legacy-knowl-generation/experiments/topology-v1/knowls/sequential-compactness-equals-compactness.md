---
title: "Sequential compactness equals compactness"
description: "In metric spaces, compactness is equivalent to sequential compactness"
---

**Sequential compactness equals compactness**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$. Then $K$ is {{< knowl id="compact-set" text="compact" >}} if and only if $K$ is {{< knowl id="sequentially-compact-set" text="sequentially compact" >}}.

This theorem bridges the open-cover definition of compactness with the behavior of sequences, which is often more convenient in analysis. One common route is to use the analytic criterion {{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}} together with the fact that total boundedness yields Cauchy subsequences.

**Proof sketch**: (Compact $\Rightarrow$ sequentially compact) Use compactness to show $K$ is totally bounded; then any sequence has a Cauchy subsequence, and compactness implies completeness, so the subsequence converges in $K$. (Sequentially compact $\Rightarrow$ compact) Show sequential compactness forces total boundedness and completeness; then apply the complete-plus-totally-bounded compactness criterion.

**Examples:**
- In $\mathbb{R}^n$, every compact set is sequentially compact and conversely.
- In general topological spaces (not metrizable), compactness and sequential compactness can differ.
