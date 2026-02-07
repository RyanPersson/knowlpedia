---
title: "Continuous map"
description: "A function whose preimage of every open set is open."
---

A **continuous map** between {{< knowl id="topological-space" text="topological spaces" >}} $(X,\mathcal{T}_X)$ and $(Y,\mathcal{T}_Y)$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:X\to Y$ such that for every {{< knowl id="open-set" text="open set" >}} $V\in\mathcal{T}_Y$, the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} $f^{-1}(V)$ is open in $X$.

Equivalently, $f$ is continuous if the preimage of every {{< knowl id="closed-set" text="closed set" >}} in $Y$ is closed in $X$. In practice, continuity is often checked using a {{< knowl id="basis-of-topology" text="basis" >}} or {{< knowl id="subbasis-of-topology" text="subbasis" >}} of the topology on $Y$.

**Examples:**
- The identity map $\mathrm{id}_X:X\to X$ is continuous for any topological space $X$.
- Any constant map $f:X\to Y$ (sending all of $X$ to a single point of $Y$) is continuous.
- If $Y\subseteq X$ has the {{< knowl id="subspace-topology" text="subspace topology" >}}, the inclusion map $i:Y\to X$ is continuous.
