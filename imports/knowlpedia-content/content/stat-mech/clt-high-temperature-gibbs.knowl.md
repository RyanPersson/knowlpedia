+++
id = "stat-mech/clt-high-temperature-gibbs"
title = "Central Limit Theorem in the High-Temperature Gibbs Regime"
kind = "knowl"
summary = "A CLT for spatial sums of local observables under a unique high-temperature Gibbs measure, with variance given by the integrated covariance (susceptibility-type) formula."
aliases = ["clt-high-temperature-gibbs", "Central Limit Theorem in the High-Temperature Gibbs Regime"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/clt-high-temperature-gibbs.md"
+++

## Prerequisites

- [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]
- [[stat-mech-lattice/dlr-equation|DLR equation]]
- [[stat-mech/correlation-function-two-point|two-point correlation function]]
- [[stat-mech/correlation-length|correlation length]]
- [[probability/expectation|expectation]]
- [[probability/variance|variance]]
- [[stat-mech/cluster-expansion-theorem|cluster expansion theorem]]

## Setting

Let $\mu$ be a translation-invariant infinite-volume Gibbs measure on $\mathbb{Z}^d$ (see [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]), arising from a finite-range interaction in a **high-temperature / uniqueness regime** (for example, a parameter region where a [[stat-mech/cluster-expansion-theorem|cluster expansion]] yields exponential decay of correlations).

Let $f$ be a **local observable** (depends only on finitely many spins) with zero mean:
$$
\mu(f)=0.
$$

Let $\tau_x$ denote the lattice shift by $x$, and define the sum over a finite region $\Lambda\subset\mathbb{Z}^d$:
$$
S_\Lambda = \sum_{x\in\Lambda} f\circ \tau_x.
$$

## Theorem (CLT under high-temperature mixing)

Assume $\mu$ is strongly mixing with summable covariances for $f$, i.e.
$$
\sum_{x\in\mathbb{Z}^d} \big|\mathrm{Cov}_\mu\big(f, f\circ\tau_x\big)\big| < \infty.
$$

Then, for a sequence of boxes $\Lambda_n$ with $|\Lambda_n|\to\infty$,
$$
\frac{S_{\Lambda_n}}{\sqrt{|\Lambda_n|}}
\;\Rightarrow\;
\mathcal{N}(0,\sigma_f^2),
$$
where the asymptotic variance is given by the integrated covariance formula
$$
\sigma_f^2
={}
\sum_{x\in\mathbb{Z}^d}
\mathrm{Cov}_\mu\big(f, f\circ\tau_x\big)
\;\;\in\;[0,\infty).
$$
Moreover,
$$
\lim_{n\to\infty}\frac{\mathrm{Var}_\mu(S_{\Lambda_n})}{|\Lambda_n|}=\sigma_f^2.
$$

A multivariate version holds for finitely many local observables $(f_1,\dots,f_k)$, yielding a Gaussian limit with covariance matrix given by the corresponding summed cross-covariances.

## Interpretation in statistical mechanics

- The high-temperature (uniqueness) regime typically implies exponential decay of [[stat-mech/correlation-function-two-point|correlations]] and a finite [[stat-mech/correlation-length|correlation length]], which is precisely what makes the covariance sum converge.
- The variance formula above is the $k=0$ limit of a Fourier-space fluctuation observable; it connects naturally to [[stat-mech/structure-factor|structure factor]].
- At or near criticality (large correlation length), the covariance sum may diverge or decay too slowly, and the CLT can fail or require non-Gaussian scaling limits (see [[stat-mech/critical-exponent|critical exponents]] and [[stat-mech/scaling-relation-exponents|scaling relations]] for how this is encoded in critical behavior).
