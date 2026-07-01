+++
id = "stat-mech/construction-canonical-partition-function"
title = "Constructing the canonical partition function"
kind = "knowl"
summary = "Definition of the canonical partition function as the normalization of the canonical ensemble and as a Laplace transform of the density of states."
aliases = ["construction-canonical-partition-function", "Constructing the canonical partition function"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-canonical-partition-function.md"
+++

The canonical ensemble describes a system at fixed temperature $T$, volume $V$, and particle number $N$ (see [[stat-mech/canonical-ensemble|canonical ensemble]]). Its normalization constant is the **canonical partition function**, which also acts as a generating function for thermodynamic quantities.

## Setup (microstates and energy)

A classical microstate is a point in [[stat-mech/phase-space-classical|classical phase space]], and the energy of a microstate $x$ is given by the [[stat-mech/hamiltonian-function-classical|Hamiltonian function]] $H(x)$. Integration over microstates uses the [[stat-mech/phase-space-volume-element|phase-space volume element]] $d\Gamma(x)$ (which may include conventions such as $h^{-dN}$ and $1/N!$ for identical particles).

## Definition (classical canonical partition function)

Fix $(N,V)$ and inverse temperature $\beta$ (see [[thermodynamics/inverse-temperature-beta|inverse temperature]]). The canonical partition function is
$$
Z_N(\beta,V) \;=\; \int_{\Gamma_{N,V}} e^{-\beta H(x)}\, d\Gamma(x),
$$

where $\Gamma_{N,V}$ denotes the accessible phase space at particle number $N$ and volume $V$.

The associated canonical probability measure on microstates is
$$
\mathbb{P}_\beta(dx) \;=\; \frac{e^{-\beta H(x)}}{Z_N(\beta,V)}\, d\Gamma(x),
$$

so $Z_N$ is precisely the normalizing constant that turns the Boltzmann weight into a probability distribution. Expectations with respect to this measure are [[stat-mech/ensemble-average|ensemble averages]].

## Quantum version (trace form)

For a quantum system with Hamiltonian operator $\hat H$ on the $N$-particle Hilbert space (and suitable boundary conditions implementing $V$), the canonical partition function is
$$
Z_N(\beta,V) \;=\; \mathrm{Tr}\, e^{-\beta \hat H}.
$$

## Density-of-states representation

If $g_N(E;V)$ is the [[stat-mech/density-of-states|density of states]] (so that $g_N(E;V)\,dE$ counts microstates with energy in $[E,E+dE]$ in an appropriate sense), then
$$
Z_N(\beta,V) \;=\; \int e^{-\beta E}\, g_N(E;V)\, dE,
$$

i.e. $Z_N$ is the Laplace transform of the density of states. This ties the canonical construction to microcanonical objects such as the [[stat-mech/microcanonical-shell|microcanonical shell]] and [[stat-mech/microcanonical-measure|microcanonical measure]].

## Physical interpretation

- $e^{-\beta H(x)}$ penalizes high-energy microstates at low temperature: larger $\beta$ concentrates the measure on lower-energy regions of phase space.
- $Z_N(\beta,V)$ encodes “how many” energetically accessible microstates exist once weighted by temperature; it is the central object from which the [[stat-mech/construction-free-energy-from-partition|free energy is constructed]].
- The thermodynamic temperature is related to $\beta$ by $\beta = 1/(k_B T)$, where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]].
