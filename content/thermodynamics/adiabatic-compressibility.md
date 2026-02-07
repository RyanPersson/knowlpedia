---
title: "Adiabatic compressibility"
description: "A response function measuring the fractional change of volume with pressure at fixed entropy (and composition)."
---

The **adiabatic compressibility** (often called the **isentropic compressibility**) is a {{< knowl id="response-function-thermo" text="response function" >}}
that measures how the {{< knowl id="volume-thermo" text="volume" >}} of a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}}
responds to changes in {{< knowl id="pressure-thermo" text="pressure" >}} when the {{< knowl id="thermodynamic-entropy" text="entropy" >}} is held fixed.

It is defined by
$$
\kappa_S \equiv -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_{S,N},
$$

with composition fixed (e.g. fixed {{< knowl id="particle-number" text="particle number" >}} $N$ for a single-component system).

## Physical interpretation
An entropy constraint is appropriate for a {{< knowl id="reversible-process" text="reversible" >}} process with no heat exchange (an idealized “adiabatic” change, e.g. via an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}}).
For a small quasistatic isentropic compression,
$$
\frac{dV}{V} = -\kappa_S\,dp.
$$

Because an isentropic compression generally heats the system, the material typically resists compression more strongly than in an isothermal process, so one often finds $\kappa_S < \kappa_T$, where $\kappa_T$ is the {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}}.

A common physical setting is acoustics: small-amplitude sound waves in fluids are well-approximated as isentropic, and $\kappa_S$ controls the relation between pressure and density changes.

## Key relations and properties
- **Relation to isothermal compressibility and heat capacities:** For a simple compressible system,
  $$
  \kappa_S = \kappa_T\,\frac{C_V}{C_P},
  $$

  where $C_V$ and $C_P$ are the {{< knowl id="heat-capacity-constant-volume" text="constant-volume" >}} and {{< knowl id="heat-capacity-constant-pressure" text="constant-pressure" >}} heat capacities, respectively.

- **Difference between compressibilities:** An equivalent identity is
  $$
  \kappa_T - \kappa_S = \frac{T\,V\,\alpha^2}{C_P},
  $$

  involving the {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}} $\alpha$.

- **Stability sign:** In stable single-phase equilibrium, one expects $\kappa_S>0$; violations are linked to {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}.

- **Connection to sound speed (common form):** Writing $\rho$ for the mass density, the isentropic stiffness appears in
  $$
  \left(\frac{\partial p}{\partial \rho}\right)_S = \frac{1}{\rho\,\kappa_S},
  $$
  which underlies the standard expression for the adiabatic speed of sound in a fluid.
