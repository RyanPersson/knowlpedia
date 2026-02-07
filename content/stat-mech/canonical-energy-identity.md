---
title: "Canonical energy identity"
description: "In the canonical ensemble, the mean energy equals minus the derivative of log partition function with respect to β."
---

## Statement
Let a classical system be distributed according to the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} with inverse temperature $\beta$ and {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}} $Z(\beta)$.
Then the canonical mean energy (internal energy) satisfies
$$
\langle H\rangle_\beta \;=\; -\frac{\partial}{\partial \beta}\log Z(\beta).
$$

Equivalently, for the canonical free energy {{< knowl id="free-energy-statistical" section="stat-mech" text="free energy" >}} $F(\beta)=-(1/\beta)\log Z(\beta)$,
$$
\langle H\rangle_\beta \;=\; \frac{\partial}{\partial \beta}\big(\beta F(\beta)\big).
$$

## Key hypotheses
- A well-defined {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} with normalizing constant $Z(\beta)<\infty$.
- Differentiation under the integral defining {{< knowl id="partition-function-canonical" section="stat-mech" text="Z(β)" >}} is justified (e.g., dominated convergence).

## Conclusion
- The mean energy is obtained by differentiating $\log Z(\beta)$ with respect to $\beta$.
- This provides an efficient route from {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}} to thermodynamic energy.

## Cross-links to definitions
- {{< knowl id="canonical-ensemble" section="stat-mech" text="Canonical ensemble" >}}
- {{< knowl id="partition-function-canonical" section="stat-mech" text="Canonical partition function" >}}
- {{< knowl id="ensemble-average" section="stat-mech" text="Ensemble average" >}}
- {{< knowl id="free-energy-statistical" section="stat-mech" text="Statistical free energy" >}}
- {{< knowl id="internal-energy-thermo" section="thermodynamics" text="Internal energy (thermodynamics)" >}}

