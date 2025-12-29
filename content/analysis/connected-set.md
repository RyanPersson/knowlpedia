---
title: "Connected set"
description: "A set that cannot be decomposed into two disjoint nonempty relatively open pieces."
---

Let $(X,d)$ be a metric space and let $E\subseteq X$. A subset $U\subseteq E$ is **open in the subspace $E$** (also called **relatively open**) if there exists an open set $O\subseteq X$ such that
$$U = E\cap O.$$

The set $E$ is **connected** if there do not exist nonempty disjoint sets $U,V\subseteq E$ that are open in $E$ and satisfy
$$E = U\cup V.$$
Equivalently, the only subsets of $E$ that are both open in $E$ and closed in $E$ (i.e. **clopen** in $E$) are $\varnothing$ and $E$.

Connectedness is the topological abstraction of "being in one piece." It is fundamental for the intermediate value property and for global qualitative behavior of continuous functions.

**Examples:**
- Any interval $[a,b]\subset\mathbb{R}$ is connected.
- The set $(0,1)\cup(2,3)\subset\mathbb{R}$ is not connected.
- The unit circle $S^1=\{(x,y)\in\mathbb{R}^2:x^2+y^2=1\}$ is connected.
