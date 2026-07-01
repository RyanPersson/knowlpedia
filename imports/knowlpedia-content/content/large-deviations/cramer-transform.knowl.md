+++
id = "large-deviations/cramer-transform"
title = "Cramér transform"
kind = "knowl"
summary = "The convex dual of a log moment generating function, giving a canonical large-deviation rate function."
aliases = ["cramer-transform", "Cramér transform"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/cramer-transform.md"
+++

A **Cramér transform** associated with a log moment generating function $\Lambda:\mathbb R^d\to(-\infty,\infty]$ is the function $I:\mathbb R^d\to[0,\infty]$ defined by
$$
I(x)=\sup_{\theta\in\mathbb R^d}\big\{\langle \theta,x\rangle-\Lambda(\theta)\big\}.
$$

This is the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]] of $\Lambda$ (equivalently, the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]] of $\Lambda$).

In large deviations, when $\Lambda$ is the [[large-deviations/log-moment-generating-function|log moment generating function]] of a random variable, $I$ is the canonical candidate [[large-deviations/rate-function|rate function]] for the LDP of empirical means; this is made precise by [[large-deviations/cramers-theorem|Cramér's theorem]] and, in broader settings, by the [[large-deviations/gartner-ellis-theorem|Gärtner–Ellis theorem]].

**Examples:**
- If $\Lambda(\theta)=\frac{\sigma^2\theta^2}{2}$ on $\mathbb R$ (Gaussian case), then
  $$
  I(x)=\frac{x^2}{2\sigma^2}.
  $$

- If $X\sim \mathrm{Bernoulli}(p)$ with log-MGF $\Lambda(\theta)=\log\big((1-p)+p e^{\theta}\big)$, then the Cramér transform is
  $$
  I(x)=
  \begin{cases}
  x\log\!\left(\frac{x}{p}\right)+(1-x)\log\!\left(\frac{1-x}{1-p}\right), & x\in[0,1],\\
  +\infty, & x\notin[0,1].
  \end{cases}
  $$
