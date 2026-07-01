+++
id = "stat-mech/third-law-unattainability"
title = "Unattainability formulation of the third law"
kind = "knowl"
summary = "Absolute zero temperature cannot be reached by any finite sequence of thermodynamic operations consistent with the second law."
aliases = ["third-law-unattainability", "Unattainability formulation of the third law"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/third-law-unattainability.md"
+++

## Statement
(**Unattainability principle.**) For a [[thermodynamics/thermodynamic-system|thermodynamic system]] governed by the [[thermodynamics/second-law-thermodynamics|second law of thermodynamics]], it is impossible to reach the state $T=0$ (absolute zero [[thermodynamics/temperature-thermo|temperature]]) from any initial state with $T>0$ by a **finite** sequence of thermodynamic operations.

Common equivalent operational readings include:
- No finite number of (idealized) reversible or irreversible steps can take a system from $T>0$ to $T=0$.
- Any cooling protocol that respects the second law requires resources (time, steps, or auxiliary reservoirs) that diverge as $T\to 0$.

## Key hypotheses
- Thermodynamic description in equilibrium (or quasi-static limits) with well-defined temperature.
- Validity of the second law (e.g., via Kelvin–Planck/Clausius statements; see [[thermodynamics/kelvin-planck-clausius-equivalence|Kelvin–Planck/Clausius equivalence]]).
- “Finite process” interpreted as finitely many steps with finite reservoirs/controls; idealizations are allowed, but not infinite concatenations.

## Conclusions
- $T=0$ is a limit point that cannot be attained by finite operations starting from $T>0$.
- The approach to $T=0$ is constrained even if entropy decreases are allowed via heat extraction; in particular, the ability to use Carnot-like refrigeration cycles is limited as the cold temperature decreases (compare [[stat-mech/carnot-theorem|Carnot theorem]] and [[stat-mech/carnot-efficiency-formula|Carnot efficiency formula]]).
