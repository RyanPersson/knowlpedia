+++
id = "topology/finite-intersection-property"
title = "Finite intersection property"
kind = "knowl"
summary = "A property of a family of sets where every finite subfamily has nonempty intersection."
aliases = ["finite-intersection-property", "Finite intersection property"]
domains = ["topology"]
legacy_source_path = "topology/finite-intersection-property.md"
+++

A family $\mathcal F$ of subsets of a set $X$ has the **finite intersection property** if for every finite choice $F_1,\dots,F_n\in\mathcal F$ one has
\[
F_1\cap\cdots\cap F_n \neq \varnothing,
\]
where $\varnothing$ is the [[shared-foundations/empty-set|empty set]].

In topology, the finite intersection property is especially useful for families of [[topology/closed-set|closed sets]]: [[topology/compact-set|compactness]] can be characterized by requiring that every family of closed sets with this property has nonempty total intersection.

**Examples:**
- In $\mathbb{R}$, the family $F_n=[n,\infty)$ has the finite intersection property (any finite intersection is nonempty), but $\bigcap_{n\ge 1}F_n=\varnothing$.
- In a set $X=\{1,2,3,4\}$, the family $\{\{1,2\},\{2,3\},\{2,4\}\}$ has the finite intersection property, since every finite intersection contains $2$.
