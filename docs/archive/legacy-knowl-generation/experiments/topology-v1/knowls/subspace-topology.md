---
title: "Subspace topology"
description: "The topology induced on a subset by intersecting with open sets."
---

Let $(X,\tau)$ be a topological space and let $Y\subseteq X$. The **subspace topology** on $Y$ is
$$
\tau_Y=\{U\cap Y : U\in \tau\}.
$$
A set is open in $Y$ exactly when it is the {{< knowl id="intersection" text="intersection" >}} of $Y$ with an {{< knowl id="open-set" text="open set" >}} of $X$.

This construction is the standard way to make a {{< knowl id="subset" text="subset" >}} into a topological space compatible with the ambient {{< knowl id="topology" text="topology" >}}. With this topology, the inclusion map $Y\hookrightarrow X$ is {{< knowl id="continuous-map" text="continuous" >}}.

**Examples:**
- The interval $[0,1]\subseteq \mathbb{R}$ with the subspace topology has open sets of the form $(a,b)\cap [0,1]$.
- If $Y$ is a single point, the only open sets in $Y$ are $\varnothing$ and $Y$.
