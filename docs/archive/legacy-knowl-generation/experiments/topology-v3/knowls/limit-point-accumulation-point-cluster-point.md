---
title: "Limit point (accumulation point, cluster point)"
description: "A point that every neighborhood meets in the set away from the point itself."
---

Let $A\subseteq X$ be a subset of a {{{< knowl id="topological-space" text="topological space" >}}} $X$. A point $x\in X$ is a **limit point** of $A$ (also called an **accumulation point** or **cluster point**) if every {{{< knowl id="neighborhood" text="neighborhood" >}}} $N$ of $x$ satisfies
\[
(N\setminus\{x\})\cap A \neq \varnothing.
\]
Equivalently, $x$ lies in the {{{< knowl id="closure" text="closure" >}}} of the {{{< knowl id="set-difference" section="shared-foundations" text="set difference" >}}} $A\setminus\{x\}$.

The set of all limit points of $A$ is its {{{< knowl id="derived-set" text="derived set" >}}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $0$ is a limit point of the set $\{1/n : n\in\mathbb{N}\}$.
