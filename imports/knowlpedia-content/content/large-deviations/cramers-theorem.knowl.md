+++
id = "large-deviations/cramers-theorem"
title = "Cramér's theorem"
kind = "knowl"
summary = "Large deviations for empirical means of independent identically distributed real random variables."
aliases = ["cramers-theorem", "Cramér's theorem"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/cramers-theorem.md"
+++

**Cramér's theorem:** Let $(X_i)_{i\ge 1}$ be an [[probability/iid-sequence|i.i.d. sequence]] of real-valued [[probability/random-variable|random variables]]. Assume the [[probability/moment-generating-function|moment generating function]] $M(\theta)=\mathbb{E}[e^{\theta X_1}]$ is finite for all $\theta$ in some open interval containing $0$, and let $\Lambda(\theta)=\log M(\theta)$ be the [[large-deviations/log-moment-generating-function|log moment generating function]]. Define the empirical mean $\overline X_n=\frac{1}{n}\sum_{i=1}^n X_i$. Then $(\overline X_n)$ satisfies a [[large-deviations/large-deviation-principle|large deviation principle]] on $\mathbb{R}$ with speed $n$ and [[large-deviations/good-rate-function|good rate function]]
\[
I(x)=\sup_{\theta\in\mathbb{R}}\bigl\{\theta x-\Lambda(\theta)\bigr\}.
\]

The rate function $I$ is the [[large-deviations/cramer-transform|Cramér transform]], i.e. the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]] ([[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]) of $\Lambda$.
