---
title: "Closed system"
description: "A thermodynamic system that can exchange energy (heat/work) but not matter with its surroundings."
---

A **closed system** is a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} for which **no matter crosses** the {{< knowl id="system-boundary" text="boundary" >}}, while **energy exchange may occur** with the {{< knowl id="surroundings-environment" text="surroundings" >}} as {{< knowl id="heat-inexact-differential" text="heat" >}} and/or {{< knowl id="work-inexact-differential" text="work" >}}.

This is the standard “control mass” setting of classical equilibrium thermodynamics.

## Physical interpretation
Examples include:
- A sealed piston–cylinder device, where the boundary can move and mechanical work occurs, but no mass enters or leaves.
- A rigid sealed container placed in thermal contact with a bath through a {{< knowl id="diathermal-wall" text="diathermal wall" >}}, allowing heat flow without mass flow.

A closed system differs from:
- an {{< knowl id="open-system" text="open system" >}}, which allows matter exchange across a permeable boundary, and
- an {{< knowl id="isolated-system" text="isolated system" >}}, which allows neither matter nor energy exchange.

## Key relations
- **Fixed amount of matter:** For a single-component closed system, the {{< knowl id="particle-number" text="particle number" >}} $N$ is constant:
  $$ dN = 0. $$

- **First-law form:** The {{< knowl id="first-law-thermodynamics" text="first law of thermodynamics" >}} relates changes in {{< knowl id="internal-energy-thermo" text="internal energy" >}} to boundary transfers. Using the {{< knowl id="work-sign-convention" text="common convention" >}} that $\delta W$ is work done *by* the system on the surroundings,
  $$ dU = \delta Q - \delta W. $$

  (If $\delta W$ is instead defined as work done *on* the system, the sign changes accordingly.)
- **Mechanical boundary work:** For a simple compressible closed system, one common contribution to work is pressure–volume work of magnitude $p\,dV$; sign details are set by the {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work sign convention" >}}. The variables {{< knowl id="pressure-thermo" text="pressure" >}} $p$ and {{< knowl id="volume-thermo" text="volume" >}} $V$ are then central state variables.

## Process viewpoint
Because heat and work are {{< knowl id="path-function" text="path dependent" >}}, specifying a closed system is not enough to determine $U$-changes; one must also specify the {{< knowl id="thermodynamic-process" text="process" >}} (e.g., the boundary constraints and driving protocol) that dictates how energy is exchanged with the surroundings.
