---
title: "Riemann integral"
description: "The common value determined by Riemann sums when a function is integrable."
---

A **Riemann integral** of a {{< knowl id="riemann-integrable-function" text="Riemann integrable function" >}} $f:[a,b]\to\mathbb R$ is the number
\[
\int_a^b f(x)\,dx
\]
defined by
\[
\int_a^b f(x)\,dx=\sup_P L(f,P)=\inf_P U(f,P),
\]
where $L(f,P)$ and $U(f,P)$ are the {{< knowl id="lower-sum" text="lower" >}} and {{< knowl id="upper-sum" text="upper sums" >}} over all partitions $P$ of $[a,b]$.

This definition matches the limit of {{< knowl id="riemann-sum" text="Riemann sums" >}} along partitions of small mesh, and it is the starting point for results such as {{< knowl id="riemann-linearity" text="linearity" >}} and the {{< knowl id="fundamental-theorem-of-calculus-i" text="Fundamental Theorem of Calculus" >}}.

**Examples:**
- If $f(x)=c$ is constant on $[a,b]$, then $\int_a^b f(x)\,dx=c(b-a)$.
- For $f(x)=x$ on $[0,1]$, one has $\int_0^1 x\,dx=\tfrac12$.
