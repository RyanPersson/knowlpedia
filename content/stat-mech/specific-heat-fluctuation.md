---
title: "Specific heat from energy fluctuations"
description: "Canonical-ensemble identity relating the constant-volume heat capacity to the variance of energy."
---

In equilibrium statistical mechanics, the constant-volume heat capacity can be expressed directly in terms of equilibrium energy fluctuations. This is one of the most important examples of a fluctuation–response relation.

## Setup

Work in the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} at fixed volume $V$ and particle number $N$, with Hamiltonian (energy) $H$. Let $\beta$ be the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} and $k_B$ the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}.

The mean energy is the {{< knowl id="ensemble-average" text="ensemble average" >}} $\langle H\rangle$. The constant-volume heat capacity (total, not per particle) is the thermodynamic derivative
$$
C_V \;=\; \left(\frac{\partial \langle H\rangle}{\partial T}\right)_{V,N},
$$

matching the thermodynamic notion in {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="$C_V$" >}}.

## Fluctuation formula

Let $Z(\beta)$ be the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}. Then
$$
\langle H\rangle \;=\; -\frac{\partial}{\partial \beta}\log Z(\beta),
\qquad
\mathrm{Var}(H) \;=\; \langle H^2\rangle - \langle H\rangle^2 \;=\; \frac{\partial^2}{\partial \beta^2}\log Z(\beta),
$$

where $\mathrm{Var}(H)$ is the {{< knowl id="variance-observable-ensemble" text="ensemble variance" >}} of the energy.

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

This is a special case of the general machinery summarized in {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuation formulas from $\log Z$" >}} and {{< knowl id="construction-observables-from-log-z" text="observables from $\log Z$" >}}.

## Physical interpretation

- $C_V$ measures how strongly the mean energy reacts to a change in {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- The identity above says: **large energy fluctuations imply large heat capacity**, and vice versa.
- In the canonical ensemble, $\mathrm{Var}(H)\ge 0$ forces $C_V\ge 0$. (Other ensembles, or systems with long-range interactions, can behave differently, but the canonical fluctuation identity itself is always nonnegative.)

For intensive versions, one often defines $c_V=C_V/N$ (per particle) or $C_V/V$ (per volume), depending on context.
