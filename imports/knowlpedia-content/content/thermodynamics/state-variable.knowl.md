+++
id = "thermodynamics/state-variable"
title = "State variable"
kind = "knowl"
summary = "A macroscopic quantity with a definite value in each equilibrium thermodynamic state."
aliases = ["state-variable", "State variable"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/state-variable.md"
+++

A **state variable** is a macroscopic quantity that is well-defined for each [[thermodynamics/thermodynamic-state|thermodynamic state]] in the class of states under consideration (typically equilibrium states). Equivalently, it is a coordinate-like function on state space: it assigns to each state a value that can, in principle, be measured without reference to the history of how the state was prepared.

A suitable set of *independent* state variables uniquely specifies the equilibrium state (the “state postulate”), and all other equilibrium properties are then [[thermodynamics/state-function|state functions]] of that chosen set.

**Physical interpretation.** Common state variables include:
- extensive variables such as [[thermodynamics/volume-thermo|volume]], [[thermodynamics/internal-energy-thermo|internal energy]], [[thermodynamics/thermodynamic-entropy|entropy]], and [[thermodynamics/particle-number|particle number]];
- intensive variables such as [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], and [[thermodynamics/chemical-potential-thermo|chemical potential]].

The intensive/extensive distinction is formalized by [[thermodynamics/intensive-variable|intensive variables]] and [[thermodynamics/extensive-variable|extensive variables]]; one often also uses normalized [[thermodynamics/specific-quantity|specific quantities]] (per mass, per mole) or densities.

**Conjugate pairs from a fundamental relation.** If equilibrium energy is described by a [[thermodynamics/fundamental-relation-energy|fundamental relation]] $U=U(S,V,N)$ for a single-component simple compressible system, then conjugate intensive variables are obtained as partial derivatives:
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N},\qquad
P = -\left(\frac{\partial U}{\partial V}\right)_{S,N},\qquad
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$
Here the derivatives are understood in the sense of the [[real-analysis/partial-derivative|partial derivative]].

**Constraints and equations of state.** State variables are not all independent: constraints and an [[thermodynamics/equation-of-state|equation of state]] link them. Differentiating these relations produces measurable [[thermodynamics/response-function-thermo|response functions]] such as compressibilities and thermal expansion coefficients.
