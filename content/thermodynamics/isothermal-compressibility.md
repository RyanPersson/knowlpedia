---
title: "Isothermal compressibility"
description: "A response function measuring the fractional change of volume with pressure at fixed temperature (and composition)."
---

The **isothermal compressibility** is a {{< knowl id="response-function-thermo" text="response function" >}} describing how a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} in {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}}
changes its {{< knowl id="volume-thermo" text="volume" >}} when the {{< knowl id="pressure-thermo" text="pressure" >}} is varied while keeping the {{< knowl id="temperature-thermo" text="temperature" >}} fixed (and keeping composition fixed, e.g. fixed {{< knowl id="particle-number" text="particle number" >}} $N$).

It is defined by
$$
\kappa_T \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{T,N}.
$$

The minus sign is conventional: for ordinary stable matter, increasing $p$ decreases $V$, so $(\partial V/\partial p)_{T,N}<0$ and $\kappa_T>0$.

## Physical interpretation
For a small, quasistatic isothermal change (the system is kept at fixed $T$, e.g. by contact with a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}}), the definition implies
$$
\frac{dV}{V} = -\kappa_T\,dp.
$$

Thus $\kappa_T$ is the **fractional volume decrease per unit pressure increase** under isothermal conditions. Its inverse,
often called the (isothermal) bulk modulus, quantifies mechanical stiffness.

## Key relations and properties
- **Stability sign:** In stable single-phase equilibrium, one requires $\kappa_T>0$; a negative value signals mechanical instability and is closely tied to {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}.

- **Link to other response functions:** For a simple compressible system,
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  relating $\kappa_T$ to the {{< knowl id="heat-capacity-constant-pressure" text="constant-pressure heat capacity" >}} $C_P$, the {{< knowl id="heat-capacity-constant-volume" text="constant-volume heat capacity" >}} $C_V$, and the {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}} $\alpha$.

- **Comparison with adiabatic compressibility:** The {{< knowl id="adiabatic-compressibility" text="adiabatic (isentropic) compressibility" >}} satisfies
  $$
  \kappa_S = \kappa_T\,\frac{C_V}{C_P},
  $$

  so typically $\kappa_S \le \kappa_T$ when $C_P \ge C_V$.

- **Fluctuation formula (statistical mechanics):** In an isothermal–isobaric setting (fixed $T$, $p$, $N$), $\kappa_T$ can be expressed through the {{< knowl id="variance" section="probability" text="variance" >}} of volume fluctuations:
  $$
  \kappa_T = \frac{\langle (\Delta V)^2\rangle}{k_B\,T\,\langle V\rangle},
  $$

  where $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} and $\langle\cdot\rangle$ denotes an ensemble {{< knowl id="expectation" section="probability" text="expectation" >}}.
