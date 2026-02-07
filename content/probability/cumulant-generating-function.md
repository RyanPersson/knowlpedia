---
title: "Cumulant generating function"
description: "The logarithm of the moment generating function, when the latter is finite near zero."
---

A **cumulant generating function** is the real-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $K_X$ associated to a {{< knowl id="random-variable" text="random variable" >}} $X$ whose {{< knowl id="moment-generating-function" text="moment generating function" >}} $M_X(t)=\mathbb{E}[e^{tX}]$ is finite on an open interval containing $0$, defined by
$$
K_X(t) \;=\; \log M_X(t),
$$

for all $t$ where $M_X(t)$ is finite. Derivatives of $K_X$ at $0$ (when they exist) produce the {{< knowl id="cumulant" text="cumulants" >}} of $X$; in particular, this links $K_X$ to {{< knowl id="expectation" text="expectation" >}} and {{< knowl id="variance" text="variance" >}}. If $X$ and $Y$ are {{< knowl id="independence-random-variables" text="independent random variables" >}} and both cumulant generating functions exist near $0$, then $K_{X+Y}(t)=K_X(t)+K_Y(t)$.

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $K_X(t)=\mu t+\tfrac12\sigma^2 t^2$ (finite for all $t\in\mathbb{R}$).
- If $X\sim \mathrm{Bernoulli}(p)$, then $K_X(t)=\log\!\bigl((1-p)+p\,e^{t}\bigr)$.
