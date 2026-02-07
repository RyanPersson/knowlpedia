---
title: "Thermodynamic-limit state function"
description: "A quantity that becomes a well-defined, boundary-independent function of the thermodynamic state after taking the thermodynamic limit."
---

Finite systems often exhibit size- and boundary-dependent corrections: a thermodynamic potential may depend weakly on container shape, boundary conditions, or $1/V$ effects even at equilibrium. In the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}, many of these corrections disappear, and properly scaled quantities become genuine {{< knowl id="state-function" text="state functions" >}} of the macroscopic {{< knowl id="thermodynamic-state" text="thermodynamic state" >}}.

**Definition.** A quantity $A$ (or a density derived from it) is a **thermodynamic-limit state function** if there is a scaling (typically “per volume” or “per particle”) such that along a thermodynamic-limit sequence the limit exists and depends only on the limiting state variables (densities and/or intensive parameters), not on the path by which the limit is taken or on boundary details.

Concrete examples include:
- **Helmholtz free energy density.** With $F(T,V,N)$ the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} in the canonical setting, one defines
  $$
  f(T,\rho)=\lim_{V\to\infty,\ N/V\to\rho}\frac{F(T,V,N)}{V}.
  $$

  When the limit exists, $f$ depends only on the temperature and density (or equivalent intensive data), yielding an {{< knowl id="equation-of-state" text="equation of state" >}} through derivatives.
- **Entropy density.** With $S(U,V,N)$ the {{< knowl id="thermodynamic-entropy" text="entropy" >}}, one similarly considers
  $$
  s(u,\rho)=\lim_{V\to\infty,\ U/V\to u,\ N/V\to\rho}\frac{S(U,V,N)}{V}.
  $$

- **Pressure as a limit potential.** In the grand canonical setting, the {{< knowl id="grand-potential" text="grand potential" >}} typically satisfies $\Omega(T,V,\mu)\approx -PV$ for large $V$, so the limiting pressure becomes a state function of $T$ and the {{< knowl id="chemical-potential-thermo" text="chemical potential" >}}.

**Physical interpretation.** Thermodynamic-limit state functions are the “bulk” thermodynamic objects measured in macroscopic experiments: they are insensitive to microscopic boundary details and encode equilibrium properties of matter.

**Structural properties.**
- **Homogeneity and Euler/Gibbs–Duhem structure.** When {{< knowl id="extensivity-postulate" text="extensivity" >}} holds, extensive potentials become (asymptotically) {{< knowl id="homogeneous-function-degree-one" text="homogeneous of degree one" >}} in extensive variables, leading in the limit to identities such as the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} and the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}.
- **Convexity/concavity from stability.** Under {{< knowl id="thermodynamic-stability" text="stability" >}}, limiting free-energy-like densities are convex in their natural variables, while entropy-like densities are concave; this mirrors {{< knowl id="energy-convexity-stability" text="energy convexity vs. entropy concavity" >}}.
- **Ensemble consistency.** In many settings, the existence and uniqueness of these limits underlies equivalence between {{< knowl id="canonical-ensemble-convention" text="canonical" >}} and {{< knowl id="grand-canonical-ensemble-convention" text="grand canonical" >}} descriptions at the level of thermodynamic functions.
