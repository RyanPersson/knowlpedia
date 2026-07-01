+++
id = "real-analysis/fundamental-theorem-of-calculus-i"
title = "Fundamental theorem of calculus I"
kind = "knowl"
summary = "The integral defines an antiderivative at points where the integrand is continuous."
aliases = ["fundamental-theorem-of-calculus-i", "Fundamental theorem of calculus I"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/fundamental-theorem-of-calculus-i.md"
+++

**Fundamental theorem of calculus I:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be a [[real-analysis/riemann-integrable-function|Riemann integrable function]]. Define
$$
F(x)=\int_a^x f(t)\,dt \quad (x\in[a,b]).
$$

Then $F$ is continuous on $[a,b]$. Moreover, if $f$ is continuous at a point $c\in(a,b)$, then $F$ is [[real-analysis/differentiability-1d|differentiable]] at $c$ and
$$
F'(c)=f(c).
$$

This links the [[real-analysis/riemann-integral|Riemann integral]] to the [[real-analysis/derivative|derivative]] by showing the integral produces an antiderivative wherever the integrand has no [[real-analysis/discontinuity-point|discontinuity]].
