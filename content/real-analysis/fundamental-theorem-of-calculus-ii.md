---
title: "Fundamental theorem of calculus II"
description: "A Riemann integral can be computed from any antiderivative."
---

**Fundamental theorem of calculus II:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be a {{< knowl id="riemann-integrable-function" text="Riemann integrable function" >}}. Suppose $F:[a,b]\to\mathbb{R}$ is continuous on $[a,b]$, {{< knowl id="differentiability-1d" text="differentiable" >}} on $(a,b)$, and satisfies $F'(x)=f(x)$ for all $x\in(a,b)$. Then
$$
\int_a^b f(x)\,dx = F(b)-F(a).
$$

Combined with {{< knowl id="fundamental-theorem-of-calculus-i" text="fundamental theorem of calculus I" >}}, this explains why differentiation rules can be used to evaluate definite {{< knowl id="riemann-integral" text="integrals" >}} via antiderivatives.
