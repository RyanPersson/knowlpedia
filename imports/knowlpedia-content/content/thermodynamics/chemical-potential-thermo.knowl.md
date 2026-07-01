+++
id = "thermodynamics/chemical-potential-thermo"
title = "Chemical potential"
kind = "knowl"
summary = "The intensive variable conjugate to particle number, governing matter exchange, diffusion, and chemical equilibrium."
aliases = ["chemical-potential-thermo", "Chemical potential"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/chemical-potential-thermo.md"
+++

## Definition and physical interpretation

The **chemical potential** $\mu$ is an [[thermodynamics/intensive-variable|intensive]] thermodynamic variable conjugate to the [[thermodynamics/particle-number|particle number]] $N$. It quantifies how the system’s energy (or free energy) changes when one adds or removes matter, holding appropriate other variables fixed.

Physically, gradients or mismatches in $\mu$ drive particle transfer: when two subsystems can exchange particles through a permeable boundary, net flow occurs in the direction that lowers the appropriate thermodynamic potential, and equilibrium is reached when chemical potentials match (the condition for [[thermodynamics/chemical-equilibrium|chemical equilibrium]]).

## Thermodynamic definitions

For a simple compressible single-component system with fundamental relation $U=U(S,V,N)$,
$$
dU = T\,dS - p\,dV + \mu\,dN,
$$
and therefore
$$
\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

Using thermodynamic potentials obtained by a [[convex-analysis/legendre-transform|Legendre transform]] gives equivalent and often more practical characterizations:

- From the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)=U-TS$,
  $$
  \mu=\left(\frac{\partial F}{\partial N}\right)_{T,V}.
  $$

- From the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,p,N)=U-TS+pV$,
  $$
  \mu=\left(\frac{\partial G}{\partial N}\right)_{T,p}.
  $$

These identities make clear which laboratory controls (fixed $T,V$ or fixed $T,p$) correspond to the “cost of adding a particle” in different experimental situations.

## Exchange, equilibrium, and the grand potential

When particle exchange with a reservoir is allowed (an [[thermodynamics/open-system|open system]]), it is natural to work with the [[thermodynamics/grand-potential|grand potential]]
$\Omega = U - TS - \mu N$.
At fixed [[thermodynamics/temperature-thermo|temperature]], volume, and $\mu$, equilibrium corresponds to minimizing $\Omega$ (subject to constraints). This is the thermodynamic underpinning of the [[thermodynamics/grand-canonical-ensemble-convention|grand canonical ensemble]] description in statistical mechanics.

## Key relations and constraints

- **Euler and Gibbs–Duhem structure:** For systems satisfying the [[thermodynamics/extensivity-postulate|extensivity postulate]] and standard homogeneity assumptions, $\mu$ participates in the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] and is not independent of the other intensive variables. Infinitesimal constraints among intensives are captured by the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]].

- **Connection to number density:** For homogeneous matter, $\mu$ is often viewed as a function of $(T,n)$ where $n$ is the [[thermodynamics/number-density|number density]]. This emphasizes that $\mu$ controls composition at fixed temperature, much like [[thermodynamics/pressure-thermo|pressure]] controls mechanical equilibrium.

- **Sign and “chemical work” bookkeeping:** The term $\mu\,dN$ in the fundamental differential is the standard accounting of energy change due to matter exchange; conventions for separating this from other work-like contributions are summarized by the [[thermodynamics/chemical-work-convention|chemical work convention]].
