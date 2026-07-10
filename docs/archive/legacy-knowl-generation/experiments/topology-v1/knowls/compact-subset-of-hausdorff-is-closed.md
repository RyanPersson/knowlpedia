---
title: "Compact subset of Hausdorff is closed"
description: "In a Hausdorff space, every compact subset is closed"
---

**Compact subset of Hausdorff is closed**: If $X$ is a {{< knowl id="hausdorff-space" text="Hausdorff space" >}} and $K\subseteq X$ is {{< knowl id="compact-set" text="compact" >}}, then $K$ is {{< knowl id="closed-set" text="closed" >}} in $X$.

**Proof sketch**: Fix $x\in X\setminus K$. For each $y\in K$, Hausdorffness gives disjoint open sets separating $x$ and $y$, so choose an open neighborhood $U_y$ of $y$ with $x\notin \overline{U_y}$ (equivalently, find disjoint neighborhoods of $x$ and $y$). The sets $\{U_y\}_{y\in K}$ form an {{< knowl id="open-cover" text="open cover" >}} of $K$, so compactness yields a finite subcover $U_{y_1},\dots,U_{y_n}$. Intersect the corresponding neighborhoods of $x$ to obtain an open set containing $x$ and disjoint from $K$. Thus $X\setminus K$ is open, hence $K$ is closed.

**Examples:**
- In $\mathbb{R}^n$, every compact set is closed.
- In a non-Hausdorff space, compact sets need not be closed (showing the separation hypothesis is genuinely needed).
