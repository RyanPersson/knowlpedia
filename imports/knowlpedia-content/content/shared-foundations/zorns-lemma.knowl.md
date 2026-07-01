+++
id = "shared-foundations/zorns-lemma"
title = "Zorn's lemma"
kind = "knowl"
summary = "A maximal-element principle for partially ordered sets."
aliases = ["zorns-lemma", "Zorn's lemma"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/zorns-lemma.md"
+++

**Zorn's lemma:** Let $(P,\le)$ be a [[shared-foundations/partial-order|partially ordered set]]. If every chain $C\subseteq P$ has an [[shared-foundations/upper-bound|upper bound]] in $P$, then $P$ has a maximal element.

Here a **chain** means a subset $C\subseteq P$ on which the restriction of $\le$ is a [[shared-foundations/total-order|total order]], and an element $m\in P$ is **maximal** if there is no $p\in P$ with $m<p$ (i.e., $m\le p$ and $m\ne p$). Over ZF, Zorn's lemma is equivalent to the [[shared-foundations/axiom-of-choice|Axiom of Choice]] and to the [[shared-foundations/well-ordering-theorem|well-ordering theorem]].
