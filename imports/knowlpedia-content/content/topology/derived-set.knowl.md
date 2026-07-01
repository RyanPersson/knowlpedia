+++
id = "topology/derived-set"
title = "Derived set"
kind = "knowl"
summary = "The set of all limit points of a subset."
aliases = ["derived-set", "Derived set"]
domains = ["topology"]
legacy_source_path = "topology/derived-set.md"
+++

The **derived set** of a subset $A\subseteq X$ in a [[topology/topological-space|topological space]] is the set
\[
A'=\{x\in X : x \text{ is a limit point of } A\},
\]
where “limit point” is as in [[topology/limit-point|limit point]].

The derived set records the accumulation behavior of $A$, and it satisfies the basic relationship with [[topology/closure|closure]]:
\[
\overline{A}=A\cup A'.
\]

**Examples:**
- In $\mathbb{R}$, if $A=\{1/n : n\in\mathbb{N}\}$ then $A'=\{0\}$.
- In $\mathbb{R}$, if $A=\mathbb{Z}$ then $A'=\varnothing$.
- In $\mathbb{R}$, if $A=(0,1)$ then $A'=[0,1]$.
