+++
id = "stat-mech/microcanonical-ensemble"
title = "Microcanonical ensemble"
kind = "knowl"
summary = "The statistical ensemble of isolated systems with fixed energy, particle number, and volume."
aliases = ["microcanonical-ensemble", "Microcanonical ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/microcanonical-ensemble.md"
+++

The **microcanonical ensemble** describes an isolated thermodynamic system with fixed total energy \(E\), particle number \(N\), and volume \(V\).

## Classical formulation
The ensemble assigns equal probability to all [[stat-mech/microstate-classical|microstates]] in a thin energy shell:
$$
\rho(q, p) = \frac{1}{\Omega(E, V, N)} \delta(H(q,p) - E)
$$
where \(\Omega\) is the [[stat-mech/density-of-states|density of states]] and \(H\) is the [[stat-mech/hamiltonian-function-classical|Hamiltonian]].

## Microcanonical entropy
The [[stat-mech/boltzmann-entropy|Boltzmann entropy]] is
$$
S(E, V, N) = k_B \ln \Omega(E, V, N)
$$
where \(\Omega\) counts the number of accessible microstates (or phase space volume).

## Thermodynamic quantities
Temperature and pressure emerge from entropy derivatives:
$$
\frac{1}{T} = \frac{\partial S}{\partial E}\bigg|_{V,N}, \quad \frac{P}{T} = \frac{\partial S}{\partial V}\bigg|_{E,N}.
$$

## Relation to other ensembles
In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], the microcanonical ensemble is equivalent to the [[stat-mech/canonical-ensemble|canonical]] and [[stat-mech/grand-canonical-ensemble|grand canonical]] ensembles for typical observables.
