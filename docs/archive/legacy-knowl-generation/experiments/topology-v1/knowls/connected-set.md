---
title: "Connected set"
description: "A subset of a topological space that cannot be split into two nonempty separated open pieces"
---

A **connected set** is a subset $A$ of a {{< knowl id="topological-space" text="topological space" >}} $X$ such that there do not exist disjoint nonempty subsets $U,V\subseteq A$ with $A$ equal to the {{< knowl id="union" text="union" >}} of $U$ and $V$, where $U$ and $V$ are {{< knowl id="open-set" text="open" >}} in the {{< knowl id="subspace-topology" text="subspace topology" >}} on $A$.

Equivalently, $A$ is connected iff it cannot be written as a union of two nonempty {{< knowl id="separated-sets" text="separated" >}} subsets; equivalently, the only subsets of $A$ that are both {{< knowl id="closed-set" text="closed" >}} and open (in the subspace topology) are $A$ and the {{< knowl id="empty-set" text="empty set" >}}.

**Examples:**
- In the real line with its usual topology, any interval such as $(0,1)$ or $[0,1]$ is connected.
- The subset $\{0,1\}\subseteq \mathbb{R}$ is not connected: it splits into two disjoint nonempty open subsets in the subspace topology.
- Every singleton subset of any topological space is connected (and, by convention, so is the empty set).
