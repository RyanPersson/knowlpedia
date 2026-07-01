+++
id = "thermodynamics/kelvin-planck-clausius-equivalence"
title = "Kelvin–Planck–Clausius equivalence"
kind = "knowl"
summary = "The Kelvin–Planck and Clausius formulations of the second law are logically equivalent: violating either implies a violation of the other."
aliases = ["kelvin-planck-clausius-equivalence", "Kelvin–Planck–Clausius equivalence"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/kelvin-planck-clausius-equivalence.md"
+++

## Statement

Two standard formulations of the [[thermodynamics/second-law-thermodynamics|second law of thermodynamics]] are:

- **Kelvin–Planck statement.** No cyclic device can extract heat from a single thermal reservoir and convert it entirely into work (i.e., no 100% efficient single-reservoir heat engine).

- **Clausius statement.** No cyclic device can transfer heat from a colder reservoir to a hotter reservoir without net work input (i.e., no “spontaneous” pumping of heat uphill for free).

**Equivalence theorem.** The Kelvin–Planck statement holds if and only if the Clausius statement holds.

## Key hypotheses and conclusions

**Hypotheses**
- Standard macroscopic bookkeeping consistent with the [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]] (energy conservation over cycles).
- Reservoirs are idealized as bodies at fixed [[thermodynamics/temperature-thermo|temperature]] that can supply/absorb heat without changing temperature.

**Conclusions**
- Either statement may be taken as the second law without loss of generality.
- Carnot-type bounds and entropy inequalities can be derived from either formulation:
  - [[stat-mech/carnot-theorem|Carnot theorem]]
  - [[thermodynamics/clausius-theorem-entropy|Clausius theorem (entropy)]]
  - [[thermodynamics/clausius-inequality|Clausius inequality]]

## Cross-links to definitions

- Second law: [[thermodynamics/second-law-thermodynamics|second law of thermodynamics]].
- Energy conservation over cycles: [[thermodynamics/first-law-thermodynamics|first law]].
- Temperature and reservoirs: [[thermodynamics/temperature-thermo|temperature]].

**Significance.** This equivalence justifies treating “the second law” as a robust principle independent of which operational impossibility statement one starts from, and it underpins both [[stat-mech/carnot-theorem|Carnot’s theorem]] and entropy-based formulations.
