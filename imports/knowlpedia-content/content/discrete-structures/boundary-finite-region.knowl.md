+++
id = "discrete-structures/boundary-finite-region"
title = "Boundary of a finite region"
kind = "knowl"
summary = "Standard notions of boundary for a finite subset of a graph or lattice."
aliases = ["boundary-finite-region", "Boundary of a finite region"]
domains = ["discrete-structures"]
legacy_source_path = "discrete-structures/boundary-finite-region.md"
+++

Let \(\Lambda\) be a finite subset of vertices in a graph. In the lattice setting, take \(\Lambda\subset \mathbb{Z}^d\) with adjacency given by [[discrete-structures/nearest-neighbor-zd|nearest-neighbor-zd]].

Write \(x\sim y\) if \(x\) and \(y\) are adjacent.

**Outer (external) vertex boundary.** The **outer boundary** of \(\Lambda\) is
\[
\partial \Lambda := \{y\notin \Lambda : \exists x\in \Lambda \text{ such that } x\sim y\}.
\]
These are the vertices outside \(\Lambda\) that are one step away from \(\Lambda\).

**Inner (internal) vertex boundary.** The **inner boundary** is
\[
\partial^{-}\Lambda := \{x\in \Lambda : \exists y\notin \Lambda \text{ such that } x\sim y\}.
\]
These are the vertices inside \(\Lambda\) that have at least one neighbor outside.

**Edge boundary.** The **edge boundary** (also called the set of **cut edges**) is
\[
\delta \Lambda := \{\{x,y\} : x\in \Lambda,\ y\notin \Lambda,\ x\sim y\}.
\]

Different authors may use different boundary conventions (vertex vs. edge boundary, inner vs. outer), so it is good practice to check which version is intended in a given argument.
