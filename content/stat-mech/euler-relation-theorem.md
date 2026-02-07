---
title: "Euler relation for extensive thermodynamic potentials"
description: "For an extensive fundamental relation U(S,V,N), Euler’s theorem gives U = TS − pV + μN (and multicomponent variants)."
---

## Statement
Let a {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}} be in {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}} and admit a differentiable fundamental relation for the {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} of the form $U=U(S,V,N)$, where $S,V,N$ are extensive variables.  
Assume $U$ is **extensive**, i.e. homogeneous of degree $1$:
$$
U(\lambda S,\lambda V,\lambda N)=\lambda\,U(S,V,N)\qquad(\lambda>0).
$$
Define the intensive variables in the usual way:
$$
T=\left(\frac{\partial U}{\partial S}\right)_{V,N},\qquad
p=-\left(\frac{\partial U}{\partial V}\right)_{S,N},\qquad
\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$
Then the **Euler relation** holds:
$$
U = TS - pV + \mu N.
$$

More generally, for a multicomponent system with $N=(N_1,\dots,N_r)$ and chemical potentials $\mu_i$, one has
$$
U = TS - pV + \sum_{i=1}^r \mu_i N_i.
$$

## Key hypotheses
- A well-defined {{< knowl id="thermodynamic-state" section="thermodynamics" text="thermodynamic state" >}} in equilibrium with differentiable $U(S,V,N)$.
- **Extensivity** (first-order homogeneity) of $U$ in the extensive variables.
- Standard identifications of $T,p,\mu$ as partial derivatives (see {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}, {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}, {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}).

## Conclusions
- The internal energy decomposes into intensive–extensive pairings: $U=TS-pV+\mu N$ (or the multicomponent sum).
- Differentiating the Euler relation and comparing with the {{< knowl id="first-law-thermodynamics" section="thermodynamics" text="first law" >}} yields the {{< knowl id="gibbs-duhem-theorem" section="thermodynamics" text="Gibbs–Duhem theorem" >}}.

