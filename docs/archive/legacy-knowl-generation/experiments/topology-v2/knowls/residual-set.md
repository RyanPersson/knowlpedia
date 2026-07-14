---
title: "Residual set"
description: "A set whose complement is meager; also called comeager"
---

A **residual set** in a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ is a subset $R\subseteq X$ whose {{< knowl id="complement" section="shared-foundations" text="complement" >}} $X\setminus R$ is {{< knowl id="meager-set" text="meager" >}}.

Equivalently, $R$ contains a countable intersection of subsets of $X$ that are {{< knowl id="open-set" section="topology-core" text="open" >}} and {{< knowl id="dense-set" section="topology-core" text="dense" >}} (often phrased as: $R$ contains a countable intersection of dense open sets). Such sets are also called comeager.

**Examples:**
- In $\mathbb{R}$, the irrationals are residual since $\mathbb{Q}$ is meager.
- In any {{< knowl id="baire-space" text="Baire space" >}}, every residual set is dense (because it contains a countable intersection of dense open sets).
- If $X$ is {{< knowl id="meager-set" text="meager" >}} in itself (so $X$ is not Baire), a residual set need not be dense; for instance, the empty set is residual when $X$ is meager.
