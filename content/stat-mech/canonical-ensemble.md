---
title: "Canonical ensemble"
description: "Gibbs equilibrium distribution at fixed temperature: microstates are weighted by the Boltzmann factor and normalized by the partition function."
---

The **canonical ensemble** models a system that can exchange energy with a heat bath, so its temperature is fixed while its energy fluctuates.

Let $\Gamma$ be a classical {{< knowl id="phase-space-classical" text="phase space" >}} with Liouville {{< knowl id="phase-space-volume-element" text="volume element" >}} $d\Gamma$, and let $H(x)$ be the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}}. Fix an inverse temperature {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta>0$ (equivalently a {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} $T$ via $\beta = 1/(k_B T)$ with {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann's constant" >}} $k_B$).

The canonical probability density on $\Gamma$ is
$$
\rho_\beta(x)
\;=\;
\frac{e^{-\beta H(x)}}{Z(\beta)},
\qquad
Z(\beta)
\;=\;
\int_{\Gamma} e^{-\beta H(x)}\, d\Gamma,
$$

where $Z(\beta)$ is the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}.

(Quantum version: replace the phase-space integral by a trace, $Z(\beta)=\mathrm{Tr}\,e^{-\beta \hat H}$, and $\rho_\beta$ by the Gibbs density matrix.)

## Ensemble averages
For an observable $A(x)$, the {{< knowl id="ensemble-average" text="ensemble average" >}} in the canonical ensemble is
$$
\langle A\rangle_\beta
\;=\;
\int_{\Gamma} A(x)\,\rho_\beta(x)\, d\Gamma
\;=\;
\frac{1}{Z(\beta)}\int_{\Gamma} A(x)\,e^{-\beta H(x)}\, d\Gamma.
$$

## Thermodynamic potentials from $Z$
The canonical {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} is obtained from the partition function via the {{< knowl id="free-energy-statistical" text="statistical free energy" >}}
$$
F(\beta)
\;=\;
-\frac{1}{\beta}\ln Z(\beta)
\;=\;
-k_B T \ln Z(\beta).
$$
This link is the starting point for {{< knowl id="construction-free-energy-from-partition" text="constructing free energy from the partition function" >}}.

## Energy and fluctuations
Canonical energy moments are derivatives of $\ln Z(\beta)$ (see {{< knowl id="construction-observables-from-log-z" text="observables from log partition functions" >}}):
$$
\langle E\rangle_\beta \;=\; -\frac{\partial}{\partial\beta}\ln Z(\beta),
\qquad
\mathrm{Var}_\beta(E) \;=\; \frac{\partial^2}{\partial\beta^2}\ln Z(\beta).
$$

Energy fluctuations control the heat capacity at fixed volume (in classical $N,V$ settings), encoded by {{< knowl id="specific-heat-fluctuation" text="specific heat as an energy fluctuation" >}}.

## Physical interpretation and construction
The canonical distribution weights microstates by the Boltzmann factor $e^{-\beta H}$: lower-energy states are exponentially favored, with the strength set by temperature. It can be derived either by weak coupling of the system to a large bath or by the variational principle of {{< knowl id="construction-entropy-maximization-thermal" text="maximum entropy at fixed mean energy" >}}.

In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, canonical and {{< knowl id="microcanonical-measure" text="microcanonical" >}} predictions often agree for bulk observables (ensemble equivalence), formalized by {{< knowl id="construction-canonical-from-microcanonical" text="constructing the canonical ensemble from the microcanonical one" >}}.
