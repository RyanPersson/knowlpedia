+++
id = "stat-mech/boltzmann-entropy-microcanonical"
title = "Boltzmann entropy in the microcanonical ensemble"
kind = "knowl"
summary = "Microcanonical entropy defined as k_B times the logarithm of the phase-space volume of microstates compatible with fixed energy (and other constraints)."
aliases = ["boltzmann-entropy-microcanonical", "Boltzmann entropy in the microcanonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/boltzmann-entropy-microcanonical.md"
+++

**Definition (Boltzmann microcanonical entropy).**
A classical [[stat-mech/microstate-classical|microstate]] is a point $x=(q,p)$ in [[stat-mech/phase-space-classical|phase space]], equipped with a [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H(x)$. Fix macroscopic constraints such as $(E,V,N)$ and consider the [[stat-mech/microcanonical-shell|microcanonical energy shell]] (in practice, an energy *window* of width $\Delta E$). Using the [[stat-mech/phase-space-volume-element|phase-space volume element]] $d\Gamma$, define the (dimensionless) phase-space volume of accessible states by
$$
\Omega(E,\Delta E;V,N)
=\frac{1}{h^{dN}N!}\int \mathbf{1}_{[E,E+\Delta E]}(H(x))\,d\Gamma(x),
$$

where $d$ is the spatial dimension, and the factor $h^{dN}N!$ is the standard classical normalization (Planck cell and indistinguishability).

The **Boltzmann entropy** is
$$
S_B(E,V,N)=k_B\ln \Omega(E,\Delta E;V,N),
$$

where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

**Density-of-states form.**
If one introduces the [[stat-mech/density-of-states|density of states]]
$$
\omega(E;V,N)=\frac{1}{h^{dN}N!}\int \delta(H(x)-E)\,d\Gamma(x),
$$

then for small $\Delta E$ one has $\Omega(E,\Delta E)\approx \omega(E)\,\Delta E$, so $S_B(E)$ is (up to an additive constant $k_B\ln\Delta E$) the logarithm of $\omega(E)$.

**Physical interpretation.**
$S_B$ measures “how many” microstates are compatible with a given [[stat-mech/macrostate|macrostate]] constraint (here, fixed energy). The associated [[stat-mech/microcanonical-measure|microcanonical measure]] is uniform over the energy shell/window, so $\Omega$ is literally the volume being sampled.

**Thermodynamic structure.**
In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], $S_B$ becomes extensive and agrees with [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] (for equilibrium states), while the dependence on the particular choice of $\Delta E$ drops out at the level of entropy density.

A key consequence is the microcanonical definition of temperature:
$$
\frac{1}{T}=\left(\frac{\partial S_B}{\partial E}\right)_{V,N},
$$

equivalently $\,\beta = (\partial S_B/\partial E)/k_B$, where $\beta$ is [[thermodynamics/inverse-temperature-beta|inverse temperature]] and the construction is summarized in [[stat-mech/construction-temperature-from-entropy|temperature from entropy]].
