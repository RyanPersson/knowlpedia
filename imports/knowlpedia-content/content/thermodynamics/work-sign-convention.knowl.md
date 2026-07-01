+++
id = "thermodynamics/work-sign-convention"
title = "Work sign convention"
kind = "knowl"
summary = "A bookkeeping choice for the sign of work in the first law; here δW>0 means work done by the system on the surroundings."
aliases = ["work-sign-convention", "Work sign convention"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/work-sign-convention.md"
+++

A *work sign convention* specifies whether work is counted as positive when it is done **by** the system or **on** the system. Because heat and work appear together in the [[thermodynamics/first-law-thermodynamics|first law of thermodynamics]], the sign convention must be fixed to interpret equations and plots consistently.

**Convention used in these knowls:**
- $\delta W>0$ means work is done **by the system** on the [[thermodynamics/surroundings-environment|surroundings]].
- $\delta Q>0$ means [[thermodynamics/heat-inexact-differential|heat]] flows **into** the system.

With this choice, the first law for a [[thermodynamics/closed-system|closed system]] is
$$
dU = \delta Q - \delta W,
$$

where $U$ is [[thermodynamics/internal-energy-thermo|internal energy]] and $\delta W$ is [[thermodynamics/work-inexact-differential|work]].

## Physical interpretation
Under this convention, $\delta W>0$ corresponds to energy leaving the system in an organized form (pushing a piston, turning a shaft), while $\delta Q>0$ corresponds to energy entering because of a temperature difference. The sign convention is not physics; it is bookkeeping. Physics enters through consistent application and through inequalities such as the [[thermodynamics/clausius-inequality|Clausius inequality]].

## Key consequences and examples
- **Pressure–volume work:** for boundary work against an external pressure,
  $$
  \delta W_{PV} = P_{\text{ext}}\, dV.
  $$

  Since $dV>0$ for expansion, expansion gives $\delta W_{PV}>0$ (the system does work on the surroundings). Compression gives $\delta W_{PV}<0$. A more focused discussion can be found under [[thermodynamics/pressure-volume-work-sign-convention|pressure–volume work sign convention]].

- **Reversible simple compressible system (fixed particle number):** combining $\delta Q_{\mathrm{rev}} = T\, dS$ from [[thermodynamics/thermodynamic-entropy|entropy]] with $\delta W_{\mathrm{rev}} = P\, dV$ yields
  $$
  dU = T\, dS - P\, dV,
  $$
  consistent with the [[thermodynamics/fundamental-relation-energy|fundamental relation (energy representation)]] for such a system.

- **Alternative convention (common in some chemistry texts):** some authors define $\delta W_{\text{on}}>0$ for work done *on* the system. Then $\delta W_{\text{on}} = -\delta W$ (with $\delta W$ as defined here) and the first law becomes
  $$
  dU = \delta Q + \delta W_{\text{on}}.
  $$
  Either convention is valid if used consistently, including in definitions of thermodynamic potentials such as [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] and [[thermodynamics/gibbs-free-energy|Gibbs free energy]] and in any conventions for particle exchange (see [[thermodynamics/particle-number|particle number]] and [[thermodynamics/chemical-potential-thermo|chemical potential]] together with [[thermodynamics/chemical-work-convention|chemical work conventions]]).
