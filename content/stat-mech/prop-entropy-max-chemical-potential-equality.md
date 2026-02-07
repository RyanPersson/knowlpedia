---
title: "Entropy maximization implies equality of chemical potential"
description: "For two weakly coupled subsystems exchanging particles at fixed totals, the entropy maximum implies equality of the chemical potentials (in thermal equilibrium)."
---

## Statement (chemical potential equality from entropy maximization)

Let subsystems 1 and 2 be able to exchange particles of a given species through a permeable interface. Let $S_i(U_i,V_i,N_i)$ be the {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}} of subsystem $i$, where $N_i$ is the particle number of that species.

Assume:
- the composite is isolated with fixed totals $U_{\mathrm{tot}}$, $V_{\mathrm{tot}}$, and $N_{\mathrm{tot}}$,
- the subsystems are weakly interacting so entropy is additive:
  $$
  S_{\mathrm{tot}}(U_1,V_1,N_1)=S_1(U_1,V_1,N_1)+S_2(U_{\mathrm{tot}}-U_1,V_{\mathrm{tot}}-V_1,N_{\mathrm{tot}}-N_1),
  $$

- $S_1,S_2$ are differentiable in $N$, and equilibrium corresponds to an interior maximizer of $S_{\mathrm{tot}}$.

Then entropy maximization implies
$$
\left(\frac{\partial S_1}{\partial N_1}\right)_{U_1,V_1}
={}
\left(\frac{\partial S_2}{\partial N_2}\right)_{U_2,V_2}.
$$
Using the thermodynamic identity (definition of {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}})
$$
\left(\frac{\partial S}{\partial N}\right)_{U,V}=-\frac{\mu}{T},
$$
one obtains the equilibrium condition
$$
\frac{\mu_1}{T_1}=\frac{\mu_2}{T_2}.
$$
In particular, if the subsystems are also in thermal equilibrium (so that {{< knowl id="prop-entropy-max-temperature-equality" text="temperatures are equal" >}}), then
$$
\mu_1=\mu_2.
$$

## Key hypotheses

- Particle exchange is allowed; total particle number is fixed.
- Weak coupling so entropy is additive.
- Differentiability of $S_i$ in $N_i$ and an interior entropy maximizer.
- (For the conclusion $\mu_1=\mu_2$) thermal equilibrium, i.e., $T_1=T_2$.

## Key conclusions

- The entropy maximum enforces equality of $\mu/T$:
  $$
  \mu_1/T_1=\mu_2/T_2.
  $$

- With temperature equalization ($T_1=T_2$), chemical potentials equalize:
  $$
  \mu_1=\mu_2.
  $$

## Cross-links to relevant definitions

- Chemical potential and temperature: {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Entropy and equilibrium: {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}, {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}.
- Internal energy: {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}.
- Stability conditions: {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}.

