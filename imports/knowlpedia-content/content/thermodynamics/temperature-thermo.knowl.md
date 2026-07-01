+++
id = "thermodynamics/temperature-thermo"
title = "Thermodynamic temperature"
kind = "knowl"
summary = "An intensive state variable T equalized at thermal equilibrium; formally defined by 1/T = (∂S/∂U)_{V,N} and linking heat to entropy."
aliases = ["temperature-thermo", "Thermodynamic temperature"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/temperature-thermo.md"
+++

*Thermodynamic temperature* $T$ is an [[thermodynamics/intensive-variable|intensive variable]] that characterizes thermal equilibrium. The [[thermodynamics/zeroth-law-thermodynamics|zeroth law of thermodynamics]] asserts that [[thermodynamics/thermal-equilibrium|thermal equilibrium]] defines an equivalence relation among systems, allowing each equivalence class to be labeled by a single parameter called temperature.

A precise equilibrium definition is obtained from entropy. If equilibrium states admit a [[thermodynamics/fundamental-relation-entropy|fundamental relation]] $S(U,V,N)$, then temperature is defined by
$$
\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N},
$$

using the notion of [[real-analysis/partial-derivative|partial derivative]]. Equivalently, in the [[thermodynamics/fundamental-relation-energy|energy representation]] $U(S,V,N)$,
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N}.
$$

In any [[thermodynamics/reversible-process|reversible process]], temperature is also the integrating factor that converts the [[thermodynamics/heat-inexact-differential|inexact heat differential]] into an exact entropy differential:
$$
\delta Q_{\mathrm{rev}} = T\, dS.
$$

## Physical interpretation
Temperature controls the *direction of spontaneous heat flow*: when two systems are placed in thermal contact through a [[thermodynamics/diathermal-wall|diathermal wall]], energy tends to flow as heat from the system at higher $T$ to the one at lower $T$ until [[thermodynamics/thermal-equilibrium|thermal equilibrium]] is reached.

A [[thermodynamics/thermal-reservoir|thermal reservoir]] is an idealized large system whose temperature remains approximately constant while exchanging finite heat, making it a practical reference for defining and measuring $T$.

## Key relations and examples
- **Absolute temperature scale:** temperature defined from the zeroth/second-law structure is the [[thermodynamics/absolute-temperature-scale|absolute temperature scale]] (Kelvin scale), independent of any particular material thermometer model.

- **Ideal-gas equation of state (example):**
  $$
  P V = N k_B T,
  $$

  connecting [[thermodynamics/pressure-thermo|pressure]] $P$, [[thermodynamics/volume-thermo|volume]] $V$, [[thermodynamics/particle-number|particle number]] $N$, and [[thermodynamics/boltzmann-constant|Boltzmann’s constant]] $k_B$ through an [[thermodynamics/equation-of-state|equation of state]].

- **Inverse temperature:** statistical mechanics often uses [[thermodynamics/inverse-temperature-beta|β (inverse temperature)]], defined by $\beta = 1/(k_B T)$, especially in contexts aligned with the [[thermodynamics/canonical-ensemble-convention|canonical ensemble convention]].

- **Heat capacities:** temperature dependence of energy is captured by response functions such as [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]] and [[thermodynamics/heat-capacity-constant-pressure|heat capacity at constant pressure]], which quantify how much energy (or enthalpy) must be supplied as [[thermodynamics/heat-inexact-differential|heat]] to raise $T$ under specified constraints.

- **Sign and consistency:** interpreting formulas like $dU = \delta Q - \delta W$ requires a fixed [[thermodynamics/work-sign-convention|work sign convention]], since temperature links directly to heat through $\delta Q_{\mathrm{rev}} = T\, dS$.
