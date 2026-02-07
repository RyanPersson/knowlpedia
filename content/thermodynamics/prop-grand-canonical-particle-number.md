---
title: "Grand-canonical particle number identity"
description: "In the grand canonical ensemble, the mean particle number is the μ-derivative of log Ξ, equivalently the −μ-derivative of the grand potential."
---

## Statement
In the {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}} at inverse temperature $\beta$ and chemical potential $\mu$, let the grand partition function be
$$
\Xi(\beta,\mu)=\mathrm{Tr}\,\exp\!\big(-\beta(H-\mu N)\big)
$$
(or the analogous classical phase-space integral). Then the mean particle number satisfies
$$
\langle N\rangle \;=\; \frac{1}{\beta}\,\frac{\partial}{\partial \mu}\ln \Xi(\beta,\mu).
$$

Equivalently, with the {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}} defined by $\Omega(\beta,\mu)=-(1/\beta)\ln \Xi(\beta,\mu)$,
$$
\langle N\rangle \;=\; -\,\frac{\partial \Omega}{\partial \mu}\Big|_{\beta}.
$$

## Key hypotheses
- The {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}} is well-defined for the given $(\beta,\mu)$.
- Differentiation with respect to $\mu$ can be interchanged with the trace/integral.

## Conclusions
- $\mu$ is conjugate to $N$: changing {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}} changes $\langle N\rangle$ via a derivative of $\ln\Xi$.
- Thermodynamic form: $\langle N\rangle$ is the negative $\mu$-derivative of $\Omega$.

