---
title: "Ornstein–Zernike form"
description: "Phenomenological real- and Fourier-space asymptotics of connected correlations in a phase with finite correlation length, including the Lorentzian small- structure factor."
---

The Ornstein–Zernike (OZ) form is a standard asymptotic description of how *connected* correlations decay in a translation-invariant phase with a finite correlation length $\xi$ (see {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}).

## Setup: connected correlations and structure factor

Let $G(r)$ denote the connected two-point correlation function of an observable/order-parameter field:
$$
G(r) \;=\; \langle \phi(0)\phi(r)\rangle - \langle \phi\rangle^2,
$$
as in {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation functions" >}}.

Its Fourier transform (often called the structure factor) is
$$
S(k) \;=\; \sum_{r} e^{i k\cdot r}\, G(r)
\quad \text{(lattice)}, 
\qquad
S(k) \;=\; \int_{\mathbb{R}^d} e^{i k\cdot r}\, G(r)\, d^dr
\quad \text{(continuum)},
$$

matching the notion in {{< knowl id="structure-factor" text="structure factor" >}}. The zero-mode $S(0)$ is proportional to the susceptibility.

## OZ small-$k$ ansatz (Fourier space)

The core OZ statement is a *quadratic* expansion of the inverse structure factor near $k=0$:
$$
S(k)^{-1} \;\approx\; S(0)^{-1}\,\bigl(1 + (k\xi)^2\bigr)
\qquad (|k|\xi \ll 1),
$$
equivalently
$$
S(k) \;\approx\; \frac{S(0)}{1 + (k\xi)^2}.
$$

This is the “Lorentzian” line shape: a single correlation length $\xi$ controls the width of $S(k)$ around $k=0$.

A common operational definition extracted from this expansion is the *second-moment* correlation length:
$$
\xi^2 \;=\; -\frac{1}{2d}\,\frac{\nabla_k^2 S(k)\big|_{k=0}}{S(0)},
$$

when $S(k)$ is smooth near $0$.

## Real-space asymptotic implied by OZ

Inverting the Lorentzian form yields exponential decay with an algebraic prefactor. In $d$ dimensions,
$$
G(r) \;\sim\; \frac{A}{r^{(d-1)/2}}\,e^{-r/\xi},
\qquad r\to\infty,
$$

for some amplitude $A$ (model- and observable-dependent).

Interpretation:
- $\xi$ sets the exponential decay scale.
- The power-law prefactor is the generic large-$r$ behavior of the inverse Fourier transform of a simple pole/“massive” propagator.

## Relation to critical scaling

Near a critical point (see {{< knowl id="critical-point-phase-diagram" text="critical points" >}}), the OZ form is often refined to incorporate the anomalous dimension $\eta$ (see {{< knowl id="critical-exponent" text="critical exponents" >}}):
$$
S(k) \;=\; k^{-2+\eta}\,F(k\xi),
$$

for a scaling function $F$. At criticality $\xi=\infty$, this implies
$$
S(k) \sim k^{-2+\eta},
\qquad
G(r) \sim r^{-(d-2+\eta)}.
$$

Scaling relations then connect exponents, e.g. $\gamma=(2-\eta)\nu$ (see {{< knowl id="scaling-relation-exponents" text="scaling relations" >}}).

## Prerequisites

- {{< knowl id="correlation-function-two-point" section="stat-mech" text="Two-point correlation function" >}}
- {{< knowl id="correlation-length" section="stat-mech" text="Correlation length" >}}
- {{< knowl id="structure-factor" text="Structure factor" >}}
- {{< knowl id="critical-exponent" text="Critical exponent" >}}
- {{< knowl id="scaling-relation-exponents" text="Scaling relations among exponents" >}}
