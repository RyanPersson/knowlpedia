+++
id = "thermodynamics/entropy-density"
title = "Entropy density"
kind = "knowl"
summary = "Entropy per volume, s = S/V, an intensive measure of entropy content in a unit volume."
aliases = ["entropy-density", "Entropy density"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/entropy-density.md"
+++

The **entropy density** is the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] per [[thermodynamics/volume-thermo|volume]]. It is the natural “per-volume” entropy used in continuum thermodynamics and statistical mechanics.

For a homogeneous system with entropy $S$ and volume $V$, the **entropy density** is
$$
s \equiv \frac{S}{V}.
$$

Equivalently, $S = sV$ in a homogeneous equilibrium state.

In local descriptions (e.g., local equilibrium), one may use a field $s(\mathbf{r})$ whose integral over the system volume gives the total entropy.

## Physical interpretation
Entropy density tells you how much entropy is carried by each unit volume of matter. Like [[thermodynamics/number-density|number density]] and [[thermodynamics/energy-density|energy density]], it is a [[thermodynamics/specific-quantity|specific quantity]] (per volume) and thus typically [[thermodynamics/intensive-variable|intensive]] for homogeneous systems.

It is also the natural quantity for discussing the [[thermodynamics/second-law-thermodynamics|second law]] in spatially extended systems, where entropy can flow and be produced.

## Key relations (one-component simple system)
Let $u=U/V$ be the [[thermodynamics/energy-density|energy density]] and $n=N/V$ the [[thermodynamics/number-density|number density]]. When $u$ is expressed as a function of $(s,n)$, the differential relation
$$
du = T\,ds + \mu\,dn
$$
implies the entropy-representation differential
$$
ds = \frac{1}{T}\,du - \frac{\mu}{T}\,dn.
$$

In particular, the derivative of entropy density with respect to energy density at fixed $n$ is the reciprocal of [[thermodynamics/temperature-thermo|temperature]]:
$$
\left(\frac{\partial s}{\partial u}\right)_n = \frac{1}{T}.
$$
This is the density analogue of the standard thermodynamic identity connecting entropy and energy, and it underlies the use of inverse temperature (see [[thermodynamics/inverse-temperature-beta|inverse temperature]]) once a convention for the [[thermodynamics/boltzmann-constant|Boltzmann constant]] is chosen.
