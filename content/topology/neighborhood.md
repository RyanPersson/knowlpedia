---
title: "Neighborhood"
description: "A set that contains an open set around a given point."
---

A **neighborhood** of a point $x$ in a {{< knowl id="topological-space" text="topological space" >}} $(X,\mathcal{T})$ is a subset $N\subseteq X$ such that there exists an {{< knowl id="open-set" text="open set" >}} $U\in\mathcal{T}$ with $x\in U\subseteq N$. Equivalently, $N$ is a neighborhood of $x$ if and only if $x\in \operatorname{int}(N)$, where {{< knowl id="interior" text="interior" >}} is taken in $X$.

Neighborhoods give a point-based way to express concepts like {{< knowl id="limit-point" text="limit points" >}} and {{< knowl id="continuous-map" text="continuity" >}} without referring directly to all open sets.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $(x-\varepsilon,x+\varepsilon)$ is a neighborhood of $x$ for any $\varepsilon>0$.
- In a {{< knowl id="metric-space" text="metric space" >}}, every {{< knowl id="open-ball" text="open ball" >}} centered at $x$ is a neighborhood of $x$.
- In $\mathbb{R}$, the closed interval $[x-1,x+1]$ is a neighborhood of $x$ (it contains the open interval $(x-1,x+1)$).
