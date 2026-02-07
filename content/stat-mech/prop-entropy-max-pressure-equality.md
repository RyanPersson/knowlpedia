---
title: "Entropy maximization implies equality of pressure"
description: "For two weakly coupled subsystems allowed to exchange volume at fixed totals, the entropy maximum implies equality of (generalized) mechanical intensities; with thermal equilibrium this becomes equality of pressures."
---

## Statement (pressure equality from entropy maximization)

Let subsystems 1 and 2 be separated by a movable boundary so they can exchange volume. Let $S_i(U_i,V_i,N_i)$ be the {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} of subsystem $i$.

Assume:
- the composite is isolated with fixed totals $U_{\mathrm{tot}}$ and $V_{\mathrm{tot}}$,
- particle numbers $N_1,N_2$ are fixed,
- the subsystems are weakly interacting so entropy is additive:
  $$
  S_{\mathrm{tot}}(U_1,V_1)=S_1(U_1,V_1,N_1)+S_2(U_{\mathrm{tot}}-U_1,V_{\mathrm{tot}}-V_1,N_2),
  $$

- $S_1,S_2$ are differentiable, and equilibrium corresponds to an interior maximizer of $S_{\mathrm{tot}}$.

Then the entropy maximization conditions imply
$$
\left(\frac{\partial S_1}{\partial V_1}\right)_{U_1,N_1}
={}
\left(\frac{\partial S_2}{\partial V_2}\right)_{U_2,N_2}.
$$
Using the thermodynamic identity (definition of {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}})
$$
\left(\frac{\partial S}{\partial V}\right)_{U,N}=\frac{P}{T},
$$
one obtains the equilibrium condition
$$
\frac{P_1}{T_1}=\frac{P_2}{T_2}.
$$
In particular, if the subsystems are also in thermal equilibrium (so that {{< knowl id="prop-entropy-max-temperature-equality" text="temperatures are equal" >}}), then
$$
P_1=P_2.
$$

## Key hypotheses

- Two weakly coupled subsystems, entropy additive.
- Exchange of volume allowed; totals $U_{\mathrm{tot}}$ and $V_{\mathrm{tot}}$ fixed.
- Differentiability of $S_i$ in $V_i$ and an interior entropy maximizer.

## Key conclusions

- The entropy maximum enforces equality of the mechanical intensity $P/T$:
  $$
  P_1/T_1 = P_2/T_2.
  $$

- With simultaneous thermal equilibrium ($T_1=T_2$), pressures equalize:
  $$
  P_1=P_2.
  $$

## Cross-links to relevant definitions

- Entropy and equilibrium: {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}, {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}.
- Pressure and temperature: {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Internal energy: {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}.
- Stability conditions ensuring a maximum: {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}.

