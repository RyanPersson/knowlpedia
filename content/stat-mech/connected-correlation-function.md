---
title: "Connected Correlation Function"
description: "Correlation with disconnected products removed; equals covariance of fluctuations and matches cumulants in Gibbs ensembles."
---

Correlation functions measure how observables fluctuate together in an ensemble. The **connected** correlation function subtracts the part explained by separate averages, isolating the genuinely correlated component. For two observables, this is exactly a covariance; for higher orders, it generalizes to cumulants.

## Two-point definition
For observables $A$ and $B$,
$$
\langle AB\rangle_c
\;:=\;
\langle AB\rangle - \langle A\rangle\langle B\rangle.
$$

Equivalently, in terms of the {{< knowl id="fluctuation-observable" text="fluctuations" >}} $\delta A = A-\langle A\rangle$ and $\delta B = B-\langle B\rangle$,
$$
\langle AB\rangle_c = \langle \delta A\,\delta B\rangle.
$$

For local observables $A_x,B_y$, the connected two-point function is
$$
G^{(c)}_{AB}(x,y) := \langle A_x B_y\rangle_c,
$$
and it is the connected version of the {{< knowl id="correlation-function-two-point" text="two-point correlation function" >}}.

## Relation to variance and covariance
- Setting $A=B$ gives the variance:
  $$
  \langle A^2\rangle_c = \mathrm{Var}(A),
  $$
  which connects connectedness to {{< knowl id="variance-observable-ensemble" text="ensemble variance" >}}.

- In general,
  $$
  \langle AB\rangle_c = \mathrm{Cov}(A,B),
  $$
  matching {{< knowl id="covariance-observables-ensemble" text="ensemble covariance" >}}.

## Connected correlations as cumulants
In Gibbs-type ensembles, connected correlations are the natural objects produced by differentiating $\log Z$ rather than $Z$. This is the content of {{< knowl id="construction-connected-correlations-cumulants" text="connected correlations as cumulants" >}} and {{< knowl id="construction-cumulant-generating-function" text="cumulant generating functions" >}}: derivatives of $\log Z$ with respect to fields coupled to observables generate connected correlation functions.

## Physical interpretation
- **Remove “trivial” correlations:** If $\langle A\rangle$ and $\langle B\rangle$ are nonzero, the unconnected correlator $\langle AB\rangle$ can be dominated by the product $\langle A\rangle\langle B\rangle$. The connected correlator subtracts this, leaving the part due to correlated fluctuations.

- **Clustering and phases:** In many equilibrium phases away from criticality, connected correlations decay with separation, defining a finite {{< knowl id="correlation-length" text="correlation length" >}}. Near critical points, connected correlations can become long-ranged, and their spatial integral controls macroscopic responses such as {{< knowl id="susceptibility-stat-mech" text="susceptibility" >}}.
