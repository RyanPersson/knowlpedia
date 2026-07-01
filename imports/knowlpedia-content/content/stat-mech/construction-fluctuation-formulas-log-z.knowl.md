+++
id = "stat-mech/construction-fluctuation-formulas-log-z"
title = "Fluctuation formulas from log Z"
kind = "knowl"
summary = "How derivatives of the log partition function generate variances, covariances, and response coefficients in equilibrium ensembles."
aliases = ["construction-fluctuation-formulas-log-z", "Fluctuation formulas from log Z"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-fluctuation-formulas-log-z.md"
+++

In equilibrium statistical mechanics, the logarithm of the partition function is the central generator of *both* mean values and fluctuations. Starting from the [[stat-mech/partition-function-canonical|canonical partition function]] in the [[stat-mech/canonical-ensemble|canonical ensemble]],
one can systematically obtain fluctuation and response formulas by differentiating $\log Z$ with respect to the parameters that couple to observables.

## Setup: parameters conjugate to observables

Let a family of Hamiltonians depend smoothly on parameters $\lambda=(\lambda_1,\dots,\lambda_m)$, and define the canonical partition function
$$
Z(\beta,\lambda) \;=\; \int_{\Gamma} \exp\!\big(-\beta\,H(x;\lambda)\big)\, \mathrm{d}\mu(x),
$$

where $\beta$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]] and $\mathrm{d}\mu$ is the underlying measure on [[stat-mech/phase-space-classical|phase space]] (see [[stat-mech/phase-space-volume-element|phase-space volume element]] for the classical case). The associated [[stat-mech/ensemble-average|ensemble average]] is
$$
\langle A\rangle_{\beta,\lambda}
\;=\;
\frac{1}{Z(\beta,\lambda)}\int_{\Gamma} A(x)\,e^{-\beta H(x;\lambda)}\,\mathrm{d}\mu(x).
$$

A particularly important (and common) parametrization is a *linear coupling* to observables $A_i$:
$$
H(x;\lambda) \;=\; H_0(x) \;-\; \sum_{i=1}^m \lambda_i\,A_i(x).
$$

In that case, each $\lambda_i$ is a “field” conjugate to $A_i$.

## First derivatives: means

Differentiate $\log Z$ under the integral sign (when justified; in practice this is ensured by standard dominated-convergence conditions). One obtains the general identity
$$
\frac{\partial}{\partial \lambda_i}\log Z(\beta,\lambda)
\;=\;
-\beta\,\Big\langle \frac{\partial H}{\partial \lambda_i}\Big\rangle_{\beta,\lambda}.
$$

For linear couplings $\partial_{\lambda_i}H=-A_i$, this becomes
$$
\frac{\partial}{\partial \lambda_i}\log Z(\beta,\lambda)
\;=\;
\beta\,\langle A_i\rangle_{\beta,\lambda}.
$$

A special case is differentiation with respect to $\beta$:
$$
\frac{\partial}{\partial \beta}\log Z(\beta,\lambda)
\;=\;
-\langle H\rangle_{\beta,\lambda}.
$$

Thus $\log Z$ encodes the mean energy directly.

These identities are the core of [[stat-mech/construction-observables-from-log-z|constructing observables from log Z]].

## Second derivatives: variances and covariances

Second derivatives produce fluctuations. For linear couplings, the mixed second derivative is
$$
\frac{\partial^2}{\partial \lambda_i\,\partial \lambda_j}\log Z(\beta,\lambda)
\;=\;
\beta^2\,\mathrm{Cov}_{\beta,\lambda}(A_i,A_j),
$$

where $\mathrm{Cov}(A_i,A_j)=\langle A_iA_j\rangle-\langle A_i\rangle\langle A_j\rangle$ (see [[stat-mech/covariance-observables-ensemble|covariance in an ensemble]]).

In particular,
$$
\frac{\partial^2}{\partial \lambda_i^2}\log Z(\beta,\lambda)
\;=\;
\beta^2\,\mathrm{Var}_{\beta,\lambda}(A_i),
$$

recovering the [[stat-mech/variance-observable-ensemble|variance formula]] as a derivative of $\log Z$.

For energy fluctuations (no $\lambda$ needed),
$$
\frac{\partial^2}{\partial \beta^2}\log Z(\beta)
\;=\;
\mathrm{Var}_\beta(H),
$$

since $\partial_\beta \log Z=-\langle H\rangle$ and $\partial_\beta \langle H\rangle=-\mathrm{Var}(H)$.

These are the canonical “fluctuation formulas” (see also [[stat-mech/fluctuation-observable|fluctuations of an observable]]).

## Physical interpretation: response = fluctuations

If $\lambda$ is a physical field, then $\partial_{\lambda}\langle A\rangle$ is a linear response coefficient (a susceptibility). From the identities above,
$$
\frac{\partial}{\partial \lambda_j}\langle A_i\rangle_{\beta,\lambda}
\;=\;
\beta\,\mathrm{Cov}_{\beta,\lambda}(A_i,A_j),
$$
so response is controlled by equilibrium fluctuations. In common cases this is exactly the equilibrium form of a fluctuation–dissipation relation (compare with [[stat-mech/susceptibility-stat-mech|susceptibility]]).

## Higher derivatives: cumulants

More generally, *all* higher derivatives of $\log Z$ generate higher-order connected moments (cumulants). This perspective is made explicit in
[[stat-mech/construction-cumulant-generating-function|the cumulant generating function construction]]
and in
[[stat-mech/construction-connected-correlations-cumulants|connected correlations as cumulants]].

Finally, the thermodynamic potentials inherit these derivative structures via $F=-(1/\beta)\log Z$ (see [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] and [[stat-mech/free-energy-statistical|free energy in statistical mechanics]]): convexity/concavity properties of $\log Z$ translate into stability conditions and positivity of variances.
