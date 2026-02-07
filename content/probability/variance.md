---
title: "Variance"
description: "A measure of how spread out a random variable is around its mean."
---

A **variance** of a {{< knowl id="random-variable" text="random variable" >}} \(X\) is the quantity
\[
\operatorname{Var}(X)=\mathbb E\big[(X-\mathbb E[X])^2\big],
\]
defined when \(\mathbb E[X^2]<\infty\) (so in particular the {{< knowl id="expectation" text="expectation" >}} \(\mathbb E[X]\) is finite). Equivalently,
\[
\operatorname{Var}(X)=\mathbb E[X^2]-\big(\mathbb E[X]\big)^2.
\]

Variance is the second centered {{< knowl id="moment" text="moment" >}} of \(X\). It is also the special case \(\operatorname{Var}(X)=\operatorname{Cov}(X,X)\) of {{< knowl id="covariance" text="covariance" >}}, and it is used to normalize {{< knowl id="covariance" text="covariance" >}} into the {{< knowl id="correlation-coefficient" text="correlation coefficient" >}}.

**Examples:**
- If \(X\) is Bernoulli\((p)\) (so \(\mathbb P(X=1)=p\), \(\mathbb P(X=0)=1-p\)), then \(\operatorname{Var}(X)=p(1-p)\).
- If \(X\sim N(\mu,\sigma^2)\), then \(\operatorname{Var}(X)=\sigma^2\).
