+++
id = "real-analysis/riemann-stieltjes-linearity"
title = "Linearity of the Riemann–Stieltjes integral"
kind = "knowl"
summary = "The Riemann–Stieltjes integral is linear in both the integrand and the integrator when the relevant integrals exist."
aliases = ["riemann-stieltjes-linearity", "Linearity of the Riemann–Stieltjes integral"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-stieltjes-linearity.md"
+++

**Riemann–Stieltjes linearity:** Let $a<b$ and let $f,h,g_1,g_2:[a,b]\to\mathbb{R}$. Suppose the indicated [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integrals]] exist. For scalars $\alpha,\beta\in\mathbb{R}$:
- If $\int_a^b f\,dg$ and $\int_a^b h\,dg$ exist, then $\int_a^b (\alpha f+\beta h)\,dg$ exists and
  $$
  \int_a^b (\alpha f+\beta h)\,dg = \alpha\int_a^b f\,dg+\beta\int_a^b h\,dg.
  $$

- If $\int_a^b f\,dg_1$ and $\int_a^b f\,dg_2$ exist, then $\int_a^b f\,d(\alpha g_1+\beta g_2)$ exists and
  $$
  \int_a^b f\,d(\alpha g_1+\beta g_2) = \alpha\int_a^b f\,dg_1+\beta\int_a^b f\,dg_2.
  $$

These identities are the Riemann–Stieltjes analog of [[real-analysis/riemann-linearity|linearity of the Riemann integral]] and are used routinely together with [[real-analysis/integration-by-parts-riemann-stieltjes|integration by parts]].
