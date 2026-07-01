+++
id = "stat-mech/corollary-energy-fluctuations-cv"
title = "Energy fluctuations and heat capacity in the canonical ensemble"
kind = "knowl"
summary = "In the canonical ensemble, the variance of the energy equals k_B T^2 times the constant-volume heat capacity."
aliases = ["corollary-energy-fluctuations-cv", "Energy fluctuations and heat capacity in the canonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-energy-fluctuations-cv.md"
+++

## Statement (canonical energy fluctuations)
Let a system at fixed volume $V$ and particle number $N$ be described in the [[stat-mech/canonical-ensemble|canonical ensemble]] at temperature $T$ (inverse temperature $\beta = 1/(k_B T)$), with Hamiltonian $H$ and finite [[stat-mech/partition-function-canonical|canonical partition function]] $Z(\beta)$.

Then the energy variance satisfies
$$
\operatorname{Var}_\beta(H) \;=\; k_B T^2\, C_V,
$$

where $C_V = \left(\frac{\partial \langle H\rangle}{\partial T}\right)_{V,N}$ is the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]] and $\operatorname{Var}_\beta(H)$ is the [[probability/variance|variance]] computed with respect to the canonical state.

## Key hypotheses
- The canonical measure/state exists: $Z(\beta) < \infty$ in a neighborhood of the $\beta$ of interest.
- The map $\beta \mapsto \log Z(\beta)$ is twice differentiable (enough to justify differentiating under the normalization).
- $V$ and $N$ are held fixed when defining $C_V$.

## Conclusions
- Energy fluctuations are controlled by the thermodynamic response $C_V$:
  - $C_V \ge 0$ implies $\operatorname{Var}_\beta(H)\ge 0$ (consistency check).
  - Large $C_V$ corresponds to large energy fluctuations (e.g. near criticality).
- Equivalent differential form:
  $$
  \operatorname{Var}_\beta(H)=\frac{\partial^2}{\partial \beta^2}\log Z(\beta).
  $$

## Cross-links (definitions and upstream identities)
- [[stat-mech/ensemble-average|ensemble average]], [[stat-mech/variance-observable-ensemble|variance of an observable]]
- [[stat-mech/canonical-energy-fluctuation-identity|canonical energy fluctuation identity]]
- [[thermodynamics/heat-capacity-constant-volume|definition of C_V]]
