---
title: "Lebesgue number lemma"
description: "An open cover of a compact metric set has a uniform ball size subordinate to the cover"
---

**Lebesgue number lemma:** Let $(X,d)$ be a {{{< knowl id="metric-space" section="topology-metric" text="metric space" >}}}, let $K\subseteq X$ be {{{< knowl id="compact-set" text="compact" >}}}, and let $\mathcal U$ be an {{{< knowl id="open-cover" text="open cover" >}}} of $K$. Then there exists a number $\delta>0$ such that for every $x\in K$ there is some $U\in\mathcal U$ with
\[
B(x,\delta)\cap K \subseteq U,
\]
where $B(x,\delta)$ is the {{{< knowl id="open-ball" section="topology-metric" text="open ball" >}}} of radius $\delta$ about $x$.

Any such $\delta$ is called a Lebesgue number for the cover. The lemma is often used to pass from arbitrary open covers to controlled-radius ball covers, and it is closely tied to {{{< knowl id="refinement-of-an-open-cover" text="refinements" >}}}.
