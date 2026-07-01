+++
id = "topology/compact-set"
title = "Compact set"
kind = "knowl"
summary = "A set in which every open cover has a finite subcover."
aliases = ["compact-set", "Compact set"]
domains = ["topology"]
legacy_source_path = "topology/compact-set.md"
+++

A **compact set** is a subset $K\subseteq X$ of a [[topology/topological-space|topological space]] $X$ such that every [[topology/open-cover|open cover]] of $K$ contains a finite subcover: whenever $\{U_i\}_{i\in I}$ is a family of open sets with $K\subseteq \bigcup_{i\in I}U_i$, there exist indices $i_1,\dots,i_n$ such that
\[
K \subseteq U_{i_1}\cup\cdots\cup U_{i_n}.
\]

Compactness can also be expressed in terms of [[topology/finite-intersection-property|the finite intersection property]] for families of [[topology/closed-set|closed sets]], and it interacts well with [[topology/continuous-map|continuous maps]] (for instance, via [[topology/continuous-image-of-compact-set-is-compact|continuous images of compact sets]]).

**Examples:**
- Any finite subset of any topological space is compact.
- In $\mathbb{R}$ with its usual topology, the closed interval $[0,1]$ is compact, while the open interval $(0,1)$ is not compact.
