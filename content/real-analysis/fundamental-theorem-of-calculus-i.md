---
title: "Fundamental theorem of calculus I"
description: "The integral defines an antiderivative at points where the integrand is continuous."
---

**Fundamental theorem of calculus I:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be a {{< knowl id="riemann-integrable-function" text="Riemann integrable function" >}}. Define
$$
F(x)=\int_a^x f(t)\,dt \quad (x\in[a,b]).
$$

Then $F$ is continuous on $[a,b]$. Moreover, if $f$ is continuous at a point $c\in(a,b)$, then $F$ is {{< knowl id="differentiability-1d" text="differentiable" >}} at $c$ and
$$
F'(c)=f(c).
$$

This links the {{< knowl id="riemann-integral" text="Riemann integral" >}} to the {{< knowl id="derivative" text="derivative" >}} by showing the integral produces an antiderivative wherever the integrand has no {{< knowl id="discontinuity-point" text="discontinuity" >}}.
