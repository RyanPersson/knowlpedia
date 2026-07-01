+++
id = "stat-mech/covariance-observables-ensemble"
title = "Ensemble Covariance of Two Observables"
kind = "knowl"
summary = "The mixed second central moment ⟨(A−⟨A⟩)(B−⟨B⟩)⟩ measuring joint fluctuations and linear response."
aliases = ["covariance-observables-ensemble", "Ensemble Covariance of Two Observables"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/covariance-observables-ensemble.md"
+++

For two observables $A$ and $B$ in a fixed ensemble (so [[stat-mech/ensemble-average|⟨·⟩]] is defined), the **covariance** measures how their deviations from their means fluctuate together. It is the ensemble version of [[probability/covariance|covariance]].

The **ensemble covariance** is
$$
\mathrm{Cov}(A,B)
\;:=\;
\left\langle \bigl(A-\langle A\rangle\bigr)\bigl(B-\langle B\rangle\bigr)\right\rangle
\;=\;
\langle \delta A\,\delta B\rangle,
$$

where $\delta A$ and $\delta B$ are the [[stat-mech/fluctuation-observable|fluctuations]] of $A$ and $B$.

Equivalently,
$$
\mathrm{Cov}(A,B) = \langle AB\rangle - \langle A\rangle\langle B\rangle.
$$

Special cases:
- $\mathrm{Cov}(A,A)=\mathrm{Var}(A)$, connecting covariance to [[stat-mech/variance-observable-ensemble|variance]].
- For local observables $A_x,B_y$, the quantity $\mathrm{Cov}(A_x,B_y)$ is precisely the two-point [[stat-mech/connected-correlation-function|connected correlation]].

## Key properties
For real-valued observables:
- Symmetry: $\mathrm{Cov}(A,B)=\mathrm{Cov}(B,A)$.
- Bilinearity in each argument.
- Cauchy–Schwarz bound:
  $$
  |\mathrm{Cov}(A,B)| \le \sqrt{\mathrm{Var}(A)\,\mathrm{Var}(B)}.
  $$

These statements formalize the idea that covariance measures *shared* fluctuations.

## Covariance and response (Gibbs ensembles)
In Gibbs-type ensembles built from a [[stat-mech/hamiltonian-function-classical|Hamiltonian]] and external fields, covariances arise as derivatives of expectations with respect to those fields (see [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from log Z]]).

A standard schematic setting is a canonical weight proportional to $\exp[-\beta(H - hB)]$ (field $h$ coupled linearly to $B$). Then the sensitivity of $\langle A\rangle$ to the field is controlled by $\mathrm{Cov}(A,B)$:
$$
\frac{\partial}{\partial h}\langle A\rangle = \beta\,\mathrm{Cov}(A,B).
$$
This is a basic form of fluctuation–response, and it underlies definitions such as [[stat-mech/susceptibility-stat-mech|susceptibility]].

## Physical interpretation
- $\mathrm{Cov}(A,B)>0$ means that when $A$ fluctuates upward from its mean, $B$ tends to do the same.
- $\mathrm{Cov}(A,B)<0$ means upward fluctuations of $A$ tend to coincide with downward fluctuations of $B$.
- Spatially, $\mathrm{Cov}(A_x,B_y)$ diagnoses correlations between fluctuations at different locations and is the building block of the [[stat-mech/correlation-function-two-point|two-point correlation function]] and its connected part.
