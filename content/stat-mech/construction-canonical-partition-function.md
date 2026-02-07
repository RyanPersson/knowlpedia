---
title: "Constructing the canonical partition function"
description: "Definition of the canonical partition function as the normalization of the canonical ensemble and as a Laplace transform of the density of states."
---

The canonical ensemble describes a system at fixed temperature $T$, volume $V$, and particle number $N$ (see {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}). Its normalization constant is the **canonical partition function**, which also acts as a generating function for thermodynamic quantities.

## Setup (microstates and energy)

A classical microstate is a point in {{< knowl id="phase-space-classical" text="classical phase space" >}}, and the energy of a microstate $x$ is given by the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian function" >}} $H(x)$. Integration over microstates uses the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} $d\Gamma(x)$ (which may include conventions such as $h^{-dN}$ and $1/N!$ for identical particles).

## Definition (classical canonical partition function)

Fix $(N,V)$ and inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}). The canonical partition function is
$$
Z_N(\beta,V) \;=\; \int_{\Gamma_{N,V}} e^{-\beta H(x)}\, d\Gamma(x),
$$

where $\Gamma_{N,V}$ denotes the accessible phase space at particle number $N$ and volume $V$.

The associated canonical probability measure on microstates is
$$
\mathbb{P}_\beta(dx) \;=\; \frac{e^{-\beta H(x)}}{Z_N(\beta,V)}\, d\Gamma(x),
$$

so $Z_N$ is precisely the normalizing constant that turns the Boltzmann weight into a probability distribution. Expectations with respect to this measure are {{< knowl id="ensemble-average" text="ensemble averages" >}}.

## Quantum version (trace form)

For a quantum system with Hamiltonian operator $\hat H$ on the $N$-particle Hilbert space (and suitable boundary conditions implementing $V$), the canonical partition function is
$$
Z_N(\beta,V) \;=\; \mathrm{Tr}\, e^{-\beta \hat H}.
$$

## Density-of-states representation

If $g_N(E;V)$ is the {{< knowl id="density-of-states" text="density of states" >}} (so that $g_N(E;V)\,dE$ counts microstates with energy in $[E,E+dE]$ in an appropriate sense), then
$$
Z_N(\beta,V) \;=\; \int e^{-\beta E}\, g_N(E;V)\, dE,
$$

i.e. $Z_N$ is the Laplace transform of the density of states. This ties the canonical construction to microcanonical objects such as the {{< knowl id="microcanonical-shell" text="microcanonical shell" >}} and {{< knowl id="microcanonical-measure" text="microcanonical measure" >}}.

## Physical interpretation

- $e^{-\beta H(x)}$ penalizes high-energy microstates at low temperature: larger $\beta$ concentrates the measure on lower-energy regions of phase space.
- $Z_N(\beta,V)$ encodes “how many” energetically accessible microstates exist once weighted by temperature; it is the central object from which the {{< knowl id="construction-free-energy-from-partition" text="free energy is constructed" >}}.
- The thermodynamic temperature is related to $\beta$ by $\beta = 1/(k_B T)$, where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}.
