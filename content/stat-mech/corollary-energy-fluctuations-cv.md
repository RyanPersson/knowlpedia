---
title: "Energy fluctuations and heat capacity in the canonical ensemble"
description: "In the canonical ensemble, the variance of the energy equals k_B T^2 times the constant-volume heat capacity."
---

## Statement (canonical energy fluctuations)
Let a system at fixed volume $V$ and particle number $N$ be described in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at temperature $T$ (inverse temperature $\beta = 1/(k_B T)$), with Hamiltonian $H$ and finite {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}} $Z(\beta)$.

Then the energy variance satisfies
$$
\operatorname{Var}_\beta(H) \;=\; k_B T^2\, C_V,
$$

where $C_V = \left(\frac{\partial \langle H\rangle}{\partial T}\right)_{V,N}$ is the {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}} and $\operatorname{Var}_\beta(H)$ is the {{< knowl id="variance" section="probability" text="variance" >}} computed with respect to the canonical state.

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
- {{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}}, {{< knowl id="variance-observable-ensemble" section="stat-mech" text="variance of an observable" >}}
- {{< knowl id="canonical-energy-fluctuation-identity" text="canonical energy fluctuation identity" >}}
- {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="definition of C_V" >}}

