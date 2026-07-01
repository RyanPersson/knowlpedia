+++
id = "stat-mech/macrostate"
title = "Macrostate"
kind = "knowl"
summary = "A specification of a system by its macroscopic thermodynamic variables, corresponding to many possible microstates."
aliases = ["macrostate"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/macrostate.md"
+++

A **macrostate** of a thermodynamic system is a specification in terms of macroscopic variables such as temperature $T$, pressure $P$, volume $V$, and particle number $N$ (or chemical potential $\mu$).

## Relation to microstates

Many distinct [[stat-mech/microstate-classical|microstates]] typically correspond to the same macrostate. The [[stat-mech/boltzmann-entropy|Boltzmann entropy]] quantifies this multiplicity:
$$
S = k_B \ln \Omega,
$$

where $\Omega$ is the number of microstates (or phase space volume) compatible with the given macrostate.

## In equilibrium statistical mechanics

The macrostate is characterized by the values of [[thermodynamics/state-function|state functions]]. Different [[stat-mech/thermodynamic-ensemble|ensembles]] (microcanonical, canonical, grand canonical) correspond to different choices of which macroscopic variables are held fixed.
