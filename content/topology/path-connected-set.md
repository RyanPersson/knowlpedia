---
title: "Path-connected set"
description: "A set in which any two points can be joined by a continuous path lying in the set."
---

A **path-connected set** is a subset $A\subseteq X$ of a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for any $x,y\in A$ there exists a {{< knowl id="path" text="path" >}} $\gamma\colon [0,1]\to X$ with $\gamma(0)=x$, $\gamma(1)=y$, and $\gamma([0,1])\subseteq A$.

Path-connectedness is stronger than {{< knowl id="connected-set" text="connectedness" >}} (every path-connected set is connected), and it leads to a decomposition of spaces into “path components,” analogous to {{< knowl id="connected-component" text="connected components" >}}.

**Examples:**
- Any {{< knowl id="interval" section="real-analysis" text="interval" >}} in $\mathbb{R}$ is path-connected, and more generally any convex subset of $\mathbb{R}^n$ is path-connected.
- The set $(-1,0)\cup(0,1)\subseteq\mathbb{R}$ is not path-connected.
