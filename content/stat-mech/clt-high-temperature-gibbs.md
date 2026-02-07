---
title: "Central Limit Theorem in the High-Temperature Gibbs Regime"
description: "A CLT for spatial sums of local observables under a unique high-temperature Gibbs measure, with variance given by the integrated covariance (susceptibility-type) formula."
---

## Prerequisites

- {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}
- {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}
- {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}
- {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}
- {{< knowl id="expectation" section="probability" text="expectation" >}}
- {{< knowl id="variance" section="probability" text="variance" >}}
- {{< knowl id="cluster-expansion-theorem" text="cluster expansion theorem" >}}

## Setting

Let $\mu$ be a translation-invariant infinite-volume Gibbs measure on $\mathbb{Z}^d$ (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}), arising from a finite-range interaction in a **high-temperature / uniqueness regime** (for example, a parameter region where a {{< knowl id="cluster-expansion-theorem" text="cluster expansion" >}} yields exponential decay of correlations).

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

- The high-temperature (uniqueness) regime typically implies exponential decay of {{< knowl id="correlation-function-two-point" section="stat-mech" text="correlations" >}} and a finite {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}, which is precisely what makes the covariance sum converge.
- The variance formula above is the $k=0$ limit of a Fourier-space fluctuation observable; it connects naturally to {{< knowl id="structure-factor" text="structure factor" >}}.
- At or near criticality (large correlation length), the covariance sum may diverge or decay too slowly, and the CLT can fail or require non-Gaussian scaling limits (see {{< knowl id="critical-exponent" text="critical exponents" >}} and {{< knowl id="scaling-relation-exponents" text="scaling relations" >}} for how this is encoded in critical behavior).
