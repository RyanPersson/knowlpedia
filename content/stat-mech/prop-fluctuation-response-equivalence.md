---
title: "Fluctuation–response equivalence (canonical covariance identities)"
description: "In the canonical ensemble, linear response to a coupling equals a variance/covariance: derivatives of expectations are β-times covariances."
---

## Statement
Let $\langle \cdot \rangle$ denote {{< knowl id="ensemble-average" section="stat-mech" text="ensemble averages" >}} in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at inverse temperature $\beta$. Suppose the Hamiltonian is perturbed by a coupling $h$ to an observable $A$:
$$
H_h = H_0 - h\,A.
$$
Then, whenever differentiation under the integral/trace is justified,
$$
\frac{\partial}{\partial h}\,\langle A\rangle_h \;=\; \beta\,\mathrm{Var}_h(A),
$$

where $\mathrm{Var}_h(A)$ is the {{< knowl id="variance-observable-ensemble" section="stat-mech" text="variance" >}} computed in the perturbed ensemble.

More generally, for two observables $A,B$ with a coupling $g$ to $B$ via $H_g=H_0-gB$,
$$
\frac{\partial}{\partial g}\,\langle A\rangle_g \;=\; \beta\,\mathrm{Cov}_g(A,B),
$$

with $\mathrm{Cov}_g(A,B)=\langle AB\rangle_g-\langle A\rangle_g\langle B\rangle_g$.

## Key hypotheses
- Equilibrium canonical state exists and is differentiable in the coupling (see {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} and {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}).
- Observable(s) and perturbation are such that exchanging differentiation and expectation is valid.

## Conclusions
- Response (a derivative of a mean) equals a fluctuation (variance/covariance).
- Susceptibilities are variances/covariances; e.g. a linear susceptibility is a special case of {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}}.

