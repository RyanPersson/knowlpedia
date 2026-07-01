+++
id = "stat-mech/euler-relation-theorem"
title = "Euler relation for extensive thermodynamic potentials"
kind = "knowl"
summary = "For an extensive fundamental relation U(S,V,N), Euler’s theorem gives U = TS − pV + μN (and multicomponent variants)."
aliases = ["euler-relation-theorem", "Euler relation for extensive thermodynamic potentials"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/euler-relation-theorem.md"
+++

## Statement
Let a [[thermodynamics/thermodynamic-system|thermodynamic system]] be in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] and admit a differentiable fundamental relation for the [[thermodynamics/internal-energy-thermo|internal energy]] of the form $U=U(S,V,N)$, where $S,V,N$ are extensive variables.
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
- A well-defined [[thermodynamics/thermodynamic-state|thermodynamic state]] in equilibrium with differentiable $U(S,V,N)$.
- **Extensivity** (first-order homogeneity) of $U$ in the extensive variables.
- Standard identifications of $T,p,\mu$ as partial derivatives (see [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]]).

## Conclusions
- The internal energy decomposes into intensive–extensive pairings: $U=TS-pV+\mu N$ (or the multicomponent sum).
- Differentiating the Euler relation and comparing with the [[thermodynamics/first-law-thermodynamics|first law]] yields the [[thermodynamics/gibbs-duhem-theorem|Gibbs–Duhem theorem]].
