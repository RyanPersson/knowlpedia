+++
id = "measure-theory/lebesgue-criterion-for-riemann-integrability"
title = "Lebesgue criterion for Riemann integrability"
kind = "knowl"
summary = "A bounded function on a closed interval is Riemann integrable exactly when its discontinuities form a Lebesgue null set."
aliases = ["lebesgue-criterion-for-riemann-integrability", "Lebesgue criterion for Riemann integrability"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lebesgue-criterion-for-riemann-integrability.md"
+++

**Lebesgue criterion for Riemann integrability:** Let $f:[a,b]\to\mathbb{R}$ be a bounded function on the closed interval $[a,b]$ (see [[real-analysis/interval|interval]]). Let $D_f\subseteq [a,b]$ be the set of points where $f$ is discontinuous. Then $f$ is Riemann integrable on $[a,b]$ if and only if $D_f$ is a [[measure-theory/null-set|null set]] with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]] on $\mathbb{R}$.

Equivalently, a bounded function is Riemann integrable exactly when it is continuous [[measure-theory/almost-everywhere|almost everywhere]] on $[a,b]$ with respect to Lebesgue measure.
