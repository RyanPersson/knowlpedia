+++
id = "thermodynamics/thermal-equilibrium"
title = "Thermal equilibrium"
kind = "knowl"
summary = "A condition of no net heat flow: systems in diathermal contact exchange no heat in steady state, which is captured by equality of temperature."
aliases = ["thermal-equilibrium", "Thermal equilibrium"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermal-equilibrium.md"
+++

Two systems are in **thermal equilibrium** if, when placed in contact through a [[thermodynamics/diathermal-wall|diathermal wall]] (allowing energy transfer as heat) while otherwise isolated from external influences, there is no net energy transfer as [[thermodynamics/heat-inexact-differential|heat]] and no macroscopic change of state occurs.

In equilibrium thermodynamics this condition is summarized by equality of the [[thermodynamics/temperature-thermo|temperature]]:
if systems 1 and 2 are in thermal equilibrium, then $T_1 = T_2$.

For a single extended system, “internal” thermal equilibrium means there are no sustained temperature gradients driving heat currents (a prerequisite for [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).

## Physical interpretation
Thermal equilibrium is the state in which energy exchange has no preferred direction: neither system can increase total [[thermodynamics/thermodynamic-entropy|entropy]] by sending a small amount of energy to the other purely as heat. A [[thermodynamics/thermal-reservoir|thermal reservoir]] is an idealized system that remains at effectively fixed temperature despite exchanging finite heat; bringing a system into contact with a reservoir drives it toward the reservoir’s temperature.

## Key relation: entropy maximization and equality of temperature
Consider two subsystems that can exchange energy but not [[thermodynamics/particle-number|particles]] or volume, with total energy fixed. Writing $U_{\text{tot}} = U_1 + U_2$ and $U_2 = U_{\text{tot}} - U_1$, equilibrium corresponds to an extremum of the total entropy:
$$
\frac{dS_{\text{tot}}}{dU_1}
={}
\left(\frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1}
-{}
\left(\frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2}
=0.
$$

Using the equilibrium definition $1/T = (\partial S/\partial U)_{V,N}$ (from the [[thermodynamics/fundamental-relation-entropy|fundamental entropy relation]]), the condition becomes $1/T_1 = 1/T_2$, i.e. $T_1=T_2$.

It is often convenient to package temperature as the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta = 1/(k_B T)$, with $k_B$ the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

## Connection to the zeroth law
The empirical content that makes temperature a consistent state variable is the [[thermodynamics/zeroth-law-thermodynamics|zeroth law of thermodynamics]]; it is often phrased as the transitivity of thermal equilibrium and formalized via [[thermodynamics/zeroth-law-equivalence|zeroth-law equivalence]].
