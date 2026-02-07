---
title: "Mechanical equilibrium"
description: "Force balance in a thermodynamic system: no unbalanced stresses or pressure differences that would drive macroscopic motion."
---

A {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} is in **mechanical equilibrium** if there is no net macroscopic force producing acceleration of any part of the system. Operationally, this means stresses balance so that there is no spontaneous bulk motion driven by pressure (or more general mechanical) imbalances.

For a simple compressible fluid, mechanical equilibrium typically implies:
- the {{< knowl id="pressure-thermo" text="pressure" >}} is uniform within each connected region (in the absence of body forces), and
- at a movable {{< knowl id="system-boundary" text="boundary" >}} (e.g., a frictionless piston), the internal pressure matches the external mechanical load from the {{< knowl id="surroundings-environment" text="surroundings" >}}.

## Physical interpretation
If mechanical equilibrium fails, pressure/stress differences do work on the system’s parts, producing motion (expansion, compression, flow) until force balance is restored. Such motion is a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} and—when accompanied by friction, viscosity, shocks, or turbulence—typically generates dissipation and thus {{< knowl id="irreversible-process" text="irreversibility" >}}.

Mechanical equilibrium is one ingredient of full {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}; the latter also requires {{< knowl id="thermal-equilibrium" text="thermal" >}} and {{< knowl id="chemical-equilibrium" text="chemical" >}} equilibration.

## Key properties and relations
**Boundary force balance (piston model).** For a piston of area $A$ with external load force $F_{\text{load}}$ (including weights), force balance gives
$$
P_{\text{in}} A = P_{\text{out}} A + F_{\text{load}},
$$

so $P_{\text{in}} = P_{\text{out}} + F_{\text{load}}/A$. In the common idealization of negligible additional load, $P_{\text{in}} = P_{\text{out}}$.

**Hydrostatic balance (body forces).** In a static fluid under gravity, mechanical equilibrium allows a pressure gradient that balances weight:
$$
\frac{dP}{dz} = -\rho g,
$$
so “no motion” does not necessarily mean “spatially constant pressure” when body forces act.

**Thermodynamic conjugacy.** In equilibrium thermodynamics, pressure is the intensive variable conjugate to {{< knowl id="volume-thermo" text="volume" >}}. For a simple system described by {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U(S,V,N)$, one relation is
$$
P = -\left(\frac{\partial U}{\partial V}\right)_{S,N},
$$
linking mechanical response to derivatives of an equilibrium state function.
