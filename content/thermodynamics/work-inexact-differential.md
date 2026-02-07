---
title: "Work (inexact differential)"
description: "The symbol δW denotes path-dependent energy transfer via generalized forces and displacements; it is not a state function."
---

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} undergoing a {{< knowl id="thermodynamic-process" text="process" >}}, the *work increment* $\delta W$ is the infinitesimal amount of energy transferred **out of** the system (or into it, depending on sign) through *organized* interactions that can be modeled as generalized forces acting through generalized displacements at the {{< knowl id="system-boundary" text="boundary" >}} or via a {{< knowl id="work-reservoir" text="work reservoir" >}}.

Like {{< knowl id="heat-inexact-differential" text="heat" >}}, work is an **inexact differential**: there is no {{< knowl id="state-function" text="state function" >}} $W$ with $\delta W=dW$. Its integral depends on the path in state space, so $\delta W$ is a {{< knowl id="path-function" text="path function" >}}.

This knowl follows the {{< knowl id="work-sign-convention" text="work sign convention" >}} used throughout: $\delta W>0$ means work is done *by the system* on the {{< knowl id="surroundings-environment" text="surroundings" >}}.

## Physical interpretation
Work represents energy transfer in a form that is, in principle, fully convertible into mechanical or other “organized” forms (lifting a weight, turning a shaft, charging a capacitor). It contrasts with heat, which is energy transfer driven by a temperature difference and typically associated with microscopic degrees of freedom.

## Key relations
- **First law (closed system):** for a {{< knowl id="closed-system" text="closed system" >}},
  $$
  dU = \delta Q - \delta W,
  $$

  where $U$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}}.

- **Pressure–volume work:** for a simple compressible system with a moving boundary (piston),
  $$
  \delta W_{PV} = P_{\text{ext}}\, dV,
  $$

  where $V$ is {{< knowl id="volume-thermo" text="volume" >}} and $P_{\text{ext}}$ is the external pressure exerted by the surroundings. In a {{< knowl id="quasistatic-process" text="quasistatic process" >}}, $P_{\text{ext}}$ matches the system {{< knowl id="pressure-thermo" text="pressure" >}} along the path, and for a {{< knowl id="reversible-process" text="reversible process" >}} this gives the reversible work.

- **Generalized work form:** many work modes can be written schematically as
  $$
  \delta W = \sum_i Y_i\, dX_i,
  $$

  where $X_i$ are generalized displacements (often {{< knowl id="extensive-variable" text="extensive variables" >}}) and $Y_i$ are conjugate generalized forces (often {{< knowl id="intensive-variable" text="intensive variables" >}}). The precise list of terms depends on what exchanges are allowed across the boundary (compare {{< knowl id="open-system" text="open systems" >}} versus {{< knowl id="closed-system" text="closed systems" >}}) and on bookkeeping conventions (see {{< knowl id="chemical-work-convention" text="chemical work conventions" >}}).

- **Cycles:** in a {{< knowl id="cyclic-process" text="cycle" >}} of a closed system, $\Delta U=0$, so
  $$
  \oint \delta W = \oint \delta Q,
  $$
  emphasizing that the net work over a cycle generally does not vanish and depends on the path taken in state space.
