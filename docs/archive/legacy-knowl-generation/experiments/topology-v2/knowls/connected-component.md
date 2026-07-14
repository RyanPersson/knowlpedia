---
title: "Connected component"
description: "A maximal connected subset containing a given point, forming an equivalence class"
---

A **connected component** of a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ is a subset $C\subseteq X$ that is {{< knowl id="connected-set" text="connected" >}} and maximal with respect to inclusion among connected subsets of $X$.

Equivalently, for a point $x\in X$, the connected component of $x$ is the {{< knowl id="union" section="shared-foundations" text="union" >}} of all connected subsets of $X$ that contain $x$. The relation “$x$ and $y$ lie in a common connected subset” is an {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}}, and the connected components are its {{< knowl id="equivalence-class" section="shared-foundations" text="equivalence classes" >}} (hence they form a {{< knowl id="partition" section="shared-foundations" text="partition" >}} of $X$).

**Examples:**
- In $\mathbb{R}\setminus\{0\}$ (usual topology), the connected components are $(-\infty,0)$ and $(0,\infty)$.
- In a discrete space, every singleton $\{x\}$ is a connected component.
- If $X$ is the disjoint union of two circles in $\mathbb{R}^2$, each circle is a connected component of $X$.
