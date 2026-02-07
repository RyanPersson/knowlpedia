---
title: "Chemical potential"
description: "The intensive variable conjugate to particle number, governing matter exchange, diffusion, and chemical equilibrium."
---

## Definition and physical interpretation

The **chemical potential** $\mu$ is an {{< knowl id="intensive-variable" text="intensive" >}} thermodynamic variable conjugate to the {{< knowl id="particle-number" text="particle number" >}} $N$. It quantifies how the system’s energy (or free energy) changes when one adds or removes matter, holding appropriate other variables fixed.

Physically, gradients or mismatches in $\mu$ drive particle transfer: when two subsystems can exchange particles through a permeable boundary, net flow occurs in the direction that lowers the appropriate thermodynamic potential, and equilibrium is reached when chemical potentials match (the condition for {{< knowl id="chemical-equilibrium" text="chemical equilibrium" >}}).

## Thermodynamic definitions

For a simple compressible single-component system with fundamental relation $U=U(S,V,N)$,
$$
dU = T\,dS - p\,dV + \mu\,dN,
$$
and therefore
$$
\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

Using thermodynamic potentials obtained by a {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} gives equivalent and often more practical characterizations:

- From the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F(T,V,N)=U-TS$,
  $$
  \mu=\left(\frac{\partial F}{\partial N}\right)_{T,V}.
  $$

- From the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G(T,p,N)=U-TS+pV$,
  $$
  \mu=\left(\frac{\partial G}{\partial N}\right)_{T,p}.
  $$

These identities make clear which laboratory controls (fixed $T,V$ or fixed $T,p$) correspond to the “cost of adding a particle” in different experimental situations.

## Exchange, equilibrium, and the grand potential

When particle exchange with a reservoir is allowed (an {{< knowl id="open-system" text="open system" >}}), it is natural to work with the {{< knowl id="grand-potential" text="grand potential" >}}
$\Omega = U - TS - \mu N$.
At fixed {{< knowl id="temperature-thermo" text="temperature" >}}, volume, and $\mu$, equilibrium corresponds to minimizing $\Omega$ (subject to constraints). This is the thermodynamic underpinning of the {{< knowl id="grand-canonical-ensemble-convention" text="grand canonical ensemble" >}} description in statistical mechanics.

## Key relations and constraints

- **Euler and Gibbs–Duhem structure:** For systems satisfying the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} and standard homogeneity assumptions, $\mu$ participates in the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}} and is not independent of the other intensive variables. Infinitesimal constraints among intensives are captured by the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}.

- **Connection to number density:** For homogeneous matter, $\mu$ is often viewed as a function of $(T,n)$ where $n$ is the {{< knowl id="number-density" text="number density" >}}. This emphasizes that $\mu$ controls composition at fixed temperature, much like {{< knowl id="pressure-thermo" text="pressure" >}} controls mechanical equilibrium.

- **Sign and “chemical work” bookkeeping:** The term $\mu\,dN$ in the fundamental differential is the standard accounting of energy change due to matter exchange; conventions for separating this from other work-like contributions are summarized by the {{< knowl id="chemical-work-convention" text="chemical work convention" >}}.
