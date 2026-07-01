+++
id = "real-analysis/integration-by-parts-riemann-stieltjes"
title = "Integration by parts for Riemann–Stieltjes integrals"
kind = "knowl"
summary = "A boundary-term identity relating two Riemann–Stieltjes integrals."
aliases = ["integration-by-parts-riemann-stieltjes", "Integration by parts for Riemann–Stieltjes integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/integration-by-parts-riemann-stieltjes.md"
+++

**Integration by parts (Riemann–Stieltjes):** Let $a<b$. Assume $f,g:[a,b]\to\mathbb{R}$ are [[real-analysis/bounded-variation-function|of bounded variation]] and that at least one of $f$ or $g$ is continuous. Then both Riemann–Stieltjes integrals $\int_a^b f\,dg$ and $\int_a^b g\,df$ exist, and
$$
\int_a^b f\,dg \;+\; \int_a^b g\,df \;=\; f(b)g(b)-f(a)g(a).
$$

This generalizes the usual [[real-analysis/integration-by-parts|integration by parts]] (obtained by taking $g(x)=x$ and interpreting $df=f'(x)\,dx$), and existence is ensured by the [[real-analysis/riemann-stieltjes-integrability-theorem|Riemann–Stieltjes integrability theorem]].
