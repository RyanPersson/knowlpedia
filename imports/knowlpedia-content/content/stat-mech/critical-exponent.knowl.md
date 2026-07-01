+++
id = "stat-mech/critical-exponent"
title = "Critical exponents"
kind = "knowl"
summary = "Definitions of the standard critical exponents and what physical singularities they quantify near a continuous phase transition."
aliases = ["critical-exponent", "Critical exponents"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/critical-exponent.md"
+++

**Critical exponents** quantify how thermodynamic observables and correlations become singular as the system approaches a critical point. They are central to [[stat-mech/universality-class|universality]]: many microscopic models share the same exponents.

Let $t=(T-T_c)/T_c$ and let $h$ be the field conjugate to the [[stat-mech-lattice/order-parameter|order parameter]] (e.g., magnetic field for magnetization).

## Standard thermodynamic exponents
### Heat capacity exponent $\alpha$
For the constant-volume heat capacity (or its analog),
$$
C \sim |t|^{-\alpha}.
$$
(Connects to [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]].)

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
The [[stat-mech/correlation-length|correlation length]] diverges as
$$
\xi(t,0)\sim |t|^{-\nu}.
$$

### Anomalous dimension exponent $\eta$
At criticality, the two-point [[stat-mech/correlation-function-two-point|correlation function]] typically has power-law decay:
$$
\langle \phi(0)\phi(r)\rangle_c \sim \frac{1}{|r|^{d-2+\eta}}
\quad (|r|\to\infty,\ t=0),
$$

for an appropriate local field $\phi$ (e.g., spin component).

## Where these come from (organizing principle)
Many exponents can be read from the singular part of the free energy density (see [[stat-mech/free-energy-statistical|statistical free energy]]) and from how coarse-graining changes effective couplings under a [[stat-mech/renormalization-group-transformation|renormalization-group transformation]].

## Prerequisites
- [[stat-mech/critical-point-phase-diagram|critical points in phase diagrams]]
- [[stat-mech/scaling-relation-exponents|scaling relations among exponents]]
- [[stat-mech-lattice/phase-transition-gibbs|phase transitions and Gibbs measures]]
