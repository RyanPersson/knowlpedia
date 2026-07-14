---
title: "Closed subset of compact set is compact"
description: "A closed subset of a compact set is compact in the subspace topology"
---

**Closed subset of compact set is compact**: Let $K$ be a {{< knowl id="compact-set" text="compact set" >}} in a topological space $X$, and let $F\subseteq K$ be {{< knowl id="closed-set" text="closed" >}} (in $X$, equivalently in $K$ with the {{< knowl id="subspace-topology" text="subspace topology" >}}). Then $F$ is compact.

**Proof sketch**: Let $\mathcal{U}$ be an {{< knowl id="open-cover" text="open cover" >}} of $F$ (by open sets in the subspace). Add the open set $X\setminus F$ to get an open cover of $K$. By compactness of $K$, extract a finite subcover; removing $X\setminus F$ leaves a finite subcover of $F$.

**Examples:**
- Since $[0,1]$ is compact in $\mathbb{R}$, any closed subset such as $\{0\}$ or $[1/3,2/3]$ is compact.
- If $K$ is compact, then $K\cap C$ is compact for any closed set $C$ in the ambient space.
