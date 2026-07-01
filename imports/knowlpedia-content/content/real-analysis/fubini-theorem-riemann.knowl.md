+++
id = "real-analysis/fubini-theorem-riemann"
title = "Fubini theorem for Riemann integrals"
kind = "knowl"
summary = "For continuous functions on a rectangle, iterated integrals exist and agree with the double Riemann integral."
aliases = ["fubini-theorem-riemann", "Fubini theorem for Riemann integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/fubini-theorem-riemann.md"
+++

**Fubini theorem (Riemann):**

Let $a<b$ and $c<d$, and let $f:[a,b]\times[c,d]\to\mathbb{R}$ be continuous. Then $f$ is [[real-analysis/multiple-riemann-integral|Riemann integrable on the rectangle]], the two [[real-analysis/iterated-integral|iterated integrals]] exist, and
$$
\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx = \int_c^d\left(\int_a^b f(x,y)\,dx\right)dy =
$$
$$
\iint_{[a,b]\times[c,d]} f(x,y)\,dA.
$$

This allows one to compute a [[real-analysis/multiple-riemann-integral|double Riemann integral]] by integrating one variable at a time, and it is a key tool for evaluating many [[real-analysis/multiple-riemann-integral|multiple integrals]] in practice.
