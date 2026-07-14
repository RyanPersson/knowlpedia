---
title: "Path-connected set"
description: "A subset in which every pair of points can be joined by a continuous path"
---

A **path-connected set** is a subset $A$ of a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ such that for every $x,y\in A$ there exists a {{< knowl id="path" text="path" >}} $\gamma:[0,1]\to A$ with $\gamma(0)=x$ and $\gamma(1)=y$ (where $A$ carries the {{< knowl id="subspace-topology" section="topology-core" text="subspace topology" >}}).

Path-connectedness implies {{< knowl id="connected-set" text="connectedness" >}} (so each path-connected set lies in a single {{< knowl id="connected-component" text="connected component" >}}), but the converse can fail in general topological spaces.

**Examples:**
- Any interval in $\mathbb{R}$ is path-connected.
- The circle $S^1\subseteq \mathbb{R}^2$ is path-connected.
- The set $(0,1)\cup(2,3)\subseteq \mathbb{R}$ is not path-connected (there is no path joining a point in $(0,1)$ to a point in $(2,3)$).
