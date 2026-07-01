+++
id = "topology/open-cover"
title = "Open cover"
kind = "knowl"
summary = "A cover consisting entirely of open sets in a topological space."
aliases = ["open-cover", "Open cover"]
domains = ["topology"]
legacy_source_path = "topology/open-cover.md"
+++

An **open cover** of a subset $A\subseteq X$ in a [[topology/topological-space|topological space]] $X$ is a cover $\{U_i\}_{i\in I}$ of $A$ such that each $U_i$ is an [[topology/open-set|open set]] in $X$.
Equivalently, $A\subseteq \bigcup_{i\in I}U_i$ and every $U_i$ is open in $X$.

Open covers are the basic input to the definition of [[topology/compact-set|compactness]], and refinements of open covers are central in many “finiteness” arguments.

**Examples:**
- In $\mathbb{R}$ with the usual topology, the family $\{(n-1,n+1)\}_{n\in\mathbb{Z}}$ is an open cover of $\mathbb{R}$.
- In $\mathbb{R}$, the family $\{(-1/n,\,1+1/n)\}_{n\in\mathbb{N}}$ is an open cover of $[0,1]$.
