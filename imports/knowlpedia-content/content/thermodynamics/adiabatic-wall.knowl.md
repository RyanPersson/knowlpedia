+++
id = "thermodynamics/adiabatic-wall"
title = "Adiabatic wall"
kind = "knowl"
summary = "A system boundary that prohibits heat transfer (ideal thermal insulation)."
aliases = ["adiabatic-wall", "Adiabatic wall"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/adiabatic-wall.md"
+++

An **adiabatic wall** is an idealized [[thermodynamics/system-boundary|system boundary]] that **does not allow heat transfer** between a [[thermodynamics/thermodynamic-system|system]] and its [[thermodynamics/surroundings-environment|surroundings]]. Equivalently, the net heat flow across an adiabatic wall is taken to be zero, so the heat term described by the [[thermodynamics/heat-inexact-differential|inexact differential of heat]] satisfies
$$
\delta Q = 0
$$
for energy exchange across that boundary.

**Physical interpretation.**
An adiabatic wall models perfect thermal insulation: even if there is a temperature difference, no energy crosses the boundary *as heat*. Real-world approximations include vacuum insulation, multilayer reflective shields, or very short time scales where there is negligible time for heat conduction.

**What an adiabatic wall does *not* specify.**
“Adiabatic” only constrains heat transfer. It does not, by itself, determine whether the system is [[thermodynamics/closed-system|closed]] or [[thermodynamics/open-system|open]] (matter transfer is a separate idealization), nor whether the boundary permits mechanical motion and hence [[thermodynamics/work-inexact-differential|work transfer]].

**Connection to the first law.**
For a closed system separated from its environment by an adiabatic wall, the [[thermodynamics/first-law-thermodynamics|first law]] reduces to a pure work balance:
- heat exchange vanishes across the wall, so changes in [[thermodynamics/internal-energy-thermo|internal energy]] are accounted for entirely by work transfer (with the sign determined by the [[thermodynamics/work-sign-convention|work sign convention]] used).

This is one reason adiabatic walls are conceptually important: they isolate work effects and help distinguish [[thermodynamics/state-function|state functions]] (like internal energy) from [[thermodynamics/path-function|path functions]] (like heat and work).

**Contrast.**
The complementary idealization is a [[thermodynamics/diathermal-wall|diathermal wall]], which allows heat exchange and enables thermal equilibration.
