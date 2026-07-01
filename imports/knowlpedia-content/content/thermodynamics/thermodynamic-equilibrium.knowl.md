+++
id = "thermodynamics/thermodynamic-equilibrium"
title = "Thermodynamic equilibrium"
kind = "knowl"
summary = "A stable state with no spontaneous macroscopic change, characterized by simultaneous mechanical, thermal, and chemical equilibrium."
aliases = ["thermodynamic-equilibrium", "Thermodynamic equilibrium"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-equilibrium.md"
+++

A [[thermodynamics/thermodynamic-system|thermodynamic system]] is in **thermodynamic equilibrium** if, with its external constraints and [[thermodynamics/system-boundary|boundary conditions]] held fixed, its [[thermodynamics/thermodynamic-state|macroscopic state]] does not change in time and exhibits no sustained macroscopic currents (of energy, momentum, or matter). Equivalently, there are no internal “driving forces” (such as gradients of intensive variables) that would generate a spontaneous [[thermodynamics/irreversible-process|irreversible process]].

In thermodynamic equilibrium, macroscopic properties can be described by a set of [[thermodynamics/state-variable|state variables]], and all [[thermodynamics/state-function|state functions]] are well-defined for that state.

## Physical interpretation
Thermodynamic equilibrium is the endpoint of spontaneous relaxation: the system has “used up” all allowed ways of increasing [[thermodynamics/thermodynamic-entropy|entropy]] (for an [[thermodynamics/isolated-system|isolated system]]) or of lowering the appropriate free-energy-like potential (for a system constrained by its [[thermodynamics/surroundings-environment|environment]]).

A common characterization is variational:

- For an isolated simple system with fixed $U,V,N$, equilibrium makes the entropy locally maximal: $\delta S = 0$ with $\delta^2 S < 0$ for allowed variations.
- Under external constraints imposed by reservoirs, equilibrium minimizes the relevant thermodynamic potential; for example, at fixed $(T,V,N)$ it minimizes the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], and at fixed $(T,P,N)$ it minimizes the [[thermodynamics/gibbs-free-energy|Gibbs free energy]].

## Key properties and relations
Thermodynamic equilibrium packages several component equilibria:

- [[thermodynamics/mechanical-equilibrium|Mechanical equilibrium]] (no unbalanced forces; pressure/stress balance),
- [[thermodynamics/thermal-equilibrium|Thermal equilibrium]] (no net heat flow; equality of temperature across diathermal contacts),
- [[thermodynamics/chemical-equilibrium|Chemical equilibrium]] (no net matter flow or reaction progress; appropriate chemical-potential conditions).

Equilibrium states support the standard “thermodynamic calculus”: the [[thermodynamics/equation-of-state|equation of state]] and identities like the [[thermodynamics/maxwell-relation|Maxwell relations]] are statements about derivatives *at equilibrium*. By contrast, [[thermodynamics/heat-inexact-differential|heat]] and [[thermodynamics/work-inexact-differential|work]] remain path-dependent even when they connect two equilibrium states via a [[thermodynamics/thermodynamic-process|process]].

Finally, a [[thermodynamics/quasistatic-process|quasistatic process]] is idealized as a sequence of equilibrium states; if it is also free of dissipation it is [[thermodynamics/reversible-process|reversible]]. Stability of equilibrium against small perturbations is encoded in [[thermodynamics/thermodynamic-stability|thermodynamic stability]], often expressed via [[thermodynamics/entropy-concavity-stability|entropy concavity]] (or equivalently [[thermodynamics/energy-convexity-stability|energy convexity]]) in the appropriate variables.
