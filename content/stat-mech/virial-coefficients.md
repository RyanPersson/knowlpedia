---
title: "Virial coefficients"
description: "Coefficients in the low-density expansion of the equation of state; encode interactions via integrals (Mayer -function) and connected-graph expansions."
---

Virial coefficients $B_n(T)$ describe interaction corrections to the ideal-gas law in the low-density regime.

They are most naturally derived from the activity/cluster expansion (see {{< knowl id="cluster-integrals-mayer" text="Mayer cluster integrals" >}}) and appear as coefficients in the density expansion of the pressure.

## Virial expansion of the equation of state

Let $\rho=N/V$ be the number density and let $\beta = 1/(k_B T)$, with temperature $T$ as in {{< knowl id="temperature-thermo" section="thermodynamics" text="thermodynamic temperature" >}}.

The virial expansion is
$$
\beta p \;=\; \rho \;+\; B_2(T)\rho^2 \;+\; B_3(T)\rho^3 \;+\; \cdots,
$$

where $p$ is the pressure (see {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}).

Equivalently, the compressibility factor satisfies
$$
Z(\rho,T) \;=\; \frac{\beta p}{\rho} \;=\; 1 + B_2(T)\rho + B_3(T)\rho^2 + \cdots.
$$

Interpretation:
- $B_2(T)$ captures the leading “two-body” correction (excluded volume and/or attraction).
- Higher $B_n(T)$ encode genuine $n$-body correlation effects created by interactions.

## Second virial coefficient from the Mayer $f$-function

For a classical fluid with pair potential $u(r)$ (translation-invariant), define the Mayer $f$-function
$$
f(r) \;=\; e^{-\beta u(r)} - 1.
$$

In $d$ dimensions, the second virial coefficient is
$$
B_2(T) \;=\; -\frac{1}{2}\int_{\mathbb{R}^d} f(r)\, d^dr.
$$

### Example: hard spheres (3D)

For hard spheres of diameter $\sigma$ in $d=3$,
- $u(r)=\infty$ for $r<\sigma$ and $u(r)=0$ for $r\ge \sigma$,
- hence $f(r)=-1$ for $r<\sigma$ and $f(r)=0$ otherwise,

so
$$
B_2 \;=\; -\frac{1}{2}\int_{|r|<\sigma} (-1)\, d^3r
\;=\; \frac{1}{2}\cdot \frac{4\pi}{3}\sigma^3
\;=\; \frac{2\pi}{3}\sigma^3.
$$

## Higher virial coefficients and Mayer graphs

For $n\ge 3$, $B_n(T)$ can be written as integrals over connected graphs built from $f$-bonds, most systematically via the cluster integrals in {{< knowl id="cluster-integrals-mayer" text="Mayer’s expansion" >}}.

Concretely, one typically computes:
1. the connected-graph coefficients $b_n(T)$ in the activity expansion of $\log \Xi$, then
2. eliminates the activity to rewrite $\beta p$ as a series in $\rho$.

In the common convention where the ideal term is normalized so that $b_1=1$, the first relations are
$$
B_2 = -b_2,
\qquad
B_3 = 4b_2^2 - 2b_3.
$$

(Conventions vary by where thermal-wavelength factors are placed; the structure “virial coefficients are polynomials in cluster integrals” is robust.)

## Convergence and regime of validity

The virial series is an *asymptotic/analytic* expansion in $\rho$ whose convergence depends on temperature and the interaction potential. Rigorous convergence criteria are typically proved using cluster expansion methods (see {{< knowl id="cluster-expansion-theorem" text="cluster expansion theorems" >}} and {{< knowl id="virial-expansion-convergence" text="virial expansion convergence" >}}).

## Prerequisites

- {{< knowl id="pressure-thermo" section="thermodynamics" text="Pressure" >}}
- {{< knowl id="temperature-thermo" section="thermodynamics" text="Temperature" >}}
- {{< knowl id="canonical-ensemble" section="stat-mech" text="Canonical ensemble" >}}
- {{< knowl id="partition-function-canonical" section="stat-mech" text="Canonical partition function" >}}
- {{< knowl id="cluster-integrals-mayer" text="Mayer cluster integrals" >}}
