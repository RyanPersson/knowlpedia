---
title: "Canonical ensemble convention"
description: "The convention that a system in thermal contact with a heat bath at temperature T is described by the canonical ensemble."
---

The **canonical ensemble** describes a system in thermal equilibrium with a heat bath at fixed {{< knowl id="temperature-thermo" text="temperature" >}} $T$. The system can exchange energy with the bath but has fixed volume $V$ and particle number $N$.

## Probability distribution

In the canonical ensemble, the probability of finding the system in {{< knowl id="microstate-classical" section="stat-mech" text="microstate" >}} $(q, p)$ is
$$
\rho(q, p) = \frac{1}{Z} e^{-\beta H(q, p)},
$$

where:
- $\beta = 1/(k_B T)$ is the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}}
- $H$ is the {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="Hamiltonian" >}}
- $Z$ is the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}

The natural thermodynamic potential for this ensemble is the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}}. The bath is modeled as a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}}. For the full formal definition, see {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}.
