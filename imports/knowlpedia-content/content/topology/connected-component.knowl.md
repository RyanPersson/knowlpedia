+++
id = "topology/connected-component"
title = "Connected component"
kind = "knowl"
summary = "A maximal connected subset of a topological space."
aliases = ["connected-component", "Connected component"]
domains = ["topology"]
legacy_source_path = "topology/connected-component.md"
+++

A **connected component** of a [[topology/topological-space|topological space]] $X$ is a maximal [[topology/connected-set|connected set]] (with respect to inclusion). Concretely, for a point $x\in X$, its connected component is
\[
C(x)=\bigcup\{\,C\subseteq X : C \text{ is connected and } x\in C\,\},
\]
and $C(x)$ is the largest connected subset of $X$ containing $x$.

Connected components give a canonical decomposition of $X$ into connected pieces; compare this with [[topology/path-connected-set|path-connectedness]], which uses [[topology/path|paths]].

**Examples:**
- In $\mathbb{R}\setminus\{0\}$ (usual topology), the connected components are $(-\infty,0)$ and $(0,\infty)$.
- In a discrete topological space, every singleton $\{x\}$ is a connected component.
