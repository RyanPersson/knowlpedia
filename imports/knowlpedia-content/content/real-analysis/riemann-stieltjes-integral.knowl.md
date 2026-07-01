+++
id = "real-analysis/riemann-stieltjes-integral"
title = "Riemann–Stieltjes integral"
kind = "knowl"
summary = "An integral defined using increments of an integrator function."
aliases = ["riemann-stieltjes-integral", "Riemann–Stieltjes integral"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-stieltjes-integral.md"
+++

A **Riemann–Stieltjes integral** of a bounded function $f:[a,b]\to\mathbb R$ with respect to an [[real-analysis/integrator-function|integrator function]] $\alpha:[a,b]\to\mathbb R$ is a number
\[
\int_a^b f\,d\alpha
\]
such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that, for every [[real-analysis/tagged-partition|tagged partition]] $(P,\{t_i\})$ with mesh $\|P\|<\delta$,
\[
\left|\sum_{i=1}^n f(t_i)\bigl(\alpha(x_i)-\alpha(x_{i-1})\bigr)-\int_a^b f\,d\alpha\right|<\varepsilon.
\]
(The sum is called a Riemann–Stieltjes sum.)

This generalizes the [[real-analysis/riemann-integral|Riemann integral]] (take $\alpha(x)=x$) and is especially well-behaved when $\alpha$ is a [[real-analysis/bounded-variation-function|function of bounded variation]]; see [[real-analysis/riemann-stieltjes-integrability-theorem|Riemann–Stieltjes integrability]] and [[real-analysis/integration-by-parts-riemann-stieltjes|integration by parts]].

**Examples:**
- If $\alpha(x)=x$, then $\int_a^b f\,d\alpha=\int_a^b f(x)\,dx$.
- If $\alpha$ is constant on $[a,b]$, then $\int_a^b f\,d\alpha=0$ (whenever the integral is defined).
