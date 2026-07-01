+++
id = "thermodynamics/thermodynamic-limit-state-function"
title = "Thermodynamic-limit state function"
kind = "knowl"
summary = "A quantity that becomes a well-defined, boundary-independent function of the thermodynamic state after taking the thermodynamic limit."
aliases = ["thermodynamic-limit-state-function", "Thermodynamic-limit state function"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-limit-state-function.md"
+++

Finite systems often exhibit size- and boundary-dependent corrections: a thermodynamic potential may depend weakly on container shape, boundary conditions, or $1/V$ effects even at equilibrium. In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], many of these corrections disappear, and properly scaled quantities become genuine [[thermodynamics/state-function|state functions]] of the macroscopic [[thermodynamics/thermodynamic-state|thermodynamic state]].

**Definition.** A quantity $A$ (or a density derived from it) is a **thermodynamic-limit state function** if there is a scaling (typically “per volume” or “per particle”) such that along a thermodynamic-limit sequence the limit exists and depends only on the limiting state variables (densities and/or intensive parameters), not on the path by which the limit is taken or on boundary details.

Concrete examples include:
- **Helmholtz free energy density.** With $F(T,V,N)$ the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] in the canonical setting, one defines
  $$
  f(T,\rho)=\lim_{V\to\infty,\ N/V\to\rho}\frac{F(T,V,N)}{V}.
  $$

  When the limit exists, $f$ depends only on the temperature and density (or equivalent intensive data), yielding an [[thermodynamics/equation-of-state|equation of state]] through derivatives.
- **Entropy density.** With $S(U,V,N)$ the [[thermodynamics/thermodynamic-entropy|entropy]], one similarly considers
  $$
  s(u,\rho)=\lim_{V\to\infty,\ U/V\to u,\ N/V\to\rho}\frac{S(U,V,N)}{V}.
  $$

- **Pressure as a limit potential.** In the grand canonical setting, the [[thermodynamics/grand-potential|grand potential]] typically satisfies $\Omega(T,V,\mu)\approx -PV$ for large $V$, so the limiting pressure becomes a state function of $T$ and the [[thermodynamics/chemical-potential-thermo|chemical potential]].

**Physical interpretation.** Thermodynamic-limit state functions are the “bulk” thermodynamic objects measured in macroscopic experiments: they are insensitive to microscopic boundary details and encode equilibrium properties of matter.

**Structural properties.**
- **Homogeneity and Euler/Gibbs–Duhem structure.** When [[thermodynamics/extensivity-postulate|extensivity]] holds, extensive potentials become (asymptotically) [[thermodynamics/homogeneous-function-degree-one|homogeneous of degree one]] in extensive variables, leading in the limit to identities such as the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] and the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]].
- **Convexity/concavity from stability.** Under [[thermodynamics/thermodynamic-stability|stability]], limiting free-energy-like densities are convex in their natural variables, while entropy-like densities are concave; this mirrors [[thermodynamics/energy-convexity-stability|energy convexity vs. entropy concavity]].
- **Ensemble consistency.** In many settings, the existence and uniqueness of these limits underlies equivalence between [[thermodynamics/canonical-ensemble-convention|canonical]] and [[thermodynamics/grand-canonical-ensemble-convention|grand canonical]] descriptions at the level of thermodynamic functions.
