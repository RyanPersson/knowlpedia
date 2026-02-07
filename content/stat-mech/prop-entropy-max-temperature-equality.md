---
title: "Entropy maximization implies equality of temperature"
description: "For two weakly coupled subsystems exchanging energy at fixed total energy, maximization of total entropy yields equality of temperatures at equilibrium."
---

## Statement (temperature equality from entropy maximization)

Let two weakly interacting subsystems 1 and 2 form an isolated composite system. Let $U_i$ be the {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} of subsystem $i$, and let $S_i(U_i,V_i,N_i)$ be its {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} (with $V_i,N_i$ fixed).

Assume:
- the subsystems can exchange energy but not volume or particles,
- the total energy is fixed: $U_1+U_2=U_{\mathrm{tot}}$,
- the total entropy is additive:
  $$
  S_{\mathrm{tot}}(U_1)= S_1(U_1,V_1,N_1) + S_2(U_{\mathrm{tot}}-U_1,V_2,N_2),
  $$

- $S_1,S_2$ are differentiable in $U$ and the equilibrium corresponds to an interior maximizer of $S_{\mathrm{tot}}$.

Then at equilibrium,
$$
\left(\frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1}
={}
\left(\frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2}.
$$
Using the definition of {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}},
$$
\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N},
$$
it follows that the equilibrium condition is
$$
T_1 = T_2.
$$

## Key hypotheses

- Two subsystems with negligible interaction energy so that entropy is additive.
- Exchange of energy only, with fixed $(V_i,N_i)$.
- Differentiability of $S_i$ in $U_i$.
- Equilibrium characterized by a (local) maximum of $S_{\mathrm{tot}}$ at fixed $U_{\mathrm{tot}}$.

## Key conclusions

- **Equality of temperatures** is the equilibrium condition for thermal contact:
  $$
  T_1=T_2.
  $$

- If, additionally, the entropies are strictly concave in $U$ (a stability condition), the entropy maximizer (hence the equilibrium energy split) is unique and stable.

## Cross-links to relevant definitions

- Entropy and its equilibrium role: {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}, {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}.
- Temperature as an intensive variable: {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Internal energy: {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}.
- Stability/concavity viewpoint: {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}.

