+++
id = "topology/topological-space"
title = "Topological space"
kind = "knowl"
summary = "A set equipped with a topology, specifying which subsets are open."
aliases = ["topological-space", "Topological space"]
domains = ["topology"]
legacy_source_path = "topology/topological-space.md"
+++

A **topological space** is an [[shared-foundations/ordered-pair|ordered pair]] $(X,\mathcal{T})$ where $X$ is a [[shared-foundations/set|set]] and $\mathcal{T}\subseteq \mathcal{P}(X)$ is a [[topology/topology|topology]] on $X$, meaning:
- $\varnothing\in\mathcal{T}$ and $X\in\mathcal{T}$,
- if $\{U_i\}_{i\in I}\subseteq\mathcal{T}$ then $\bigcup_{i\in I}U_i\in\mathcal{T}$,
- if $U,V\in\mathcal{T}$ then $U\cap V\in\mathcal{T}$.

Here $\mathcal{P}(X)$ denotes the [[shared-foundations/power-set|power set]] of $X$, and the members of $\mathcal{T}$ are the [[topology/open-set|open sets]] (whose complements are the [[topology/closed-set|closed sets]]). Many standard constructions—such as the [[topology/subspace-topology|subspace topology]], [[topology/product-topology|product topology]], and [[topology/quotient-topology|quotient topology]]—produce new topological spaces from existing ones.

**Examples:**
- $\mathbb{R}$ with its usual topology (open sets are unions of open intervals).
- Any set $X$ with the discrete topology $\mathcal{T}=\mathcal{P}(X)$.
- Any [[topology/metric-space|metric space]] $(X,d)$, using the [[topology/metric-induced-topology|topology induced by the metric]].
