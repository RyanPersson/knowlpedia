---
title: "Limit point (accumulation point, cluster point)"
description: "A point whose every neighborhood meets the set away from the point."
---

Let $(X,\tau)$ be a topological space and let $A\subseteq X$. A point $x\in X$ is a **limit point** (also called an accumulation or cluster point) of $A$ if every {{< knowl id="neighborhood" text="neighborhood" >}} $N$ of $x$ satisfies
$$
\bigl(N \cap (A\setminus\{x\})\bigr)\neq \varnothing,
$$
where $A\setminus\{x\}$ is a {{< knowl id="set-difference" text="set difference" >}}.

The set of all limit points of $A$ is the {{< knowl id="derived-set" text="derived set" >}} $A'$. Limit points also help describe {{< knowl id="closure" text="closure" >}}: $x\in \overline{A}$ iff every neighborhood of $x$ meets $A$ (without removing $x$).

**Examples:**
- In $\mathbb{R}$, $0$ is a limit point of $\{1/n : n\in\mathbb{N}\}$.
- Any finite subset of a $T_1$ space has no limit points.
- In a discrete topology, no set has a limit point (each singleton is a neighborhood).
