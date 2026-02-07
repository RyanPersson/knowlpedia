---
title: "Substitution rule"
description: "A change of variables formula for one-dimensional Riemann integrals."
---

**Substitution rule:** Let $\alpha<\beta$, let $\varphi:[\alpha,\beta]\to\mathbb{R}$ be continuously differentiable and strictly increasing, and set $a=\varphi(\alpha)$ and $b=\varphi(\beta)$. If $f:[a,b]\to\mathbb{R}$ is continuous, then
$$
\int_a^b f(x)\,dx = \int_\alpha^\beta f(\varphi(t))\,\varphi'(t)\,dt.
$$

This is the one-dimensional instance of the general {{< knowl id="change-of-variables-formula" text="change of variables formula" >}}, and it is closely tied to the {{< knowl id="chain-rule" text="chain rule" >}} and {{< knowl id="fundamental-theorem-of-calculus-ii" text="fundamental theorem of calculus II" >}}.
