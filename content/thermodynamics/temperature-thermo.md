---
title: "Thermodynamic temperature"
description: "An intensive state variable T equalized at thermal equilibrium; formally defined by 1/T = (∂S/∂U)_{V,N} and linking heat to entropy."
---

*Thermodynamic temperature* $T$ is an {{< knowl id="intensive-variable" text="intensive variable" >}} that characterizes thermal equilibrium. The {{< knowl id="zeroth-law-thermodynamics" text="zeroth law of thermodynamics" >}} asserts that {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} defines an equivalence relation among systems, allowing each equivalence class to be labeled by a single parameter called temperature.

A precise equilibrium definition is obtained from entropy. If equilibrium states admit a {{< knowl id="fundamental-relation-entropy" text="fundamental relation" >}} $S(U,V,N)$, then temperature is defined by
$$
\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N},
$$

using the notion of {{< knowl id="partial-derivative" section="real-analysis" text="partial derivative" >}}. Equivalently, in the {{< knowl id="fundamental-relation-energy" text="energy representation" >}} $U(S,V,N)$,
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N}.
$$

In any {{< knowl id="reversible-process" text="reversible process" >}}, temperature is also the integrating factor that converts the {{< knowl id="heat-inexact-differential" text="inexact heat differential" >}} into an exact entropy differential:
$$
\delta Q_{\mathrm{rev}} = T\, dS.
$$

## Physical interpretation
Temperature controls the *direction of spontaneous heat flow*: when two systems are placed in thermal contact through a {{< knowl id="diathermal-wall" text="diathermal wall" >}}, energy tends to flow as heat from the system at higher $T$ to the one at lower $T$ until {{< knowl id="thermal-equilibrium" text="thermal equilibrium" >}} is reached.

A {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} is an idealized large system whose temperature remains approximately constant while exchanging finite heat, making it a practical reference for defining and measuring $T$.

## Key relations and examples
- **Absolute temperature scale:** temperature defined from the zeroth/second-law structure is the {{< knowl id="absolute-temperature-scale" text="absolute temperature scale" >}} (Kelvin scale), independent of any particular material thermometer model.

- **Ideal-gas equation of state (example):**
  $$
  P V = N k_B T,
  $$

  connecting {{< knowl id="pressure-thermo" text="pressure" >}} $P$, {{< knowl id="volume-thermo" text="volume" >}} $V$, {{< knowl id="particle-number" text="particle number" >}} $N$, and {{< knowl id="boltzmann-constant" text="Boltzmann’s constant" >}} $k_B$ through an {{< knowl id="equation-of-state" text="equation of state" >}}.

- **Inverse temperature:** statistical mechanics often uses {{< knowl id="inverse-temperature-beta" text="β (inverse temperature)" >}}, defined by $\beta = 1/(k_B T)$, especially in contexts aligned with the {{< knowl id="canonical-ensemble-convention" text="canonical ensemble convention" >}}.

- **Heat capacities:** temperature dependence of energy is captured by response functions such as {{< knowl id="heat-capacity-constant-volume" text="heat capacity at constant volume" >}} and {{< knowl id="heat-capacity-constant-pressure" text="heat capacity at constant pressure" >}}, which quantify how much energy (or enthalpy) must be supplied as {{< knowl id="heat-inexact-differential" text="heat" >}} to raise $T$ under specified constraints.

- **Sign and consistency:** interpreting formulas like $dU = \delta Q - \delta W$ requires a fixed {{< knowl id="work-sign-convention" text="work sign convention" >}}, since temperature links directly to heat through $\delta Q_{\mathrm{rev}} = T\, dS$.
