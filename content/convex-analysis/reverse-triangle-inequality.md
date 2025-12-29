---
title: "Reverse triangle inequality"
description: "The norm difference is bounded by the norm of the difference"
---

**Proposition (Reverse triangle inequality).**
In a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} $(X,\|\cdot\|)$, for all $x,y\in X$,
$$
\big|\|x\|-\|y\|\big|\le \|x-y\|.
$$

**Context.** This inequality is a key tool for showing that norm convergence implies convergence of norms and for proving continuity of the norm mapping.

**Proof sketch.** From the triangle inequality,
$$
\|x\|=\|(x-y)+y\|\le \|x-y\|+\|y\|\quad\Rightarrow\quad \|x\|-\|y\|\le \|x-y\|.
$$
Swap $x$ and $y$ to get $\|y\|-\|x\|\le \|x-y\|$, and combine both.
