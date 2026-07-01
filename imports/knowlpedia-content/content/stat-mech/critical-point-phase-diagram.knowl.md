+++
id = "stat-mech/critical-point-phase-diagram"
title = "Critical points in phase diagrams"
kind = "knowl"
summary = "How critical points appear in phase diagrams as endpoints of coexistence lines and where correlation length diverges."
aliases = ["critical-point-phase-diagram", "Critical points in phase diagrams"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/critical-point-phase-diagram.md"
+++

A **critical point** is a point in a phase diagram where two distinct phases become indistinguishable and the system exhibits scale-invariant fluctuations. In many systems it is the endpoint of a first-order coexistence curve.

## Canonical picture: coexistence line ending at a critical point
Consider a liquid–vapor system in the $(T,p)$ or $(T,\rho)$ plane, or the Ising/lattice-gas system in the $(T,h)$ or $(T,\mu)$ plane. A typical structure:

- For $T<T_c$: two-phase region with a first-order transition (coexistence).
- At $T=T_c$: the coexistence line ends at a **critical point**.
- For $T>T_c$: a single phase.

In Ising language, the coexistence line is the $h=0$ line for $T<T_c$, where two symmetry-related magnetized phases coexist; see [[stat-mech-lattice/phase-transition-gibbs|phase transitions in Gibbs measures]].

## Scaling variables near criticality
Let
$$
t=\frac{T-T_c}{T_c}
$$
be the reduced temperature. Standard critical behavior is expressed via [[stat-mech/critical-exponent|critical exponents]]:

- Order parameter (e.g., magnetization or density difference):
$$
m(t,0)\sim (-t)^\beta \quad (t\to 0^-).
$$
- Susceptibility:
$$
\chi(t,0)\sim |t|^{-\gamma}.
$$
- Correlation length:
$$
\xi(t,0)\sim |t|^{-\nu},
$$

where $\xi$ is the [[stat-mech/correlation-length|correlation length]] associated to the two-point [[stat-mech/correlation-function-two-point|correlation function]].

At the critical point, $\xi$ diverges and the system becomes effectively scale-free.

## Phase-diagram interpretation in lattice models
- In the [[stat-mech-lattice/ising-model|Ising model]] with coupling $J>0$, $(T,h)$ is the natural diagram:
  - For $T<T_c$: discontinuity of $m$ across $h=0$ (first-order in the field variable).
  - At $T=T_c, h=0$: critical point.
- Via [[stat-mech-lattice/lattice-gas-ising-mapping|lattice gas–Ising mapping]], the same structure describes liquid–vapor criticality in a lattice gas.

## Prerequisites
- [[stat-mech-lattice/order-parameter|order parameters]]
- [[stat-mech-lattice/ising-2d-phase-transition|2D Ising phase transition]]
- [[stat-mech/scaling-relation-exponents|scaling relations]]
