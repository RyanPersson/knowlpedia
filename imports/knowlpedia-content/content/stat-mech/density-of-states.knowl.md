+++
id = "stat-mech/density-of-states"
title = "Density of states"
kind = "knowl"
summary = "Measure of how many microstates occur per unit energy (classically via phase-space volume, quantum mechanically via spectral degeneracy)."
aliases = ["density-of-states", "Density of states"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/density-of-states.md"
+++

Consider a classical [[thermodynamics/thermodynamic-system|thermodynamic system]] modeled by a [[stat-mech/microstate-classical|microstate]] $x$ ranging over a classical [[stat-mech/phase-space-classical|phase space]] $\Gamma$, equipped with the Liouville [[stat-mech/phase-space-volume-element|phase-space volume element]] $d\Gamma$. Let $H(x)$ denote the [[stat-mech/hamiltonian-function-classical|Hamiltonian]] (total energy).

## Definition (classical)
The **cumulative phase-space volume below energy $E$** is
$$
\Omega(E) \;=\; \int_{\Gamma} \mathbf{1}\!\left\{H(x)\le E\right\}\, d\Gamma.
$$

When $\Omega$ is differentiable (or in a distributional sense), the **density of states** is
$$
g(E) \;=\; \frac{d\Omega}{dE}(E).
$$
Equivalently, using the Dirac delta to localize on the energy surface,
$$
g(E) \;=\; \int_{\Gamma} \delta\!\big(E - H(x)\big)\, d\Gamma.
$$

## Energy shells and counting interpretation
For a thin [[stat-mech/microcanonical-shell|microcanonical shell]] of width $\Delta E>0$,
$$
\Omega(E,\Delta E) \;=\; \int_{\Gamma}\mathbf{1}\!\left\{E\le H(x)\le E+\Delta E\right\} d\Gamma
\;=\; \Omega(E+\Delta E)-\Omega(E)
\;\approx\; g(E)\,\Delta E,
$$

so $g(E)$ is the phase-space “number of microstates per unit energy” (up to the conventional normalization of $d\Gamma$).

## Quantum version (spectral density)
For a quantum Hamiltonian $\hat H$ with discrete spectrum $\{E_n\}$ (finite volume), one often encodes the density of states as a measure
$$
g(E) \;=\; \sum_n \delta(E-E_n),
$$

or, equivalently, by the **counting function** $N(E)=\#\{n: E_n\le E\}$, which plays the role of $\Omega(E)$.

## Link to entropy and temperature
The density of states controls the microcanonical notion of [[thermodynamics/thermodynamic-entropy|entropy]] via the [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann entropy]]. In a thin shell,
$$
S(E) \;\approx\; k_B \ln\!\big(g(E)\,\Delta E\big),
$$

with [[thermodynamics/boltzmann-constant|Boltzmann's constant]] $k_B$.

Differentiating $S(E)$ with respect to energy yields the microcanonical inverse temperature, implemented in practice by [[stat-mech/construction-temperature-from-entropy|extracting temperature from entropy]] and matched to the thermodynamic [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$ in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].
