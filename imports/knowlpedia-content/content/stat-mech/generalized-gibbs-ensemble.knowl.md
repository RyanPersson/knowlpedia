+++
id = "stat-mech/generalized-gibbs-ensemble"
title = "Generalized Gibbs ensemble (GGE)"
kind = "knowl"
summary = "Maximum-entropy equilibrium state constrained by multiple (often extensive) conserved quantities."
aliases = ["generalized-gibbs-ensemble", "Generalized Gibbs ensemble (GGE)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/generalized-gibbs-ensemble.md"
+++

A **generalized Gibbs ensemble** (GGE) is an equilibrium distribution obtained by maximizing entropy subject to *several* expectation-value constraints, typically associated with conserved quantities. It generalizes the familiar [[stat-mech/canonical-ensemble|canonical ensemble]] (energy constraint) and [[stat-mech/grand-canonical-ensemble|grand-canonical ensemble]] (energy and particle-number constraints).

Let $\{Q_i\}_{i\in I}$ be a collection of observables (often commuting conserved quantities in the dynamics). The GGE is defined as the entropy maximizer among all states with prescribed expectations $\langle Q_i\rangle = q_i$ for all $i\in I$, where entropy is taken as the [[stat-mech/gibbs-entropy-shannon|Gibbs/Shannon entropy]] (compare the probabilistic [[probability/shannon-entropy|Shannon entropy]]).

## Maximum-entropy construction

The variational principle (see [[stat-mech/construction-entropy-maximization-thermal|entropy maximization construction]]) yields a state of exponential form. In quantum language, the density operator is
$$
\rho_{\mathrm{GGE}} = \frac{1}{Z_{\mathrm{GGE}}}\exp\!\Big(-\sum_{i\in I}\lambda_i Q_i\Big),
$$

where the $\lambda_i$ are Lagrange multipliers fixed by the constraints, and the normalization is
$$
Z_{\mathrm{GGE}} = \mathrm{Tr}\,\exp\!\Big(-\sum_{i\in I}\lambda_i Q_i\Big).
$$

In a classical phase-space description, the same structure appears as a probability density on [[stat-mech/phase-space-classical|phase space]] with weight $\exp(-\sum_i \lambda_i Q_i(x))$ relative to the [[stat-mech/phase-space-volume-element|phase-space volume element]].

The multipliers $\lambda_i$ can be interpreted as **generalized inverse temperatures** conjugate to the conserved quantities $Q_i$. The ordinary inverse temperature $\beta$ (see [[thermodynamics/inverse-temperature-beta|inverse temperature]]) is recovered when one of the constraints is the energy $H$.

## Special cases and interpretation

- If the only constrained quantity is the energy $Q_1 = H$, then $\rho_{\mathrm{GGE}}$ reduces to the canonical Gibbs state (see [[stat-mech/canonical-ensemble|canonical ensemble]]), with $\lambda_1=\beta$.
- If energy and particle number are constrained, $Q_1=H$ and $Q_2=N$, the GGE reduces to the grand-canonical state (see [[stat-mech/grand-canonical-ensemble|grand-canonical ensemble]]), with multipliers $(\beta,-\beta\mu)$ where $\mu$ is the [[thermodynamics/chemical-potential-thermo|chemical potential]].

Physically, the GGE is useful when there are *many* relevant constraints (for example in integrable models with an extensive family of conserved quantities), in which case a small set of thermodynamic parameters is insufficient to characterize equilibrium.

## Partition function, convexity, and generating relations

The logarithm of the GGE normalization,
$$
\psi(\lambda) = \ln Z_{\mathrm{GGE}}(\{\lambda_i\}),
$$
plays the role of a cumulant-generating function (see [[stat-mech/construction-cumulant-generating-function|cumulant generating functions]]). Differentiation generates constrained expectations:
$$
\langle Q_i\rangle_{\mathrm{GGE}} = -\frac{\partial \ln Z_{\mathrm{GGE}}}{\partial \lambda_i},
\qquad
\mathrm{Cov}(Q_i,Q_j)_{\mathrm{GGE}} = \frac{\partial^2 \ln Z_{\mathrm{GGE}}}{\partial \lambda_i\,\partial \lambda_j}.
$$
This expresses fluctuation structure in the same way as in standard Gibbs ensembles (see [[stat-mech/construction-connected-correlations-cumulants|connected correlations and cumulants]]).

From a mathematical standpoint, $\psi(\lambda)$ is convex in the multipliers, reflecting general properties of log-partition functions connected to [[convex-analysis/legendre-transform|Legendre transforms]] and thermodynamic duality.
