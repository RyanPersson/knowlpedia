---
title: "Zorn's lemma"
description: "A maximal-element principle for partially ordered sets."
---

**Zorn's lemma:** Let $(P,\le)$ be a {{< knowl id="partial-order" text="partially ordered set" >}}. If every chain $C\subseteq P$ has an {{< knowl id="upper-bound" text="upper bound" >}} in $P$, then $P$ has a maximal element.

Here a **chain** means a subset $C\subseteq P$ on which the restriction of $\le$ is a {{< knowl id="total-order" text="total order" >}}, and an element $m\in P$ is **maximal** if there is no $p\in P$ with $m<p$ (i.e., $m\le p$ and $m\ne p$). Over ZF, Zorn's lemma is equivalent to the {{< knowl id="axiom-of-choice" text="Axiom of Choice" >}} and to the {{< knowl id="well-ordering-theorem" text="well-ordering theorem" >}}.
