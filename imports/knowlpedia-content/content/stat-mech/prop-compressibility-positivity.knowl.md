+++
id = "stat-mech/prop-compressibility-positivity"
title = "Positivity of isothermal compressibility from stability"
kind = "knowl"
summary = "Mechanical stability implies the isothermal compressibility is nonnegative, equivalently that pressure decreases with volume at fixed temperature."
aliases = ["prop-compressibility-positivity", "Positivity of isothermal compressibility from stability"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/prop-compressibility-positivity.md"
+++

## Statement

For a thermodynamically stable equilibrium system at fixed temperature and composition, the [[thermodynamics/isothermal-compressibility|isothermal compressibility]]
$$
\kappa_T := -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{T,N}
$$
satisfies
$$
\kappa_T \ge 0.
$$
Equivalently,
$$
\left(\frac{\partial P}{\partial V}\right)_{T,N} \le 0.
$$

## Key hypotheses

- Equilibrium description in terms of the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)$.
- $F$ is twice differentiable in $V$ at fixed $T,N$.
- Mechanical stability (a component of [[thermodynamics/thermodynamic-stability|thermodynamic stability]]), expressed as convexity of $F$ in $V$ at fixed $T,N$:
  $$
  \left(\frac{\partial^2 F}{\partial V^2}\right)_{T,N} \ge 0.
  $$

## Key conclusions

- Since [[thermodynamics/pressure-thermo|pressure]] is given by
  $$
  P = -\left(\frac{\partial F}{\partial V}\right)_{T,N},
  $$
  one has
  $$
  \left(\frac{\partial P}{\partial V}\right)_{T,N}
  ={}
  -\left(\frac{\partial^2 F}{\partial V^2}\right)_{T,N}
  \le 0,
  $$

  and therefore $\kappa_T \ge 0$.
- At phase coexistence, $\left(\frac{\partial P}{\partial V}\right)_{T,N}$ can approach $0$, leading to very large (formally divergent) $\kappa_T$, consistent with $\kappa_T\ge 0$.

## Cross-links to definitions

- [[thermodynamics/isothermal-compressibility|isothermal compressibility $\kappa_T$]]
- [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]
- [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/temperature-thermo|temperature]]
- [[thermodynamics/thermodynamic-stability|thermodynamic stability]]
