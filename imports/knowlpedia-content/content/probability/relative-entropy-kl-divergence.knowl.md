+++
id = "probability/relative-entropy-kl-divergence"
title = "Relative entropy (KL divergence)"
kind = "knowl"
summary = "A directed measure of discrepancy between two probability distributions, defined by an expectation of a log-likelihood ratio."
aliases = ["relative-entropy-kl-divergence", "Relative entropy (KL divergence)"]
domains = ["probability"]
legacy_source_path = "probability/relative-entropy-kl-divergence.md"
+++

A **relative entropy (Kullback–Leibler divergence)** is an extended real number $D_{\mathrm{KL}}(P\|Q)$ associated to two [[probability/probability-measure|probability measures]] $P$ and $Q$ on the same measurable space, defined (when $P$ is absolutely continuous with respect to $Q$) by
\[
D_{\mathrm{KL}}(P\|Q)\;=\;\int \log\!\Big(\frac{dP}{dQ}\Big)\,dP,
\]
where $\frac{dP}{dQ}$ is the Radon–Nikodym derivative (see the [[probability/radon-nikodym-theorem|Radon–Nikodym theorem]]). If $P$ is not absolutely continuous with respect to $Q$, one sets $D_{\mathrm{KL}}(P\|Q)=+\infty$.

In the discrete case with mass functions $p,q$ on a countable set, this becomes
\[
D_{\mathrm{KL}}(P\|Q)=\sum_x p(x)\,\log\frac{p(x)}{q(x)},
\]
with the convention that terms with $p(x)=0$ contribute $0$, and any $x$ with $p(x)>0$ and $q(x)=0$ forces $D_{\mathrm{KL}}(P\|Q)=+\infty$. Relative entropy is always nonnegative by [[probability/gibbs-inequality-kl|Gibbs' inequality]], equals $0$ iff $P=Q$ (in the appropriate sense), and is not symmetric in general. It is related to other discrepancy notions such as [[probability/total-variation-distance|total variation distance]] (for example via [[probability/pinsker-inequality|Pinsker's inequality]]).

**Examples:**
- If $P=\mathrm{Bernoulli}(p)$ and $Q=\mathrm{Bernoulli}(q)$ with $p,q\in(0,1)$, then
  \[
  D_{\mathrm{KL}}(P\|Q)=p\log\frac{p}{q}+(1-p)\log\frac{1-p}{1-q}.
  \]
- If $P=\mathcal{N}(\mu_1,\sigma^2)$ and $Q=\mathcal{N}(\mu_2,\sigma^2)$ with the same variance $\sigma^2>0$, then
  \[
  D_{\mathrm{KL}}(P\|Q)=\frac{(\mu_1-\mu_2)^2}{2\sigma^2}.
  \]
