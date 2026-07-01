+++
id = "thermodynamics/thermodynamic-system"
title = "Thermodynamic system"
kind = "knowl"
summary = "A chosen portion of the universe whose macroscopic behavior is described with thermodynamic variables and laws."
aliases = ["thermodynamic-system", "Thermodynamic system"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-system.md"
+++

A **thermodynamic system** is the portion of the physical world selected for study, treated as a well-defined entity that can (in general) exchange energy and/or matter with its [[thermodynamics/surroundings-environment|surroundings]] across a [[thermodynamics/system-boundary|system boundary]].

The “system” may be a material body (e.g., a gas in a cylinder), a region of space (e.g., a control volume in fluid flow), or a composite object (e.g., two phases plus an interface), provided the boundary and allowed exchanges are specified.

## Physical interpretation
Choosing the system is a modeling step: it decides what you call “inside” and “outside,” and therefore what counts as energy transfer *into* the system as [[thermodynamics/heat-inexact-differential|heat]] or [[thermodynamics/work-inexact-differential|work]]. Once the system is fixed, its macroscopic condition at equilibrium is summarized by a [[thermodynamics/thermodynamic-state|thermodynamic state]] described by [[thermodynamics/state-variable|state variables]] (e.g., $T$, $p$, $V$, $N$), and its changes are described as a [[thermodynamics/thermodynamic-process|thermodynamic process]].

## Key classifications (set by exchanges across the boundary)
The system type is determined by what can cross the boundary:
- **No matter or energy exchange:** [[thermodynamics/isolated-system|isolated system]].
- **Energy exchange but no matter exchange:** [[thermodynamics/closed-system|closed system]].
- **Matter (and typically energy) exchange:** [[thermodynamics/open-system|open system]].

These distinctions are not intrinsic “properties of the material” but of the *system + boundary choice*.

## Core relation to energy bookkeeping
For any thermodynamic system, the energy accounting is organized around [[thermodynamics/internal-energy-thermo|internal energy]] $U$ (a [[thermodynamics/state-function|state function]]) and transfers across the boundary as heat and work (both [[thermodynamics/path-function|path functions]]). This is the content formalized by the [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]].
