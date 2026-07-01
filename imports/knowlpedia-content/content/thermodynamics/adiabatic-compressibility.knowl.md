+++
id = "thermodynamics/adiabatic-compressibility"
title = "Adiabatic compressibility"
kind = "knowl"
summary = "A response function measuring the fractional change of volume with pressure at fixed entropy (and composition)."
aliases = ["adiabatic-compressibility", "Adiabatic compressibility"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/adiabatic-compressibility.md"
+++

The **adiabatic compressibility** (often called the **isentropic compressibility**) is a [[thermodynamics/response-function-thermo|response function]]
that measures how the [[thermodynamics/volume-thermo|volume]] of a [[thermodynamics/thermodynamic-system|thermodynamic system]]
responds to changes in [[thermodynamics/pressure-thermo|pressure]] when the [[thermodynamics/thermodynamic-entropy|entropy]] is held fixed.

It is defined by
$$
\kappa_S \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{S,N},
$$

with composition fixed (e.g. fixed [[thermodynamics/particle-number|particle number]] $N$ for a single-component system).

## Physical interpretation
An entropy constraint is appropriate for a [[thermodynamics/reversible-process|reversible]] process with no heat exchange (an idealized “adiabatic” change, e.g. via an [[thermodynamics/adiabatic-wall|adiabatic wall]]).
For a small quasistatic isentropic compression,
$$
\frac{dV}{V} = -\kappa_S\,dp.
$$

Because an isentropic compression generally heats the system, the material typically resists compression more strongly than in an isothermal process, so one often finds $\kappa_S < \kappa_T$, where $\kappa_T$ is the [[thermodynamics/isothermal-compressibility|isothermal compressibility]].

A common physical setting is acoustics: small-amplitude sound waves in fluids are well-approximated as isentropic, and $\kappa_S$ controls the relation between pressure and density changes.

## Key relations and properties
- **Relation to isothermal compressibility and heat capacities:** For a simple compressible system,
  $$
  \kappa_S = \kappa_T\,\frac{C_V}{C_P},
  $$

  where $C_V$ and $C_P$ are the [[thermodynamics/heat-capacity-constant-volume|constant-volume]] and [[thermodynamics/heat-capacity-constant-pressure|constant-pressure]] heat capacities, respectively.

- **Difference between compressibilities:** An equivalent identity is
  $$
  \kappa_T - \kappa_S = \frac{T\,V\,\alpha^2}{C_P},
  $$

  involving the [[thermodynamics/thermal-expansion-coefficient|thermal expansion coefficient]] $\alpha$.

- **Stability sign:** In stable single-phase equilibrium, one expects $\kappa_S>0$; violations are linked to [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

- **Connection to sound speed (common form):** Writing $\rho$ for the mass density, the isentropic stiffness appears in
  $$
  \left(\frac{\partial p}{\partial \rho}\right)_S = \frac{1}{\rho\,\kappa_S},
  $$
  which underlies the standard expression for the adiabatic speed of sound in a fluid.
