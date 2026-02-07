---
title: "Separated sets"
description: "Two sets in a topological space that do not meet each other's closure."
---

Two **separated sets** $A$ and $B$ in a {{< knowl id="topological-space" text="topological space" >}} $X$ are subsets such that
\[
A\cap \overline{B}=\varnothing
\quad\text{and}\quad
\overline{A}\cap B=\varnothing,
\]
where $\overline{A}$ and $\overline{B}$ denote {{< knowl id="closure" text="closures" >}} in $X$.

Separatedness is the key notion used to define {{< knowl id="connected-set" text="connectedness" >}}: a space is disconnected exactly when it can be written as a union of two nonempty separated sets.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $A=(0,1)$ and $B=(1,2)$ are separated.
- In $\mathbb{R}$, the rationals $\mathbb{Q}$ and the irrationals $\mathbb{R}\setminus\mathbb{Q}$ are not separated, since each is dense and has closure $\mathbb{R}$.
