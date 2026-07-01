+++
id = "stat-mech/microcanonical-entropy-density"
title = "Microcanonical entropy density"
kind = "knowl"
summary = "The entropy per unit volume (or per particle) in the microcanonical ensemble, derived from the density of states."
aliases = ["microcanonical-entropy-density", "Microcanonical entropy density"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/microcanonical-entropy-density.md"
+++

In the [[stat-mech/microcanonical-ensemble|microcanonical ensemble]] at energy $E$, the **microcanonical entropy** is
$$
S(E, V, N) = k_B \ln \Omega(E, V, N),
$$

where $\Omega(E, V, N)$ is the number of [[stat-mech/microstate-classical|microstates]] (or the [[stat-mech/phase-space-volume-element|phase space volume]]) at energy $E$.

## Entropy density

The **entropy density** (entropy per unit volume) is
$$
s = \frac{S}{V} = \frac{k_B}{V} \ln \Omega(E, V, N).
$$

In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] $V, N \to \infty$ with fixed density $\rho = N/V$ and energy density $u = E/V$, one typically has
$$
s(u, \rho) = \lim_{V \to \infty} \frac{S(uV, V, \rho V)}{V}.
$$

## Connection to temperature

The [[thermodynamics/temperature-thermo|temperature]] is determined by
$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V, N} = \frac{\partial s}{\partial u}.
$$

This relates the microcanonical entropy to the [[stat-mech/canonical-ensemble|canonical ensemble]] via Legendre transformation.
