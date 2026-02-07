---
title: "Gibbs–Duhem theorem"
description: "Intensive variables are not independent: for a simple system, S dT − V dp + N dμ = 0 (and multicomponent generalizations)."
---

## Statement
For an equilibrium {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} with extensive fundamental relation $U=U(S,V,N)$, assume the hypotheses of the {{< knowl id="euler-relation-theorem" section="stat-mech" text="Euler relation theorem" >}} so that
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
- {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="Thermodynamic equilibrium" >}} and differentiability of the fundamental relation.
- Extensivity (first-order homogeneity), used via {{< knowl id="euler-relation-theorem" section="stat-mech" text="Euler’s relation" >}}.
- Validity of the differential form of the {{< knowl id="first-law-thermodynamics" section="thermodynamics" text="first law" >}}:
$$
dU = T\,dS - p\,dV + \mu\,dN
$$
(or the multicomponent variant).

## Conclusions
- The intensive variables $T,p,\mu$ (or $T,p,\mu_i$) cannot be chosen independently; they satisfy one linear differential constraint.
- Along a one-phase equilibrium manifold, specifying two of $(T,p,\mu)$ locally determines the third (subject to regularity).

