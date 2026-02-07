---
title: "Identity function"
description: "The function that maps every element of a set to itself"
---

An **identity function** on a set $A$ is the {{< knowl id="function" text="function" >}} $\mathrm{id}_A:A\to A$ defined by
$$
\mathrm{id}_A(a)=a\quad\text{for all }a\in A.
$$

Identity functions are neutral elements for {{< knowl id="composition" text="composition" >}}: if $f:A\to B$ is any function, then $f\circ \mathrm{id}_A=f$ and $\mathrm{id}_B\circ f=f$. The identity function is always {{< knowl id="bijective-function" text="bijective" >}}, and its {{< knowl id="inverse-function" text="inverse function" >}} is itself.

**Examples:**
- On {{< knowl id="real-numbers" text="the real numbers" >}}, $\mathrm{id}_{\mathbb{R}}(x)=x$ for all $x\in\mathbb{R}$.
- On the {{< knowl id="power-set" text="power set" >}} $\mathcal{P}(A)$ of a set $A$, the identity function sends each subset $S\subseteq A$ to itself.
