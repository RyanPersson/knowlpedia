---
title: "Subspace topology"
description: "The topology on a subset obtained by intersecting with open sets of the ambient space."
---

The **subspace topology** on a subset $Y\subseteq X$ of a {{< knowl id="topological-space" text="topological space" >}} $(X,\mathcal{T})$ is the topology
\[
\mathcal{T}_Y=\{U\cap Y : U\in\mathcal{T}\}.
\]
With this topology, $(Y,\mathcal{T}_Y)$ becomes a topological space, called a subspace of $X$.

A subset $V\subseteq Y$ is {{< knowl id="open-set" text="open" >}} in the subspace exactly when it is the intersection of $Y$ with an open set of $X$. The inclusion map $i:Y\to X$ is automatically {{< knowl id="continuous-map" text="continuous" >}} for the subspace topology.

**Examples:**
- $[0,1]\subseteq \mathbb{R}$ with the subspace topology has open sets of the form $U\cap[0,1]$, where $U$ is open in $\mathbb{R}$.
- If $Y=\{x_0\}$ is a singleton subset of any space $X$, then $Y$ has the indiscrete (and also discrete) topology $\{\varnothing,Y\}$.
- Any subset of a discrete space is discrete in the subspace topology.
