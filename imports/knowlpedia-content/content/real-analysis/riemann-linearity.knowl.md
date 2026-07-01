+++
id = "real-analysis/riemann-linearity"
title = "Riemann linearity"
kind = "knowl"
summary = "Linearity of the Riemann integral with respect to addition and scalar multiplication."
aliases = ["riemann-linearity", "Riemann linearity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-linearity.md"
+++

**Riemann linearity:** Let $f,g:[a,b]\to\mathbb R$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] on the [[real-analysis/interval|interval]] $[a,b]$, and let $\alpha,\beta\in\mathbb R$. Then $\alpha f+\beta g$ is Riemann integrable on $[a,b]$, and
$$
\int_a^b (\alpha f+\beta g)=\alpha\int_a^b f+\beta\int_a^b g.
$$

This is the basic linear structure behind the [[real-analysis/riemann-integral|Riemann integral]] and is used throughout the algebraic manipulation of integrals.
