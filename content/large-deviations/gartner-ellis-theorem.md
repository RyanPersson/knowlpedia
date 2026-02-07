---
title: "Gärtner–Ellis theorem"
description: "A large deviation principle obtained from limits of scaled log moment generating functions."
---

**Gärtner–Ellis theorem:** Let $(Z_n)$ be $\mathbb{R}^d$-valued {{< knowl id="random-variable" section="probability" text="random variables" >}} and let $a_n\to\infty$. Define the scaled {{< knowl id="log-moment-generating-function" text="log moment generating function" >}}
\[
\Lambda_n(\theta)=\frac{1}{a_n}\log \mathbb{E}\bigl[\exp\bigl(a_n\langle \theta, Z_n\rangle\bigr)\bigr],\qquad \theta\in\mathbb{R}^d,
\]
and assume the pointwise limit $\Lambda(\theta)=\lim_{n\to\infty}\Lambda_n(\theta)$ exists in $(-\infty,\infty]$ for all $\theta$. Suppose that $\Lambda$ is lower semicontinuous, its effective domain $\{\theta:\Lambda(\theta)<\infty\}$ has nonempty interior, and $\Lambda$ is differentiable on the interior of its effective domain and steep (meaning $\|\nabla \Lambda(\theta_k)\|\to\infty$ whenever $(\theta_k)$ approaches the boundary of the effective domain). Then $(Z_n)$ satisfies a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} on $\mathbb{R}^d$ with speed $a_n$ and {{< knowl id="rate-function" text="rate function" >}}
\[
I(x)=\sup_{\theta\in\mathbb{R}^d}\bigl\{\langle \theta,x\rangle-\Lambda(\theta)\bigr\}.
\]

The function $I$ is the {{< knowl id="legendre-fenchel-transform" section="convex-analysis" text="Legendre–Fenchel transform" >}} of $\Lambda$. For empirical means of i.i.d. real variables, this recovers {{< knowl id="cramers-theorem" text="Cramér's theorem" >}} under standard regularity assumptions.
