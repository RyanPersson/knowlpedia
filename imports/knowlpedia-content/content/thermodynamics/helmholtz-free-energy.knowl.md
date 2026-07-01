+++
id = "thermodynamics/helmholtz-free-energy"
title = "Helmholtz free energy"
kind = "knowl"
summary = "A thermodynamic potential that controls equilibrium and maximum useful work at fixed and ."
aliases = ["helmholtz-free-energy", "Helmholtz free energy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/helmholtz-free-energy.md"
+++

## Definition and physical meaning

For a [[thermodynamics/thermodynamic-system|thermodynamic system]] with [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/temperature-thermo|temperature]] $T$, and [[thermodynamics/thermodynamic-entropy|entropy]] $S$, the **Helmholtz free energy** (often just “free energy”) is the [[thermodynamics/state-function|state function]]
$$
F \equiv U - TS.
$$

The term $TS$ represents the part of energy that is “bound up” as thermal disorder when the system is at temperature $T$. In contact with a [[thermodynamics/thermal-reservoir|thermal reservoir]] that fixes $T$, decreases in $F$ quantify how much energy can be converted into useful work while respecting the [[thermodynamics/second-law-thermodynamics|second law of thermodynamics]].

## Differential form and natural variables

For a simple compressible single-component system,
$$
dF = -S\,dT - p\,dV + \mu\,dN,
$$

with [[thermodynamics/pressure-thermo|pressure]] $p$, [[thermodynamics/volume-thermo|volume]] $V$, [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$, and [[thermodynamics/particle-number|particle number]] $N$.

Thus $F$ is naturally a function of $(T,V,N)$, mixing [[thermodynamics/intensive-variable|intensive variables]] (like $T$) and extensive variables (like $V$ and $N$), and it generates familiar response relations:
- $S = -\left(\partial F/\partial T\right)_{V,N}$,
- $p = -\left(\partial F/\partial V\right)_{T,N}$,
- $\mu = \left(\partial F/\partial N\right)_{T,V}$.

Cross-differentiation yields a [[thermodynamics/maxwell-relation|Maxwell relation]], for example
$$
\left(\frac{\partial S}{\partial V}\right)_{T,N}
={}
\left(\frac{\partial p}{\partial T}\right)_{V,N}.
$$

## Work interpretation at fixed temperature

For a system held at fixed temperature by a thermal reservoir, changes in $F$ bound the amount of work that can be extracted. With the [[thermodynamics/work-sign-convention|standard sign convention for work]], in an isothermal process at fixed $(T,V,N)$ the maximum work the system can deliver (i.e. “useful work,” excluding $p\,dV$ expansion work) satisfies
$$
W_{\text{useful,max}} = -\Delta F,
$$
with equality for a [[thermodynamics/reversible-process|reversible process]].

## Relation to Legendre transforms and ensembles

Starting from a [[thermodynamics/fundamental-relation-energy|fundamental relation]] $U(S,V,N)$, $F$ is obtained by a [[convex-analysis/legendre-transform|Legendre transform]] that trades the extensive variable $S$ for the conjugate temperature $T$.

In statistical mechanics (using the [[thermodynamics/canonical-ensemble-convention|canonical ensemble convention]] and [[thermodynamics/logarithm-convention-natural|natural logarithm convention]]),
$$
F = -k_B T \ln Z,
$$

where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]] and $Z$ is the canonical partition function.
