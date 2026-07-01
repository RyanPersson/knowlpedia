+++
id = "stat-mech/prop-connected-correlations-derivatives"
title = "Connected correlations as derivatives of expectations"
kind = "knowl"
summary = "In Gibbs ensembles, derivatives with respect to conjugate parameters yield covariances (connected two-point functions) and higher cumulants."
aliases = ["prop-connected-correlations-derivatives", "Connected correlations as derivatives of expectations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/prop-connected-correlations-derivatives.md"
+++

Let $\mu_\lambda$ be a Gibbs/ensemble measure (e.g. [[stat-mech/canonical-ensemble|canonical ensemble]] or [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]]) whose Hamiltonian depends on a real parameter $\lambda$ via a linear coupling to an observable $A$:
$$
H_\lambda = H_0 - \lambda A.
$$

Let $\langle \cdot\rangle_\lambda$ denote [[stat-mech/ensemble-average|ensemble averages]] with respect to $\mu_\lambda$.

## Statement
For any integrable observable $B$,
$$
\frac{\partial}{\partial\lambda}\,\langle B\rangle_\lambda
= \beta\Big(\langle A\,B\rangle_\lambda-\langle A\rangle_\lambda\,\langle B\rangle_\lambda\Big).
$$
In other words,
$$
\frac{\partial}{\partial\lambda}\,\langle B\rangle_\lambda
= \beta\,\mathrm{Cov}_\lambda(A,B),
$$

where $\mathrm{Cov}_\lambda(A,B)$ is the (two-point) connected correlation, i.e. the [[stat-mech/correlation-function-two-point|connected two-point function]] at the level of observables.

In particular, for the partition function $Z(\lambda)$ ([[stat-mech/partition-function-canonical|canonical]] or [[stat-mech-lattice/partition-function-lattice|lattice]]),
$$
\frac{\partial^2}{\partial\lambda^2}\log Z(\lambda)
= \beta^2\,\mathrm{Var}_\lambda(A),
$$
with variance as in [[stat-mech/variance-observable-ensemble|variance in an ensemble]].

More generally, if one introduces sources $\boldsymbol{\lambda}=(\lambda_1,\dots,\lambda_k)$ coupled to observables $(A_1,\dots,A_k)$, then mixed partial derivatives of $\log Z(\boldsymbol{\lambda})$ generate higher connected correlations (cumulants).

## Key hypotheses
- The parameter enters linearly: $H_\lambda=H_0-\lambda A$ (or, more generally, differentiably with $\partial_\lambda H_\lambda=-A$).
- The relevant derivatives can be passed under the integral/sum defining $\langle\cdot\rangle_\lambda$ (automatic in finite volume with bounded observables).
- $\beta>0$ is fixed (inverse temperature).

## Conclusions
- Response of $B$ to the field conjugate to $A$ is controlled by their covariance.
- Taking $B=A$ recovers a fluctuation identity:
  $$
  \partial_\lambda\langle A\rangle_\lambda=\beta\,\mathrm{Var}_\lambda(A)\ge 0.
  $$
- This packages many “susceptibility = fluctuation” statements, including [[stat-mech/prop-susceptibility-variance-magnetization|susceptibility–variance for magnetization]] as a special case.
