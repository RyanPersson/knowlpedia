+++
id = "thermodynamics/grand-canonical-ensemble-convention"
title = "Grand canonical ensemble convention"
kind = "knowl"
summary = "The convention that a system in contact with a heat and particle bath is described by the grand canonical ensemble."
aliases = ["grand-canonical-ensemble-convention", "Grand canonical ensemble convention"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/grand-canonical-ensemble-convention.md"
+++

The **grand canonical ensemble** describes a system in thermal and chemical equilibrium with a reservoir at fixed [[thermodynamics/temperature-thermo|temperature]] $T$ and [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$. The system can exchange both energy and particles with the reservoir.

## Probability distribution

In the grand canonical ensemble, the probability of finding the system with $N$ particles in [[stat-mech/microstate-classical|microstate]] $(q, p)$ is
$$
\rho_N(q, p) = \frac{1}{\Xi} e^{-\beta (H_N(q, p) - \mu N)},
$$

where:
- $\beta = 1/(k_B T)$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]]
- $H_N$ is the [[stat-mech/hamiltonian-function-classical|Hamiltonian]] for $N$ particles
- $\Xi$ is the [[stat-mech/grand-partition-function|grand partition function]]

The natural thermodynamic potential for this ensemble is the [[thermodynamics/grand-potential|grand potential]]. The bath is modeled as a [[stat-mech/particle-reservoir|particle reservoir]]. For the full formal definition, see [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]].
