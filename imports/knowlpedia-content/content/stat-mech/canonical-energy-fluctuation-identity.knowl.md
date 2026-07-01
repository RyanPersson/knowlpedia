+++
id = "stat-mech/canonical-energy-fluctuation-identity"
title = "Canonical energy fluctuation identity"
kind = "knowl"
summary = "Energy fluctuations in the canonical ensemble are given by the second β-derivative of log partition function and relate to heat capacity."
aliases = ["canonical-energy-fluctuation-identity", "Canonical energy fluctuation identity"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/canonical-energy-fluctuation-identity.md"
+++

## Statement
In the [[stat-mech/canonical-ensemble|canonical ensemble]] with partition function [[stat-mech/partition-function-canonical|Z(β)]], the variance of the energy satisfies
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
- The [[stat-mech/canonical-ensemble|canonical ensemble]] is well-defined and $Z(\beta)$ is twice differentiable in $\beta$ (with differentiation under the integral justified).
- The energy variance is finite: $\langle H^2\rangle_\beta < \infty$.

## Conclusion
- Energy fluctuations are controlled by curvature of $\log Z(\beta)$ in $\beta$.
- Positivity $\operatorname{Var}_\beta(H)\ge 0$ implies $C_V\ge 0$ under the usual identification (compare [[thermodynamics/thermodynamic-stability|stability]]).

## Cross-links to definitions
- [[stat-mech/variance-observable-ensemble|Variance in an ensemble]]
- [[stat-mech/partition-function-canonical|Canonical partition function]]
- [[stat-mech/canonical-energy-identity|Canonical energy identity]]
- [[thermodynamics/heat-capacity-constant-volume|Heat capacity at constant volume]]
