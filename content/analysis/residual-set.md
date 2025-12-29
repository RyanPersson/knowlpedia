---
title: "Residual set"
description: "A set whose complement is meager."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}. A set $R\subseteq X$ is **residual** (or **comeager**) if its complement is {{< knowl id="meager-set" text="meager" >}}:
$
X\setminus R\ \text{is meager in }X.
$

Residual sets are "topologically large" in {{< knowl id="complete-metric-space" text="complete metric spaces" >}}: by the Baire category theorem (see {{< knowl id="baire-space" text="Baire space" >}}), residual sets are {{< knowl id="dense-set" text="dense" >}} (in fact, they contain a dense $G_\delta$ set, though that terminology requires additional definitions).

**Examples:**
- In $\mathbb{R}$, the set of irrational numbers $\mathbb{R}\setminus\mathbb{Q}$ is residual, since $\mathbb{Q}$ is meager.
- If $X$ is a complete metric space, then $X$ itself is residual in $X$.
- The complement of a nowhere dense set need not be residual unless the set is meager; residualness is a "countable" notion.
