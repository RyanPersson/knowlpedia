---
title: "Generalized Gibbs ensemble (GGE)"
description: "Maximum-entropy equilibrium state constrained by multiple (often extensive) conserved quantities."
---


A **generalized Gibbs ensemble** (GGE) is an equilibrium distribution obtained by maximizing entropy subject to *several* expectation-value constraints, typically associated with conserved quantities. It generalizes the familiar {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} (energy constraint) and {{< knowl id="grand-canonical-ensemble" text="grand-canonical ensemble" >}} (energy and particle-number constraints).

Let $\{Q_i\}_{i\in I}$ be a collection of observables (often commuting conserved quantities in the dynamics). The GGE is defined as the entropy maximizer among all states with prescribed expectations $\langle Q_i\rangle = q_i$ for all $i\in I$, where entropy is taken as the {{< knowl id="gibbs-entropy-shannon" text="Gibbs/Shannon entropy" >}} (compare the probabilistic {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}).

## Maximum-entropy construction

The variational principle (see {{< knowl id="construction-entropy-maximization-thermal" text="entropy maximization construction" >}}) yields a state of exponential form. In quantum language, the density operator is
$$
\rho_{\mathrm{GGE}} = \frac{1}{Z_{\mathrm{GGE}}}\exp\!\Big(-\sum_{i\in I}\lambda_i Q_i\Big),
$$

where the $\lambda_i$ are Lagrange multipliers fixed by the constraints, and the normalization is
$$
Z_{\mathrm{GGE}} = \mathrm{Tr}\,\exp\!\Big(-\sum_{i\in I}\lambda_i Q_i\Big).
$$

In a classical phase-space description, the same structure appears as a probability density on {{< knowl id="phase-space-classical" text="phase space" >}} with weight $\exp(-\sum_i \lambda_i Q_i(x))$ relative to the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}}.

The multipliers $\lambda_i$ can be interpreted as **generalized inverse temperatures** conjugate to the conserved quantities $Q_i$. The ordinary inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}) is recovered when one of the constraints is the energy $H$.

## Special cases and interpretation

- If the only constrained quantity is the energy $Q_1 = H$, then $\rho_{\mathrm{GGE}}$ reduces to the canonical Gibbs state (see {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}), with $\lambda_1=\beta$.
- If energy and particle number are constrained, $Q_1=H$ and $Q_2=N$, the GGE reduces to the grand-canonical state (see {{< knowl id="grand-canonical-ensemble" text="grand-canonical ensemble" >}}), with multipliers $(\beta,-\beta\mu)$ where $\mu$ is the {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}.

Physically, the GGE is useful when there are *many* relevant constraints (for example in integrable models with an extensive family of conserved quantities), in which case a small set of thermodynamic parameters is insufficient to characterize equilibrium.

## Partition function, convexity, and generating relations

The logarithm of the GGE normalization,
$$
\psi(\lambda) = \ln Z_{\mathrm{GGE}}(\{\lambda_i\}),
$$
plays the role of a cumulant-generating function (see {{< knowl id="construction-cumulant-generating-function" text="cumulant generating functions" >}}). Differentiation generates constrained expectations:
$$
\langle Q_i\rangle_{\mathrm{GGE}} = -\frac{\partial \ln Z_{\mathrm{GGE}}}{\partial \lambda_i},
\qquad
\mathrm{Cov}(Q_i,Q_j)_{\mathrm{GGE}} = \frac{\partial^2 \ln Z_{\mathrm{GGE}}}{\partial \lambda_i\,\partial \lambda_j}.
$$
This expresses fluctuation structure in the same way as in standard Gibbs ensembles (see {{< knowl id="construction-connected-correlations-cumulants" text="connected correlations and cumulants" >}}).

From a mathematical standpoint, $\psi(\lambda)$ is convex in the multipliers, reflecting general properties of log-partition functions connected to {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transforms" >}} and thermodynamic duality.
