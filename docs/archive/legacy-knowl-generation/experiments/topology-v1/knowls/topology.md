---
title: "Topology"
description: "A collection of subsets closed under unions and finite intersections."
---

A **topology** on a {{< knowl id="set" text="set" >}} $X$ is a collection $\tau$ of {{< knowl id="subset" text="subsets" >}} of $X$ such that:
- $\varnothing \in \tau$ and $X \in \tau$,
- if $\{U_i\}_{i\in I}\subseteq \tau$, then $\bigcup_{i\in I} U_i\in \tau$,
- if $U,V\in \tau$, then $U\cap V\in \tau$.

The members of $\tau$ are called {{< knowl id="open-set" text="open sets" >}}, and the pair $(X,\tau)$ is a {{< knowl id="topological-space" text="topological space" >}}.

**Examples:**
- **Discrete topology:** every subset of $X$ is open.
- **Indiscrete topology:** only $\varnothing$ and $X$ are open.
- For a {{< knowl id="metric-space" text="metric space" >}}, the open balls generate the {{< knowl id="metric-induced-topology" text="usual topology coming from the metric" >}}.
