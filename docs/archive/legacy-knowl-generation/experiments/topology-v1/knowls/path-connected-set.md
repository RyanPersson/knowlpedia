---
title: "Path-connected set"
description: "A set in which any two points can be joined by a continuous path"
---

A subset $A$ of a {{< knowl id="topological-space" text="topological space" >}} $X$ is **path-connected** if, for every $x,y\in A$, there exists a {{< knowl id="path" text="path" >}} $\gamma:[0,1]\to A$ that is continuous for the {{< knowl id="subspace-topology" text="subspace topology" >}} on $A$ and satisfies $\gamma(0)=x$ and $\gamma(1)=y$.

Every path-connected set is {{< knowl id="connected-set" text="connected" >}}. The converse can fail in general topological spaces, so path connectedness is a stronger condition than connectedness.

**Examples:**
- Any interval in the real line is path-connected (join two points by the straight-line path).
- The set $(0,1)\cup(2,3)\subseteq\mathbb{R}$ is not path-connected (no path can cross the gap).
- In a discrete topological space, the path-connected subsets are exactly the singletons (and the empty set).
