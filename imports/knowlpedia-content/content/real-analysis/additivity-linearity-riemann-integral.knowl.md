+++
id = "real-analysis/additivity-linearity-riemann-integral"
title = "Additivity and linearity lemmas for Riemann and Riemann–Stieltjes integrals"
kind = "knowl"
summary = "Linearity in the integrand and additivity over subintervals for Riemann and Riemann–Stieltjes integrals"
aliases = ["additivity-linearity-riemann-integral", "Additivity and linearity lemmas for Riemann and Riemann–Stieltjes integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/additivity-linearity-riemann-integral.md"
+++

**Additivity and linearity (Riemann integral)**: Let $f,g:[a,b]\to\mathbb{R}$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] and let $\alpha,\beta\in\mathbb{R}$. Then:
- $\alpha f+\beta g$ is Riemann integrable on $[a,b]$, and
  $\int_a^b (\alpha f(x)+\beta g(x))\,dx = \alpha\int_a^b f(x)\,dx+\beta\int_a^b g(x)\,dx.$
- For any $c\in[a,b]$, $f$ is Riemann integrable on $[a,c]$ and on $[c,b]$, and
  $\int_a^b f(x)\,dx=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx.$

**Additivity and linearity (Riemann–Stieltjes integral)**: Let $\gamma:[a,b]\to\mathbb{R}$ be [[real-analysis/monotone-function|increasing]]. If $f,g$ are [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integrable]] with respect to $\gamma$ on $[a,b]$ and $\alpha,\beta\in\mathbb{R}$, then $\alpha f+\beta g$ is Riemann–Stieltjes integrable with respect to $\gamma$ and
$\int_a^b (\alpha f+\beta g)\,d\gamma = \alpha\int_a^b f\,d\gamma+\beta\int_a^b g\,d\gamma.$
Moreover, for any $c\in[a,b]$,
$\int_a^b f\,d\gamma=\int_a^c f\,d\gamma+\int_c^b f\,d\gamma.$

These are the basic algebraic rules that make integration behave like a linear functional and allow [[real-analysis/interval|interval]] decomposition.
