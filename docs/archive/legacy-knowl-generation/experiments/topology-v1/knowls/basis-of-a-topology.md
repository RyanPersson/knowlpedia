---
title: "Basis of a topology"
description: "A collection of sets whose unions form all open sets."
---

Let $X$ be a set. A **basis** for a topology on $X$ is a collection $\mathcal{B}$ of subsets of $X$ such that:
1. For every $x\in X$, there exists $B\in\mathcal{B}$ with $x\in B$.
2. If $x\in B_1\cap B_2$ for $B_1,B_2\in\mathcal{B}$, then there exists $B_3\in\mathcal{B}$ with $x\in B_3\subseteq B_1\cap B_2$.

Given such $\mathcal{B}$, the {{< knowl id="topology" text="topology" >}} it generates consists of all {{< knowl id="union" text="unions" >}} of elements of $\mathcal{B}$; those are exactly the {{< knowl id="open-set" text="open sets" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual topology, the open intervals form a basis.
- In a {{< knowl id="metric-space" text="metric space" >}}, the family of {{< knowl id="open-ball" text="open balls" >}} is a basis for the metric-induced topology.
