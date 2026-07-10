---
title: "Subspace topology"
description: "The topology on a subset induced by intersecting with open sets of the ambient space."
---

Let $(X,\tau)$ be a {{{< knowl id="topological-space" text="topological space" >}}} and let $Y\subseteq X$. The **subspace topology** on $Y$ is the collection
\[
\tau_Y=\{U\cap Y : U\in\tau\}.
\]
A set $V\subseteq Y$ is open in $Y$ (with this topology) exactly when $V=U\cap Y$ for some {{{< knowl id="open-set" text="open set" >}}} $U$ in $X$.

The subspace topology is the standard way to regard a {{{< knowl id="subset" section="shared-foundations" text="subset" >}}} as a topological space in its own right.

**Examples:**
- Let $Y=[0,1]\subseteq\mathbb{R}$ with the usual topology on $\mathbb{R}$. Then sets like $(0,1]$ are open in $Y$ because $(0,2)\cap[0,1]=(0,1]$.
