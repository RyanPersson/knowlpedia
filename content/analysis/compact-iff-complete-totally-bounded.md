---
title: "Compact iff complete and totally bounded"
description: "In metric spaces, compactness is equivalent to completeness plus total boundedness"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $K\subseteq X$ with the subspace metric.

**Theorem**: The following are equivalent:
- $K$ is {{< knowl id="compact-set" text="compact" >}}.
- $K$ is {{< knowl id="complete-metric-space" text="complete" >}} and {{< knowl id="totally-bounded-set" text="totally bounded" >}}.

This theorem is the fundamental metric characterization of compactness: "no missing limits" (completeness) plus "finite $\varepsilon$-approximation at every scale" (total boundedness).

**Proof sketch**:
($\Rightarrow$) If $K$ is compact, then $K$ is complete (every {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} has a {{< knowl id="convergent-sequence" text="convergent" >}} {{< knowl id="subsequence" text="subsequence" >}}, and hence the full sequence converges) and totally bounded (the balls $\{{{< knowl id="open-ball" text="$B$" >}}(x,\varepsilon):x\in K\}$ form an {{< knowl id="open-cover" text="open cover" >}}; take a finite subcover).

($\Leftarrow$) If $K$ is totally bounded, then {{< knowl id="totally-bounded-cauchy-subsequence" text="every sequence in $K$ has a Cauchy subsequence" >}}. If $K$ is complete, that Cauchy subsequence converges to a point in $K$. Hence $K$ is {{< knowl id="sequential-compactness" text="sequentially compact" >}}. In metric spaces, sequential compactness is equivalent to compactness.
