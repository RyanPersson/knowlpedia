---
title: "Mixed energy–number fluctuation identity (grand canonical)"
description: "In the grand canonical ensemble, derivatives with respect to μ or β yield covariances with N or with H−μN; in particular Cov(H,N) relates to mixed derivatives and to β-variation of ⟨N⟩."
---

## Statement
In the {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}} with density proportional to $\exp(-\beta(H-\mu N))$, the following differentiation identities hold for any observable $A$ (when justified):
$$
\frac{\partial}{\partial \mu}\langle A\rangle \;=\; \beta\,\mathrm{Cov}(A,N),
\qquad
\frac{\partial}{\partial \beta}\langle A\rangle \;=\; -\,\mathrm{Cov}\!\big(A,\,H-\mu N\big).
$$
Specializing gives a mixed fluctuation identity linking energy–number covariance to parameter derivatives:
$$
\mathrm{Cov}(H,N) \;=\; \frac{1}{\beta}\,\frac{\partial}{\partial \mu}\langle H\rangle
\;=\; \mu\,\mathrm{Var}(N)\;-\;\frac{\partial}{\partial \beta}\langle N\rangle.
$$

## Key hypotheses
- The grand canonical state exists and is differentiable in $(\beta,\mu)$.
- Differentiation can be interchanged with the trace/integral defining expectations.

## Conclusions
- $\mu$-response produces covariance with $N$; $\beta$-response produces covariance with $H-\mu N$.
- Energy–number correlations are controlled by mixed thermodynamic responses:
  $\partial_\mu\langle H\rangle = \beta\,\mathrm{Cov}(H,N)$ and
  $\partial_\beta\langle N\rangle = -\mathrm{Cov}(N,H)+\mu\,\mathrm{Var}(N)$.
- Together with {{< knowl id="prop-grand-canonical-number-fluctuation" text="number fluctuation identity" >}}, these yield a closed set of fluctuation/response relations for $(H,N)$.

