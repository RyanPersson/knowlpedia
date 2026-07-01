+++
id = "thermodynamics/closed-system"
title = "Closed system"
kind = "knowl"
summary = "A thermodynamic system that can exchange energy (heat/work) but not matter with its surroundings."
aliases = ["closed-system", "Closed system"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/closed-system.md"
+++

A **closed system** is a [[thermodynamics/thermodynamic-system|thermodynamic system]] for which **no matter crosses** the [[thermodynamics/system-boundary|boundary]], while **energy exchange may occur** with the [[thermodynamics/surroundings-environment|surroundings]] as [[thermodynamics/heat-inexact-differential|heat]] and/or [[thermodynamics/work-inexact-differential|work]].

This is the standard “control mass” setting of classical equilibrium thermodynamics.

## Physical interpretation
Examples include:
- A sealed piston–cylinder device, where the boundary can move and mechanical work occurs, but no mass enters or leaves.
- A rigid sealed container placed in thermal contact with a bath through a [[thermodynamics/diathermal-wall|diathermal wall]], allowing heat flow without mass flow.

A closed system differs from:
- an [[thermodynamics/open-system|open system]], which allows matter exchange across a permeable boundary, and
- an [[thermodynamics/isolated-system|isolated system]], which allows neither matter nor energy exchange.

## Key relations
- **Fixed amount of matter:** For a single-component closed system, the [[thermodynamics/particle-number|particle number]] $N$ is constant:
  $$ dN = 0. $$

- **First-law form:** The [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]] relates changes in [[thermodynamics/internal-energy-thermo|internal energy]] to boundary transfers. Using the [[thermodynamics/work-sign-convention|common convention]] that $\delta W$ is work done *by* the system on the surroundings,
  $$ dU = \delta Q - \delta W. $$

  (If $\delta W$ is instead defined as work done *on* the system, the sign changes accordingly.)
- **Mechanical boundary work:** For a simple compressible closed system, one common contribution to work is pressure–volume work of magnitude $p\,dV$; sign details are set by the [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work sign convention]]. The variables [[thermodynamics/pressure-thermo|pressure]] $p$ and [[thermodynamics/volume-thermo|volume]] $V$ are then central state variables.

## Process viewpoint
Because heat and work are [[thermodynamics/path-function|path dependent]], specifying a closed system is not enough to determine $U$-changes; one must also specify the [[thermodynamics/thermodynamic-process|process]] (e.g., the boundary constraints and driving protocol) that dictates how energy is exchanged with the surroundings.
