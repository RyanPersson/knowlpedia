---
title: "Grand potential"
description: "A thermodynamic potential natural for fixed , , and chemical potential."
---

## Definition and physical meaning

For a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} with {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="temperature-thermo" text="temperature" >}} $T$, {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$, {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} $\mu$, and {{< knowl id="particle-number" text="particle number" >}} $N$, the **grand potential** is the {{< knowl id="state-function" text="state function" >}}
$$
\Omega \equiv U - TS - \mu N.
$$

Equivalently, $\Omega = F - \mu N$ in terms of the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F$. It is the natural thermodynamic potential for an {{< knowl id="open-system" text="open system" >}} that can exchange both energy (as heat) and particles with large reservoirs that fix $T$ and $\mu$, while the volume $V$ is controlled.

## Differential form and natural variables

For a simple compressible single-component system,
$$
d\Omega = -S\,dT - p\,dV - N\,d\mu,
$$

where $p$ is the {{< knowl id="pressure-thermo" text="pressure" >}} and $V$ the {{< knowl id="volume-thermo" text="volume" >}}.

Thus $\Omega$ is naturally a function of $(T,V,\mu)$, and it generates:
- $S = -\left(\partial \Omega/\partial T\right)_{V,\mu}$,
- $p = -\left(\partial \Omega/\partial V\right)_{T,\mu}$,
- $N = -\left(\partial \Omega/\partial \mu\right)_{T,V}$.

At fixed $(T,V,\mu)$, equilibrium corresponds to minimizing $\Omega$ (the appropriate analog of minimizing {{< knowl id="helmholtz-free-energy" text="$F$" >}} at fixed $(T,V,N)$).

## Pressure relation in the thermodynamic limit

For a uniform macroscopic system satisfying standard {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} assumptions, $\Omega$ is extensive in $V$ and one has the important identity
$$
\Omega = -pV,
$$

which makes $\Omega$ a convenient generator of the {{< knowl id="equation-of-state" text="equation of state" >}} in grand-canonical settings.

## Relation to Legendre transforms and the grand-canonical ensemble

Starting from $F(T,V,N)$, the grand potential is obtained by a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} that trades the extensive $N$ for its conjugate intensive variable $\mu$.

In statistical mechanics (using the {{< knowl id="grand-canonical-ensemble-convention" text="grand-canonical ensemble convention" >}} and {{< knowl id="logarithm-convention-natural" text="natural logarithm convention" >}}),
$$
\Omega = -k_B T \ln \Xi,
$$

where $\Xi$ is the grand partition function, $k_B$ is the {{< knowl id="boltzmann-constant" text="Boltzmann constant" >}}, and the temperature can also be packaged via the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}} $\beta$.
