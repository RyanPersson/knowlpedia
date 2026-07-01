+++
id = "thermodynamics/surroundings-environment"
title = "Surroundings and environment"
kind = "knowl"
summary = "Everything external to the chosen thermodynamic system, which can exchange energy and/or matter with it through the boundary."
aliases = ["surroundings-environment", "Surroundings and environment"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/surroundings-environment.md"
+++

The **surroundings** (or **environment**) are everything *outside* a [[thermodynamics/thermodynamic-system|thermodynamic system]]. Together, “system + surroundings” form the remainder of the universe relevant to the thermodynamic description, with interactions occurring only through the [[thermodynamics/system-boundary|system boundary]].

## Physical interpretation
In thermodynamics, the surroundings represent the “rest of the world” that can impose constraints and exchange quantities with the system:
- If the boundary permits, energy may be transferred as [[thermodynamics/heat-inexact-differential|heat]] (driven by temperature differences) or [[thermodynamics/work-inexact-differential|work]] (via generalized forces and boundary displacements).
- If the boundary is permeable, matter exchange can occur, changing [[thermodynamics/particle-number|particle number]] or composition inside the system.

A common idealization is to treat part of the surroundings as a **reservoir**: a very large system whose intensive variables are effectively unchanged by exchanges. For example, a [[thermodynamics/thermal-reservoir|thermal reservoir]] maintains an approximately constant [[thermodynamics/temperature-thermo|temperature]], and a [[thermodynamics/work-reservoir|work reservoir]] can supply or absorb work without appreciable change in its own macroscopic state.

## Key properties and relations
- The distinction between “system” and “surroundings” is a modeling boundary choice; moving the [[thermodynamics/system-boundary|boundary]] reassigns what is counted as internal energy versus energy transfer.
- For a system treated as [[thermodynamics/isolated-system|isolated]], the surroundings are thermodynamically irrelevant because no exchange is permitted across the boundary; in practice, “isolated” means interactions with the environment are negligible on the timescale of interest.
- When the surroundings can be idealized as fixed-$T$ or fixed-$p$ reservoirs, they provide the simplest physical route to defining controlled processes such as contact at fixed [[thermodynamics/pressure-thermo|pressure]] or temperature.
