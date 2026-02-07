---
title: "Thermodynamic response function"
description: "A derivative that quantifies how an equilibrium state variable changes under an infinitesimal change of its conjugate control variable."
---

A **thermodynamic response function** is a (typically equilibrium) partial derivative that measures how a state variable responds to an infinitesimal change in a control parameter, holding other specified variables fixed. Concretely, it is a derivative of the form $(\partial X/\partial Y)_{Z,\dots}$, evaluated along the equilibrium manifold described by an {{< knowl id="equation-of-state" text="equation of state" >}}.

**Physical interpretation.** Response functions quantify *susceptibility* and *stiffness*: large magnitude means the system changes a lot for a small applied change (high susceptibility), while small magnitude means the system is hard to change (stiff). In macroscopic thermodynamics they are measurable via small, quasi-static perturbations around {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}}.

Common examples include:
- Heat capacities: $C_V=(\partial U/\partial T)_{V,N}$ and $C_P=(\partial H/\partial T)_{P,N}$, linking to {{< knowl id="heat-capacity-constant-volume" text="$C_V$" >}} and {{< knowl id="heat-capacity-constant-pressure" text="$C_P$" >}}.
- Compressibilities: $\kappa_T=-\frac{1}{V}(\partial V/\partial P)_{T,N}$ and $\kappa_S=-\frac{1}{V}(\partial V/\partial P)_{S,N}$, linking to {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}} and {{< knowl id="adiabatic-compressibility" text="adiabatic compressibility" >}}.
- Thermal expansion: $\alpha=\frac{1}{V}(\partial V/\partial T)_{P,N}$, linking to {{< knowl id="thermal-expansion-coefficient" text="thermal expansion coefficient" >}}.

**Key relations.**
1. **Maxwell relations connect response functions.** When a thermodynamic potential is used as a generating function, equality of mixed partials yields identities among derivatives; see {{< knowl id="maxwell-relation" text="Maxwell relations" >}}.
2. **Stability constraints impose signs and inequalities.** For stable equilibrium, response functions such as $C_V$, $C_P$, and $\kappa_T$ are nonnegative (for simple systems) and divergences often indicate proximity to instabilities or criticality; see {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}, {{< knowl id="entropy-concavity-stability" text="entropy concavity" >}}, and {{< knowl id="energy-convexity-stability" text="energy convexity" >}}.
3. **Fluctuation interpretation (stat mech link).** In ensemble formulations, many response functions equal variances/covariances (e.g., $C_V$ related to energy fluctuations), tying thermodynamic derivatives to {{< knowl id="variance" section="probability" text="variance" >}} and {{< knowl id="expectation" section="probability" text="expectation" >}}.
