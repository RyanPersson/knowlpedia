---
title: "Gibbs–Duhem Relation"
description: "Extensivity implies a differential constraint among intensive variables, so they are not all independent."
---

## Definition and physical interpretation

For a single-phase extensive {{< knowl id="thermodynamic-system" text="thermodynamic system" >}}, the intensive variables are constrained by the **Gibbs–Duhem relation**. For a simple, single-component system with variables $(S,V,N)$, it reads
$$
S\,dT - V\,dP + N\,d\mu = 0,
$$

where $T$ is the {{< knowl id="temperature-thermo" text="temperature" >}}, $P$ the {{< knowl id="pressure-thermo" text="pressure" >}}, and $\mu$ the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}; $S$, $V$, and $N$ are the corresponding {{< knowl id="extensive-variable" text="extensive" >}} variables.

More generally, for multiple species with particle numbers $N_i$ and chemical potentials $\mu_i$,
$$
S\,dT - V\,dP + \sum_i N_i\,d\mu_i = 0.
$$

Physically, this expresses that intensities cannot vary independently once the system is extensive: the freedom to scale the system size (doubling $(S,V,N_i)$) does not introduce an independent way to scale the conjugate intensities. For a one-component system, it implies that specifying $(T,P)$ fixes $\mu$ (up to phase coexistence subtleties).

## How it arises

Starting from the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} for the {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U(S,V,N)$,
$$
U = TS - PV + \mu N,
$$
differentiate and compare with the exact differential from the {{< knowl id="fundamental-relation-energy" text="fundamental thermodynamic differential" >}}
$$
dU = T\,dS - P\,dV + \mu\,dN.
$$

The difference between these two expressions eliminates $dU$, $dS$, $dV$, and $dN$ and leaves the Gibbs–Duhem constraint.

## Useful rearrangements

- Dividing by $N$ introduces {{< knowl id="specific-quantity" text="specific (per-particle) quantities" >}} $s=S/N$ and $v=V/N$:
  $$
  d\mu = v\,dP - s\,dT.
  $$

  This makes explicit that for a one-component phase, $\mu$ is a function of $(T,P)$.

- Using {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} with $G=\mu N$ (from Euler’s relation for a simple system) gives the same constraint by comparing
  $$
  dG = -S\,dT + V\,dP + \mu\,dN
  $$

  with $d(\mu N)=\mu\,dN+N\,d\mu$.
