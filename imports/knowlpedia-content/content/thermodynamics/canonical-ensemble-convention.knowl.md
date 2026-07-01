+++
id = "thermodynamics/canonical-ensemble-convention"
title = "Canonical ensemble convention"
kind = "knowl"
summary = "The convention that a system in thermal contact with a heat bath at temperature T is described by the canonical ensemble."
aliases = ["canonical-ensemble-convention", "Canonical ensemble convention"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/canonical-ensemble-convention.md"
+++

The **canonical ensemble** describes a system in thermal equilibrium with a heat bath at fixed [[thermodynamics/temperature-thermo|temperature]] $T$. The system can exchange energy with the bath but has fixed volume $V$ and particle number $N$.

## Probability distribution

In the canonical ensemble, the probability of finding the system in [[stat-mech/microstate-classical|microstate]] $(q, p)$ is
$$
\rho(q, p) = \frac{1}{Z} e^{-\beta H(q, p)},
$$

where:
- $\beta = 1/(k_B T)$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]]
- $H$ is the [[stat-mech/hamiltonian-function-classical|Hamiltonian]]
- $Z$ is the [[stat-mech/partition-function-canonical|canonical partition function]]

The natural thermodynamic potential for this ensemble is the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]. The bath is modeled as a [[thermodynamics/thermal-reservoir|thermal reservoir]]. For the full formal definition, see [[stat-mech/canonical-ensemble|canonical ensemble]].
