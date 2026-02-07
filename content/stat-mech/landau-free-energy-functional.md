---
title: "Landau free-energy functional"
description: "A symmetry-based expansion of the free energy in terms of an order parameter (and possibly its spatial variations), used to describe phase transitions, metastability, and near-critical behavior."
---

A **Landau free-energy functional** is a phenomenological model for equilibrium behavior expressed in terms of an **order parameter** (see {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}). It captures phase transitions by encoding symmetry and stability constraints in a low-order expansion.

## Landau theory for a uniform order parameter

For a scalar order parameter $m$ (e.g., Ising magnetization), the Landau free-energy density near a transition is often written as
$$
f(m)=f_0+\frac{a}{2}m^2+\frac{b}{4}m^4-\;h\,m,
\qquad b>0.
$$

- Symmetry: for an Ising-type $\mathbb{Z}_2$ symmetry at $h=0$, only even powers of $m$ appear.
- Temperature dependence: one commonly models $a=a_0\,(T-T_c)$ (or $a$ changing sign at criticality).

### Minimizers and spontaneous magnetization

At $h=0$:
- If $a>0$, the unique minimizer is $m=0$ (disordered phase).
- If $a<0$, the minimizers are $m=\pm\sqrt{-a/b}$ (ordered phase), corresponding to symmetry breaking and nonzero magnetization; see {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} and {{< knowl id="spontaneous-symmetry-breaking-group" section="stat-mech-lattice" text="spontaneous symmetry breaking" >}}.

Multiple local minima encode metastability (see {{< knowl id="metastable-state" text="metastable states" >}}).

## Landau–Ginzburg functional for spatially varying order parameter

To model interfaces and spatial fluctuations, one introduces an order-parameter field $\phi(x)$ and writes (schematically)
$$
\mathcal{F}[\phi]
={}
\int d^d x\,
\left(
\frac{\kappa}{2}|\nabla \phi(x)|^2
+ \frac{a}{2}\phi(x)^2
+ \frac{b}{4}\phi(x)^4
- h\,\phi(x)
\right),
\qquad b>0,\; \kappa>0.
$$
- The gradient term penalizes rapid spatial variation and leads to finite interface costs, connecting to {{< knowl id="surface-tension-interface" text="surface tension and interfaces" >}}.
- The local polynomial term reproduces the uniform Landau picture when $\phi$ is constant.

## Correlation length from the quadratic approximation

In the disordered phase ($a>0$), the Gaussian (quadratic) approximation yields a characteristic length scale
$$
\xi \sim \sqrt{\kappa/a},
$$
which can be interpreted as a correlation length; compare {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} and the Ornstein–Zernike description {{< knowl id="ornstein-zernike-form" text="Ornstein–Zernike form" >}}.

## Relationship to mean-field and large deviations

- The uniform Landau function $f(m)$ is the natural outcome of a **mean-field approximation** when written as an effective free energy in terms of $m$; see {{< knowl id="mean-field-approximation" text="mean-field approximation" >}}.
- In models where $m$ satisfies an LDP, $f(m)$ often matches (up to constants) the magnetization rate function or its variational representation; see {{< knowl id="ldp-rate-function-magnetization" text="rate function for magnetization" >}}.

Landau functionals provide a bridge between microscopic equilibrium theory and macroscopic thermodynamic stability; compare {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}.
