+++
id = "thermodynamics/work-inexact-differential"
title = "Work (inexact differential)"
kind = "knowl"
summary = "The symbol δW denotes path-dependent energy transfer via generalized forces and displacements; it is not a state function."
aliases = ["work-inexact-differential", "Work (inexact differential)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/work-inexact-differential.md"
+++

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] undergoing a [[thermodynamics/thermodynamic-process|process]], the *work increment* $\delta W$ is the infinitesimal amount of energy transferred **out of** the system (or into it, depending on sign) through *organized* interactions that can be modeled as generalized forces acting through generalized displacements at the [[thermodynamics/system-boundary|boundary]] or via a [[thermodynamics/work-reservoir|work reservoir]].

Like [[thermodynamics/heat-inexact-differential|heat]], work is an **inexact differential**: there is no [[thermodynamics/state-function|state function]] $W$ with $\delta W=dW$. Its integral depends on the path in state space, so $\delta W$ is a [[thermodynamics/path-function|path function]].

This knowl follows the [[thermodynamics/work-sign-convention|work sign convention]] used throughout: $\delta W>0$ means work is done *by the system* on the [[thermodynamics/surroundings-environment|surroundings]].

## Physical interpretation
Work represents energy transfer in a form that is, in principle, fully convertible into mechanical or other “organized” forms (lifting a weight, turning a shaft, charging a capacitor). It contrasts with heat, which is energy transfer driven by a temperature difference and typically associated with microscopic degrees of freedom.

## Key relations
- **First law (closed system):** for a [[thermodynamics/closed-system|closed system]],
  $$
  dU = \delta Q - \delta W,
  $$

  where $U$ is [[thermodynamics/internal-energy-thermo|internal energy]].

- **Pressure–volume work:** for a simple compressible system with a moving boundary (piston),
  $$
  \delta W_{PV} = P_{\text{ext}}\, dV,
  $$

  where $V$ is [[thermodynamics/volume-thermo|volume]] and $P_{\text{ext}}$ is the external pressure exerted by the surroundings. In a [[thermodynamics/quasistatic-process|quasistatic process]], $P_{\text{ext}}$ matches the system [[thermodynamics/pressure-thermo|pressure]] along the path, and for a [[thermodynamics/reversible-process|reversible process]] this gives the reversible work.

- **Generalized work form:** many work modes can be written schematically as
  $$
  \delta W = \sum_i Y_i\, dX_i,
  $$

  where $X_i$ are generalized displacements (often [[thermodynamics/extensive-variable|extensive variables]]) and $Y_i$ are conjugate generalized forces (often [[thermodynamics/intensive-variable|intensive variables]]). The precise list of terms depends on what exchanges are allowed across the boundary (compare [[thermodynamics/open-system|open systems]] versus [[thermodynamics/closed-system|closed systems]]) and on bookkeeping conventions (see [[thermodynamics/chemical-work-convention|chemical work conventions]]).

- **Cycles:** in a [[thermodynamics/cyclic-process|cycle]] of a closed system, $\Delta U=0$, so
  $$
  \oint \delta W = \oint \delta Q,
  $$
  emphasizing that the net work over a cycle generally does not vanish and depends on the path taken in state space.
