+++
id = "stat-mech/van-der-waals-gas"
title = "Example: van der Waals gas"
kind = "knowl"
summary = "Mean-field model of an interacting fluid with excluded volume and attraction: equation of state, free energy, and critical point."
aliases = ["van-der-waals-gas", "Example: van der Waals gas"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/van-der-waals-gas.md"
+++

A van der Waals gas is a simple interacting-fluid model that modifies the [[stat-mech/example-ideal-gas-classical|ideal gas]] by (i) an excluded volume per particle $b$ and (ii) a mean-field attraction strength $a$.

## Equation of state
With number density $n=N/V$, the van der Waals equation is
$$
\big(p + a n^2\big)\,(1-b n)=n k_B T,
$$
equivalently
$$
\bigg(p + a\Big(\frac{N}{V}\Big)^2\bigg)\,(V-Nb)=N k_B T,
$$

where $p$ is the [[thermodynamics/pressure-thermo|pressure]] and $T$ the [[thermodynamics/temperature-thermo|temperature]].

## A free-energy representation (useful for coexistence)
A standard mean-field [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] model is
$$
F(T,V,N)=F_{\mathrm{id}}(T,V-Nb,N)-a\frac{N^2}{V},
$$

where $F_{\mathrm{id}}$ is the ideal-gas free energy evaluated at the reduced volume $V-Nb$. Differentiating gives the equation of state via
$$
p = -\left(\frac{\partial F}{\partial V}\right)_{T,N}.
$$

This form is also a natural entry point to metastability and coexistence (see [[stat-mech/metastable-state|metastable states]] and [[stat-mech/surface-tension-interface|interfaces and surface tension]]).

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
- The van der Waals model captures a liquid–gas phase transition in a mean-field way, but does not reproduce non-mean-field critical behavior (compare [[stat-mech/mean-field-approximation|mean-field approximation]], [[stat-mech/critical-exponent|critical exponents]], and [[stat-mech/universality-class|universality classes]]).
- Stability criteria can be phrased using [[thermodynamics/thermodynamic-stability|thermodynamic stability]] (e.g., positivity of isothermal compressibility outside the spinodal region).
