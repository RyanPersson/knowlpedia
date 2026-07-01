+++
id = "stat-mech/thermodynamic-ensemble"
title = "Thermodynamic ensemble"
kind = "knowl"
summary = "A probability distribution over microstates representing a macroscopic thermodynamic system."
aliases = ["thermodynamic-ensemble", "Thermodynamic ensemble"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/thermodynamic-ensemble.md"
+++

A **thermodynamic ensemble** is a probability distribution over the [[stat-mech/microstate-classical|microstates]] of a system, used to compute macroscopic observables as statistical averages.

## Main ensembles

| Ensemble | Fixed quantities | Fluctuating | Characteristic function |
|----------|-----------------|-------------|------------------------|
| [[stat-mech/microcanonical-ensemble|Microcanonical]] | \(E, V, N\) | — | Entropy \(S\) |
| [[stat-mech/canonical-ensemble|Canonical]] | \(T, V, N\) | \(E\) | Free energy \(F\) |
| [[stat-mech/grand-canonical-ensemble|Grand canonical]] | \(T, V, \mu\) | \(E, N\) | Grand potential \(\Omega\) |

## Ensemble equivalence
In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], different ensembles give the same values for intensive quantities and the same thermodynamic relations. This is **ensemble equivalence**.

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
