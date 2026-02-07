---
title: "Relative entropy (KL divergence)"
description: "A directed measure of discrepancy between two probability distributions, defined by an expectation of a log-likelihood ratio."
---

A **relative entropy (Kullback–Leibler divergence)** is an extended real number $D_{\mathrm{KL}}(P\|Q)$ associated to two {{< knowl id="probability-measure" text="probability measures" >}} $P$ and $Q$ on the same measurable space, defined (when $P$ is absolutely continuous with respect to $Q$) by
\[
D_{\mathrm{KL}}(P\|Q)\;=\;\int \log\!\Big(\frac{dP}{dQ}\Big)\,dP,
\]
where $\frac{dP}{dQ}$ is the Radon–Nikodym derivative (see the {{< knowl id="radon-nikodym-theorem" text="Radon–Nikodym theorem" >}}). If $P$ is not absolutely continuous with respect to $Q$, one sets $D_{\mathrm{KL}}(P\|Q)=+\infty$.

In the discrete case with mass functions $p,q$ on a countable set, this becomes
\[
D_{\mathrm{KL}}(P\|Q)=\sum_x p(x)\,\log\frac{p(x)}{q(x)},
\]
with the convention that terms with $p(x)=0$ contribute $0$, and any $x$ with $p(x)>0$ and $q(x)=0$ forces $D_{\mathrm{KL}}(P\|Q)=+\infty$. Relative entropy is always nonnegative by {{< knowl id="gibbs-inequality-kl" text="Gibbs' inequality" >}}, equals $0$ iff $P=Q$ (in the appropriate sense), and is not symmetric in general. It is related to other discrepancy notions such as {{< knowl id="total-variation-distance" text="total variation distance" >}} (for example via {{< knowl id="pinsker-inequality" text="Pinsker's inequality" >}}).

**Examples:**
- If $P=\mathrm{Bernoulli}(p)$ and $Q=\mathrm{Bernoulli}(q)$ with $p,q\in(0,1)$, then
  \[
  D_{\mathrm{KL}}(P\|Q)=p\log\frac{p}{q}+(1-p)\log\frac{1-p}{1-q}.
  \]
- If $P=\mathcal{N}(\mu_1,\sigma^2)$ and $Q=\mathcal{N}(\mu_2,\sigma^2)$ with the same variance $\sigma^2>0$, then
  \[
  D_{\mathrm{KL}}(P\|Q)=\frac{(\mu_1-\mu_2)^2}{2\sigma^2}.
  \]
