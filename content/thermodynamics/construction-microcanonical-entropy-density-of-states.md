---
title: "Microcanonical entropy from the density of states"
description: "Defines the density of states and constructs microcanonical (Boltzmann) entropy as k_B log Ω(E), linking phase-space volume to thermodynamics."
---

The microcanonical construction expresses entropy as the logarithm of the number (or volume) of accessible microstates at fixed energy. The key intermediate object is the {{< knowl id="density-of-states" section="stat-mech" text="density of states" >}} $\Omega(E)$ (sometimes also called the “surface” phase-space volume).

This construction underlies the {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann microcanonical entropy" >}} and provides the bridge from {{< knowl id="microstate-classical" section="stat-mech" text="microstates" >}} to macroscopic thermodynamics (compare {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}).

## Density of states and cumulative phase-space volume

For a classical system with {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="Hamiltonian" >}} $H(q,p)$ on {{< knowl id="phase-space-classical" section="stat-mech" text="phase space" >}} $\Gamma$, define the *cumulative* phase-space volume
$$
\Gamma(E) \;=\; \int_{\Gamma} \mathbf{1}\{H(q,p)\le E\}\,\mathrm{d}\omega,
$$

where $\mathrm{d}\omega$ is the {{< knowl id="phase-space-volume-element" section="stat-mech" text="phase-space volume element" >}}.

The *density of states* is, formally,
$$
\Omega(E) \;=\; \frac{\mathrm{d}}{\mathrm{d}E}\Gamma(E),
$$
and can be represented (heuristically) by a Dirac delta integral
$$
\Omega(E) \;=\; \int_{\Gamma} \delta\!\big(H(q,p)-E\big)\,\mathrm{d}\omega.
$$

In many rigorous treatments one replaces the delta by a thin energy window and works with a {{< knowl id="microcanonical-shell" section="stat-mech" text="microcanonical shell" >}} $E\le H\le E+\Delta E$.

## Microcanonical measure on an energy shell

The microcanonical ensemble is the uniform distribution over the energy surface (or shell). One convenient description is via the {{< knowl id="microcanonical-measure" section="stat-mech" text="microcanonical measure" >}}:
$$
\langle A\rangle_{E}
\;=\;
\frac{1}{\Omega(E)}\int_{\Gamma} A(q,p)\,\delta\!\big(H(q,p)-E\big)\,\mathrm{d}\omega,
$$
again interpreted as a limit of averages over shells when needed.

## Entropy from Ω(E)

The microcanonical (Boltzmann) entropy is defined by
$$
S(E) \;=\; k_B \,\log \Omega(E),
$$

where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}.

Some authors instead use $k_B\log\Gamma(E)$ (the “Gibbs volume entropy”). For macroscopic systems these definitions typically agree at the level relevant for thermodynamics (their difference is subextensive under suitable conditions), but the distinction can matter in small systems or when discussing monotonicity properties.

## Thermodynamic interpretation: temperature from derivatives

The microcanonical entropy determines temperature through its derivative:
$$
\frac{1}{T(E)} \;=\; \frac{\partial S}{\partial E}(E),
$$

consistent with {{< knowl id="temperature-thermo" section="thermodynamics" text="thermodynamic temperature" >}}. Equivalently, the microcanonical inverse temperature is $\beta(E)=\partial_E S(E)/k_B$, matching the notion in {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature β" >}}.

This derivative is the starting point for
{{< knowl id="construction-temperature-from-entropy" section="stat-mech" text="constructing temperature from entropy" >}}.

## Why log Ω(E)?

- **Counting/volume principle:** $\Omega(E)$ measures “how many” microstates realize energy $E$ (as a phase-space volume); entropy is the log of multiplicity.
- **Additivity:** For weakly interacting subsystems, densities of states approximately convolve, making $\log \Omega$ approximately additive (extensive) in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}.
- **Equilibrium as typicality:** In large systems, most microstates in the shell concentrate near a macrostate maximizing entropy, connecting this construction to {{< knowl id="macrostate" section="stat-mech" text="macrostates" >}}.

Finally, $\Omega(E)$ is also the bridge to the canonical ensemble: the canonical partition function is (formally) a Laplace transform of $\Omega(E)$, which is developed in
{{< knowl id="construction-canonical-from-microcanonical" section="stat-mech" text="constructing the canonical ensemble from the microcanonical" >}}.
