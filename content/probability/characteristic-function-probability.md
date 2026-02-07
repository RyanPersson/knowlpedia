---
title: "Characteristic function"
description: "The complex-valued function t ↦ E[exp(i t X)] associated with a real-valued random variable."
---

A **characteristic function** is the complex-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $\varphi_X:\mathbb{R}\to\mathbb{C}$ associated to a real-valued {{< knowl id="random-variable" text="random variable" >}} $X$, defined by
$$
\varphi_X(t) \;=\; \mathbb{E}\!\left[e^{itX}\right], \qquad t\in\mathbb{R}.
$$

It is defined using {{< knowl id="expectation" text="expectation" >}} and always exists (since $|e^{itX}|=1$). The characteristic function determines the {{< knowl id="distribution-law" text="distribution law" >}} of $X$, and it is closely related to the {{< knowl id="moment-generating-function" text="moment generating function" >}} (when the latter exists in a neighborhood of $0$).

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $\varphi_X(t)=\exp\!\bigl(i\mu t-\tfrac12\sigma^2 t^2\bigr)$.
- If $X\sim \mathrm{Bernoulli}(p)$, then $\varphi_X(t)=(1-p)+p\,e^{it}$.
