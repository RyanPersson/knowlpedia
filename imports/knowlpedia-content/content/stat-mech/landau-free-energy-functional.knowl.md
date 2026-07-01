+++
id = "stat-mech/landau-free-energy-functional"
title = "Landau free-energy functional"
kind = "knowl"
summary = "A symmetry-based expansion of the free energy in terms of an order parameter (and possibly its spatial variations), used to describe phase transitions, metastability, and near-critical behavior."
aliases = ["landau-free-energy-functional", "Landau free-energy functional"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/landau-free-energy-functional.md"
+++

A **Landau free-energy functional** is a phenomenological model for equilibrium behavior expressed in terms of an **order parameter** (see [[stat-mech-lattice/order-parameter|order parameter]]). It captures phase transitions by encoding symmetry and stability constraints in a low-order expansion.

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
- If $a<0$, the minimizers are $m=\pm\sqrt{-a/b}$ (ordered phase), corresponding to symmetry breaking and nonzero magnetization; see [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] and [[stat-mech-lattice/spontaneous-symmetry-breaking-group|spontaneous symmetry breaking]].

Multiple local minima encode metastability (see [[stat-mech/metastable-state|metastable states]]).

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
- The gradient term penalizes rapid spatial variation and leads to finite interface costs, connecting to [[stat-mech/surface-tension-interface|surface tension and interfaces]].
- The local polynomial term reproduces the uniform Landau picture when $\phi$ is constant.

## Correlation length from the quadratic approximation

In the disordered phase ($a>0$), the Gaussian (quadratic) approximation yields a characteristic length scale
$$
\xi \sim \sqrt{\kappa/a},
$$
which can be interpreted as a correlation length; compare [[stat-mech/correlation-length|correlation length]] and the Ornstein–Zernike description [[stat-mech/ornstein-zernike-form|Ornstein–Zernike form]].

## Relationship to mean-field and large deviations

- The uniform Landau function $f(m)$ is the natural outcome of a **mean-field approximation** when written as an effective free energy in terms of $m$; see [[stat-mech/mean-field-approximation|mean-field approximation]].
- In models where $m$ satisfies an LDP, $f(m)$ often matches (up to constants) the magnetization rate function or its variational representation; see [[stat-mech/ldp-rate-function-magnetization|rate function for magnetization]].

Landau functionals provide a bridge between microscopic equilibrium theory and macroscopic thermodynamic stability; compare [[thermodynamics/thermodynamic-stability|thermodynamic stability]].
