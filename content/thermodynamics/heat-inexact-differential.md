---
title: "Heat (inexact differential)"
description: "The symbol δQ denotes path-dependent energy transfer into a system driven by a temperature difference; it is not a state function."
---

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} undergoing a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}}, the *heat increment* $\delta Q$ is the infinitesimal amount of energy transferred **into** the system across the {{< knowl id="system-boundary" text="system boundary" >}} *because of a temperature difference* (as opposed to energy transfer classified as {{< knowl id="work-inexact-differential" text="work" >}}).

The notation $\delta Q$ (rather than $dQ$) emphasizes that heat is an **inexact differential**: there is no {{< knowl id="state-function" text="state function" >}} $Q$ with $\delta Q = dQ$. Equivalently, the integral
$\int_{\Gamma} \delta Q$ depends on the process path $\Gamma$, so heat is a {{< knowl id="path-function" text="path function" >}}.

Throughout these knowls, the sign of $\delta Q$ is coordinated with the {{< knowl id="work-sign-convention" text="work sign convention" >}}: $\delta Q>0$ means heat flows *into* the system.

## Physical interpretation
Heat is **not a “thing contained in the system”**; it is a bookkeeping label for one channel of energy transfer. Once energy has entered the system as heat, it contributes to changes in state variables such as {{< knowl id="internal-energy-thermo" text="internal energy" >}} and {{< knowl id="thermodynamic-entropy" text="entropy" >}}, but the amount “heat contained” is not defined independent of the process.

A {{< knowl id="diathermal-wall" text="diathermal wall" >}} permits $\delta Q\neq 0$ (heat exchange), while an {{< knowl id="adiabatic-wall" text="adiabatic wall" >}} enforces $\delta Q=0$.

## Key relations
- **First law (closed system):** for a {{< knowl id="closed-system" text="closed system" >}},
  $$
  dU = \delta Q - \delta W,
  $$

  where $U$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}} and $\delta W$ is {{< knowl id="work-inexact-differential" text="work (inexact differential)" >}}.

- **Cycles:** in a {{< knowl id="cyclic-process" text="cyclic process" >}}, $\Delta U=0$, so
  $$
  \oint \delta Q = \oint \delta W.
  $$

  This equality highlights that $\oint \delta Q$ is generally nonzero, reinforcing that $\delta Q$ is not exact.

- **Reversible link to entropy:** for a {{< knowl id="reversible-process" text="reversible process" >}}, the {{< knowl id="second-law-thermodynamics" text="second law" >}} gives
  $$
  \delta Q_{\mathrm{rev}} = T\, dS,
  $$

  relating heat to {{< knowl id="temperature-thermo" text="temperature" >}} $T$ and {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}} $S$. The factor $1/T$ acts as an integrating factor that turns $\delta Q_{\mathrm{rev}}$ into an exact differential.
