---
title: "Temperature from entropy"
description: "Defines thermodynamic temperature (and inverse temperature) through the derivative of entropy with respect to energy."
---

In equilibrium thermodynamics, temperature is not assumed a priori; it can be *defined* from how entropy changes with energy. Statistical mechanics implements this using microcanonical entropy.

## Microcanonical entropy as a function of energy

For an isolated system with energy $U$, volume $V$, and particle number $N$, the {{< knowl id="boltzmann-entropy-microcanonical" text="Boltzmann (microcanonical) entropy" >}} is
$$
S(U,V,N) \;=\; k_B \log \Omega(U,V,N),
$$

where $\Omega(U,V,N)$ is a density of states (or phase-space volume of a thin {{< knowl id="microcanonical-shell" text="microcanonical energy shell" >}}), as described in {{< knowl id="construction-microcanonical-entropy-density-of-states" section="thermodynamics" text="the entropy–density-of-states construction" >}}.

## Definition of temperature and inverse temperature

The **thermodynamic temperature** (as in {{< knowl id="temperature-thermo" section="thermodynamics" text="thermodynamic temperature" >}}) is defined by
$$
\frac{1}{T}
\;=\;
\left(\frac{\partial S}{\partial U}\right)_{V,N}.
$$
Equivalently, the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} is
$$
\beta \;=\; \frac{1}{k_B T}
\;=\;
\left(\frac{\partial}{\partial U}\log \Omega(U,V,N)\right)_{V,N}.
$$

This definition is meaningful when $S(U,V,N)$ is differentiable (or at least has a well-defined slope in an appropriate thermodynamic limit).

## Why this is the equilibrium temperature

Consider two weakly interacting subsystems (1) and (2) that can exchange energy, with total energy fixed:
$$
U_1 + U_2 = U_{\mathrm{tot}}.
$$
If the interaction energy is negligible, the total entropy is approximately additive:
$$
S_{\mathrm{tot}}(U_1) \approx S_1(U_1) + S_2(U_{\mathrm{tot}}-U_1).
$$

Equilibrium corresponds to maximizing $S_{\mathrm{tot}}$ with respect to $U_1$. Differentiating and setting the derivative to zero yields
$$
\left(\frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1}
={}
\left(\frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2}.
$$

Thus the equilibrium condition is equality of the quantities $1/T$, justifying the derivative definition.

## Connection to the canonical ensemble

If subsystem (2) is a very large reservoir (“heat bath”), then expanding $S_2(U_{\mathrm{tot}}-U_1)$ around $U_{\mathrm{tot}}$ gives
$$
S_2(U_{\mathrm{tot}}-U_1) \approx S_2(U_{\mathrm{tot}}) - \beta\,k_B\,U_1,
$$

with $\beta$ fixed by the bath’s slope. This leads to the canonical weight $\exp(-\beta H)$ for subsystem (1), connecting directly to the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} and to {{< knowl id="construction-entropy-maximization-thermal" text="entropy-maximization construction of thermal states" >}}.

## Physical interpretation and sign of temperature

- Large $\partial S/\partial U$ means entropy increases rapidly with energy, corresponding to low temperature.
- Small $\partial S/\partial U$ corresponds to high temperature.
- If $S(U)$ decreases with $U$ over some range (possible when the energy spectrum is bounded above, e.g. certain spin systems), then $\partial S/\partial U<0$ and the resulting temperature is negative; this is captured cleanly by the sign of $\beta$ in the definition above.
