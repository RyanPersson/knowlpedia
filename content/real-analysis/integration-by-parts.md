---
title: "Integration by parts"
description: "An identity relating the integral of a product to boundary terms and another integral."
---

**Integration by parts:** Let $a<b$ and let $u,v:[a,b]\to\mathbb{R}$ be functions that are {{< knowl id="differentiability-1d" text="differentiable" >}} on $[a,b]$, with $u'$ and $v'$ {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} on $[a,b]$. Then
$$
\int_a^b u(x)\,v'(x)\,dx = u(b)v(b)-u(a)v(a) - \int_a^b u'(x)\,v(x)\,dx.
$$

This is the integral form of the product rule from {{< knowl id="differentiation-rules" text="differentiation rules" >}}, typically justified using {{< knowl id="fundamental-theorem-of-calculus-ii" text="fundamental theorem of calculus II" >}}.
