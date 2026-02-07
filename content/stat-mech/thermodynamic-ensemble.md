---
title: "Thermodynamic ensemble"
description: "A probability distribution over microstates representing a macroscopic thermodynamic system."
---

A **thermodynamic ensemble** is a probability distribution over the {{< knowl id="microstate-classical" text="microstates" >}} of a system, used to compute macroscopic observables as statistical averages.

## Main ensembles

| Ensemble | Fixed quantities | Fluctuating | Characteristic function |
|----------|-----------------|-------------|------------------------|
| {{< knowl id="microcanonical-ensemble" text="Microcanonical" >}} | \(E, V, N\) | — | Entropy \(S\) |
| {{< knowl id="canonical-ensemble" section="stat-mech" text="Canonical" >}} | \(T, V, N\) | \(E\) | Free energy \(F\) |
| {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="Grand canonical" >}} | \(T, V, \mu\) | \(E, N\) | Grand potential \(\Omega\) |

## Ensemble equivalence
In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, different ensembles give the same values for intensive quantities and the same thermodynamic relations. This is **ensemble equivalence**.

## Statistical averages
For an observable \(A\), the ensemble average is
$$
\langle A \rangle = \sum_i p_i A_i \quad \text{(discrete)} \quad \text{or} \quad \int A(q,p) \rho(q,p)\, dq\, dp \quad \text{(continuous)}.
$$

## Fluctuations
Ensembles also predict fluctuations around mean values:
$$
\langle (\Delta A)^2 \rangle = \langle A^2 \rangle - \langle A \rangle^2.
$$
These typically scale as \(1/N\) relative to the mean.
