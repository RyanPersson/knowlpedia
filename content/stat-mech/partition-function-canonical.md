---
title: "Canonical partition function"
description: "Normalization of the canonical ensemble; generates thermodynamic potentials and equilibrium averages at fixed (β,V,N)."
---


The **canonical partition function** $Z(\beta,V,N)$ is the normalization constant of the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} describing equilibrium at fixed inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}), fixed volume $V$, and fixed particle number $N$.

For a system with discrete energy levels $\{E_s\}$ (indexed by microstates $s$), it is defined by
$$
Z(\beta,V,N) = \sum_{s} e^{-\beta E_s}.
$$

For a classical system with {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} $H(x)$ on {{< knowl id="phase-space-classical" text="phase space" >}}, one writes schematically
$$
Z(\beta,V,N) = \int dx\; e^{-\beta H(x)},
$$

where $dx$ denotes the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} at fixed $V$ (often with conventional prefactors such as $1/N!$ and powers of Planck’s constant to make $Z$ dimensionless).

In either case, the canonical probability of a microstate is
$$
\mathbb{P}(s) = \frac{e^{-\beta E_s}}{Z(\beta,V,N)},
\qquad\text{or}\qquad
\mathbb{P}(dx) = \frac{e^{-\beta H(x)}}{Z(\beta,V,N)}\,dx.
$$

## Connection to density of states

If $\Omega(E;V,N)$ denotes the {{< knowl id="density-of-states" text="density of states" >}} (or microcanonical level density), then $Z$ is its Laplace transform:
$$
Z(\beta,V,N) = \int dE\; \Omega(E;V,N)\, e^{-\beta E}.
$$
This is the basic bridge between canonical equilibrium and the {{< knowl id="microcanonical-measure" text="microcanonical description" >}} (see also {{< knowl id="construction-canonical-from-microcanonical" text="canonical-from-microcanonical construction" >}}).

## Thermodynamic potential: Helmholtz free energy

The canonical partition function generates the {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}:
$$
F(T,V,N) = -k_B T \ln Z(\beta,V,N),
$$

where $k_B$ is the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}} and $\beta = 1/(k_B T)$. In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, $F$ becomes extensive and is the natural potential at fixed $(T,V,N)$ (compare with {{< knowl id="free-energy-statistical" text="statistical free energy" >}}).

## Key derivative formulas (energy, pressure, fluctuations)

The logarithm of $Z$ is a generating function for equilibrium averages (see {{< knowl id="construction-observables-from-log-z" text="observables from log partition functions" >}}). In particular:

**Mean energy**
$$
\langle E\rangle = -\frac{\partial \ln Z}{\partial \beta}.
$$

**Energy fluctuations and heat capacity**
$$
\mathrm{Var}(E) = \frac{\partial^2 \ln Z}{\partial \beta^2},
\qquad
C_V = \left(\frac{\partial \langle E\rangle}{\partial T}\right)_{V,N}
= k_B \beta^2\, \mathrm{Var}(E).
$$
This is the canonical fluctuation formula behind {{< knowl id="specific-heat-fluctuation" text="specific heat from fluctuations" >}}.

**Pressure from $Z$**
The mechanical pressure can be obtained from volume dependence of $Z$:
$$
p = k_B T \left(\frac{\partial \ln Z}{\partial V}\right)_{\beta,N},
$$
as summarized in {{< knowl id="pressure-from-partition-function" text="pressure from the partition function" >}}.

These identities show how $Z$ simultaneously normalizes the ensemble and encodes the response of the equilibrium state to changes in control parameters.
