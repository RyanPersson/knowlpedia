---
title: "Characteristic function (indicator function)"
description: "The function that records membership in a set by 0/1 values."
---

Let $X$ be a set and let $A\subseteq X$. The **characteristic function** (or **indicator function**) of $A$ is the function $\mathbf{1}_A:X\to\{0,1\}$ defined by
$$
\mathbf{1}_A(x):=
\begin{cases}
1,& x\in A,\\
0,& x\notin A.
\end{cases}
$$

Indicator functions convert set membership questions into algebraic statements and are a standard device in integration and measure theory (e.g., simple functions are finite linear combinations of indicators).

**Examples:**
- If $X=\mathbb{R}$ and $A=[0,1]$, then $\mathbf{1}_A(x)=1$ for $x\in[0,1]$ and $0$ otherwise.
- If $A=\varnothing$, then $\mathbf{1}_A$ is the constant-$0$ function on $X$.
- If $A=\mathbb{Q}\subseteq\mathbb{R}$, then $\mathbf{1}_{\mathbb{Q}}$ is $1$ on rationals and $0$ on irrationals (a classical highly discontinuous function).
