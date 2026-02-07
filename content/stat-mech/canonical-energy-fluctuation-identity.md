---
title: "Canonical energy fluctuation identity"
description: "Energy fluctuations in the canonical ensemble are given by the second β-derivative of log partition function and relate to heat capacity."
---

## Statement
In the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} with partition function {{< knowl id="partition-function-canonical" section="stat-mech" text="Z(β)" >}}, the variance of the energy satisfies
$$
\operatorname{Var}_\beta(H)
\;=\;
\frac{\partial^2}{\partial \beta^2}\log Z(\beta)
\;=\;
-\frac{\partial}{\partial \beta}\langle H\rangle_\beta.
$$

In terms of temperature $T$ (with $\beta = 1/(k_B T)$), the heat capacity at constant volume satisfies
$$
C_V \;=\;\left(\frac{\partial \langle H\rangle}{\partial T}\right)_V
\;=\;
\frac{1}{k_B T^2}\operatorname{Var}_\beta(H),
$$
equivalently,
$$
\operatorname{Var}_\beta(H) = k_B T^2\, C_V.
$$

## Key hypotheses
- The {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} is well-defined and $Z(\beta)$ is twice differentiable in $\beta$ (with differentiation under the integral justified).
- The energy variance is finite: $\langle H^2\rangle_\beta < \infty$.

## Conclusion
- Energy fluctuations are controlled by curvature of $\log Z(\beta)$ in $\beta$.
- Positivity $\operatorname{Var}_\beta(H)\ge 0$ implies $C_V\ge 0$ under the usual identification (compare {{< knowl id="thermodynamic-stability" section="thermodynamics" text="stability" >}}).

## Cross-links to definitions
- {{< knowl id="variance-observable-ensemble" section="stat-mech" text="Variance in an ensemble" >}}
- {{< knowl id="partition-function-canonical" section="stat-mech" text="Canonical partition function" >}}
- {{< knowl id="canonical-energy-identity" text="Canonical energy identity" >}}
- {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="Heat capacity at constant volume" >}}

