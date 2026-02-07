---
title: "Lebesgue number lemma"
description: "Every open cover of a compact metric space has a uniform scale that fits inside the cover."
---

**Lebesgue number lemma:** Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and assume $X$ is {{< knowl id="compact-set" text="compact" >}}. For every {{< knowl id="open-cover" text="open cover" >}} $\mathcal{U}$ of $X$, there exists a number $\delta>0$ (a Lebesgue number for $\mathcal{U}$) such that for every $x\in X$ there is some $U\in\mathcal{U}$ with
\[
B(x,\delta)\subseteq U,
\]
where $B(x,\delta)$ is the {{< knowl id="open-ball" text="open ball" >}}. Equivalently, every subset of $X$ with {{< knowl id="diameter" text="diameter" >}} less than $\delta$ is contained in some member of the cover.

This lemma turns qualitative compactness (existence of finite subcovers) into a quantitative uniform scale, and it is a key tool in results about {{< knowl id="uniformly-continuous-map" text="uniform continuity" >}} and {{< knowl id="refinement-of-open-cover" text="refinements of open covers" >}}.
