+++
id = "stat-mech/specific-heat-fluctuation"
title = "Specific heat from energy fluctuations"
kind = "knowl"
summary = "Canonical-ensemble identity relating the constant-volume heat capacity to the variance of energy."
aliases = ["specific-heat-fluctuation", "Specific heat from energy fluctuations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/specific-heat-fluctuation.md"
+++

In equilibrium statistical mechanics, the constant-volume heat capacity can be expressed directly in terms of equilibrium energy fluctuations. This is one of the most important examples of a fluctuation–response relation.

## Setup

Work in the [[stat-mech/canonical-ensemble|canonical ensemble]] at fixed volume $V$ and particle number $N$, with Hamiltonian (energy) $H$. Let $\beta$ be the [[thermodynamics/inverse-temperature-beta|inverse temperature]] and $k_B$ the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

The mean energy is the [[stat-mech/ensemble-average|ensemble average]] $\langle H\rangle$. The constant-volume heat capacity (total, not per particle) is the thermodynamic derivative
$$
C_V \;=\; \left(\frac{\partial \langle H\rangle}{\partial T}\right)_{V,N},
$$

matching the thermodynamic notion in [[thermodynamics/heat-capacity-constant-volume|$C_V$]].

## Fluctuation formula

Let $Z(\beta)$ be the [[stat-mech/partition-function-canonical|canonical partition function]]. Then
$$
\langle H\rangle \;=\; -\frac{\partial}{\partial \beta}\log Z(\beta),
\qquad
\mathrm{Var}(H) \;=\; \langle H^2\rangle - \langle H\rangle^2 \;=\; \frac{\partial^2}{\partial \beta^2}\log Z(\beta),
$$

where $\mathrm{Var}(H)$ is the [[stat-mech/variance-observable-ensemble|ensemble variance]] of the energy.

Using $\beta = 1/(k_B T)$, one finds
$$
C_V
\;=\;
\frac{\mathrm{Var}(H)}{k_B T^2}
\;=\;
k_B\,\beta^2\,\mathrm{Var}(H).
$$
Equivalently,
$$
\mathrm{Var}(H) \;=\; k_B T^2\, C_V.
$$

This is a special case of the general machinery summarized in [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from $\log Z$]] and [[stat-mech/construction-observables-from-log-z|observables from $\log Z$]].

## Physical interpretation

- $C_V$ measures how strongly the mean energy reacts to a change in [[thermodynamics/temperature-thermo|temperature]].
- The identity above says: **large energy fluctuations imply large heat capacity**, and vice versa.
- In the canonical ensemble, $\mathrm{Var}(H)\ge 0$ forces $C_V\ge 0$. (Other ensembles, or systems with long-range interactions, can behave differently, but the canonical fluctuation identity itself is always nonnegative.)

For intensive versions, one often defines $c_V=C_V/N$ (per particle) or $C_V/V$ (per volume), depending on context.
