---
title: "Thermal equilibrium"
description: "A condition of no net heat flow: systems in diathermal contact exchange no heat in steady state, which is captured by equality of temperature."
---

Two systems are in **thermal equilibrium** if, when placed in contact through a {{< knowl id="diathermal-wall" text="diathermal wall" >}} (allowing energy transfer as heat) while otherwise isolated from external influences, there is no net energy transfer as {{< knowl id="heat-inexact-differential" text="heat" >}} and no macroscopic change of state occurs.

In equilibrium thermodynamics this condition is summarized by equality of the {{< knowl id="temperature-thermo" text="temperature" >}}:
if systems 1 and 2 are in thermal equilibrium, then $T_1 = T_2$.

For a single extended system, “internal” thermal equilibrium means there are no sustained temperature gradients driving heat currents (a prerequisite for {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}).

## Physical interpretation
Thermal equilibrium is the state in which energy exchange has no preferred direction: neither system can increase total {{< knowl id="thermodynamic-entropy" text="entropy" >}} by sending a small amount of energy to the other purely as heat. A {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} is an idealized system that remains at effectively fixed temperature despite exchanging finite heat; bringing a system into contact with a reservoir drives it toward the reservoir’s temperature.

## Key relation: entropy maximization and equality of temperature
Consider two subsystems that can exchange energy but not {{< knowl id="particle-number" text="particles" >}} or volume, with total energy fixed. Writing $U_{\text{tot}} = U_1 + U_2$ and $U_2 = U_{\text{tot}} - U_1$, equilibrium corresponds to an extremum of the total entropy:
$$
\frac{dS_{\text{tot}}}{dU_1}
={}
\left(\frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1}
-{}
\left(\frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2}
=0.
$$

Using the equilibrium definition $1/T = (\partial S/\partial U)_{V,N}$ (from the {{< knowl id="fundamental-relation-entropy" text="fundamental entropy relation" >}}), the condition becomes $1/T_1 = 1/T_2$, i.e. $T_1=T_2$.

It is often convenient to package temperature as the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} $\beta = 1/(k_B T)$, with $k_B$ the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}.

## Connection to the zeroth law
The empirical content that makes temperature a consistent state variable is the {{< knowl id="zeroth-law-thermodynamics" text="zeroth law of thermodynamics" >}}; it is often phrased as the transitivity of thermal equilibrium and formalized via {{< knowl id="zeroth-law-equivalence" text="zeroth-law equivalence" >}}.
