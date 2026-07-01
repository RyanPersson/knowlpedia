+++
id = "thermodynamics/gibbs-duhem-relation"
title = "Gibbs–Duhem Relation"
kind = "knowl"
summary = "Extensivity implies a differential constraint among intensive variables, so they are not all independent."
aliases = ["gibbs-duhem-relation", "Gibbs–Duhem Relation"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/gibbs-duhem-relation.md"
+++

## Definition and physical interpretation

For a single-phase extensive [[thermodynamics/thermodynamic-system|thermodynamic system]], the intensive variables are constrained by the **Gibbs–Duhem relation**. For a simple, single-component system with variables $(S,V,N)$, it reads
$$
S\,dT - V\,dP + N\,d\mu = 0,
$$

where $T$ is the [[thermodynamics/temperature-thermo|temperature]], $P$ the [[thermodynamics/pressure-thermo|pressure]], and $\mu$ the [[thermodynamics/chemical-potential-thermo|chemical potential]]; $S$, $V$, and $N$ are the corresponding [[thermodynamics/extensive-variable|extensive]] variables.

More generally, for multiple species with particle numbers $N_i$ and chemical potentials $\mu_i$,
$$
S\,dT - V\,dP + \sum_i N_i\,d\mu_i = 0.
$$

Physically, this expresses that intensities cannot vary independently once the system is extensive: the freedom to scale the system size (doubling $(S,V,N_i)$) does not introduce an independent way to scale the conjugate intensities. For a one-component system, it implies that specifying $(T,P)$ fixes $\mu$ (up to phase coexistence subtleties).

## How it arises

Starting from the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] for the [[thermodynamics/internal-energy-thermo|internal energy]] $U(S,V,N)$,
$$
U = TS - PV + \mu N,
$$
differentiate and compare with the exact differential from the [[thermodynamics/fundamental-relation-energy|fundamental thermodynamic differential]]
$$
dU = T\,dS - P\,dV + \mu\,dN.
$$

The difference between these two expressions eliminates $dU$, $dS$, $dV$, and $dN$ and leaves the Gibbs–Duhem constraint.

## Useful rearrangements

- Dividing by $N$ introduces [[thermodynamics/specific-quantity|specific (per-particle) quantities]] $s=S/N$ and $v=V/N$:
  $$
  d\mu = v\,dP - s\,dT.
  $$

  This makes explicit that for a one-component phase, $\mu$ is a function of $(T,P)$.

- Using [[thermodynamics/gibbs-free-energy|Gibbs free energy]] with $G=\mu N$ (from Euler’s relation for a simple system) gives the same constraint by comparing
  $$
  dG = -S\,dT + V\,dP + \mu\,dN
  $$

  with $d(\mu N)=\mu\,dN+N\,d\mu$.
