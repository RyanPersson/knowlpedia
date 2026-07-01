+++
id = "large-deviations/gartner-ellis-theorem"
title = "Gärtner–Ellis theorem"
kind = "knowl"
summary = "A large deviation principle obtained from limits of scaled log moment generating functions."
aliases = ["gartner-ellis-theorem", "Gärtner–Ellis theorem"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/gartner-ellis-theorem.md"
+++

**Gärtner–Ellis theorem:** Let $(Z_n)$ be $\mathbb{R}^d$-valued [[probability/random-variable|random variables]] and let $a_n\to\infty$. Define the scaled [[large-deviations/log-moment-generating-function|log moment generating function]]
\[
\Lambda_n(\theta)=\frac{1}{a_n}\log \mathbb{E}\bigl[\exp\bigl(a_n\langle \theta, Z_n\rangle\bigr)\bigr],\qquad \theta\in\mathbb{R}^d,
\]
and assume the pointwise limit $\Lambda(\theta)=\lim_{n\to\infty}\Lambda_n(\theta)$ exists in $(-\infty,\infty]$ for all $\theta$. Suppose that $\Lambda$ is lower semicontinuous, its effective domain $\{\theta:\Lambda(\theta)<\infty\}$ has nonempty interior, and $\Lambda$ is differentiable on the interior of its effective domain and steep (meaning $\|\nabla \Lambda(\theta_k)\|\to\infty$ whenever $(\theta_k)$ approaches the boundary of the effective domain). Then $(Z_n)$ satisfies a [[large-deviations/large-deviation-principle|large deviation principle]] on $\mathbb{R}^d$ with speed $a_n$ and [[large-deviations/rate-function|rate function]]
\[
I(x)=\sup_{\theta\in\mathbb{R}^d}\bigl\{\langle \theta,x\rangle-\Lambda(\theta)\bigr\}.
\]

The function $I$ is the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]] of $\Lambda$. For empirical means of i.i.d. real variables, this recovers [[large-deviations/cramers-theorem|Cramér's theorem]] under standard regularity assumptions.
