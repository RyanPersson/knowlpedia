---
title: "Indicator function"
description: "A function that equals 1 on a set and 0 outside it."
---

An **indicator function** of a subset $A\subseteq X$ is the function $\mathbf 1_A:X\to\{0,1\}$ defined by $\mathbf 1_A(x)=1$ for $x\in A$ and $\mathbf 1_A(x)=0$ for $x\notin A$.

Indicator functions translate set operations into algebraic ones and are the basic building blocks of {{< knowl id="simple-function" text="simple functions" >}}. In a {{< knowl id="measurable-space" text="measurable space" >}} $(X,\Sigma)$, $\mathbf 1_A$ is {{< knowl id="measurable-function" text="measurable" >}} exactly when $A$ is a {{< knowl id="measurable-set" text="measurable set" >}} (with $\{0,1\}$ carrying its power-set sigma-algebra).

**Examples:**
- On $(\mathbb R,\mathcal B(\mathbb R))$, the indicator function $\mathbf 1_{(0,1)}$ of the open {{< knowl id="interval" section="real-analysis" text="interval" >}} $(0,1)$ is measurable.
- If $N$ is a {{< knowl id="null-set" text="null set" >}} in a measure space, then $\mathbf 1_N$ equals $0$ {{< knowl id="almost-everywhere" text="almost everywhere" >}}.
