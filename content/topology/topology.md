---
title: "Topology"
description: "A collection of subsets declared open, closed under unions and finite intersections."
---

A **topology** on a {{< knowl id="set" section="shared-foundations" text="set" >}} $X$ is a collection $\mathcal{T}\subseteq \mathcal{P}(X)$ such that:
- $\varnothing\in\mathcal{T}$ and $X\in\mathcal{T}$,
- if $\{U_i\}_{i\in I}\subseteq\mathcal{T}$ then $\bigcup_{i\in I}U_i\in\mathcal{T}$,
- if $U,V\in\mathcal{T}$ then $U\cap V\in\mathcal{T}$.

The elements of $\mathcal{T}$ are the {{< knowl id="open-set" text="open sets" >}}, and they determine notions such as {{< knowl id="closed-set" text="closed sets" >}}, {{< knowl id="neighborhood" text="neighborhoods" >}}, {{< knowl id="interior" text="interior" >}}, {{< knowl id="closure" text="closure" >}}, and {{< knowl id="continuous-map" text="continuity" >}}. A {{< knowl id="topological-space" text="topological space" >}} is a set together with a chosen topology.

**Examples:**
- The discrete topology on $X$, given by $\mathcal{T}=\mathcal{P}(X)$.
- The indiscrete topology on $X$, given by $\mathcal{T}=\{\varnothing,X\}$.
- The {{< knowl id="metric-induced-topology" text="topology induced by a metric" >}} on a {{< knowl id="metric-space" text="metric space" >}}.
