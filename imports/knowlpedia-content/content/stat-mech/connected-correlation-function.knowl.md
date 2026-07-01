+++
id = "stat-mech/connected-correlation-function"
title = "Connected Correlation Function"
kind = "knowl"
summary = "Correlation with disconnected products removed; equals covariance of fluctuations and matches cumulants in Gibbs ensembles."
aliases = ["connected-correlation-function", "Connected Correlation Function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/connected-correlation-function.md"
+++

Correlation functions measure how observables fluctuate together in an ensemble. The **connected** correlation function subtracts the part explained by separate averages, isolating the genuinely correlated component. For two observables, this is exactly a covariance; for higher orders, it generalizes to cumulants.

## Two-point definition
For observables $A$ and $B$,
$$
\langle AB\rangle_c
\;:=\;
\langle AB\rangle - \langle A\rangle\langle B\rangle.
$$

Equivalently, in terms of the [[stat-mech/fluctuation-observable|fluctuations]] $\delta A = A-\langle A\rangle$ and $\delta B = B-\langle B\rangle$,
$$
\langle AB\rangle_c = \langle \delta A\,\delta B\rangle.
$$

For local observables $A_x,B_y$, the connected two-point function is
$$
G^{(c)}_{AB}(x,y) := \langle A_x B_y\rangle_c,
$$
and it is the connected version of the [[stat-mech/correlation-function-two-point|two-point correlation function]].

## Relation to variance and covariance
- Setting $A=B$ gives the variance:
  $$
  \langle A^2\rangle_c = \mathrm{Var}(A),
  $$
  which connects connectedness to [[stat-mech/variance-observable-ensemble|ensemble variance]].

- In general,
  $$
  \langle AB\rangle_c = \mathrm{Cov}(A,B),
  $$
  matching [[stat-mech/covariance-observables-ensemble|ensemble covariance]].

## Connected correlations as cumulants
In Gibbs-type ensembles, connected correlations are the natural objects produced by differentiating $\log Z$ rather than $Z$. This is the content of [[stat-mech/construction-connected-correlations-cumulants|connected correlations as cumulants]] and [[stat-mech/construction-cumulant-generating-function|cumulant generating functions]]: derivatives of $\log Z$ with respect to fields coupled to observables generate connected correlation functions.

## Physical interpretation
- **Remove “trivial” correlations:** If $\langle A\rangle$ and $\langle B\rangle$ are nonzero, the unconnected correlator $\langle AB\rangle$ can be dominated by the product $\langle A\rangle\langle B\rangle$. The connected correlator subtracts this, leaving the part due to correlated fluctuations.

- **Clustering and phases:** In many equilibrium phases away from criticality, connected correlations decay with separation, defining a finite [[stat-mech/correlation-length|correlation length]]. Near critical points, connected correlations can become long-ranged, and their spatial integral controls macroscopic responses such as [[stat-mech/susceptibility-stat-mech|susceptibility]].
