---
title: "Maxwell Relations"
description: "Equalities between mixed partial derivatives of thermodynamic potentials, following from exact differentials."
---

## Definition and physical interpretation

A **Maxwell relation** is an identity obtained by equating mixed {{< knowl id="partial-derivative" section="real-analysis" text="partial derivatives" >}} of a thermodynamic potential. The key input is that a thermodynamic potential is a {{< knowl id="state-function" text="state function" >}} with an exact differential, and (assuming sufficient smoothness, e.g. twice continuously {{< knowl id="differentiable-map" section="real-analysis" text="differentiable" >}}) mixed derivatives commute.

Physically, Maxwell relations let you replace derivatives involving hard-to-measure quantities such as the {{< knowl id="thermodynamic-entropy" text="entropy" >}} by derivatives of more directly accessible observables such as {{< knowl id="pressure-thermo" text="pressure" >}}, {{< knowl id="volume-thermo" text="volume" >}}, and {{< knowl id="temperature-thermo" text="temperature" >}}.

## Standard set for a simple compressible system (fixed composition)

Holding $N$ fixed for clarity:

1) From the {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U(S,V)$ with
$$
dU = T\,dS - P\,dV,
$$
one obtains
$$
\left(\frac{\partial T}{\partial V}\right)_{S}
={}
-\left(\frac{\partial P}{\partial S}\right)_{V}.
$$

2) From the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F(T,V)$ with
$$
dF = -S\,dT - P\,dV,
$$
one obtains
$$
\left(\frac{\partial S}{\partial V}\right)_{T}
={}
\left(\frac{\partial P}{\partial T}\right)_{V}.
$$

3) From the {{< knowl id="enthalpy" text="enthalpy" >}} $H(S,P)$ with
$$
dH = T\,dS + V\,dP,
$$
one obtains
$$
\left(\frac{\partial T}{\partial P}\right)_{S}
={}
\left(\frac{\partial V}{\partial S}\right)_{P}.
$$

4) From the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G(T,P)$ with
$$
dG = -S\,dT + V\,dP,
$$
one obtains
$$
\left(\frac{\partial S}{\partial P}\right)_{T}
={}
-\left(\frac{\partial V}{\partial T}\right)_{P}.
$$

These identities are frequently combined with an {{< knowl id="equation-of-state" text="equation of state" >}} and {{< knowl id="response-function-thermo" text="response functions" >}} to convert between different measurable derivatives.
