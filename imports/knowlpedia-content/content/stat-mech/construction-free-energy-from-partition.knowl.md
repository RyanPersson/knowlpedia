+++
id = "stat-mech/construction-free-energy-from-partition"
title = "Constructing free energies from partition functions"
kind = "knowl"
summary = "How thermodynamic potentials arise as (minus) inverse-temperature times the logarithm of partition functions."
aliases = ["construction-free-energy-from-partition", "Constructing free energies from partition functions"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-free-energy-from-partition.md"
+++

Partition functions are normalization constants for equilibrium ensembles, but their deeper role is that their logarithms produce the thermodynamic potentials governing macroscopic behavior (see [[stat-mech/free-energy-statistical|statistical free energy]] and [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).

## Canonical free energy from the canonical partition function

In the [[stat-mech/canonical-ensemble|canonical ensemble]] (fixed $T,V,N$), the partition function $Z_N(\beta,V)$ is constructed by [[stat-mech/construction-canonical-partition-function|the canonical partition-function construction]].

The **Helmholtz free energy** (as a function of $(T,V,N)$) is defined by
$$
F(T,V,N) \;=\; -\frac{1}{\beta}\,\log Z_N(\beta,V),
$$

with $\beta$ the [[thermodynamics/inverse-temperature-beta|inverse temperature]]. Equivalently, using $T$ explicitly and the [[thermodynamics/boltzmann-constant|Boltzmann constant]] $k_B$,
$$
F(T,V,N) \;=\; -k_B T \,\log Z_N(\beta,V).
$$
This agrees (in the thermodynamic limit and under standard regularity assumptions) with the thermodynamic [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]].

## Grand potential from the grand partition function

In the [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]] (fixed $T,V,\mu$), the grand partition function $\Xi(\beta,\mu,V)$ is constructed by [[stat-mech/construction-grand-canonical-partition-function|the grand-canonical partition-function construction]].

The corresponding thermodynamic potential is the **grand potential**
$$
\Omega(T,V,\mu) \;=\; -\frac{1}{\beta}\,\log \Xi(\beta,\mu,V),
$$
matching the thermodynamic [[thermodynamics/grand-potential|grand potential]].

## Why the logarithm?

The use of $\log Z$ (and $\log \Xi$) reflects extensivity and additivity:

- For (approximately) independent subsystems, partition functions multiply, while free energies add:
  if $Z \approx Z^{(1)} Z^{(2)}$, then $-\beta^{-1}\log Z \approx -\beta^{-1}\log Z^{(1)} - \beta^{-1}\log Z^{(2)}$.
- In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], one expects $\log Z$ to scale like volume, so $F$ scales like an extensive quantity.

## Connection to Legendre structure

Switching which variables are held fixed corresponds to Legendre transforms between potentials. For example, the grand potential is the Legendre transform of $F$ with respect to particle number, as explained in [[stat-mech/construction-legendre-f-to-omega|the construction from $F$ to $\Omega$]]. This mirrors the conjugacy between $N$ and the [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$.

## Physical interpretation

- $F$ measures the “useful work” available at fixed $(T,V,N)$ once entropic effects are included; minimizing $F$ at fixed $(T,V,N)$ characterizes equilibrium.
- $\Omega$ is the potential adapted to particle exchange; minimizing $\Omega$ at fixed $(T,V,\mu)$ characterizes equilibrium in the presence of a particle reservoir.
- Derivatives of $\log Z$ and $\log \Xi$ generate observable averages and fluctuations; see [[stat-mech/construction-observables-from-log-z|constructing observables from log partition functions]].
