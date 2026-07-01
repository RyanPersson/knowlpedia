+++
id = "topology/path-connected-set"
title = "Path-connected set"
kind = "knowl"
summary = "A set in which any two points can be joined by a continuous path lying in the set."
aliases = ["path-connected-set", "Path-connected set"]
domains = ["topology"]
legacy_source_path = "topology/path-connected-set.md"
+++

A **path-connected set** is a subset $A\subseteq X$ of a [[topology/topological-space|topological space]] $X$ such that for any $x,y\in A$ there exists a [[topology/path|path]] $\gamma\colon [0,1]\to X$ with $\gamma(0)=x$, $\gamma(1)=y$, and $\gamma([0,1])\subseteq A$.

Path-connectedness is stronger than [[topology/connected-set|connectedness]] (every path-connected set is connected), and it leads to a decomposition of spaces into “path components,” analogous to [[topology/connected-component|connected components]].

**Examples:**
- Any [[real-analysis/interval|interval]] in $\mathbb{R}$ is path-connected, and more generally any convex subset of $\mathbb{R}^n$ is path-connected.
- The set $(-1,0)\cup(0,1)\subseteq\mathbb{R}$ is not path-connected.
