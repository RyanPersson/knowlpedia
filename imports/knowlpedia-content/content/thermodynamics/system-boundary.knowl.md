+++
id = "thermodynamics/system-boundary"
title = "System boundary"
kind = "knowl"
summary = "The (real or imaginary) surface that separates a thermodynamic system from its surroundings and controls what can be exchanged."
aliases = ["system-boundary", "System boundary"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/system-boundary.md"
+++

A **system boundary** is the surface (or more generally, the interface region) that separates a [[thermodynamics/thermodynamic-system|thermodynamic system]] from its [[thermodynamics/surroundings-environment|surroundings]]. It may be a physical wall (container, membrane, piston) or an imaginary surface drawn through a continuum (as in control-volume descriptions).

The boundary specification determines which exchanges are allowed:
- **Energy exchange** as [[thermodynamics/heat-inexact-differential|heat]] and/or [[thermodynamics/work-inexact-differential|work]].
- **Matter exchange** (permeable vs impermeable).

## Physical interpretation
The boundary is where “interaction with the outside world” happens. In thermodynamic bookkeeping, changes of [[thermodynamics/internal-energy-thermo|internal energy]] are attributed either to transfers across this boundary or to changes within the system’s state.

Two especially important boundary idealizations are:
- A [[thermodynamics/diathermal-wall|diathermal wall]] that permits heat exchange (thermal contact).
- An [[thermodynamics/adiabatic-wall|adiabatic wall]] that forbids heat exchange.

Similarly, the boundary may be:
- **Rigid** or **movable**, controlling whether mechanical boundary work can occur.
- **Permeable** or **impermeable**, controlling whether the system can be [[thermodynamics/open-system|open]] (matter exchange) or remain [[thermodynamics/closed-system|closed]] (no matter exchange).

## Key relations (energy transfer at the boundary)
- Heat and work are boundary-crossing energy transfers and are therefore [[thermodynamics/path-function|path dependent]] rather than state properties. Their differentials are typically written as $\delta Q$ and $\delta W$ to emphasize they are not exact differentials (see [[thermodynamics/heat-inexact-differential|heat as an inexact differential]] and [[thermodynamics/work-inexact-differential|work as an inexact differential]]).
- For a simple compressible system with a moving boundary, mechanical interaction often appears as pressure–volume work of magnitude $p\,dV$. The sign depends on the chosen convention (see the [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work sign convention]] and the more general [[thermodynamics/work-sign-convention|work sign convention]]).

## Boundary choice and system type
By design, the boundary choice determines whether the same physical material is modeled as an [[thermodynamics/isolated-system|isolated system]] (no exchange), a [[thermodynamics/closed-system|closed system]] (energy exchange only), or an [[thermodynamics/open-system|open system]] (matter exchange allowed).
