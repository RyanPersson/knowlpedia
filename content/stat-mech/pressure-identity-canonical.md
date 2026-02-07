---
title: "Pressure identity in the canonical ensemble"
description: "In the canonical ensemble, pressure equals (1/β) times the volume derivative of log partition function, equivalently -∂F/∂V."
---

## Statement
For a system in the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at inverse temperature $\beta$, with canonical partition function {{< knowl id="partition-function-canonical" section="stat-mech" text="Z(β,V)" >}} depending on the volume parameter $V$, define the Helmholtz free energy
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
- {{< knowl id="pressure-thermo" section="thermodynamics" text="Thermodynamic pressure" >}}
- {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}
- {{< knowl id="partition-function-canonical" section="stat-mech" text="Canonical partition function" >}}
- {{< knowl id="free-energy-statistical" section="stat-mech" text="Statistical free energy" >}}

