---
title: "Random variable"
description: "A measurable real-valued function on a probability space."
---

A **random variable** is a {{< knowl id="measurable-function" section="measure-theory" text="measurable function" >}} $X:(\Omega,\mathcal{F})\to(\mathbb{R},\mathcal{B}(\mathbb{R}))$ defined on a {{< knowl id="probability-space" text="probability space" >}} $(\Omega,\mathcal{F},\mathbb{P})$, meaning that for every Borel set $B\subseteq\mathbb{R}$ one has $X^{-1}(B)\in\mathcal{F}$.

A random variable induces a {{< knowl id="distribution-law" text="distribution (law)" >}} on {{< knowl id="real-numbers" section="shared-foundations" text="the real numbers" >}} via $\mathbb{P}_X(B)=\mathbb{P}(X\in B)$, and quantities such as {{< knowl id="expectation" text="expectation" >}} and {{< knowl id="variance" text="variance" >}} are defined from this law.

**Examples:**
- For an event $A\in\mathcal{F}$, the indicator $X=\mathbf{1}_A$ (equal to $1$ on $A$ and $0$ on $A^c$) is a random variable.
- In a fair coin toss space, the function $X(H)=1$ and $X(T)=0$ is a random variable taking values in $\{0,1\}$.
