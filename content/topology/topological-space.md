---
title: "Topological space"
description: "A set equipped with a topology, specifying which subsets are open."
---

A **topological space** is an {{< knowl id="ordered-pair" section="shared-foundations" text="ordered pair" >}} $(X,\mathcal{T})$ where $X$ is a {{< knowl id="set" section="shared-foundations" text="set" >}} and $\mathcal{T}\subseteq \mathcal{P}(X)$ is a {{< knowl id="topology" text="topology" >}} on $X$, meaning:
- $\varnothing\in\mathcal{T}$ and $X\in\mathcal{T}$,
- if $\{U_i\}_{i\in I}\subseteq\mathcal{T}$ then $\bigcup_{i\in I}U_i\in\mathcal{T}$,
- if $U,V\in\mathcal{T}$ then $U\cap V\in\mathcal{T}$.

Here $\mathcal{P}(X)$ denotes the {{< knowl id="power-set" section="shared-foundations" text="power set" >}} of $X$, and the members of $\mathcal{T}$ are the {{< knowl id="open-set" text="open sets" >}} (whose complements are the {{< knowl id="closed-set" text="closed sets" >}}). Many standard constructions—such as the {{< knowl id="subspace-topology" text="subspace topology" >}}, {{< knowl id="product-topology" text="product topology" >}}, and {{< knowl id="quotient-topology" text="quotient topology" >}}—produce new topological spaces from existing ones.

**Examples:**
- $\mathbb{R}$ with its usual topology (open sets are unions of open intervals).
- Any set $X$ with the discrete topology $\mathcal{T}=\mathcal{P}(X)$.
- Any {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, using the {{< knowl id="metric-induced-topology" text="topology induced by the metric" >}}.
