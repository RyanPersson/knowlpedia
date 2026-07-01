+++
id = "stat-mech/pressure-identity-canonical"
title = "Pressure identity in the canonical ensemble"
kind = "knowl"
summary = "In the canonical ensemble, pressure equals (1/β) times the volume derivative of log partition function, equivalently -∂F/∂V."
aliases = ["pressure-identity-canonical", "Pressure identity in the canonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/pressure-identity-canonical.md"
+++

## Statement
For a system in the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta$, with canonical partition function [[stat-mech/partition-function-canonical|Z(β,V)]] depending on the volume parameter $V$, define the Helmholtz free energy
$F(\beta,V)=-(1/\beta)\log Z(\beta,V)$.

Then the canonical pressure satisfies
$$
p(\beta,V) \;=\; -\left(\frac{\partial F}{\partial V}\right)_{\beta}
\;=\;
\frac{1}{\beta}\left(\frac{\partial}{\partial V}\log Z(\beta,V)\right)_{\beta}.
$$

## Key hypotheses
- A well-defined dependence of the Hamiltonian and/or configuration domain on the volume parameter $V$, so that $Z(\beta,V)$ is differentiable in $V$.
- Interchange of $\partial/\partial V$ with the integral defining $Z(\beta,V)$ is justified.

## Conclusion
- Pressure is a logarithmic derivative of the canonical partition function with respect to volume.
- Equivalently, pressure is the negative volume derivative of the Helmholtz free energy.

## Cross-links to definitions
- [[thermodynamics/pressure-thermo|Thermodynamic pressure]]
- [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]
- [[stat-mech/partition-function-canonical|Canonical partition function]]
- [[stat-mech/free-energy-statistical|Statistical free energy]]
