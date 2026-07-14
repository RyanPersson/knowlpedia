---
title: "Limit point"
description: "A point where every neighborhood meets the set at a point different from it."
---

A **limit point** (also called an accumulation point or cluster point) of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} is a point $x\in X$ such that every {{< knowl id="neighborhood" text="neighborhood" >}} $N$ of $x$ satisfies $N\cap (A\setminus\{x\})\neq\varnothing$.

Limit points describe where a set “accumulates” and are collected in the {{< knowl id="derived-set" text="derived set" >}}; they also control the {{< knowl id="closure" text="closure" >}} of $A$.

**Examples:**
- In $\mathbb{R}$, $0$ is a limit point of $\{1/n : n\in\mathbb{N}\}$.
- In $\mathbb{R}$, every point of $[0,1]$ is a limit point of $[0,1]$.
- In the discrete topology on $X$, no subset has any limit points.
