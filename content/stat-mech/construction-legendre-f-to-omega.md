---
title: "Legendre transform from Helmholtz free energy to grand potential"
description: "How the grand potential arises as the Legendre transform of the Helmholtz free energy with respect to particle number."
---

In equilibrium thermodynamics, different constraints lead naturally to different thermodynamic potentials. The **grand potential** is the potential adapted to fixed temperature $T$, volume $V$, and chemical potential $\mu$, i.e. the setting of the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}}.

## Definition (thermodynamic Legendre transform)

Let $F(T,V,N)$ be the Helmholtz free energy, i.e. the potential adapted to fixed $(T,V,N)$ (see {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} and {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}}).  
The **grand potential** $\Omega(T,V,\mu)$ is defined as the Legendre transform of $F$ with respect to the particle number $N$:
$$
\Omega(T,V,\mu) \;=\; \inf_{N\in\mathbb{N}} \bigl(F(T,V,N) - \mu N\bigr).
$$

At the minimizing $N=N^*(T,V,\mu)$ (when it exists), the stationarity condition is the familiar conjugacy relation
$$
\mu \;=\; \left(\frac{\partial F}{\partial N}\right)_{T,V}.
$$

Here $\mu$ is the {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}, i.e. the intensive variable conjugate to $N$.

In the thermodynamic limit (see {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}), one often treats $N$ as effectively continuous, and the infimum can be interpreted as a minimum over $N\ge 0$.

## Statistical-mechanical counterpart

In statistical mechanics, the same transform is encoded by switching from the canonical normalization factor {{< knowl id="partition-function-canonical" text="canonical partition function" >}} to the {{< knowl id="grand-partition-function" text="grand partition function" >}}. Concretely, if the canonical free energy is defined by the construction {{< knowl id="construction-free-energy-from-partition" text="free energy from a partition function" >}}, then the grand potential satisfies
$$
\Omega(T,V,\mu) \;=\; -\frac{1}{\beta}\,\log \Xi(\beta,\mu,V),
$$

where $\beta$ is the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} and $\Xi$ is constructed by {{< knowl id="construction-grand-canonical-partition-function" text="the grand-canonical partition-function construction" >}}.

## Physical interpretation

- Passing from $F(T,V,N)$ to $\Omega(T,V,\mu)$ exchanges the constraint “fixed particle number” for “fixed chemical potential,” matching the physics of a system in particle exchange with a reservoir.
- The term $-\mu N$ represents the energetic/entropic bookkeeping associated with exchanging particles with that reservoir.
- In homogeneous equilibrium, $\Omega$ is extensive in $V$ and encodes the pressure $p$ via
$$
\Omega(T,V,\mu) \;=\; -p(T,\mu)\,V
$$
(up to boundary corrections), connecting directly to {{< knowl id="grand-potential" section="thermodynamics" text="the thermodynamic grand potential" >}}.
