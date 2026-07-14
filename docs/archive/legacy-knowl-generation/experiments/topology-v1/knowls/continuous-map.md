---
title: "Continuous map"
description: "A function that pulls back open sets to open sets."
---

A **continuous map** between topological spaces $(X,\tau_X)$ and $(Y,\tau_Y)$ is a {{< knowl id="function" text="function" >}} $f:X\to Y$ such that for every open set $V\in\tau_Y$, the {{< knowl id="preimage" text="preimage" >}} $f^{-1}(V)$ is an {{< knowl id="open-set" text="open set" >}} in $X$.

Equivalently, $f$ is continuous iff the preimage of every {{< knowl id="closed-set" text="closed set" >}} in $Y$ is closed in $X$. Continuity is the basic morphism notion in {{< knowl id="topological-space" text="topology" >}} (maps that respect the open-set structure).

**Examples:**
- The {{< knowl id="identity-function" text="identity map" >}} on any space is continuous.
- Any constant function $f:X\to Y$ is continuous.
- If $Y\subseteq X$ has the subspace topology, the inclusion $Y\hookrightarrow X$ is continuous.
