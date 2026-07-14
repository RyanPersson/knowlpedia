---
title: "Connected set"
description: "A subset of a topological space that cannot be separated into two disjoint nonempty open parts"
---

A **connected set** is a subset $A$ of a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ such that there do not exist disjoint nonempty subsets $U,V\subseteq A$ with $A=U\cup V$ and with $U$ and $V$ {{< knowl id="open-set" section="topology-core" text="open" >}} in $A$ (with the {{< knowl id="subspace-topology" section="topology-core" text="subspace topology" >}}).

Equivalently, the only subsets of $A$ that are both open and {{< knowl id="closed-set" section="topology-core" text="closed" >}} in $A$ are $\varnothing$ and $A$ itself. Connectedness is refined by {{< knowl id="connected-component" text="connected components" >}} and strengthened by {{< knowl id="path-connected-set" text="path-connectedness" >}}; it is also preserved under {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images" >}}.

**Examples:**
- Any interval $[a,b]\subseteq \mathbb{R}$ is connected (with the usual topology).
- The unit circle $S^1\subseteq \mathbb{R}^2$ is connected.
- The set $(0,1)\cup(2,3)\subseteq \mathbb{R}$ is not connected (it splits into two disjoint nonempty open subsets in the subspace topology).
