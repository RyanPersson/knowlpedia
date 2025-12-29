---
title: "Compact set"
description: "A set for which every open cover has a finite subcover."
---

Let $(X,d)$ be a metric space and let $K\subseteq X$. The set $K$ is **compact** if for every family of open sets $\{U_i\}_{i\in I}$ in $X$ such that
$$K\subseteq \bigcup_{i\in I} U_i,$$
there exist finitely many indices $i_1,\dots,i_N\in I$ such that
$$K\subseteq U_{i_1}\cup\cdots\cup U_{i_N}.$$

Compactness is a finiteness condition on the topology. In analysis it is the hypothesis behind uniform continuity (Heine–Cantor), attainment of extrema (Extreme Value Theorem), and many extraction arguments (existence of convergent subsequences).

**Examples:**
- In $\mathbb{R}$ with the usual metric, $[a,b]$ is compact.
- In $\mathbb{R}^k$, every closed ball $\overline{B}(0,R)$ is compact (Heine–Borel).
- The open interval $(0,1)\subset\mathbb{R}$ is not compact (cover it by $(0,1-\tfrac1n)$ for $n\ge 2$; no finite subcover).
