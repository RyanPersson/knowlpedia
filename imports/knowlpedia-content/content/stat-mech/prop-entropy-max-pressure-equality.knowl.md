+++
id = "stat-mech/prop-entropy-max-pressure-equality"
title = "Entropy maximization implies equality of pressure"
kind = "knowl"
summary = "For two weakly coupled subsystems allowed to exchange volume at fixed totals, the entropy maximum implies equality of (generalized) mechanical intensities; with thermal equilibrium this becomes equality of pressures."
aliases = ["prop-entropy-max-pressure-equality", "Entropy maximization implies equality of pressure"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/prop-entropy-max-pressure-equality.md"
+++

## Statement (pressure equality from entropy maximization)

Let subsystems 1 and 2 be separated by a movable boundary so they can exchange volume. Let $S_i(U_i,V_i,N_i)$ be the [[thermodynamics/thermodynamic-entropy|entropy]] of subsystem $i$.

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
Using the thermodynamic identity (definition of [[thermodynamics/pressure-thermo|pressure]])
$$
\left(\frac{\partial S}{\partial V}\right)_{U,N}=\frac{P}{T},
$$
one obtains the equilibrium condition
$$
\frac{P_1}{T_1}=\frac{P_2}{T_2}.
$$
In particular, if the subsystems are also in thermal equilibrium (so that [[stat-mech/prop-entropy-max-temperature-equality|temperatures are equal]]), then
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

- Entropy and equilibrium: [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]].
- Pressure and temperature: [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/temperature-thermo|temperature]].
- Internal energy: [[thermodynamics/internal-energy-thermo|internal energy]].
- Stability conditions ensuring a maximum: [[thermodynamics/thermodynamic-stability|thermodynamic stability]].
