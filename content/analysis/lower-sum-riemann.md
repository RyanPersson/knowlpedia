---
title: "Lower sum (Riemann)"
description: "A weighted sum of infima of f over subintervals of a partition."
---

Let $f:[a,b]\to\mathbb{R}$ be bounded and let $P:a=x_0<\cdots<x_n=b$ be a partition. For each subinterval, define
$$m_i := \inf\{f(x): x\in[x_{i-1},x_i]\}.$$
The **lower sum** of $f$ with respect to $P$ is
$$L(f,P) := \sum_{i=1}^n m_i\, (x_i-x_{i-1}).$$

Lower sums approximate the integral from below. As the partition is refined, lower sums increase (or stay the same).

**Examples:**
- If $f(x)=x$ on $[0,1]$ and $P:0<1/2<1$, then $m_1=0$, $m_2=1/2$, so $L(f,P)=0\cdot\frac12+\frac12\cdot\frac12=\frac14$.
- If $f(x)=c$ is constant, then $L(f,P)=c(b-a)$ for every $P$.
- For $f=\mathbf{1}_{\mathbb{Q}}$ on $[0,1]$, every subinterval has $m_i=0$ and $M_i=1$, so $L(f,P)=0$ and $U(f,P)=1$ for all $P$.
