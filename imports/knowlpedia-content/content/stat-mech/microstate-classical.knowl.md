+++
id = "stat-mech/microstate-classical"
title = "Microstate (classical)"
kind = "knowl"
summary = "A complete specification of the positions and momenta of all particles in a classical system; a single point in phase space."
aliases = ["microstate-classical", "Microstate (classical)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/microstate-classical.md"
+++

A **microstate** of a classical mechanical system is a complete specification of its instantaneous configuration: the positions and momenta of all constituent particles.

Formally, a microstate is a point $(q, p)$ in the system's [[stat-mech/phase-space-classical|phase space]] $\Gamma$.

## Contrast with macrostate

While a microstate specifies all microscopic details, a [[stat-mech/macrostate|macrostate]] specifies only macroscopic observables (temperature, pressure, volume, etc.). Many distinct microstates typically correspond to the same macrostate.

## In statistical mechanics

The fundamental postulate of statistical mechanics is that equilibrium properties can be computed by averaging over microstates according to an appropriate probability distribution:

- [[stat-mech/microcanonical-ensemble|Microcanonical ensemble]]: uniform distribution over microstates at fixed energy.
- [[stat-mech/canonical-ensemble|Canonical ensemble]]: Boltzmann distribution $\propto e^{-\beta H}$ over all microstates.
- [[stat-mech/grand-canonical-ensemble|Grand canonical ensemble]]: distribution over microstates with varying particle number.
