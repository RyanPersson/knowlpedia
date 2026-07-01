+++
id = "stat-mech/canonical-energy-identity"
title = "Canonical energy identity"
kind = "knowl"
summary = "In the canonical ensemble, the mean energy equals minus the derivative of log partition function with respect to β."
aliases = ["canonical-energy-identity", "Canonical energy identity"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/canonical-energy-identity.md"
+++

## Statement
Let a classical system be distributed according to the [[stat-mech/canonical-ensemble|canonical ensemble]] with inverse temperature $\beta$ and [[stat-mech/partition-function-canonical|partition function]] $Z(\beta)$.
Then the canonical mean energy (internal energy) satisfies
$$
\langle H\rangle_\beta \;=\; -\frac{\partial}{\partial \beta}\log Z(\beta).
$$

Equivalently, for the canonical free energy [[stat-mech/free-energy-statistical|free energy]] $F(\beta)=-(1/\beta)\log Z(\beta)$,
$$
\langle H\rangle_\beta \;=\; \frac{\partial}{\partial \beta}\big(\beta F(\beta)\big).
$$

## Key hypotheses
- A well-defined [[stat-mech/canonical-ensemble|canonical ensemble]] with normalizing constant $Z(\beta)<\infty$.
- Differentiation under the integral defining [[stat-mech/partition-function-canonical|Z(β)]] is justified (e.g., dominated convergence).

## Conclusion
- The mean energy is obtained by differentiating $\log Z(\beta)$ with respect to $\beta$.
- This provides an efficient route from [[stat-mech/partition-function-canonical|partition function]] to thermodynamic energy.

## Cross-links to definitions
- [[stat-mech/canonical-ensemble|Canonical ensemble]]
- [[stat-mech/partition-function-canonical|Canonical partition function]]
- [[stat-mech/ensemble-average|Ensemble average]]
- [[stat-mech/free-energy-statistical|Statistical free energy]]
- [[thermodynamics/internal-energy-thermo|Internal energy (thermodynamics)]]
