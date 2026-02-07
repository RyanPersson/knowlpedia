---
title: "Density of states"
description: "Measure of how many microstates occur per unit energy (classically via phase-space volume, quantum mechanically via spectral degeneracy)."
---

Consider a classical {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} modeled by a {{< knowl id="microstate-classical" text="microstate" >}} $x$ ranging over a classical {{< knowl id="phase-space-classical" text="phase space" >}} $\Gamma$, equipped with the Liouville {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} $d\Gamma$. Let $H(x)$ denote the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} (total energy).

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
For a thin {{< knowl id="microcanonical-shell" text="microcanonical shell" >}} of width $\Delta E>0$,
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
The density of states controls the microcanonical notion of {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} via the {{< knowl id="boltzmann-entropy-microcanonical" text="Boltzmann entropy" >}}. In a thin shell,
$$
S(E) \;\approx\; k_B \ln\!\big(g(E)\,\Delta E\big),
$$

with {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann's constant" >}} $k_B$.

Differentiating $S(E)$ with respect to energy yields the microcanonical inverse temperature, implemented in practice by {{< knowl id="construction-temperature-from-entropy" text="extracting temperature from entropy" >}} and matched to the thermodynamic {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta$ in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}.
