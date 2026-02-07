---
title: "Cumulant"
description: "A numerical summary of a distribution given by derivatives of the cumulant generating function at zero."
---

A **cumulant** (of order $n$) of a {{< knowl id="random-variable" text="random variable" >}} $X$ is the number
$$
\kappa_n(X) \;=\; K_X^{(n)}(0),
$$

provided the {{< knowl id="cumulant-generating-function" text="cumulant generating function" >}} $K_X$ exists in a neighborhood of $0$ and is $n$ times differentiable at $0$. The first two cumulants are $\kappa_1(X)=\mathbb{E}[X]$ and $\kappa_2(X)=\mathrm{Var}(X)$, linking cumulants to {{< knowl id="expectation" text="expectation" >}} and {{< knowl id="variance" text="variance" >}}. Cumulants are additive over sums of {{< knowl id="independence-random-variables" text="independent random variables" >}} (when defined), which makes them useful for studying distributional limits and approximations.

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $\kappa_1(X)=\mu$, $\kappa_2(X)=\sigma^2$, and $\kappa_n(X)=0$ for all $n\ge 3$.
- If $X\sim \mathrm{Bernoulli}(p)$, then $\kappa_1(X)=p$, $\kappa_2(X)=p(1-p)$, and $\kappa_3(X)=p(1-p)(1-2p)$.
