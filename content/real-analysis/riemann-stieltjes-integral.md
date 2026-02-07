---
title: "Riemann–Stieltjes integral"
description: "An integral defined using increments of an integrator function."
---

A **Riemann–Stieltjes integral** of a bounded function $f:[a,b]\to\mathbb R$ with respect to an {{< knowl id="integrator-function" text="integrator function" >}} $\alpha:[a,b]\to\mathbb R$ is a number
\[
\int_a^b f\,d\alpha
\]
such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that, for every {{< knowl id="tagged-partition" text="tagged partition" >}} $(P,\{t_i\})$ with mesh $\|P\|<\delta$,
\[
\left|\sum_{i=1}^n f(t_i)\bigl(\alpha(x_i)-\alpha(x_{i-1})\bigr)-\int_a^b f\,d\alpha\right|<\varepsilon.
\]
(The sum is called a Riemann–Stieltjes sum.)

This generalizes the {{< knowl id="riemann-integral" text="Riemann integral" >}} (take $\alpha(x)=x$) and is especially well-behaved when $\alpha$ is a {{< knowl id="bounded-variation-function" text="function of bounded variation" >}}; see {{< knowl id="riemann-stieltjes-integrability-theorem" text="Riemann–Stieltjes integrability" >}} and {{< knowl id="integration-by-parts-riemann-stieltjes" text="integration by parts" >}}.

**Examples:**
- If $\alpha(x)=x$, then $\int_a^b f\,d\alpha=\int_a^b f(x)\,dx$.
- If $\alpha$ is constant on $[a,b]$, then $\int_a^b f\,d\alpha=0$ (whenever the integral is defined).
