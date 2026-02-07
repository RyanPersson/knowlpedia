---
title: "Microcanonical entropy density"
description: "The entropy per unit volume (or per particle) in the microcanonical ensemble, derived from the density of states."
---

In the {{< knowl id="microcanonical-ensemble" text="microcanonical ensemble" >}} at energy $E$, the **microcanonical entropy** is
$$
S(E, V, N) = k_B \ln \Omega(E, V, N),
$$

where $\Omega(E, V, N)$ is the number of {{< knowl id="microstate-classical" text="microstates" >}} (or the {{< knowl id="phase-space-volume-element" text="phase space volume" >}}) at energy $E$.

## Entropy density

The **entropy density** (entropy per unit volume) is
$$
s = \frac{S}{V} = \frac{k_B}{V} \ln \Omega(E, V, N).
$$

In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}} $V, N \to \infty$ with fixed density $\rho = N/V$ and energy density $u = E/V$, one typically has
$$
s(u, \rho) = \lim_{V \to \infty} \frac{S(uV, V, \rho V)}{V}.
$$

## Connection to temperature

The {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} is determined by
$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V, N} = \frac{\partial s}{\partial u}.
$$

This relates the microcanonical entropy to the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} via Legendre transformation.
