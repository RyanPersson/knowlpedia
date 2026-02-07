---
title: "Particle reservoir"
description: "A large system that exchanges particles with a smaller system at fixed chemical potential."
---

A **particle reservoir** is a thermodynamic system so large that it can exchange particles with another system without significantly changing its own chemical potential \(\mu\).

## Role in grand canonical ensemble
When a system is in contact with both a {{< knowl id="thermal-reservoir" section="thermodynamics" text="heat bath" >}} (temperature \(T\)) and a particle reservoir (chemical potential \(\mu\)), it is described by the {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}}.

The reservoir imposes a fixed chemical potential, while the system's particle number \(N\) fluctuates.

## Mathematical idealization
A reservoir has effectively infinite capacity:
- Adding or removing particles does not change \(\mu\).
- The combined system (reservoir + small system) is isolated.
- At equilibrium, chemical potentials equalize.

## Grand canonical distribution
The probability of a microstate with energy \(E\) and particle number \(N\) is
$$
P(E, N) = \frac{1}{\Xi} e^{-\beta(E - \mu N)}
$$
where \(\Xi\) is the {{< knowl id="grand-partition-function" section="stat-mech" text="grand partition function" >}} and \(\beta = 1/(k_B T)\).

## Applications
- Open systems in chemistry and biology.
- Quantum gases with variable particle number.
- Adsorption phenomena.
