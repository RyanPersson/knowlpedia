+++
id = "thermodynamics/thermodynamic-process"
title = "Thermodynamic process"
kind = "knowl"
summary = "A transformation that carries a thermodynamic system between states along a specified path of interactions with its surroundings."
aliases = ["thermodynamic-process", "Thermodynamic process"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-process.md"
+++

A **thermodynamic process** is a time-ordered transformation of a [[thermodynamics/thermodynamic-system|thermodynamic system]] driven by interactions with the [[thermodynamics/surroundings-environment|surroundings]] across a [[thermodynamics/system-boundary|system boundary]]. Depending on whether the system is [[thermodynamics/isolated-system|isolated]], [[thermodynamics/closed-system|closed]], or [[thermodynamics/open-system|open]], the process may involve exchange of energy (as heat and/or work) and possibly matter.

When the system is (at least approximately) in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] throughout, the process can be represented as a continuous path through [[thermodynamics/thermodynamic-state|thermodynamic states]] parameterized by [[thermodynamics/state-variable|state variables]] (e.g., temperature, pressure, volume, particle number). In general, a process may pass through nonequilibrium configurations, in which case only the endpoints may be equilibrium states with well-defined macroscopic state variables.

## Physical interpretation
A process is “what you do to the system” (or “what happens to it”)—compressing a gas, heating it in contact with a reservoir, letting it expand against an external pressure, mixing components, or allowing chemical change—specified by the constraints and how external controls vary in time. The same initial and final equilibrium states can often be connected by many different processes; the distinction matters because some quantities depend on the path.

## Key structural distinctions
A thermodynamic process separates naturally into:

- **State changes** described by [[thermodynamics/state-function|state functions]] (quantities determined solely by the state). For any state function $X$, the change $\Delta X$ depends only on the initial and final equilibrium states, not on the process used to connect them.
- **Transfers** described by [[thermodynamics/path-function|path functions]] (quantities defined through the process history). In particular, heat and work are represented by the [[thermodynamics/heat-inexact-differential|inexact differential of heat]] $\delta Q$ and the [[thermodynamics/work-inexact-differential|inexact differential of work]] $\delta W$, whose integrals generally depend on the path.

A standard differential statement of the [[thermodynamics/first-law-thermodynamics|first law]] is
$$
dU = \delta Q - \delta W,
$$

where $U$ is the [[thermodynamics/internal-energy-thermo|internal energy]] and the sign of $\delta W$ follows the chosen [[thermodynamics/work-sign-convention|work sign convention]].

## Common refinements
Important special classes of thermodynamic process include the [[thermodynamics/quasistatic-process|quasistatic process]] (intermediate states remain arbitrarily close to equilibrium), the [[thermodynamics/reversible-process|reversible process]] (idealized, no dissipation and no net change to system+surroundings upon reversal), the [[thermodynamics/irreversible-process|irreversible process]] (realistic, dissipative, entropy-producing), and the [[thermodynamics/cyclic-process|cyclic process]] (returns to the initial state).
