---
title: "T0 space"
description: "A topological space where distinct points can be separated by an open set."
---

A **$T_0$ space** is a {{< knowl id="topological-space" text="topological space" >}} $(X,\tau)$ such that for any two distinct points $x\neq y$ in $X$, there exists an {{< knowl id="open-set" text="open set" >}} $U\in\tau$ with either $x\in U$ and $y\notin U$, or $y\in U$ and $x\notin U$.

Equivalently, $x\neq y$ implies $\overline{\{x\}}\neq \overline{\{y\}}$, where $\overline{A}$ denotes the {{< knowl id="closure" text="closure" >}} of $A$.

The $T_0$ axiom is the weakest of the standard separation axioms: every {{< knowl id="t1-space" text="T1 space" >}} is $T_0$, and every {{< knowl id="hausdorff-space" text="Hausdorff space" >}} is $T_1$ (hence $T_0$).

**Examples:**
- **Discrete topology:** If every subset of $X$ is open, then for $x\neq y$ the set $\{x\}$ is open and contains $x$ but not $y$, so the space is $T_0$.
- **Sierpiński space:** Let $X=\{0,1\}$ with open sets $\varnothing,\{1\},X$. Then $0$ and $1$ are distinguishable (since $\{1\}$ contains $1$ but not $0$), so the space is $T_0$, but it is not $T_1$ because $\{1\}$ is not closed.
