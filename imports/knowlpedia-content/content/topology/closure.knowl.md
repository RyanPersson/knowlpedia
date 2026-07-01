+++
id = "topology/closure"
title = "Closure"
kind = "knowl"
summary = "The smallest closed set containing a given subset."
aliases = ["closure"]
domains = ["topology"]
legacy_source_path = "topology/closure.md"
+++

The **closure** of a subset $A\subseteq X$ in a [[topology/topological-space|topological space]] $(X,\mathcal{T})$ is
\[
\overline{A}=\bigcap\{F\subseteq X : F \text{ is a closed set and } A\subseteq F\}.
\]
Equivalently, a point $x\in X$ lies in $\overline{A}$ if and only if every [[topology/neighborhood|neighborhood]] of $x$ intersects $A$.

A set $F$ is [[topology/closed-set|closed]] exactly when $F=\overline{F}$. Closure is closely tied to [[topology/limit-point|limit points]] and the [[topology/derived-set|derived set]].

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\overline{(0,1)}=[0,1]$.
- In $\mathbb{R}$ with the usual topology, $\overline{\mathbb{Q}}=\mathbb{R}$.
- $\overline{\varnothing}=\varnothing$ in any topological space.
