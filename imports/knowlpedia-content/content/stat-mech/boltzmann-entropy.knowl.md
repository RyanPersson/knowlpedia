+++
id = "stat-mech/boltzmann-entropy"
title = "Boltzmann entropy"
kind = "knowl"
summary = "The entropy defined as the logarithm of the number of accessible microstates."
aliases = ["boltzmann-entropy", "Boltzmann entropy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/boltzmann-entropy.md"
+++

The **Boltzmann entropy** of a [[stat-mech/macrostate|macrostate]] is
$$
S = k_B \ln \Omega
$$
where \(\Omega\) is the number of [[stat-mech/microstate-classical|microstates]] compatible with the macroscopic constraints, and \(k_B\) is Boltzmann's constant.

## Interpretation
Entropy measures the logarithm of the phase space volume (or state count) accessible to the system. Higher entropy means more microscopic configurations are compatible with the observed macroscopic state.

## Properties
- **Extensivity**: For independent subsystems, \(\Omega_{\text{tot}} = \Omega_1 \Omega_2\), so \(S_{\text{tot}} = S_1 + S_2\).
- **Non-negativity**: \(S \geq 0\) (since \(\Omega \geq 1\)).
- **Maximum at equilibrium**: Isolated systems evolve toward states of maximum entropy.

## Relation to Gibbs entropy
For the [[stat-mech/microcanonical-ensemble|microcanonical ensemble]] with uniform distribution, the Gibbs entropy \(S = -k_B \sum_i p_i \ln p_i\) reduces to the Boltzmann form.

## Historical note
Boltzmann's formula \(S = k \log W\) is inscribed on his tombstone in Vienna.
