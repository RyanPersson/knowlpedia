+++
id = "thermodynamics/construction-microcanonical-entropy-density-of-states"
title = "Microcanonical entropy from the density of states"
kind = "knowl"
summary = "Defines the density of states and constructs microcanonical (Boltzmann) entropy as k_B log Ω(E), linking phase-space volume to thermodynamics."
aliases = ["construction-microcanonical-entropy-density-of-states", "Microcanonical entropy from the density of states"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/construction-microcanonical-entropy-density-of-states.md"
+++

The microcanonical construction expresses entropy as the logarithm of the number (or volume) of accessible microstates at fixed energy. The key intermediate object is the [[stat-mech/density-of-states|density of states]] $\Omega(E)$ (sometimes also called the “surface” phase-space volume).

This construction underlies the [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann microcanonical entropy]] and provides the bridge from [[stat-mech/microstate-classical|microstates]] to macroscopic thermodynamics (compare [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]]).

## Density of states and cumulative phase-space volume

For a classical system with [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H(q,p)$ on [[stat-mech/phase-space-classical|phase space]] $\Gamma$, define the *cumulative* phase-space volume
$$
\Gamma(E) \;=\; \int_{\Gamma} \mathbf{1}\{H(q,p)\le E\}\,\mathrm{d}\omega,
$$

where $\mathrm{d}\omega$ is the [[stat-mech/phase-space-volume-element|phase-space volume element]].

The *density of states* is, formally,
$$
\Omega(E) \;=\; \frac{\mathrm{d}}{\mathrm{d}E}\Gamma(E),
$$
and can be represented (heuristically) by a Dirac delta integral
$$
\Omega(E) \;=\; \int_{\Gamma} \delta\!\big(H(q,p)-E\big)\,\mathrm{d}\omega.
$$

In many rigorous treatments one replaces the delta by a thin energy window and works with a [[stat-mech/microcanonical-shell|microcanonical shell]] $E\le H\le E+\Delta E$.

## Microcanonical measure on an energy shell

The microcanonical ensemble is the uniform distribution over the energy surface (or shell). One convenient description is via the [[stat-mech/microcanonical-measure|microcanonical measure]]:
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

where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

Some authors instead use $k_B\log\Gamma(E)$ (the “Gibbs volume entropy”). For macroscopic systems these definitions typically agree at the level relevant for thermodynamics (their difference is subextensive under suitable conditions), but the distinction can matter in small systems or when discussing monotonicity properties.

## Thermodynamic interpretation: temperature from derivatives

The microcanonical entropy determines temperature through its derivative:
$$
\frac{1}{T(E)} \;=\; \frac{\partial S}{\partial E}(E),
$$

consistent with [[thermodynamics/temperature-thermo|thermodynamic temperature]]. Equivalently, the microcanonical inverse temperature is $\beta(E)=\partial_E S(E)/k_B$, matching the notion in [[thermodynamics/inverse-temperature-beta|inverse temperature β]].

This derivative is the starting point for
[[stat-mech/construction-temperature-from-entropy|constructing temperature from entropy]].

## Why log Ω(E)?

- **Counting/volume principle:** $\Omega(E)$ measures “how many” microstates realize energy $E$ (as a phase-space volume); entropy is the log of multiplicity.
- **Additivity:** For weakly interacting subsystems, densities of states approximately convolve, making $\log \Omega$ approximately additive (extensive) in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].
- **Equilibrium as typicality:** In large systems, most microstates in the shell concentrate near a macrostate maximizing entropy, connecting this construction to [[stat-mech/macrostate|macrostates]].

Finally, $\Omega(E)$ is also the bridge to the canonical ensemble: the canonical partition function is (formally) a Laplace transform of $\Omega(E)$, which is developed in
[[stat-mech/construction-canonical-from-microcanonical|constructing the canonical ensemble from the microcanonical]].
