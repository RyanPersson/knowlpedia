---
title: "Path function"
description: "A process-dependent quantity whose value depends on the path taken between states (e.g., heat or work)."
---

A **path function** is a quantity associated with a {{< knowl id="thermodynamic-process" text="thermodynamic process" >}} rather than with a {{< knowl id="thermodynamic-state" text="thermodynamic state" >}}. Its value for a change of state depends on the particular path taken through state space, so it cannot be expressed as the difference of a single-valued function of state.

Path functions are commonly written with an **inexact differential** symbol $\delta$ to emphasize that there is no underlying state function whose differential it is. Canonical examples are {{< knowl id="heat-inexact-differential" text="heat" >}} $\delta Q$ and {{< knowl id="work-inexact-differential" text="work" >}} $\delta W$.

**Physical interpretation.** Path functions quantify transfer across the {{< knowl id="system-boundary" text="boundary" >}} during a process—energy carried as heat, mechanical work, electrical work, or energy advected with matter in an {{< knowl id="open-system" text="open system" >}}. Because transfers depend on how the process is executed (with friction, with gradients, rapidly vs slowly, etc.), they are not fixed by endpoint states alone.

**Key relations**
- **First law bookkeeping:** the {{< knowl id="first-law-thermodynamics" text="first law" >}} relates path-dependent transfers to the change in {{< knowl id="internal-energy-thermo" text="internal energy" >}} (a {{< knowl id="state-function" text="state function" >}}) via
  $dU = \delta Q - \delta W$,
  with signs set by the {{< knowl id="work-sign-convention" text="work sign convention" >}} (and, for $P\,dV$ work, the {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work convention" >}}).
- **Cycles need not vanish:** for a {{< knowl id="cyclic-process" text="cycle" >}} one has $\Delta U=0$, but generally $\oint \delta Q \neq 0$ and $\oint \delta W \neq 0$ (indeed, they are equal in magnitude with consistent signs).
- **Reversible limit:** along a {{< knowl id="reversible-process" text="reversible process" >}}, heat transfer is tied to entropy by $\delta Q_{\mathrm{rev}} = T\,dS$, linking the path function $\delta Q$ to the state function {{< knowl id="thermodynamic-entropy" text="entropy" >}} and the state variable {{< knowl id="temperature-thermo" text="temperature" >}}.
- **Irreversibility constraint:** in irreversible cycles the {{< knowl id="clausius-inequality" text="Clausius inequality" >}} implies $\oint \delta Q/T \le 0$, expressing that the same endpoints can be connected by paths with different heat/work transfers.
