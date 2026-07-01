+++
id = "thermodynamics/maxwell-relation"
title = "Maxwell Relations"
kind = "knowl"
summary = "Equalities between mixed partial derivatives of thermodynamic potentials, following from exact differentials."
aliases = ["maxwell-relation", "Maxwell Relations"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/maxwell-relation.md"
+++

## Definition and physical interpretation

A **Maxwell relation** is an identity obtained by equating mixed [[real-analysis/partial-derivative|partial derivatives]] of a thermodynamic potential. The key input is that a thermodynamic potential is a [[thermodynamics/state-function|state function]] with an exact differential, and (assuming sufficient smoothness, e.g. twice continuously [[real-analysis/differentiable-map|differentiable]]) mixed derivatives commute.

Physically, Maxwell relations let you replace derivatives involving hard-to-measure quantities such as the [[thermodynamics/thermodynamic-entropy|entropy]] by derivatives of more directly accessible observables such as [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/volume-thermo|volume]], and [[thermodynamics/temperature-thermo|temperature]].

## Standard set for a simple compressible system (fixed composition)

Holding $N$ fixed for clarity:

1) From the [[thermodynamics/internal-energy-thermo|internal energy]] $U(S,V)$ with
$$
dU = T\,dS - P\,dV,
$$
one obtains
$$
\left(\frac{\partial T}{\partial V}\right)_{S}
={}
-\left(\frac{\partial P}{\partial S}\right)_{V}.
$$

2) From the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V)$ with
$$
dF = -S\,dT - P\,dV,
$$
one obtains
$$
\left(\frac{\partial S}{\partial V}\right)_{T}
={}
\left(\frac{\partial P}{\partial T}\right)_{V}.
$$

3) From the [[thermodynamics/enthalpy|enthalpy]] $H(S,P)$ with
$$
dH = T\,dS + V\,dP,
$$
one obtains
$$
\left(\frac{\partial T}{\partial P}\right)_{S}
={}
\left(\frac{\partial V}{\partial S}\right)_{P}.
$$

4) From the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,P)$ with
$$
dG = -S\,dT + V\,dP,
$$
one obtains
$$
\left(\frac{\partial S}{\partial P}\right)_{T}
={}
-\left(\frac{\partial V}{\partial T}\right)_{P}.
$$

These identities are frequently combined with an [[thermodynamics/equation-of-state|equation of state]] and [[thermodynamics/response-function-thermo|response functions]] to convert between different measurable derivatives.
