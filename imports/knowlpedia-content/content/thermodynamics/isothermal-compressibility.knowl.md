+++
id = "thermodynamics/isothermal-compressibility"
title = "Isothermal compressibility"
kind = "knowl"
summary = "A response function measuring the fractional change of volume with pressure at fixed temperature (and composition)."
aliases = ["isothermal-compressibility", "Isothermal compressibility"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/isothermal-compressibility.md"
+++

The **isothermal compressibility** is a [[thermodynamics/response-function-thermo|response function]] describing how a [[thermodynamics/thermodynamic-system|thermodynamic system]] in [[thermodynamics/thermodynamic-equilibrium|equilibrium]]
changes its [[thermodynamics/volume-thermo|volume]] when the [[thermodynamics/pressure-thermo|pressure]] is varied while keeping the [[thermodynamics/temperature-thermo|temperature]] fixed (and keeping composition fixed, e.g. fixed [[thermodynamics/particle-number|particle number]] $N$).

It is defined by
$$
\kappa_T \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{T,N}.
$$

The minus sign is conventional: for ordinary stable matter, increasing $p$ decreases $V$, so $(\partial V/\partial p)_{T,N}<0$ and $\kappa_T>0$.

## Physical interpretation
For a small, quasistatic isothermal change (the system is kept at fixed $T$, e.g. by contact with a [[thermodynamics/thermal-reservoir|thermal reservoir]]), the definition implies
$$
\frac{dV}{V} = -\kappa_T\,dp.
$$

Thus $\kappa_T$ is the **fractional volume decrease per unit pressure increase** under isothermal conditions. Its inverse,
often called the (isothermal) bulk modulus, quantifies mechanical stiffness.

## Key relations and properties
- **Stability sign:** In stable single-phase equilibrium, one requires $\kappa_T>0$; a negative value signals mechanical instability and is closely tied to [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

- **Link to other response functions:** For a simple compressible system,
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  relating $\kappa_T$ to the [[thermodynamics/heat-capacity-constant-pressure|constant-pressure heat capacity]] $C_P$, the [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]] $C_V$, and the [[thermodynamics/thermal-expansion-coefficient|thermal expansion coefficient]] $\alpha$.

- **Comparison with adiabatic compressibility:** The [[thermodynamics/adiabatic-compressibility|adiabatic (isentropic) compressibility]] satisfies
  $$
  \kappa_S = \kappa_T\,\frac{C_V}{C_P},
  $$

  so typically $\kappa_S \le \kappa_T$ when $C_P \ge C_V$.

- **Fluctuation formula (statistical mechanics):** In an isothermal–isobaric setting (fixed $T$, $p$, $N$), $\kappa_T$ can be expressed through the [[probability/variance|variance]] of volume fluctuations:
  $$
  \kappa_T = \frac{\langle (\Delta V)^2\rangle}{k_B\,T\,\langle V\rangle},
  $$

  where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]] and $\langle\cdot\rangle$ denotes an ensemble [[probability/expectation|expectation]].
