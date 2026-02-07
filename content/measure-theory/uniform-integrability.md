---
title: "Uniform integrability"
description: "A condition preventing L1 functions from concentrating too much mass on large values or small sets."
---

A **uniformly integrable** family is a collection of integrable functions whose mass cannot escape to arbitrarily large values on sets of small measure. Let $(X,\mathcal{A},\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $\mathcal{F}\subset L^1(X)$ (see {{< knowl id="l1-function" text="L1 function" >}}). The family $\mathcal{F}$ is **uniformly integrable** if
$$
\lim_{M\to\infty}\ \sup_{f\in\mathcal{F}} \int_{\{|f|>M\}} |f|\,d\mu = 0.
$$

A {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} $(f_n)$ is uniformly integrable if the set $\{f_n:\ n\ge 1\}$ is uniformly integrable.

Uniform integrability is used to justify passing limits through the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}} when one only has weaker convergence, such as {{< knowl id="convergence-in-measure" text="convergence in measure" >}}; it rules out “spikes” that carry significant integral while living on very small sets.

**Examples:**
- If $(f_n)$ satisfies $|f_n|\le g$ almost everywhere for some $g\in L^1(X)$, then $\{f_n\}$ is uniformly integrable; the integrable envelope $g$ forces the tail integrals over $\{|f_n|>M\}$ to be small uniformly in $n$.
- On $([0,1],\mathcal{B},\lambda)$, the functions $f_n = n\,\mathbf{1}_{[0,1/n]}$ are not uniformly integrable: for any $M>0$ choose $n>M$, then
  $$
  \int_{\{|f_n|>M\}} |f_n|\,d\lambda = \int_0^{1/n} n\,dx = 1,
  $$

  so the supremum of the tail integrals does not go to $0$ as $M\to\infty$.
