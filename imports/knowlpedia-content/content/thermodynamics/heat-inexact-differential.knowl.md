+++
id = "thermodynamics/heat-inexact-differential"
title = "Heat (inexact differential)"
kind = "knowl"
summary = "The symbol δQ denotes path-dependent energy transfer into a system driven by a temperature difference; it is not a state function."
aliases = ["heat-inexact-differential", "Heat (inexact differential)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/heat-inexact-differential.md"
+++

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] undergoing a [[thermodynamics/thermodynamic-process|thermodynamic process]], the *heat increment* $\delta Q$ is the infinitesimal amount of energy transferred **into** the system across the [[thermodynamics/system-boundary|system boundary]] *because of a temperature difference* (as opposed to energy transfer classified as [[thermodynamics/work-inexact-differential|work]]).

The notation $\delta Q$ (rather than $dQ$) emphasizes that heat is an **inexact differential**: there is no [[thermodynamics/state-function|state function]] $Q$ with $\delta Q = dQ$. Equivalently, the integral
$\int_{\Gamma} \delta Q$ depends on the process path $\Gamma$, so heat is a [[thermodynamics/path-function|path function]].

Throughout these knowls, the sign of $\delta Q$ is coordinated with the [[thermodynamics/work-sign-convention|work sign convention]]: $\delta Q>0$ means heat flows *into* the system.

## Physical interpretation
Heat is **not a “thing contained in the system”**; it is a bookkeeping label for one channel of energy transfer. Once energy has entered the system as heat, it contributes to changes in state variables such as [[thermodynamics/internal-energy-thermo|internal energy]] and [[thermodynamics/thermodynamic-entropy|entropy]], but the amount “heat contained” is not defined independent of the process.

A [[thermodynamics/diathermal-wall|diathermal wall]] permits $\delta Q\neq 0$ (heat exchange), while an [[thermodynamics/adiabatic-wall|adiabatic wall]] enforces $\delta Q=0$.

## Key relations
- **First law (closed system):** for a [[thermodynamics/closed-system|closed system]],
  $$
  dU = \delta Q - \delta W,
  $$

  where $U$ is [[thermodynamics/internal-energy-thermo|internal energy]] and $\delta W$ is [[thermodynamics/work-inexact-differential|work (inexact differential)]].

- **Cycles:** in a [[thermodynamics/cyclic-process|cyclic process]], $\Delta U=0$, so
  $$
  \oint \delta Q = \oint \delta W.
  $$

  This equality highlights that $\oint \delta Q$ is generally nonzero, reinforcing that $\delta Q$ is not exact.

- **Reversible link to entropy:** for a [[thermodynamics/reversible-process|reversible process]], the [[thermodynamics/second-law-thermodynamics|second law]] gives
  $$
  \delta Q_{\mathrm{rev}} = T\, dS,
  $$

  relating heat to [[thermodynamics/temperature-thermo|temperature]] $T$ and [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] $S$. The factor $1/T$ acts as an integrating factor that turns $\delta Q_{\mathrm{rev}}$ into an exact differential.
