+++
id = "thermodynamics/gibbs-duhem-theorem"
title = "Gibbs–Duhem theorem"
kind = "knowl"
summary = "Intensive variables are not independent: for a simple system, S dT − V dp + N dμ = 0 (and multicomponent generalizations)."
aliases = ["gibbs-duhem-theorem", "Gibbs–Duhem theorem"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/gibbs-duhem-theorem.md"
+++

## Statement
For an equilibrium [[thermodynamics/thermodynamic-system|thermodynamic system]] with extensive fundamental relation $U=U(S,V,N)$, assume the hypotheses of the [[stat-mech/euler-relation-theorem|Euler relation theorem]] so that
$$
U = TS - pV + \mu N.
$$
Then the **Gibbs–Duhem relation** holds:
$$
S\,dT - V\,dp + N\,d\mu = 0.
$$

For a multicomponent system with particle numbers $N_1,\dots,N_r$ and chemical potentials $\mu_1,\dots,\mu_r$,
$$
S\,dT - V\,dp + \sum_{i=1}^r N_i\,d\mu_i = 0.
$$

## Key hypotheses
- [[thermodynamics/thermodynamic-equilibrium|Thermodynamic equilibrium]] and differentiability of the fundamental relation.
- Extensivity (first-order homogeneity), used via [[stat-mech/euler-relation-theorem|Euler’s relation]].
- Validity of the differential form of the [[thermodynamics/first-law-thermodynamics|first law]]:
$$
dU = T\,dS - p\,dV + \mu\,dN
$$
(or the multicomponent variant).

## Conclusions
- The intensive variables $T,p,\mu$ (or $T,p,\mu_i$) cannot be chosen independently; they satisfy one linear differential constraint.
- Along a one-phase equilibrium manifold, specifying two of $(T,p,\mu)$ locally determines the third (subject to regularity).
