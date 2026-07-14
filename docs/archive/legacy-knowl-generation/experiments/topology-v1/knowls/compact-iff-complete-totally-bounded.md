---
title: "Compact iff complete and totally bounded"
description: "A metric space is compact exactly when it is complete and totally bounded"
---

**Compact iff complete and totally bounded**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$. Then $K$ is {{< knowl id="compact-set" text="compact" >}} if and only if:

1. $K$ is {{< knowl id="complete-metric-space" text="complete" >}} (with the restricted metric), and
2. $K$ is {{< knowl id="totally-bounded-set" text="totally bounded" >}}.

**Proof sketch**: If $K$ is compact, then {{< knowl id="compactness-implies-total-boundedness" text="compactness implies total boundedness" >}} and {{< knowl id="compactness-implies-completeness" text="compactness implies completeness" >}}. Conversely, if $K$ is totally bounded, any sequence has a {{< knowl id="totally-bounded-cauchy-subsequence" text="Cauchy subsequence" >}}; completeness then gives a convergent subsequence in $K$, so $K$ is sequentially compact. In metric spaces, sequential compactness implies compactness by {{< knowl id="sequential-compactness-equals-compactness" text="sequential compactness equals compactness" >}}.

This criterion is often the most practical way to prove compactness in analysis.

**Examples:**
- A closed interval in $\mathbb{R}$ is complete and totally bounded, hence compact.
- An infinite discrete metric space is complete but not totally bounded, hence not compact.
