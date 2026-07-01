+++
id = "topology/limit-point"
title = "Limit point"
kind = "knowl"
summary = "A point whose every neighborhood meets a set away from that point."
aliases = ["limit-point", "Limit point"]
domains = ["topology"]
legacy_source_path = "topology/limit-point.md"
+++

A **limit point** (or accumulation point) of a subset $A\subseteq X$ in a [[topology/topological-space|topological space]] is a point $x\in X$ such that every [[topology/neighborhood|neighborhood]] $N$ of $x$ satisfies
\[
(N\cap (A\setminus\{x\}))\neq\varnothing.
\]

The set of all limit points of $A$ is the [[topology/derived-set|derived set]] of $A$. Limit points also describe [[topology/closure|closure]] via the identity $\overline{A}=A\cup A'$.

**Examples:**
- In $\mathbb{R}$, $0$ is a limit point of the set $\{1/n : n\in\mathbb{N}\}$.
- In $\mathbb{R}$, every point of $(0,1)$ is a limit point of $(0,1)$.
- In a discrete topological space, no subset has a limit point (every point has a singleton neighborhood).
