---
title: "Connected component"
description: "A maximal connected subset of a topological space."
---

A **connected component** of a {{< knowl id="topological-space" text="topological space" >}} $X$ is a maximal {{< knowl id="connected-set" text="connected set" >}} (with respect to inclusion). Concretely, for a point $x\in X$, its connected component is
\[
C(x)=\bigcup\{\,C\subseteq X : C \text{ is connected and } x\in C\,\},
\]
and $C(x)$ is the largest connected subset of $X$ containing $x$.

Connected components give a canonical decomposition of $X$ into connected pieces; compare this with {{< knowl id="path-connected-set" text="path-connectedness" >}}, which uses {{< knowl id="path" text="paths" >}}.

**Examples:**
- In $\mathbb{R}\setminus\{0\}$ (usual topology), the connected components are $(-\infty,0)$ and $(0,\infty)$.
- In a discrete topological space, every singleton $\{x\}$ is a connected component.
