---
title: "Constructing free energies from partition functions"
description: "How thermodynamic potentials arise as (minus) inverse-temperature times the logarithm of partition functions."
---

Partition functions are normalization constants for equilibrium ensembles, but their deeper role is that their logarithms produce the thermodynamic potentials governing macroscopic behavior (see {{< knowl id="free-energy-statistical" text="statistical free energy" >}} and {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}).

## Canonical free energy from the canonical partition function

In the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} (fixed $T,V,N$), the partition function $Z_N(\beta,V)$ is constructed by {{< knowl id="construction-canonical-partition-function" text="the canonical partition-function construction" >}}.

The **Helmholtz free energy** (as a function of $(T,V,N)$) is defined by
$$
F(T,V,N) \;=\; -\frac{1}{\beta}\,\log Z_N(\beta,V),
$$

with $\beta$ the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}. Equivalently, using $T$ explicitly and the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}} $k_B$,
$$
F(T,V,N) \;=\; -k_B T \,\log Z_N(\beta,V).
$$
This agrees (in the thermodynamic limit and under standard regularity assumptions) with the thermodynamic {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}.

## Grand potential from the grand partition function

In the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}} (fixed $T,V,\mu$), the grand partition function $\Xi(\beta,\mu,V)$ is constructed by {{< knowl id="construction-grand-canonical-partition-function" text="the grand-canonical partition-function construction" >}}.

The corresponding thermodynamic potential is the **grand potential**
$$
\Omega(T,V,\mu) \;=\; -\frac{1}{\beta}\,\log \Xi(\beta,\mu,V),
$$
matching the thermodynamic {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}}.

## Why the logarithm?

The use of $\log Z$ (and $\log \Xi$) reflects extensivity and additivity:

- For (approximately) independent subsystems, partition functions multiply, while free energies add:
  if $Z \approx Z^{(1)} Z^{(2)}$, then $-\beta^{-1}\log Z \approx -\beta^{-1}\log Z^{(1)} - \beta^{-1}\log Z^{(2)}$.
- In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, one expects $\log Z$ to scale like volume, so $F$ scales like an extensive quantity.

## Connection to Legendre structure

Switching which variables are held fixed corresponds to Legendre transforms between potentials. For example, the grand potential is the Legendre transform of $F$ with respect to particle number, as explained in {{< knowl id="construction-legendre-f-to-omega" text="the construction from $F$ to $\Omega$" >}}. This mirrors the conjugacy between $N$ and the {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}} $\mu$.

## Physical interpretation

- $F$ measures the “useful work” available at fixed $(T,V,N)$ once entropic effects are included; minimizing $F$ at fixed $(T,V,N)$ characterizes equilibrium.
- $\Omega$ is the potential adapted to particle exchange; minimizing $\Omega$ at fixed $(T,V,\mu)$ characterizes equilibrium in the presence of a particle reservoir.
- Derivatives of $\log Z$ and $\log \Xi$ generate observable averages and fluctuations; see {{< knowl id="construction-observables-from-log-z" text="constructing observables from log partition functions" >}}.
