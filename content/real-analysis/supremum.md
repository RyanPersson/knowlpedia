---
title: "Supremum"
description: "The least upper bound of a nonempty set of real numbers."
---

A **supremum** of a nonempty set $A\subseteq\mathbb R$ that is {{< knowl id="bounded-above" text="bounded above" >}} is a real number $s\in\mathbb R$ such that:
1. $s$ is an upper bound of $A$ (i.e., $x\le s$ for all $x\in A$), and
2. for every upper bound $u$ of $A$, one has $s\le u$.

The supremum is the “least upper bound” and may exist even when $A$ has no {{< knowl id="maximum" text="maximum" >}}. The {{< knowl id="completeness-axiom" text="completeness axiom" >}} asserts that every nonempty bounded-above set of real numbers has a supremum.

**Examples:**
- If $A=(0,1)$, then $\sup A=1$.
- If $A=\{1-\tfrac1n : n\in\mathbb N\}$, then $\sup A=1$ (even though $1\notin A$).
