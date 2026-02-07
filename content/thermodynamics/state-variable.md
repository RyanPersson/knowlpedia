---
title: "State variable"
description: "A macroscopic quantity with a definite value in each equilibrium thermodynamic state."
---

A **state variable** is a macroscopic quantity that is well-defined for each {{< knowl id="thermodynamic-state" text="thermodynamic state" >}} in the class of states under consideration (typically equilibrium states). Equivalently, it is a coordinate-like function on state space: it assigns to each state a value that can, in principle, be measured without reference to the history of how the state was prepared.

A suitable set of *independent* state variables uniquely specifies the equilibrium state (the “state postulate”), and all other equilibrium properties are then {{< knowl id="state-function" text="state functions" >}} of that chosen set.

**Physical interpretation.** Common state variables include:
- extensive variables such as {{< knowl id="volume-thermo" text="volume" >}}, {{< knowl id="internal-energy-thermo" text="internal energy" >}}, {{< knowl id="thermodynamic-entropy" text="entropy" >}}, and {{< knowl id="particle-number" text="particle number" >}};
- intensive variables such as {{< knowl id="temperature-thermo" text="temperature" >}}, {{< knowl id="pressure-thermo" text="pressure" >}}, and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}.

The intensive/extensive distinction is formalized by {{< knowl id="intensive-variable" text="intensive variables" >}} and {{< knowl id="extensive-variable" text="extensive variables" >}}; one often also uses normalized {{< knowl id="specific-quantity" text="specific quantities" >}} (per mass, per mole) or densities.

**Conjugate pairs from a fundamental relation.** If equilibrium energy is described by a {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} $U=U(S,V,N)$ for a single-component simple compressible system, then conjugate intensive variables are obtained as partial derivatives:
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N},\qquad
P = -\left(\frac{\partial U}{\partial V}\right)_{S,N},\qquad
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$
Here the derivatives are understood in the sense of the {{< knowl id="partial-derivative" section="real-analysis" text="partial derivative" >}}.

**Constraints and equations of state.** State variables are not all independent: constraints and an {{< knowl id="equation-of-state" text="equation of state" >}} link them. Differentiating these relations produces measurable {{< knowl id="response-function-thermo" text="response functions" >}} such as compressibilities and thermal expansion coefficients.
