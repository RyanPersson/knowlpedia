+++
id = "large-deviations/laplace-principle"
title = "Laplace principle"
kind = "knowl"
summary = "A variational limit for exponential integrals that encodes large-deviation behavior."
aliases = ["laplace-principle", "Laplace principle"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/laplace-principle.md"
+++

A **Laplace principle** for a sequence of [[probability/probability-measure|probability measures]] $(\mu_n)$ on a space $X$, with speed $a_n\to\infty$ and [[large-deviations/rate-function|rate function]] $I\colon X\to[0,\infty]$, is the statement that for every bounded continuous function $\varphi\colon X\to\mathbb{R}$,
\[
\lim_{n\to\infty}\frac{1}{a_n}\log \int_X \exp\bigl(-a_n\varphi(x)\bigr)\,\mu_n(dx)
= -\inf_{x\in X}\bigl\{\varphi(x)+I(x)\bigr\}.
\]

This is the Laplace-transform formulation of the [[large-deviations/large-deviation-principle|large deviation principle]]. Under standard hypotheses (for example, $X$ Polish and $(\mu_n)$ [[large-deviations/exponential-tightness|exponentially tight]]), the Laplace principle with a [[large-deviations/good-rate-function|good rate function]] is equivalent to an LDP with the same rate function.

**Examples:**
- By [[large-deviations/cramers-theorem|Cramér's theorem]], the empirical mean of an [[probability/iid-sequence|i.i.d. sequence]] of real-valued [[probability/random-variable|random variables]] satisfies the Laplace principle with speed $n$ and rate given by the [[large-deviations/cramer-transform|Cramér transform]].
- By [[large-deviations/sanovs-theorem|Sanov's theorem]], the empirical measure of an i.i.d. sample satisfies the Laplace principle with speed $n$ and rate given by [[probability/relative-entropy-kl-divergence|relative entropy]] with respect to the common law.
