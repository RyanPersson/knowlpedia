---
title: "Lower sum"
description: "A Riemann lower sum built from infima on each subinterval."
---

A **lower sum** of a bounded function $f:[a,b]\to\mathbb R$ with respect to a {{< knowl id="partition-of-an-interval" text="partition" >}} $P=\{x_0,\dots,x_n\}$ is the number
\[
L(f,P)=\sum_{i=1}^n m_i\,(x_i-x_{i-1}),
\]
where $m_i=\inf\{f(x):x\in[x_{i-1},x_i]\}$ is the {{< knowl id="infimum" text="infimum" >}} of $f$ on the $i$th subinterval.

Lower sums are paired with {{< knowl id="upper-sum" text="upper sums" >}} to define {{< knowl id="riemann-integrable-function" text="Riemann integrability" >}} via the gap $U(f,P)-L(f,P)$.

**Examples:**
- For $f(x)=x$ on $[0,1]$ and $P=\{0,\tfrac12,1\}$, one gets $L(f,P)=0\cdot\tfrac12+\tfrac12\cdot\tfrac12=\tfrac14$.
- If $f(x)=c$ is constant on $[a,b]$, then $L(f,P)=c(b-a)$ for every partition $P$.
