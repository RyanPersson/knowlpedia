---
title: "Mesh of a partition"
description: "The maximum subinterval length in a partition of [a,b]."
---

Let $P$ be a partition of $[a,b]$ given by $a=x_0<\cdots<x_n=b$. The **mesh** (or **norm**) of $P$ is
$$\|P\| := \max_{1\le i\le n}(x_i-x_{i-1})=\max_{1\le i\le n}\Delta x_i.$$

The mesh measures how fine a partition is. Many convergence statements for Riemann sums are phrased in terms of $\|P\|\to 0$.

**Examples:**
- For the uniform partition $x_i=a+i(b-a)/n$, one has $\|P\|=(b-a)/n$.
- If $P:0<0.9<1$, then $\|P\|=0.9$.
- Refining a partition cannot increase the mesh: if $Q$ refines $P$, then $\|Q\|\le \|P\|$.
