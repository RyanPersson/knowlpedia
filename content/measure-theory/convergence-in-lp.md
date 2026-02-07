---
title: "Convergence in $L^p$"
description: "Norm convergence in an Lp space."
---

A **convergence in $L^p$** is norm convergence in a {{< knowl id="lp-space" text="Lp space" >}}. Let $(X,\mathcal{A},\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $1\le p<\infty$. A {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} $(f_n)$ in $L^p(X)$ **converges in $L^p$** to $f\in L^p(X)$ if
$$
\|f_n-f\|_p \to 0 \quad \text{as } n\to\infty,
$$

where $\|\cdot\|_p$ is the {{< knowl id="lp-norm" text="Lp norm" >}}. For $p=\infty$, one defines convergence in $L^\infty$ by $\|f_n-f\|_\infty\to 0$, where $\|\cdot\|_\infty$ is the essential supremum norm (see {{< knowl id="essential-supremum" text="essential supremum" >}}).

Convergence in $L^p$ controls the size of the error in an averaged sense. In particular, for $1\le p<\infty$ the estimate
$$
\mu(\{|f_n-f|>\varepsilon\}) \le \varepsilon^{-p}\|f_n-f\|_p^p
$$

shows that convergence in $L^p$ implies {{< knowl id="convergence-in-measure" text="convergence in measure" >}}.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the functions $f_n(x)=x^n$ satisfy $f_n\to 0$ in $L^p$ for every $1\le p<\infty$ since
  $$
  \|f_n\|_p^p=\int_0^1 x^{np}\,dx=\frac{1}{np+1}\to 0.
  $$

- On $([0,1],\mathcal{B},\lambda)$ and for fixed $1\le p<\infty$, the functions $g_n = n^{1/p}\mathbf{1}_{[0,1/n]}$ satisfy $g_n\to 0$ in measure, but not in $L^p$, because
  $$
  \|g_n\|_p^p = \int_0^{1/n} n\,dx = 1
  $$

  for all $n$.
