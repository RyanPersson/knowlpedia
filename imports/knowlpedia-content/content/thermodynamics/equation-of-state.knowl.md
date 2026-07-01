+++
id = "thermodynamics/equation-of-state"
title = "Equation of state"
kind = "knowl"
summary = "A constraint relation among equilibrium state variables that characterizes a material or phase."
aliases = ["equation-of-state", "Equation of state"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/equation-of-state.md"
+++

An **equation of state (EOS)** is a relation among equilibrium [[thermodynamics/state-variable|state variables]] that holds for a specified material, phase, and range of conditions. It restricts the allowed [[thermodynamics/thermodynamic-state|thermodynamic states]] by specifying a functional constraint such as
$P = P(T,V,N)$ (or equivalently $f(P,T,V,N)=0$),
where $P$ is [[thermodynamics/pressure-thermo|pressure]], $T$ is [[thermodynamics/temperature-thermo|temperature]], $V$ is [[thermodynamics/volume-thermo|volume]], and $N$ is [[thermodynamics/particle-number|particle number]].

**Physical interpretation.** The EOS encodes the material’s mechanical/thermal response in equilibrium: it tells you what pressure results from specifying temperature and volume (and composition), or conversely how the system’s volume adjusts under changes in pressure and temperature. In practice, an EOS is determined empirically or derived from a microscopic model in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].

**How it is used.**
- Combined with a [[thermodynamics/fundamental-relation-energy|fundamental relation]] (or an equivalent thermodynamic potential), an EOS allows calculation of derivatives and [[thermodynamics/response-function-thermo|response functions]].
- In a *simple compressible system* with fixed $N$, specifying an EOS plus one additional independent relation (e.g., a caloric relation for $U$) is often enough to determine thermodynamic behavior.

**Key properties/relations.**
- **Consistency with extensivity.** For extensive systems, the EOS should respect scaling of extensive variables; this is naturally expressed using [[thermodynamics/homogeneous-function-degree-one|homogeneity of degree one]] in an appropriate formulation.
- **Local stability constraints.** Physical EOS must yield stable response functions (e.g., $\kappa_T\ge 0$), connecting directly to [[thermodynamics/thermodynamic-stability|stability conditions]].
- **Derivable EOS from potentials.** If a potential (e.g., Helmholtz free energy) is known, the EOS can be obtained by differentiation, and cross-derivative identities yield [[thermodynamics/maxwell-relation|Maxwell relations]].
