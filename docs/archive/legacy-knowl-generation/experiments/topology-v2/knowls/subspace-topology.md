---
title: "Subspace topology"
description: "The topology on a subset induced from a larger topological space."
---

The **subspace topology** on a subset $Y\subseteq X$ of a {{< knowl id="topological-space" text="topological space" >}} $(X,\tau)$ is the collection
\[
\tau_Y=\{\,U\cap Y : U\in\tau\,\}.
\]

With this topology, a set is {{< knowl id="open-set" text="open" >}} in $Y$ exactly when it is the {{< knowl id="intersection" section="shared-foundations" text="intersection" >}} of $Y$ with an open set of $X$.

**Examples:**
- $[0,1]\subseteq\mathbb{R}$ with the subspace topology has basic open sets of the form $(a,b)\cap[0,1]$.
- If $X$ has the discrete topology, then every subset $Y\subseteq X$ is discrete in the subspace topology.
- If $X$ is indiscrete and $Y\neq\varnothing$, then $Y$ is indiscrete in the subspace topology.
