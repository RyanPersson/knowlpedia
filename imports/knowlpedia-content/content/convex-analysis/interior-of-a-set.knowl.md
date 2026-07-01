+++
id = "convex-analysis/interior-of-a-set"
title = "Interior"
kind = "knowl"
summary = "The largest open set contained in a given set"
aliases = ["interior-of-a-set", "Interior"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/interior-of-a-set.md"
+++

Let $(X,d)$ be a metric space and let $E\subset X$.

The **interior** of $E$, denoted $\operatorname{int}(E)$ or $E^\circ$, is defined by
$$
\operatorname{int}(E):=\bigcup\{\,G\subset E \mid G \text{ is open}\,\}.
$$

Equivalently, $\operatorname{int}(E)$ is the **largest** [[convex-analysis/open-subset|open set]] contained in $E$.

A pointwise characterization is given by [[convex-analysis/interior-characterized-by-existence-of-a-ball|balls inside the set]].

**Examples:**
- In $\mathbb{R}$, $\operatorname{int}([0,1])=(0,1)$.
- If $E$ is open, then $\operatorname{int}(E)=E$.
- If $E$ has empty interior (e.g., the rationals in $\mathbb{R}$), then $\operatorname{int}(E)=\emptyset$.
