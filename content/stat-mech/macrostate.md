---
title: "Macrostate"
description: "A specification of a system by its macroscopic thermodynamic variables, corresponding to many possible microstates."
---

A **macrostate** of a thermodynamic system is a specification in terms of macroscopic variables such as temperature $T$, pressure $P$, volume $V$, and particle number $N$ (or chemical potential $\mu$).

## Relation to microstates

Many distinct {{< knowl id="microstate-classical" text="microstates" >}} typically correspond to the same macrostate. The {{< knowl id="boltzmann-entropy" text="Boltzmann entropy" >}} quantifies this multiplicity:
$$
S = k_B \ln \Omega,
$$

where $\Omega$ is the number of microstates (or phase space volume) compatible with the given macrostate.

## In equilibrium statistical mechanics

The macrostate is characterized by the values of {{< knowl id="state-function" section="thermodynamics" text="state functions" >}}. Different {{< knowl id="thermodynamic-ensemble" text="ensembles" >}} (microcanonical, canonical, grand canonical) correspond to different choices of which macroscopic variables are held fixed.
