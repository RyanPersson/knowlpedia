+++
id = "thermodynamics/diathermal-wall"
title = "Diathermal wall"
kind = "knowl"
summary = "A system boundary that permits heat transfer, allowing subsystems to come to thermal equilibrium."
aliases = ["diathermal-wall", "Diathermal wall"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/diathermal-wall.md"
+++

A **diathermal wall** is an idealized [[thermodynamics/system-boundary|system boundary]] that **allows heat transfer** between a [[thermodynamics/thermodynamic-system|system]] and its [[thermodynamics/surroundings-environment|surroundings]]. In other words, energy may cross the boundary *as heat*, described by the [[thermodynamics/heat-inexact-differential|inexact differential of heat]] $\delta Q$.

**Physical interpretation.**
A diathermal wall models good thermal contact (e.g., a thin metal interface) so that, when two systems are separated only by such a wall and are otherwise constrained, heat can flow in response to a temperature difference.

**Thermal equilibration.**
If two subsystems can exchange heat through a diathermal wall and the composite is otherwise isolated from the external environment, they relax toward [[thermodynamics/thermal-equilibrium|thermal equilibrium]], characterized (in equilibrium thermodynamics) by equality of their temperatures:
$$
T_1 = T_2.
$$
This operational role is tightly connected to the [[thermodynamics/zeroth-law-thermodynamics|zeroth law]]: diathermal contact is the mechanism by which “having the same temperature” becomes an experimentally meaningful notion.

**Contact with a thermal reservoir.**
When a system is placed in diathermal contact with a [[thermodynamics/thermal-reservoir|thermal reservoir]], the reservoir idealization implies the system can exchange heat while the reservoir remains at fixed temperature, so the system can relax toward $T = T_R$ (subject to other constraints).

**What a diathermal wall does *not* specify.**
Diathermal refers only to heat permeability. The wall may still be mechanically rigid (preventing boundary work) or movable (allowing [[thermodynamics/work-inexact-differential|work]] transfer), and it may be impermeable or permeable to matter depending on whether the system is [[thermodynamics/closed-system|closed]] or [[thermodynamics/open-system|open]].

**Contrast.**
A perfectly insulating boundary is an [[thermodynamics/adiabatic-wall|adiabatic wall]], across which heat transfer is excluded.
