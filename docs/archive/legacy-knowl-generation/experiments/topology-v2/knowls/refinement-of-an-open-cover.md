---
title: "Refinement of an open cover"
description: "A cover in which every set lies inside some member of a given open cover"
---

A **refinement** of an {{< knowl id="open-cover" text="open cover" >}} $\mathcal U$ of a set $A$ is another open cover $\mathcal V$ of $A$ such that for every $V\in\mathcal V$ there exists $U\in\mathcal U$ with $V\subseteq U$.

Refinements are a way to replace a cover by a “finer” one while keeping the same covered set, and they are commonly used in arguments about {{< knowl id="compact-set" text="compactness" >}}.

**Examples:**
- In $\mathbb R$, if $\mathcal U=\{(-2,2)\}$ covers $[-1,1]$, then $\mathcal V=\{(-1,1)\}$ is a refinement of $\mathcal U$ (and still covers $[-1,1]$).
- If $\mathcal U=\{(0,2),(1,3)\}$ covers $(1,2)$, then $\mathcal V=\{(1.2,1.8)\}$ is a refinement of $\mathcal U$ covering $(1,2)$.
