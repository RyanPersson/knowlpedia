---
title: "Thermodynamic process"
description: "A transformation that carries a thermodynamic system between states along a specified path of interactions with its surroundings."
---

A **thermodynamic process** is a time-ordered transformation of a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} driven by interactions with the {{< knowl id="surroundings-environment" text="surroundings" >}} across a {{< knowl id="system-boundary" text="system boundary" >}}. Depending on whether the system is {{< knowl id="isolated-system" text="isolated" >}}, {{< knowl id="closed-system" text="closed" >}}, or {{< knowl id="open-system" text="open" >}}, the process may involve exchange of energy (as heat and/or work) and possibly matter.

When the system is (at least approximately) in {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}} throughout, the process can be represented as a continuous path through {{< knowl id="thermodynamic-state" text="thermodynamic states" >}} parameterized by {{< knowl id="state-variable" text="state variables" >}} (e.g., temperature, pressure, volume, particle number). In general, a process may pass through nonequilibrium configurations, in which case only the endpoints may be equilibrium states with well-defined macroscopic state variables.

## Physical interpretation
A process is “what you do to the system” (or “what happens to it”)—compressing a gas, heating it in contact with a reservoir, letting it expand against an external pressure, mixing components, or allowing chemical change—specified by the constraints and how external controls vary in time. The same initial and final equilibrium states can often be connected by many different processes; the distinction matters because some quantities depend on the path.

## Key structural distinctions
A thermodynamic process separates naturally into:

- **State changes** described by {{< knowl id="state-function" text="state functions" >}} (quantities determined solely by the state). For any state function $X$, the change $\Delta X$ depends only on the initial and final equilibrium states, not on the process used to connect them.
- **Transfers** described by {{< knowl id="path-function" text="path functions" >}} (quantities defined through the process history). In particular, heat and work are represented by the {{< knowl id="heat-inexact-differential" text="inexact differential of heat" >}} $\delta Q$ and the {{< knowl id="work-inexact-differential" text="inexact differential of work" >}} $\delta W$, whose integrals generally depend on the path.

A standard differential statement of the {{< knowl id="first-law-thermodynamics" text="first law" >}} is
$$
dU = \delta Q - \delta W,
$$

where $U$ is the {{< knowl id="internal-energy-thermo" text="internal energy" >}} and the sign of $\delta W$ follows the chosen {{< knowl id="work-sign-convention" text="work sign convention" >}}.

## Common refinements
Important special classes of thermodynamic process include the {{< knowl id="quasistatic-process" text="quasistatic process" >}} (intermediate states remain arbitrarily close to equilibrium), the {{< knowl id="reversible-process" text="reversible process" >}} (idealized, no dissipation and no net change to system+surroundings upon reversal), the {{< knowl id="irreversible-process" text="irreversible process" >}} (realistic, dissipative, entropy-producing), and the {{< knowl id="cyclic-process" text="cyclic process" >}} (returns to the initial state).
