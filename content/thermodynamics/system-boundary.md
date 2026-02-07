---
title: "System boundary"
description: "The (real or imaginary) surface that separates a thermodynamic system from its surroundings and controls what can be exchanged."
---

A **system boundary** is the surface (or more generally, the interface region) that separates a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} from its {{< knowl id="surroundings-environment" text="surroundings" >}}. It may be a physical wall (container, membrane, piston) or an imaginary surface drawn through a continuum (as in control-volume descriptions).

The boundary specification determines which exchanges are allowed:
- **Energy exchange** as {{< knowl id="heat-inexact-differential" text="heat" >}} and/or {{< knowl id="work-inexact-differential" text="work" >}}.
- **Matter exchange** (permeable vs impermeable).

## Physical interpretation
The boundary is where “interaction with the outside world” happens. In thermodynamic bookkeeping, changes of {{< knowl id="internal-energy-thermo" text="internal energy" >}} are attributed either to transfers across this boundary or to changes within the system’s state.

Two especially important boundary idealizations are:
- A {{< knowl id="diathermal-wall" text="diathermal wall" >}} that permits heat exchange (thermal contact).
- An {{< knowl id="adiabatic-wall" text="adiabatic wall" >}} that forbids heat exchange.

Similarly, the boundary may be:
- **Rigid** or **movable**, controlling whether mechanical boundary work can occur.
- **Permeable** or **impermeable**, controlling whether the system can be {{< knowl id="open-system" text="open" >}} (matter exchange) or remain {{< knowl id="closed-system" text="closed" >}} (no matter exchange).

## Key relations (energy transfer at the boundary)
- Heat and work are boundary-crossing energy transfers and are therefore {{< knowl id="path-function" text="path dependent" >}} rather than state properties. Their differentials are typically written as $\delta Q$ and $\delta W$ to emphasize they are not exact differentials (see {{< knowl id="heat-inexact-differential" text="heat as an inexact differential" >}} and {{< knowl id="work-inexact-differential" text="work as an inexact differential" >}}).
- For a simple compressible system with a moving boundary, mechanical interaction often appears as pressure–volume work of magnitude $p\,dV$. The sign depends on the chosen convention (see the {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work sign convention" >}} and the more general {{< knowl id="work-sign-convention" text="work sign convention" >}}).

## Boundary choice and system type
By design, the boundary choice determines whether the same physical material is modeled as an {{< knowl id="isolated-system" text="isolated system" >}} (no exchange), a {{< knowl id="closed-system" text="closed system" >}} (energy exchange only), or an {{< knowl id="open-system" text="open system" >}} (matter exchange allowed).
