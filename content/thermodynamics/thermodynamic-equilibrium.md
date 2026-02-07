---
title: "Thermodynamic equilibrium"
description: "A stable state with no spontaneous macroscopic change, characterized by simultaneous mechanical, thermal, and chemical equilibrium."
---

A {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} is in **thermodynamic equilibrium** if, with its external constraints and {{< knowl id="system-boundary" text="boundary conditions" >}} held fixed, its {{< knowl id="thermodynamic-state" text="macroscopic state" >}} does not change in time and exhibits no sustained macroscopic currents (of energy, momentum, or matter). Equivalently, there are no internal “driving forces” (such as gradients of intensive variables) that would generate a spontaneous {{< knowl id="irreversible-process" text="irreversible process" >}}.

In thermodynamic equilibrium, macroscopic properties can be described by a set of {{< knowl id="state-variable" text="state variables" >}}, and all {{< knowl id="state-function" text="state functions" >}} are well-defined for that state.

## Physical interpretation
Thermodynamic equilibrium is the endpoint of spontaneous relaxation: the system has “used up” all allowed ways of increasing {{< knowl id="thermodynamic-entropy" text="entropy" >}} (for an {{< knowl id="isolated-system" text="isolated system" >}}) or of lowering the appropriate free-energy-like potential (for a system constrained by its {{< knowl id="surroundings-environment" text="environment" >}}).

A common characterization is variational:

- For an isolated simple system with fixed $U,V,N$, equilibrium makes the entropy locally maximal: $\delta S = 0$ with $\delta^2 S < 0$ for allowed variations.
- Under external constraints imposed by reservoirs, equilibrium minimizes the relevant thermodynamic potential; for example, at fixed $(T,V,N)$ it minimizes the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}}, and at fixed $(T,P,N)$ it minimizes the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}}.

## Key properties and relations
Thermodynamic equilibrium packages several component equilibria:

- {{< knowl id="mechanical-equilibrium" text="Mechanical equilibrium" >}} (no unbalanced forces; pressure/stress balance),
- {{< knowl id="thermal-equilibrium" text="Thermal equilibrium" >}} (no net heat flow; equality of temperature across diathermal contacts),
- {{< knowl id="chemical-equilibrium" text="Chemical equilibrium" >}} (no net matter flow or reaction progress; appropriate chemical-potential conditions).

Equilibrium states support the standard “thermodynamic calculus”: the {{< knowl id="equation-of-state" text="equation of state" >}} and identities like the {{< knowl id="maxwell-relation" text="Maxwell relations" >}} are statements about derivatives *at equilibrium*. By contrast, {{< knowl id="heat-inexact-differential" text="heat" >}} and {{< knowl id="work-inexact-differential" text="work" >}} remain path-dependent even when they connect two equilibrium states via a {{< knowl id="thermodynamic-process" text="process" >}}.

Finally, a {{< knowl id="quasistatic-process" text="quasistatic process" >}} is idealized as a sequence of equilibrium states; if it is also free of dissipation it is {{< knowl id="reversible-process" text="reversible" >}}. Stability of equilibrium against small perturbations is encoded in {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}, often expressed via {{< knowl id="entropy-concavity-stability" text="entropy concavity" >}} (or equivalently {{< knowl id="energy-convexity-stability" text="energy convexity" >}}) in the appropriate variables.
