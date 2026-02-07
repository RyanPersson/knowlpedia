---
title: "Critical exponents"
description: "Definitions of the standard critical exponents and what physical singularities they quantify near a continuous phase transition."
---

**Critical exponents** quantify how thermodynamic observables and correlations become singular as the system approaches a critical point. They are central to {{< knowl id="universality-class" text="universality" >}}: many microscopic models share the same exponents.

Let $t=(T-T_c)/T_c$ and let $h$ be the field conjugate to the {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}} (e.g., magnetic field for magnetization).

## Standard thermodynamic exponents
### Heat capacity exponent $\alpha$
For the constant-volume heat capacity (or its analog),
$$
C \sim |t|^{-\alpha}.
$$
(Connects to {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}.)

### Order parameter exponent $\beta$
For $h=0$ and $t\to 0^-$ (below criticality),
$$
m(t,0)\sim (-t)^\beta.
$$

### Susceptibility exponent $\gamma$
For $h=0$ and $t\to 0$,
$$
\chi(t,0)=\frac{\partial m}{\partial h}(t,0)\sim |t|^{-\gamma}.
$$

### Critical isotherm exponent $\delta$
At $t=0$ (critical temperature),
$$
m(0,h)\sim |h|^{1/\delta}\,\mathrm{sign}(h)\quad (h\to 0).
$$

## Correlation exponents
### Correlation length exponent $\nu$
The {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} diverges as
$$
\xi(t,0)\sim |t|^{-\nu}.
$$

### Anomalous dimension exponent $\eta$
At criticality, the two-point {{< knowl id="correlation-function-two-point" section="stat-mech" text="correlation function" >}} typically has power-law decay:
$$
\langle \phi(0)\phi(r)\rangle_c \sim \frac{1}{|r|^{d-2+\eta}}
\quad (|r|\to\infty,\ t=0),
$$

for an appropriate local field $\phi$ (e.g., spin component).

## Where these come from (organizing principle)
Many exponents can be read from the singular part of the free energy density (see {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}) and from how coarse-graining changes effective couplings under a {{< knowl id="renormalization-group-transformation" text="renormalization-group transformation" >}}.

## Prerequisites
- {{< knowl id="critical-point-phase-diagram" text="critical points in phase diagrams" >}}
- {{< knowl id="scaling-relation-exponents" text="scaling relations among exponents" >}}
- {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions and Gibbs measures" >}}
