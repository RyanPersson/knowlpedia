---
title: "Riemann integral"
description: "The common value of the upper and lower integrals of a Riemann integrable function."
---

If $f:[a,b]\to\mathbb{R}$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}}, its **Riemann integral** over $[a,b]$ is the common value
$$\int_a^b f(x)\,dx := \sup_P L(f,P) \;=\; \inf_P U(f,P),$$
where $P$ ranges over all {{< knowl id="partition-of-an-interval" text="partitions" >}} of $[a,b]$, and $L(f,P)$, $U(f,P)$ are the {{< knowl id="lower-sum-riemann" text="lower" >}} and {{< knowl id="upper-sum-riemann" text="upper sums" >}}.

Equivalently, $\int_a^b f$ is the number $I$ such that for every $\varepsilon>0$ there exists $\delta>0$ with
$$\|P\|<\delta \ \Rightarrow\ |S(f;P,T)-I|<\varepsilon$$
for all {{< knowl id="tagged-partition" text="tagged partitions" >}} $(P,T)$ (this equivalence requires a standard theorem).

The Riemann integral is the classical integral used in elementary calculus and remains useful for {{< knowl id="continuity-on-a-set" text="continuous" >}} and piecewise regular functions.

**Examples:**
- $\int_0^1 x\,dx=\frac12$.
- If $f(x)=c$ is constant, then $\int_a^b f(x)\,dx=c(b-a)$.
- If $f=\mathbf{1}_{[0,1/2]}$ on $[0,1]$, then $\int_0^1 f(x)\,dx=\frac12$.
