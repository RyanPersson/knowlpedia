---
title: "Infimum"
description: "The greatest lower bound of a nonempty set of real numbers."
---

An **infimum** of a nonempty set $A\subseteq\mathbb R$ that is {{< knowl id="bounded-below" text="bounded below" >}} is a real number $t\in\mathbb R$ such that:
1. $t$ is a lower bound of $A$ (i.e., $t\le x$ for all $x\in A$), and
2. for every lower bound $\ell$ of $A$, one has $\ell\le t$.

The infimum is the “greatest lower bound” and may exist even when $A$ has no {{< knowl id="minimum" text="minimum" >}}. Using the {{< knowl id="completeness-axiom" text="completeness axiom" >}}, every nonempty bounded-below set of real numbers has an infimum.

**Examples:**
- If $A=(0,1)$, then $\inf A=0$.
- If $A=\{\tfrac1n : n\in\mathbb N\}$, then $\inf A=0$ (even though $0\notin A$).
