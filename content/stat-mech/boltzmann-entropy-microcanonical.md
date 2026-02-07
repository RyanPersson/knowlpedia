---
title: "Boltzmann entropy in the microcanonical ensemble"
description: "Microcanonical entropy defined as k_B times the logarithm of the phase-space volume of microstates compatible with fixed energy (and other constraints)."
---

**Definition (Boltzmann microcanonical entropy).**  
A classical {{< knowl id="microstate-classical" text="microstate" >}} is a point $x=(q,p)$ in {{< knowl id="phase-space-classical" text="phase space" >}}, equipped with a {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} $H(x)$. Fix macroscopic constraints such as $(E,V,N)$ and consider the {{< knowl id="microcanonical-shell" text="microcanonical energy shell" >}} (in practice, an energy *window* of width $\Delta E$). Using the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} $d\Gamma$, define the (dimensionless) phase-space volume of accessible states by
$$
\Omega(E,\Delta E;V,N)
=\frac{1}{h^{dN}N!}\int \mathbf{1}_{[E,E+\Delta E]}(H(x))\,d\Gamma(x),
$$

where $d$ is the spatial dimension, and the factor $h^{dN}N!$ is the standard classical normalization (Planck cell and indistinguishability).

The **Boltzmann entropy** is
$$
S_B(E,V,N)=k_B\ln \Omega(E,\Delta E;V,N),
$$

where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}.

**Density-of-states form.**  
If one introduces the {{< knowl id="density-of-states" text="density of states" >}}
$$
\omega(E;V,N)=\frac{1}{h^{dN}N!}\int \delta(H(x)-E)\,d\Gamma(x),
$$

then for small $\Delta E$ one has $\Omega(E,\Delta E)\approx \omega(E)\,\Delta E$, so $S_B(E)$ is (up to an additive constant $k_B\ln\Delta E$) the logarithm of $\omega(E)$.

**Physical interpretation.**  
$S_B$ measures “how many” microstates are compatible with a given {{< knowl id="macrostate" text="macrostate" >}} constraint (here, fixed energy). The associated {{< knowl id="microcanonical-measure" text="microcanonical measure" >}} is uniform over the energy shell/window, so $\Omega$ is literally the volume being sampled.

**Thermodynamic structure.**  
In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, $S_B$ becomes extensive and agrees with {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} (for equilibrium states), while the dependence on the particular choice of $\Delta E$ drops out at the level of entropy density.

A key consequence is the microcanonical definition of temperature:
$$
\frac{1}{T}=\left(\frac{\partial S_B}{\partial E}\right)_{V,N},
$$

equivalently $\,\beta = (\partial S_B/\partial E)/k_B$, where $\beta$ is {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} and the construction is summarized in {{< knowl id="construction-temperature-from-entropy" text="temperature from entropy" >}}.
