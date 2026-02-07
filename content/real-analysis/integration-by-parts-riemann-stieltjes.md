---
title: "Integration by parts for Riemann–Stieltjes integrals"
description: "A boundary-term identity relating two Riemann–Stieltjes integrals."
---

**Integration by parts (Riemann–Stieltjes):** Let $a<b$. Assume $f,g:[a,b]\to\mathbb{R}$ are {{< knowl id="bounded-variation-function" text="of bounded variation" >}} and that at least one of $f$ or $g$ is continuous. Then both Riemann–Stieltjes integrals $\int_a^b f\,dg$ and $\int_a^b g\,df$ exist, and
$$
\int_a^b f\,dg \;+\; \int_a^b g\,df \;=\; f(b)g(b)-f(a)g(a).
$$

This generalizes the usual {{< knowl id="integration-by-parts" text="integration by parts" >}} (obtained by taking $g(x)=x$ and interpreting $df=f'(x)\,dx$), and existence is ensured by the {{< knowl id="riemann-stieltjes-integrability-theorem" text="Riemann–Stieltjes integrability theorem" >}}.
