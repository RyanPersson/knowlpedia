---
title: "Positivity of isothermal compressibility from stability"
description: "Mechanical stability implies the isothermal compressibility is nonnegative, equivalently that pressure decreases with volume at fixed temperature."
---

## Statement

For a thermodynamically stable equilibrium system at fixed temperature and composition, the {{< knowl id="isothermal-compressibility" section="thermodynamics" text="isothermal compressibility" >}}
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

- Equilibrium description in terms of the {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} $F(T,V,N)$.
- $F$ is twice differentiable in $V$ at fixed $T,N$.
- Mechanical stability (a component of {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}), expressed as convexity of $F$ in $V$ at fixed $T,N$:
  $$
  \left(\frac{\partial^2 F}{\partial V^2}\right)_{T,N} \ge 0.
  $$

## Key conclusions

- Since {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} is given by
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

- {{< knowl id="isothermal-compressibility" section="thermodynamics" text="isothermal compressibility $\kappa_T$" >}}
- {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}
- {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}
- {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}

