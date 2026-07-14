---
title: "Total boundedness and epsilon nets"
description: "Finite epsilon nets describe how a set can be covered by finitely many small balls"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $E\subseteq X$.

An **epsilon net** for $E$ is a finite set $\{x_1,\dots,x_n\}\subseteq X$ such that
$$
E \subseteq \bigcup_{i=1}^n B(x_i,\varepsilon),
$$
where $B(x_i,\varepsilon)$ is an {{< knowl id="open-ball" text="open ball" >}}. Equivalently, the balls of radius $\varepsilon$ around the chosen points form a finite {{< knowl id="cover" text="cover" >}} of $E$.

Epsilon nets are the standard way to express and work with {{< knowl id="totally-bounded-set" text="total boundedness" >}}.

**Examples:**
- For $E=[0,1]\subset\mathbb{R}$ and $\varepsilon=0.1$, the points $\{0,0.1,0.2,\dots,1\}$ form an epsilon net.
- In a discrete metric space, an epsilon net for $\varepsilon<1$ must contain every point of $E$, so such a net exists iff $E$ is finite.
