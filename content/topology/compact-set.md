---
title: "Compact set"
description: "A set in which every open cover has a finite subcover."
---

A **compact set** is a subset $K\subseteq X$ of a {{< knowl id="topological-space" text="topological space" >}} $X$ such that every {{< knowl id="open-cover" text="open cover" >}} of $K$ contains a finite subcover: whenever $\{U_i\}_{i\in I}$ is a family of open sets with $K\subseteq \bigcup_{i\in I}U_i$, there exist indices $i_1,\dots,i_n$ such that
\[
K \subseteq U_{i_1}\cup\cdots\cup U_{i_n}.
\]

Compactness can also be expressed in terms of {{< knowl id="finite-intersection-property" text="the finite intersection property" >}} for families of {{< knowl id="closed-set" text="closed sets" >}}, and it interacts well with {{< knowl id="continuous-map" text="continuous maps" >}} (for instance, via {{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous images of compact sets" >}}).

**Examples:**
- Any finite subset of any topological space is compact.
- In $\mathbb{R}$ with its usual topology, the closed interval $[0,1]$ is compact, while the open interval $(0,1)$ is not compact.
