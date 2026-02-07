---
title: "Stability implies concavity/convexity of thermodynamic potentials"
description: "Thermodynamic stability forces entropy to be concave in extensive variables (equivalently, energy is convex), yielding positivity of response functions."
---

## Statement
Consider an equilibrium {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} with a differentiable entropy representation
$S=S(U,V,N)$ for the {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}.
Assume standard **thermodynamic stability** in the entropy-maximum sense: for fixed additive constraints, the equilibrium state maximizes total entropy under allowed exchanges (see {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}).

Then $S(U,V,N)$ is a **concave** function of the extensive variables:
for $0\le \lambda\le 1$ and any two admissible states,
$$
S(\lambda x + (1-\lambda) y)\ \ge\ \lambda S(x) + (1-\lambda) S(y),
\qquad x=(U,V,N),\ y=(U',V',N').
$$

Equivalently, in the energy representation $U=U(S,V,N)$, the internal energy is **convex** in $(S,V,N)$.

## Key hypotheses
- Existence of equilibrium states and differentiable fundamental relations for $S(U,V,N)$ or $U(S,V,N)$.
- Additivity/ability to form composite systems and exchange conserved quantities.
- Stability as an entropy maximum (or, dually, minimum of a suitable free energy at fixed intensive parameters).

## Conclusions
- Concavity of $S$ implies the Hessian of $S$ (where it exists) is negative semidefinite; convexity of $U$ implies the Hessian of $U$ is positive semidefinite.
- Standard response-function positivities follow (under appropriate regularity and choice of independent variables), e.g.
  - {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="Heat capacity at constant volume" >}} satisfies $C_V\ge 0$ in stable regions (see also {{< knowl id="prop-cv-positivity-stability" text="C_V positivity from stability" >}}).
  - {{< knowl id="isothermal-compressibility" section="thermodynamics" text="Isothermal compressibility" >}} satisfies $\kappa_T\ge 0$ (see {{< knowl id="prop-compressibility-positivity" text="compressibility positivity" >}}).
- Stability restricts curvature of thermodynamic potentials obtained by {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transforms" >}} (e.g., convexity/concavity properties of {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} and {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}}).

