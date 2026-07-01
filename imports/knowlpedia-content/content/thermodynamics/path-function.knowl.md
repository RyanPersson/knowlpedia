+++
id = "thermodynamics/path-function"
title = "Path function"
kind = "knowl"
summary = "A process-dependent quantity whose value depends on the path taken between states (e.g., heat or work)."
aliases = ["path-function", "Path function"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/path-function.md"
+++

A **path function** is a quantity associated with a [[thermodynamics/thermodynamic-process|thermodynamic process]] rather than with a [[thermodynamics/thermodynamic-state|thermodynamic state]]. Its value for a change of state depends on the particular path taken through state space, so it cannot be expressed as the difference of a single-valued function of state.

Path functions are commonly written with an **inexact differential** symbol $\delta$ to emphasize that there is no underlying state function whose differential it is. Canonical examples are [[thermodynamics/heat-inexact-differential|heat]] $\delta Q$ and [[thermodynamics/work-inexact-differential|work]] $\delta W$.

**Physical interpretation.** Path functions quantify transfer across the [[thermodynamics/system-boundary|boundary]] during a process—energy carried as heat, mechanical work, electrical work, or energy advected with matter in an [[thermodynamics/open-system|open system]]. Because transfers depend on how the process is executed (with friction, with gradients, rapidly vs slowly, etc.), they are not fixed by endpoint states alone.

**Key relations**
- **First law bookkeeping:** the [[thermodynamics/first-law-thermodynamics|first law]] relates path-dependent transfers to the change in [[thermodynamics/internal-energy-thermo|internal energy]] (a [[thermodynamics/state-function|state function]]) via
  $dU = \delta Q - \delta W$,
  with signs set by the [[thermodynamics/work-sign-convention|work sign convention]] (and, for $P\,dV$ work, the [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work convention]]).
- **Cycles need not vanish:** for a [[thermodynamics/cyclic-process|cycle]] one has $\Delta U=0$, but generally $\oint \delta Q \neq 0$ and $\oint \delta W \neq 0$ (indeed, they are equal in magnitude with consistent signs).
- **Reversible limit:** along a [[thermodynamics/reversible-process|reversible process]], heat transfer is tied to entropy by $\delta Q_{\mathrm{rev}} = T\,dS$, linking the path function $\delta Q$ to the state function [[thermodynamics/thermodynamic-entropy|entropy]] and the state variable [[thermodynamics/temperature-thermo|temperature]].
- **Irreversibility constraint:** in irreversible cycles the [[thermodynamics/clausius-inequality|Clausius inequality]] implies $\oint \delta Q/T \le 0$, expressing that the same endpoints can be connected by paths with different heat/work transfers.
