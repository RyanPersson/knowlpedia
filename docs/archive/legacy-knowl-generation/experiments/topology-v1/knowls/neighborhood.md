---
title: "Neighborhood"
description: "A set that contains an open set around a point."
---

Let $(X,\tau)$ be a {{< knowl id="topological-space" text="topological space" >}} and let $x\in X$. A set $N\subseteq X$ is a **neighborhood** of $x$ if there exists an {{< knowl id="open-set" text="open set" >}} $U$ such that $x\in U\subseteq N$.

Neighborhoods are a point-based way to talk about the topology; they are used to define {{< knowl id="limit-point-accumulation-point-cluster-point" text="accumulation points" >}} and to express {{< knowl id="continuous-map" text="continuity" >}} in “local” terms.

**Examples:**
- In $\mathbb{R}$, any open interval $(x-\varepsilon,x+\varepsilon)$ is a neighborhood of $x$.
- If $N$ is a neighborhood of $x$ and $N\subseteq M$, then $M$ is also a neighborhood of $x$.
