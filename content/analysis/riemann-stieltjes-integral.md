---
title: "Riemann–Stieltjes integral"
description: "An integral ∫ f dα defined via limits of sums using increments of an integrator α."
---

Let $f:[a,b]\to\mathbb{R}$ be bounded, and let $\alpha:[a,b]\to\mathbb{R}$ be a function. For a partition $P:a=x_0<\cdots<x_n=b$, define
$$\Delta\alpha_i:=\alpha(x_i)-\alpha(x_{i-1}).$$
For each $i$, set
$$M_i:=\sup_{x\in[x_{i-1},x_i]} f(x),\qquad m_i:=\inf_{x\in[x_{i-1},x_i]} f(x).$$
The **upper** and **lower Riemann–Stieltjes sums** are
$$U(f,\alpha;P):=\sum_{i=1}^n M_i\,\Delta\alpha_i,\qquad
L(f,\alpha;P):=\sum_{i=1}^n m_i\,\Delta\alpha_i.$$

If $\alpha$ is increasing, one says $f$ is **Riemann–Stieltjes integrable with respect to $\alpha$** if
$$\sup_P L(f,\alpha;P)=\inf_P U(f,\alpha;P),$$
and the common value is denoted
$$\int_a^b f\,d\alpha.$$

The Riemann–Stieltjes integral generalizes the Riemann integral: taking $\alpha(x)=x$ recovers $\int_a^b f(x)\,dx$. It also encodes integration with respect to step functions (leading to sums) and is the classical precursor to Lebesgue–Stieltjes integration.

**Examples:**
- If $\alpha(x)=x$, then $\int_a^b f\,d\alpha=\int_a^b f(x)\,dx$ (Riemann integral).
- If $\alpha$ is constant, $\alpha(x)\equiv c$, then $\Delta\alpha_i=0$ for all $i$ and $\int_a^b f\,d\alpha=0$.
- If $\alpha$ is a step function with a jump at $c\in(a,b)$, then $\int_a^b f\,d\alpha$ reduces (under standard integrability assumptions) to a multiple of $f(c)$ reflecting the jump size.
