---
title: "Work sign convention"
description: "A bookkeeping choice for the sign of work in the first law; here δW>0 means work done by the system on the surroundings."
---

A *work sign convention* specifies whether work is counted as positive when it is done **by** the system or **on** the system. Because heat and work appear together in the {{< knowl id="first-law-thermodynamics" text="first law of thermodynamics" >}}, the sign convention must be fixed to interpret equations and plots consistently.

**Convention used in these knowls:**  
- $\delta W>0$ means work is done **by the system** on the {{< knowl id="surroundings-environment" text="surroundings" >}}.  
- $\delta Q>0$ means {{< knowl id="heat-inexact-differential" text="heat" >}} flows **into** the system.

With this choice, the first law for a {{< knowl id="closed-system" text="closed system" >}} is
$$
dU = \delta Q - \delta W,
$$

where $U$ is {{< knowl id="internal-energy-thermo" text="internal energy" >}} and $\delta W$ is {{< knowl id="work-inexact-differential" text="work" >}}.

## Physical interpretation
Under this convention, $\delta W>0$ corresponds to energy leaving the system in an organized form (pushing a piston, turning a shaft), while $\delta Q>0$ corresponds to energy entering because of a temperature difference. The sign convention is not physics; it is bookkeeping. Physics enters through consistent application and through inequalities such as the {{< knowl id="clausius-inequality" text="Clausius inequality" >}}.

## Key consequences and examples
- **Pressure–volume work:** for boundary work against an external pressure,
  $$
  \delta W_{PV} = P_{\text{ext}}\, dV.
  $$

  Since $dV>0$ for expansion, expansion gives $\delta W_{PV}>0$ (the system does work on the surroundings). Compression gives $\delta W_{PV}<0$. A more focused discussion can be found under {{< knowl id="pressure-volume-work-sign-convention" text="pressure–volume work sign convention" >}}.

- **Reversible simple compressible system (fixed particle number):** combining $\delta Q_{\mathrm{rev}} = T\, dS$ from {{< knowl id="thermodynamic-entropy" text="entropy" >}} with $\delta W_{\mathrm{rev}} = P\, dV$ yields
  $$
  dU = T\, dS - P\, dV,
  $$
  consistent with the {{< knowl id="fundamental-relation-energy" text="fundamental relation (energy representation)" >}} for such a system.

- **Alternative convention (common in some chemistry texts):** some authors define $\delta W_{\text{on}}>0$ for work done *on* the system. Then $\delta W_{\text{on}} = -\delta W$ (with $\delta W$ as defined here) and the first law becomes
  $$
  dU = \delta Q + \delta W_{\text{on}}.
  $$
  Either convention is valid if used consistently, including in definitions of thermodynamic potentials such as {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} and {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} and in any conventions for particle exchange (see {{< knowl id="particle-number" text="particle number" >}} and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} together with {{< knowl id="chemical-work-convention" text="chemical work conventions" >}}).
