---
title: "Microcanonical ensemble"
description: "The statistical ensemble of isolated systems with fixed energy, particle number, and volume."
---

The **microcanonical ensemble** describes an isolated thermodynamic system with fixed total energy \(E\), particle number \(N\), and volume \(V\).

## Classical formulation
The ensemble assigns equal probability to all {{< knowl id="microstate-classical" text="microstates" >}} in a thin energy shell:
$$
\rho(q, p) = \frac{1}{\Omega(E, V, N)} \delta(H(q,p) - E)
$$
where \(\Omega\) is the {{< knowl id="density-of-states" section="stat-mech" text="density of states" >}} and \(H\) is the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}}.

## Microcanonical entropy
The {{< knowl id="boltzmann-entropy" text="Boltzmann entropy" >}} is
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
In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, the microcanonical ensemble is equivalent to the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical" >}} and {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical" >}} ensembles for typical observables.
