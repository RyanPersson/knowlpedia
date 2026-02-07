---
title: "Differential entropy"
description: "The entropy of a continuous distribution defined via an integral of the log-density."
---

A **differential entropy** is a number $h(X)$ associated to a real-valued {{< knowl id="random-variable" text="random variable" >}} $X$ that admits a density $f$ (with respect to {{< knowl id="lebesgue-measure" section="measure-theory" text="Lebesgue measure" >}}), defined by
\[
h(X)\;=\;-\int_{\mathbb{R}} f(x)\,\log f(x)\,dx,
\]
where the integral is understood as a {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}} (and $\log$ is typically the natural logarithm).

Differential entropy resembles {{< knowl id="shannon-entropy" text="Shannon entropy" >}} but behaves differently: it can be negative and it is not invariant under changes of variables (for instance, scaling $X$ shifts $h(X)$ by an additive constant). It is used in continuous-information settings and in the {{< knowl id="maximum-entropy-principle" text="maximum entropy principle" >}} for continuous distributions.

**Examples:**
- If $X\sim \mathcal{N}(\mu,\sigma^2)$, then $h(X)=\tfrac12\log(2\pi e\,\sigma^2)$.
- If $X$ is uniform on $[0,1]$, then $h(X)=0$.
