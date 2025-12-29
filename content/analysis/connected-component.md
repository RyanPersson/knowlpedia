---
title: "Connected component"
description: "A maximal connected subset containing a given point."
---

Let $(X,d)$ be a metric space and let $E\subseteq X$. For $x\in E$, the **connected component** of $x$ in $E$ is the set
$$C_E(x):=\bigcup\{A\subseteq E : A\ \text{is connected and}\ x\in A\}.$$

Equivalently, $C_E(x)$ is the unique maximal (by inclusion) connected subset of $E$ that contains $x$. Connected components partition $E$ into disjoint connected pieces.

**Examples:**
- If $E=(0,1)\cup(2,3)\subset\mathbb{R}$, then there are two connected components: $(0,1)$ and $(2,3)$.
- If $E=\mathbb{Q}\subset\mathbb{R}$ with the subspace topology, then every connected component is a singleton $\{q\}$ (since $\mathbb{Q}$ is totally disconnected).
- If $E$ is connected, then it has exactly one connected component, namely $E$ itself.
