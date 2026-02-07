---
title: "Entropy density"
description: "Entropy per volume, s = S/V, an intensive measure of entropy content in a unit volume."
---

The **entropy density** is the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}} per {{< knowl id="volume-thermo" text="volume" >}}. It is the natural “per-volume” entropy used in continuum thermodynamics and statistical mechanics.

For a homogeneous system with entropy $S$ and volume $V$, the **entropy density** is
$$
s \equiv \frac{S}{V}.
$$

Equivalently, $S = sV$ in a homogeneous equilibrium state.

In local descriptions (e.g., local equilibrium), one may use a field $s(\mathbf{r})$ whose integral over the system volume gives the total entropy.

## Physical interpretation
Entropy density tells you how much entropy is carried by each unit volume of matter. Like {{< knowl id="number-density" text="number density" >}} and {{< knowl id="energy-density" text="energy density" >}}, it is a {{< knowl id="specific-quantity" text="specific quantity" >}} (per volume) and thus typically {{< knowl id="intensive-variable" text="intensive" >}} for homogeneous systems.

It is also the natural quantity for discussing the {{< knowl id="second-law-thermodynamics" text="second law" >}} in spatially extended systems, where entropy can flow and be produced.

## Key relations (one-component simple system)
Let $u=U/V$ be the {{< knowl id="energy-density" text="energy density" >}} and $n=N/V$ the {{< knowl id="number-density" text="number density" >}}. When $u$ is expressed as a function of $(s,n)$, the differential relation
$$
du = T\,ds + \mu\,dn
$$
implies the entropy-representation differential
$$
ds = \frac{1}{T}\,du - \frac{\mu}{T}\,dn.
$$

In particular, the derivative of entropy density with respect to energy density at fixed $n$ is the reciprocal of {{< knowl id="temperature-thermo" text="temperature" >}}:
$$
\left(\frac{\partial s}{\partial u}\right)_n = \frac{1}{T}.
$$
This is the density analogue of the standard thermodynamic identity connecting entropy and energy, and it underlies the use of inverse temperature (see {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}}) once a convention for the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} is chosen.
