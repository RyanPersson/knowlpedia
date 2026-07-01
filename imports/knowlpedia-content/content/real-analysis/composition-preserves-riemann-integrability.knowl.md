+++
id = "real-analysis/composition-preserves-riemann-integrability"
title = "Composition preserves Riemann integrability"
kind = "knowl"
summary = "Composing a Riemann integrable function with a continuous function preserves integrability."
aliases = ["composition-preserves-riemann-integrability", "Composition preserves Riemann integrability"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/composition-preserves-riemann-integrability.md"
+++

**Composition preserves Riemann integrability:** Let $f:[a,b]\to\mathbb R$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] on $[a,b]$, and let $\varphi:J\to\mathbb R$ be [[topology/continuous-map|continuous]] on an [[real-analysis/interval|interval]] $J$ that contains the range $f([a,b])$. Then $\varphi\circ f$ is Riemann integrable on $[a,b]$.

In particular, taking $\varphi(t)=t^2$ shows that $f^2$ is integrable whenever $f$ is integrable, and taking $\varphi(t)=|t|$ connects directly to [[real-analysis/absolute-value-preserves-integrability|absolute value preserving integrability]].
