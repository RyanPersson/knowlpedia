---
title: "Ensemble Covariance of Two Observables"
description: "The mixed second central moment ⟨(A−⟨A⟩)(B−⟨B⟩)⟩ measuring joint fluctuations and linear response."
---

For two observables $A$ and $B$ in a fixed ensemble (so {{< knowl id="ensemble-average" text="⟨·⟩" >}} is defined), the **covariance** measures how their deviations from their means fluctuate together. It is the ensemble version of {{< knowl id="covariance" section="probability" text="covariance" >}}.

The **ensemble covariance** is
$$
\mathrm{Cov}(A,B)
\;:=\;
\left\langle \bigl(A-\langle A\rangle\bigr)\bigl(B-\langle B\rangle\bigr)\right\rangle
\;=\;
\langle \delta A\,\delta B\rangle,
$$

where $\delta A$ and $\delta B$ are the {{< knowl id="fluctuation-observable" text="fluctuations" >}} of $A$ and $B$.

Equivalently,
$$
\mathrm{Cov}(A,B) = \langle AB\rangle - \langle A\rangle\langle B\rangle.
$$

Special cases:
- $\mathrm{Cov}(A,A)=\mathrm{Var}(A)$, connecting covariance to {{< knowl id="variance-observable-ensemble" text="variance" >}}.
- For local observables $A_x,B_y$, the quantity $\mathrm{Cov}(A_x,B_y)$ is precisely the two-point {{< knowl id="connected-correlation-function" text="connected correlation" >}}.

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
In Gibbs-type ensembles built from a {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} and external fields, covariances arise as derivatives of expectations with respect to those fields (see {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuation formulas from log Z" >}}).

A standard schematic setting is a canonical weight proportional to $\exp[-\beta(H - hB)]$ (field $h$ coupled linearly to $B$). Then the sensitivity of $\langle A\rangle$ to the field is controlled by $\mathrm{Cov}(A,B)$:
$$
\frac{\partial}{\partial h}\langle A\rangle = \beta\,\mathrm{Cov}(A,B).
$$
This is a basic form of fluctuation–response, and it underlies definitions such as {{< knowl id="susceptibility-stat-mech" text="susceptibility" >}}.

## Physical interpretation
- $\mathrm{Cov}(A,B)>0$ means that when $A$ fluctuates upward from its mean, $B$ tends to do the same.
- $\mathrm{Cov}(A,B)<0$ means upward fluctuations of $A$ tend to coincide with downward fluctuations of $B$.
- Spatially, $\mathrm{Cov}(A_x,B_y)$ diagnoses correlations between fluctuations at different locations and is the building block of the {{< knowl id="correlation-function-two-point" text="two-point correlation function" >}} and its connected part.
