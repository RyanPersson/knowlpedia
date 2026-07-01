+++
id = "stat-mech/canonical-ensemble"
title = "Canonical ensemble"
kind = "knowl"
summary = "Gibbs equilibrium distribution at fixed temperature: microstates are weighted by the Boltzmann factor and normalized by the partition function."
aliases = ["canonical-ensemble", "Canonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/canonical-ensemble.md"
+++

The **canonical ensemble** models a system that can exchange energy with a heat bath, so its temperature is fixed while its energy fluctuates.

Let $\Gamma$ be a classical [[stat-mech/phase-space-classical|phase space]] with Liouville [[stat-mech/phase-space-volume-element|volume element]] $d\Gamma$, and let $H(x)$ be the [[stat-mech/hamiltonian-function-classical|Hamiltonian]]. Fix an inverse temperature [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta>0$ (equivalently a [[thermodynamics/temperature-thermo|temperature]] $T$ via $\beta = 1/(k_B T)$ with [[thermodynamics/boltzmann-constant|Boltzmann's constant]] $k_B$).

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

where $Z(\beta)$ is the [[stat-mech/partition-function-canonical|canonical partition function]].

(Quantum version: replace the phase-space integral by a trace, $Z(\beta)=\mathrm{Tr}\,e^{-\beta \hat H}$, and $\rho_\beta$ by the Gibbs density matrix.)

## Ensemble averages
For an observable $A(x)$, the [[stat-mech/ensemble-average|ensemble average]] in the canonical ensemble is
$$
\langle A\rangle_\beta
\;=\;
\int_{\Gamma} A(x)\,\rho_\beta(x)\, d\Gamma
\;=\;
\frac{1}{Z(\beta)}\int_{\Gamma} A(x)\,e^{-\beta H(x)}\, d\Gamma.
$$

## Thermodynamic potentials from $Z$
The canonical [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] is obtained from the partition function via the [[stat-mech/free-energy-statistical|statistical free energy]]
$$
F(\beta)
\;=\;
-\frac{1}{\beta}\ln Z(\beta)
\;=\;
-k_B T \ln Z(\beta).
$$
This link is the starting point for [[stat-mech/construction-free-energy-from-partition|constructing free energy from the partition function]].

## Energy and fluctuations
Canonical energy moments are derivatives of $\ln Z(\beta)$ (see [[stat-mech/construction-observables-from-log-z|observables from log partition functions]]):
$$
\langle E\rangle_\beta \;=\; -\frac{\partial}{\partial\beta}\ln Z(\beta),
\qquad
\mathrm{Var}_\beta(E) \;=\; \frac{\partial^2}{\partial\beta^2}\ln Z(\beta).
$$

Energy fluctuations control the heat capacity at fixed volume (in classical $N,V$ settings), encoded by [[stat-mech/specific-heat-fluctuation|specific heat as an energy fluctuation]].

## Physical interpretation and construction
The canonical distribution weights microstates by the Boltzmann factor $e^{-\beta H}$: lower-energy states are exponentially favored, with the strength set by temperature. It can be derived either by weak coupling of the system to a large bath or by the variational principle of [[stat-mech/construction-entropy-maximization-thermal|maximum entropy at fixed mean energy]].

In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], canonical and [[stat-mech/microcanonical-measure|microcanonical]] predictions often agree for bulk observables (ensemble equivalence), formalized by [[stat-mech/construction-canonical-from-microcanonical|constructing the canonical ensemble from the microcanonical one]].
