---
title: "Step function (on an interval)"
description: "A function constant on each subinterval of a finite partition."
---

Let $[a,b]\subseteq\mathbb{R}$ and let $P$ be a partition $a=x_0<x_1<\cdots<x_n=b$. A function $\varphi:[a,b]\to\mathbb{R}$ is a **step function** (with respect to $P$) if for each $i=1,\dots,n$ there exists a constant $c_i\in\mathbb{R}$ such that
$$\varphi(x)=c_i\quad\text{for all }x\in(x_{i-1},x_i).$$
(Values at the partition points $x_i$ can be assigned arbitrarily, since they do not affect Riemann integration.)

Step functions are the simplest nontrivial functions in Riemann integration. They approximate more general integrable functions from above and below via upper and lower sums.

**Examples:**
- On $[0,1]$, $\varphi(x)=0$ for $x\in[0,1/2)$ and $\varphi(x)=1$ for $x\in[1/2,1]$ is a step function.
- Any constant function on $[a,b]$ is a step function (take $n=1$).
- The function $\varphi(x)=\lfloor 10x\rfloor$ on $[0,1]$ is a step function with partition points $0,0.1,0.2,\dots,1$.
