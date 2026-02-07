---
title: "Finite subcover lemma"
description: "A compact set has a finite subcover for every open cover"
---

**Finite subcover lemma**: Let $(X,d)$ be a {{< knowl id="metric-space" section="topology" text="metric space" >}} and let $K\subseteq X$ be {{< knowl id="compact-set" section="topology" text="compact" >}}. If $\{U_\alpha\}_{\alpha\in A}$ is an {{< knowl id="open-set" section="topology" text="open" >}} cover of $K$, meaning
$
K\subseteq \bigcup_{\alpha\in A} U_\alpha,
$
then there exist $\alpha_1,\dots,\alpha_N\in A$ such that
$
K\subseteq U_{\alpha_1}\cup\cdots\cup U_{\alpha_N}.
$

This is the defining operational feature of compactness and is used as a "black box" step in many arguments: convert infinitely many local pieces into finitely many.

**Examples:**
- The {{< knowl id="interval" text="interval" >}} $[0,1]$ is compact, so any open cover of $[0,1]$ contains a finite subcover.
- The open interval $(0,1)$ is not compact: the cover $\{(1/n,1):n\in\mathbb{N}\}$ has no finite subcover.
