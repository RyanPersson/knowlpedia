---
title: "Interior"
description: "The largest open set contained in a given set"
---

Let $(X,d)$ be a metric space and let $E\subset X$.

The **interior** of $E$, denoted $\operatorname{int}(E)$ or $E^\circ$, is defined by
$$
\operatorname{int}(E):=\bigcup\{\,G\subset E \mid G \text{ is open}\,\}.
$$
Equivalently, $\operatorname{int}(E)$ is the **largest** {{< knowl id="open-subset" text="open set" >}} contained in $E$.

A pointwise characterization is given by {{< knowl id="interior-characterized-by-existence-of-a-ball" text="balls inside the set" >}}.

**Examples:**
- In $\mathbb{R}$, $\operatorname{int}([0,1])=(0,1)$.
- If $E$ is open, then $\operatorname{int}(E)=E$.
- If $E$ has empty interior (e.g., the rationals in $\mathbb{R}$), then $\operatorname{int}(E)=\emptyset$.
