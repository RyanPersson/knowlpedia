---
title: "Upper sum (Riemann)"
description: "A weighted sum of suprema of f over subintervals of a partition."
---

Let $f:[a,b]\to\mathbb{R}$ be bounded and let $P:a=x_0<\cdots<x_n=b$ be a partition. For each subinterval, define
$$M_i := \sup\{f(x): x\in[x_{i-1},x_i]\}.$$
The **upper sum** of $f$ with respect to $P$ is
$$U(f,P) := \sum_{i=1}^n M_i\, (x_i-x_{i-1}).$$

Upper sums approximate the integral from above. As the partition is refined, upper sums decrease (or stay the same).

**Examples:**
- If $f(x)=x$ on $[0,1]$ and $P:0<1/2<1$, then $M_1=1/2$, $M_2=1$, so $U(f,P)=\frac12\cdot\frac12+1\cdot\frac12=\frac34$.
- If $f$ is constant, $f(x)=c$, then $U(f,P)=c(b-a)$ for every $P$.
- For a bounded but highly oscillatory $f$, $U(f,P)$ may remain far above any candidate limit unless the oscillations are controlled.
