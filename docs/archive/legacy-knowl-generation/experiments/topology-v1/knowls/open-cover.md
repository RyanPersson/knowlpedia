---
title: "Open cover"
description: "A collection of open sets whose union contains a given set"
---

An **open cover** of a set $A$ in a {{< knowl id="topological-space" text="topological space" >}} $X$ is a {{< knowl id="cover" text="cover" >}} $\mathcal{U}$ of {{< knowl id="open-set" text="open sets" >}} such that
$$
A \subseteq \bigcup_{U\in\mathcal{U}} U.
$$
Equivalently, the {{< knowl id="union" text="union" >}} of the sets in $\mathcal{U}$ contains $A$.

Open covers are the basic input for the definition of {{< knowl id="compact-set" text="compactness" >}}. In a {{< knowl id="metric-space" text="metric space" >}}, many natural open covers come from families of {{< knowl id="open-ball" text="open balls" >}}.

**Examples:**
- In {{< knowl id="euclidean-space" text="Euclidean space" >}} $\mathbb{R}$, the family $\{(-1/n,\,1+1/n)\}_{n\in\mathbb{N}}$ is an open cover of $[0,1]$.
- In any topological space $X$, the single set $\{X\}$ is an open cover of $X$ (and of any subset $A\subseteq X$).
