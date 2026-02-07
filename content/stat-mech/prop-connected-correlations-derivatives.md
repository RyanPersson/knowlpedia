---
title: "Connected correlations as derivatives of expectations"
description: "In Gibbs ensembles, derivatives with respect to conjugate parameters yield covariances (connected two-point functions) and higher cumulants."
---

Let $\mu_\lambda$ be a Gibbs/ensemble measure (e.g. {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} or {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}) whose Hamiltonian depends on a real parameter $\lambda$ via a linear coupling to an observable $A$:
$$
H_\lambda = H_0 - \lambda A.
$$

Let $\langle \cdot\rangle_\lambda$ denote {{< knowl id="ensemble-average" section="stat-mech" text="ensemble averages" >}} with respect to $\mu_\lambda$.

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

where $\mathrm{Cov}_\lambda(A,B)$ is the (two-point) connected correlation, i.e. the {{< knowl id="correlation-function-two-point" section="stat-mech" text="connected two-point function" >}} at the level of observables.

In particular, for the partition function $Z(\lambda)$ ({{< knowl id="partition-function-canonical" section="stat-mech" text="canonical" >}} or {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="lattice" >}}),
$$
\frac{\partial^2}{\partial\lambda^2}\log Z(\lambda)
= \beta^2\,\mathrm{Var}_\lambda(A),
$$
with variance as in {{< knowl id="variance-observable-ensemble" section="stat-mech" text="variance in an ensemble" >}}.

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
- This packages many “susceptibility = fluctuation” statements, including {{< knowl id="prop-susceptibility-variance-magnetization" text="susceptibility–variance for magnetization" >}} as a special case.

