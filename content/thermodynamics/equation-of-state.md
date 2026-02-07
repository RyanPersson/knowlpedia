---
title: "Equation of state"
description: "A constraint relation among equilibrium state variables that characterizes a material or phase."
---

An **equation of state (EOS)** is a relation among equilibrium {{< knowl id="state-variable" text="state variables" >}} that holds for a specified material, phase, and range of conditions. It restricts the allowed {{< knowl id="thermodynamic-state" text="thermodynamic states" >}} by specifying a functional constraint such as
$P = P(T,V,N)$ (or equivalently $f(P,T,V,N)=0$),
where $P$ is {{< knowl id="pressure-thermo" text="pressure" >}}, $T$ is {{< knowl id="temperature-thermo" text="temperature" >}}, $V$ is {{< knowl id="volume-thermo" text="volume" >}}, and $N$ is {{< knowl id="particle-number" text="particle number" >}}.

**Physical interpretation.** The EOS encodes the material’s mechanical/thermal response in equilibrium: it tells you what pressure results from specifying temperature and volume (and composition), or conversely how the system’s volume adjusts under changes in pressure and temperature. In practice, an EOS is determined empirically or derived from a microscopic model in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}.

**How it is used.**
- Combined with a {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} (or an equivalent thermodynamic potential), an EOS allows calculation of derivatives and {{< knowl id="response-function-thermo" text="response functions" >}}.
- In a *simple compressible system* with fixed $N$, specifying an EOS plus one additional independent relation (e.g., a caloric relation for $U$) is often enough to determine thermodynamic behavior.

**Key properties/relations.**
- **Consistency with extensivity.** For extensive systems, the EOS should respect scaling of extensive variables; this is naturally expressed using {{< knowl id="homogeneous-function-degree-one" text="homogeneity of degree one" >}} in an appropriate formulation.
- **Local stability constraints.** Physical EOS must yield stable response functions (e.g., $\kappa_T\ge 0$), connecting directly to {{< knowl id="thermodynamic-stability" text="stability conditions" >}}.
- **Derivable EOS from potentials.** If a potential (e.g., Helmholtz free energy) is known, the EOS can be obtained by differentiation, and cross-derivative identities yield {{< knowl id="maxwell-relation" text="Maxwell relations" >}}.
