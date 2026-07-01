+++
id = "real-analysis/absolute-value-preserves-integrability"
title = "Absolute value preserves integrability"
kind = "knowl"
summary = "If a function is Riemann integrable then so is its absolute value, with a triangle inequality."
aliases = ["absolute-value-preserves-integrability", "Absolute value preserves integrability"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/absolute-value-preserves-integrability.md"
+++

**Absolute value preserves integrability:** Let $f:[a,b]\to\mathbb R$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] on the [[real-analysis/interval|interval]] $[a,b]$. Then the [[real-analysis/absolute-value|absolute value]] function $|f|$ is Riemann integrable on $[a,b]$, and the triangle inequality holds:
$$
\left|\int_a^b f\right|\le \int_a^b |f|.
$$

This is often used together with [[real-analysis/riemann-linearity|linearity]] to control integrals by comparing them to integrals of nonnegative functions.
