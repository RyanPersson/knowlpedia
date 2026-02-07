---
title: "Log moment generating function"
description: "The logarithm of the moment generating function, viewed as a convex functional of the parameter."
---

A **log moment generating function** (log-MGF) of an $\mathbb R^d$-valued {{< knowl id="random-variable" section="probability" text="random variable" >}} $X$ is the function $\Lambda:\mathbb R^d\to(-\infty,\infty]$ defined by
$$
\Lambda(\theta)=\log \mathbb E\big[e^{\langle \theta, X\rangle}\big],
$$

where $\langle\theta,X\rangle$ is the Euclidean inner product and the expectation is taken in the sense of {{< knowl id="expectation" section="probability" text="expectation" >}}. Equivalently, if $\mu$ is the {{< knowl id="distribution-law" section="probability" text="law" >}} of $X$, then
$$
\Lambda(\theta)=\log\int_{\mathbb R^d} e^{\langle\theta,x\rangle}\,\mu(dx),
$$
where the integral is a special case of the {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}}.

The log-MGF is a central object in large deviations: it is convex and encodes exponential moment growth, and its convex dual gives the {{< knowl id="cramer-transform" text="Cramér transform" >}}. In particular, for sums of an {{< knowl id="iid-sequence" section="probability" text="i.i.d. sequence" >}}, the log-MGF is the starting point for {{< knowl id="cramers-theorem" text="Cramér's theorem" >}} and the {{< knowl id="gartner-ellis-theorem" text="Gärtner–Ellis theorem" >}}.

**Examples:**
- If $X\sim \mathcal N(0,\sigma^2)$ on $\mathbb R$, then $\Lambda(\theta)=\frac{\sigma^2\theta^2}{2}$ for all $\theta\in\mathbb R$.
- If $X\sim \mathrm{Bernoulli}(p)$ on $\{0,1\}$, then $\Lambda(\theta)=\log\big((1-p)+p e^{\theta}\big)$ for all $\theta\in\mathbb R$.
