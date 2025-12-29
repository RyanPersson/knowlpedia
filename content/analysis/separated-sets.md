---
title: "Separated sets"
description: "Two sets A,B are separated if neither meets the closure of the other."
---

Let $(X,d)$ be a metric space and let $A,B\subseteq X$. The sets $A$ and $B$ are **separated** if
$$\overline{A}\cap B=\varnothing \quad\text{and}\quad A\cap \overline{B}=\varnothing.$$

Separatedness is a symmetric condition stronger than disjointness: it requires each set to have a neighborhood that misses the other in a closure sense. Separations are a standard way to characterize disconnectedness.

**Examples:**
- In $\mathbb{R}$, the sets $A=(0,1)$ and $B=(2,3)$ are separated since $\overline{A}=[0,1]$ and $\overline{B}=[2,3]$ are disjoint.
- In $\mathbb{R}$, the sets $A=(0,1)$ and $B=(1,2)$ are disjoint but not separated, because $\overline{A}\cap B$ contains points arbitrarily close to $1$ (indeed $1\in\overline{A}$ and $1\in\overline{B}$).
- If $A$ and $B$ are separated then $A\cap B=\varnothing$ (take $A\cap \overline{B}=\varnothing$ and note $B\subseteq \overline{B}$).
