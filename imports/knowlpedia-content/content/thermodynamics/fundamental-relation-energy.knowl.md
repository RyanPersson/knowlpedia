+++
id = "thermodynamics/fundamental-relation-energy"
title = "Fundamental relation (energy representation)"
kind = "knowl"
summary = "The internal energy function U(S,V,N,...) that generates temperature, pressure, and chemical potential by differentiation."
aliases = ["fundamental-relation-energy", "Fundamental relation (energy representation)"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/fundamental-relation-energy.md"
+++

In the **energy representation**, the **fundamental relation** is the equilibrium internal energy written as a function of the extensive variables:
$U = U(S,V,N,\dots)$,
with $S$ the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], $V$ the [[thermodynamics/volume-thermo|volume]], and $N$ the [[thermodynamics/particle-number|particle number]] (plus any other extensive conserved quantities). Knowing this single state function determines all equilibrium thermodynamics for a system in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]].

**Physical interpretation.** The function $U(S,V,N,\dots)$ tells you the energy cost of “building” a macrostate with given entropy, size, and composition. Its derivatives are the intensive variables that govern exchange of energy, volume, and particles across the [[thermodynamics/system-boundary|system boundary]].

**Generating derivatives.** The differential form is
$$
dU = T\,dS - P\,dV + \mu\,dN + \cdots ,
$$
which defines
- $T=\left(\frac{\partial U}{\partial S}\right)_{V,N,\dots}$ ([[thermodynamics/temperature-thermo|temperature]])
- $-P=\left(\frac{\partial U}{\partial V}\right)_{S,N,\dots}$ ([[thermodynamics/pressure-thermo|pressure]])
- $\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V,\dots}$ ([[thermodynamics/chemical-potential-thermo|chemical potential]])

An [[thermodynamics/equation-of-state|equation of state]] can be obtained by re-expressing these derivatives in terms of $(T,V,N)$ or other convenient independent variables.

**Key properties.**
- **Extensivity as homogeneity.** For additive macroscopic systems, $U$ is extensive and ideally [[thermodynamics/homogeneous-function-degree-one|homogeneous of degree one]] in $(S,V,N,\dots)$, implying the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] and leading to the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]] among intensive variables.
- **Convexity and stability.** Stability in the energy representation corresponds to appropriate convexity properties of $U$ (as a function of extensive variables), connecting to [[thermodynamics/energy-convexity-stability|energy convexity (stability)]] and constraining measurable [[thermodynamics/response-function-thermo|response functions]].
- **Link to work/heat differentials.** Along a [[thermodynamics/thermodynamic-process|thermodynamic process]], the first law relates changes in $U$ to [[thermodynamics/heat-inexact-differential|heat]] and [[thermodynamics/work-inexact-differential|work]] via [[thermodynamics/first-law-thermodynamics|the first law]].
