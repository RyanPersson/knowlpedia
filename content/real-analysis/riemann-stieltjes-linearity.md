---
title: "Linearity of the Riemann–Stieltjes integral"
description: "The Riemann–Stieltjes integral is linear in both the integrand and the integrator when the relevant integrals exist."
---

**Riemann–Stieltjes linearity:** Let $a<b$ and let $f,h,g_1,g_2:[a,b]\to\mathbb{R}$. Suppose the indicated {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes integrals" >}} exist. For scalars $\alpha,\beta\in\mathbb{R}$:
- If $\int_a^b f\,dg$ and $\int_a^b h\,dg$ exist, then $\int_a^b (\alpha f+\beta h)\,dg$ exists and
  $$
  \int_a^b (\alpha f+\beta h)\,dg = \alpha\int_a^b f\,dg+\beta\int_a^b h\,dg.
  $$

- If $\int_a^b f\,dg_1$ and $\int_a^b f\,dg_2$ exist, then $\int_a^b f\,d(\alpha g_1+\beta g_2)$ exists and
  $$
  \int_a^b f\,d(\alpha g_1+\beta g_2) = \alpha\int_a^b f\,dg_1+\beta\int_a^b f\,dg_2.
  $$

These identities are the Riemann–Stieltjes analog of {{< knowl id="riemann-linearity" text="linearity of the Riemann integral" >}} and are used routinely together with {{< knowl id="integration-by-parts-riemann-stieltjes" text="integration by parts" >}}.
