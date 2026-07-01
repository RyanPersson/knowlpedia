+++
id = "probability/characteristic-function-probability"
title = "Characteristic function"
kind = "knowl"
summary = "The complex-valued function t ↦ E[exp(i t X)] associated with a real-valued random variable."
aliases = ["characteristic-function-probability", "Characteristic function"]
domains = ["probability"]
legacy_source_path = "probability/characteristic-function-probability.md"
+++

A **characteristic function** is the complex-valued [[shared-foundations/function|function]] $\varphi_X:\mathbb{R}\to\mathbb{C}$ associated to a real-valued [[probability/random-variable|random variable]] $X$, defined by
$$
\varphi_X(t) \;=\; \mathbb{E}\!\left[e^{itX}\right], \qquad t\in\mathbb{R}.
$$

It is defined using [[probability/expectation|expectation]] and always exists (since $|e^{itX}|=1$). The characteristic function determines the [[probability/distribution-law|distribution law]] of $X$, and it is closely related to the [[probability/moment-generating-function|moment generating function]] (when the latter exists in a neighborhood of $0$).

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $\varphi_X(t)=\exp\!\bigl(i\mu t-\tfrac12\sigma^2 t^2\bigr)$.
- If $X\sim \mathrm{Bernoulli}(p)$, then $\varphi_X(t)=(1-p)+p\,e^{it}$.
