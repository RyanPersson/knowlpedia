---
title: "Riemann integral"
description: "The common value of the upper and lower integrals of a Riemann integrable function."
---

If $f:[a,b]\to\mathbb{R}$ is Riemann integrable, its **Riemann integral** over $[a,b]$ is the common value
$$\int_a^b f(x)\,dx := \sup_P L(f,P) \;=\; \inf_P U(f,P),$$
where $P$ ranges over all partitions of $[a,b]$.

Equivalently, $\int_a^b f$ is the number $I$ such that for every $\varepsilon>0$ there exists $\delta>0$ with
$$\|P\|<\delta \ \Rightarrow\ |S(f;P,T)-I|<\varepsilon$$
for all tagged partitions $(P,T)$ (this equivalence requires a standard theorem).

The Riemann integral is the classical integral used in elementary calculus and remains useful for continuous and piecewise regular functions.

**Examples:**
- $\int_0^1 x\,dx=\frac12$.
- If $f(x)=c$ is constant, then $\int_a^b f(x)\,dx=c(b-a)$.
- If $f=\mathbf{1}_{[0,1/2]}$ on $[0,1]$, then $\int_0^1 f(x)\,dx=\frac12$.
