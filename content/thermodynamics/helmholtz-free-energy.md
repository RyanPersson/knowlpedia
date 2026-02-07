---
title: "Helmholtz free energy"
description: "A thermodynamic potential that controls equilibrium and maximum useful work at fixed and ."
---

## Definition and physical meaning

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} with {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="temperature-thermo" text="temperature" >}} $T$, and {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, the **Helmholtz free energy** (often just “free energy”) is the {{< knowl id="state-function" text="state function" >}}
$$
F \equiv U - TS.
$$

The term $TS$ represents the part of energy that is “bound up” as thermal disorder when the system is at temperature $T$. In contact with a {{< knowl id="thermal-reservoir" text="thermal reservoir" >}} that fixes $T$, decreases in $F$ quantify how much energy can be converted into useful work while respecting the {{< knowl id="second-law-thermodynamics" text="second law of thermodynamics" >}}.

## Differential form and natural variables

For a simple compressible single-component system,
$$
dF = -S\,dT - p\,dV + \mu\,dN,
$$

with {{< knowl id="pressure-thermo" text="pressure" >}} $p$, {{< knowl id="volume-thermo" text="volume" >}} $V$, {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} $\mu$, and {{< knowl id="particle-number" text="particle number" >}} $N$.

Thus $F$ is naturally a function of $(T,V,N)$, mixing {{< knowl id="intensive-variable" text="intensive variables" >}} (like $T$) and extensive variables (like $V$ and $N$), and it generates familiar response relations:
- $S = -\left(\partial F/\partial T\right)_{V,N}$,
- $p = -\left(\partial F/\partial V\right)_{T,N}$,
- $\mu = \left(\partial F/\partial N\right)_{T,V}$.

Cross-differentiation yields a {{< knowl id="maxwell-relation" text="Maxwell relation" >}}, for example
$$
\left(\frac{\partial S}{\partial V}\right)_{T,N}
={}
\left(\frac{\partial p}{\partial T}\right)_{V,N}.
$$

## Work interpretation at fixed temperature

For a system held at fixed temperature by a thermal reservoir, changes in $F$ bound the amount of work that can be extracted. With the {{< knowl id="work-sign-convention" text="standard sign convention for work" >}}, in an isothermal process at fixed $(T,V,N)$ the maximum work the system can deliver (i.e. “useful work,” excluding $p\,dV$ expansion work) satisfies
$$
W_{\text{useful,max}} = -\Delta F,
$$
with equality for a {{< knowl id="reversible-process" text="reversible process" >}}.

## Relation to Legendre transforms and ensembles

Starting from a {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} $U(S,V,N)$, $F$ is obtained by a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} that trades the extensive variable $S$ for the conjugate temperature $T$.

In statistical mechanics (using the {{< knowl id="canonical-ensemble-convention" text="canonical ensemble convention" >}} and {{< knowl id="logarithm-convention-natural" text="natural logarithm convention" >}}),
$$
F = -k_B T \ln Z,
$$

where $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}} and $Z$ is the canonical partition function.
