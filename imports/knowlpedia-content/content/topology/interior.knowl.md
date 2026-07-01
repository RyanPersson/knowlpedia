+++
id = "topology/interior"
title = "Interior"
kind = "knowl"
summary = "The largest open set contained in a given subset."
aliases = ["interior"]
domains = ["topology"]
legacy_source_path = "topology/interior.md"
+++

The **interior** of a subset $A\subseteq X$ in a [[topology/topological-space|topological space]] $(X,\mathcal{T})$ is
\[
\operatorname{int}(A)=\bigcup\{U\in\mathcal{T}: U\subseteq A\}.
\]
Equivalently, $\operatorname{int}(A)$ is the largest [[topology/open-set|open set]] contained in $A$.

A point $x$ lies in $\operatorname{int}(A)$ exactly when $A$ is a [[topology/neighborhood|neighborhood]] of $x$. Interior is dual to [[topology/closure|closure]] via complements: $\operatorname{int}(A)=X\setminus \overline{X\setminus A}$.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\operatorname{int}([0,1])=(0,1)$.
- In $\mathbb{R}$ with the usual topology, $\operatorname{int}(\mathbb{Q})=\varnothing$.
- If $U$ is open, then $\operatorname{int}(U)=U$.
