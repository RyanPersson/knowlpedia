---
title: "Example: van der Waals gas"
description: "Mean-field model of an interacting fluid with excluded volume and attraction: equation of state, free energy, and critical point."
---

A van der Waals gas is a simple interacting-fluid model that modifies the {{< knowl id="example-ideal-gas-classical" text="ideal gas" >}} by (i) an excluded volume per particle $b$ and (ii) a mean-field attraction strength $a$.

## Equation of state
With number density $n=N/V$, the van der Waals equation is
$$
\big(p + a n^2\big)\,(1-b n)=n k_B T,
$$
equivalently
$$
\bigg(p + a\Big(\frac{N}{V}\Big)^2\bigg)\,(V-Nb)=N k_B T,
$$

where $p$ is the {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} and $T$ the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.

## A free-energy representation (useful for coexistence)
A standard mean-field {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} model is
$$
F(T,V,N)=F_{\mathrm{id}}(T,V-Nb,N)-a\frac{N^2}{V},
$$

where $F_{\mathrm{id}}$ is the ideal-gas free energy evaluated at the reduced volume $V-Nb$. Differentiating gives the equation of state via
$$
p = -\left(\frac{\partial F}{\partial V}\right)_{T,N}.
$$

This form is also a natural entry point to metastability and coexistence (see {{< knowl id="metastable-state" text="metastable states" >}} and {{< knowl id="surface-tension-interface" text="interfaces and surface tension" >}}).

## Critical point (molar form)
Using molar volume $V_m$ and gas constant $R$,
$$
p=\frac{RT}{V_m-b}-\frac{a}{V_m^2}.
$$

The critical point occurs where $(\partial p/\partial V_m)_T=(\partial^2 p/\partial V_m^2)_T=0$, yielding
$$
V_{m,c}=3b,\qquad T_c=\frac{8a}{27Rb},\qquad p_c=\frac{a}{27b^2},
$$
and the critical compressibility factor is
$$
Z_c=\frac{p_c V_{m,c}}{R T_c}=\frac{3}{8}.
$$

## Remarks
- The van der Waals model captures a liquid–gas phase transition in a mean-field way, but does not reproduce non-mean-field critical behavior (compare {{< knowl id="mean-field-approximation" text="mean-field approximation" >}}, {{< knowl id="critical-exponent" text="critical exponents" >}}, and {{< knowl id="universality-class" text="universality classes" >}}).
- Stability criteria can be phrased using {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}} (e.g., positivity of isothermal compressibility outside the spinodal region).
