+++
id = "stat-mech/construction-legendre-f-to-omega"
title = "Legendre transform from Helmholtz free energy to grand potential"
kind = "knowl"
summary = "How the grand potential arises as the Legendre transform of the Helmholtz free energy with respect to particle number."
aliases = ["construction-legendre-f-to-omega", "Legendre transform from Helmholtz free energy to grand potential"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-legendre-f-to-omega.md"
+++

In equilibrium thermodynamics, different constraints lead naturally to different thermodynamic potentials. The **grand potential** is the potential adapted to fixed temperature $T$, volume $V$, and chemical potential $\mu$, i.e. the setting of the [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]].

## Definition (thermodynamic Legendre transform)

Let $F(T,V,N)$ be the Helmholtz free energy, i.e. the potential adapted to fixed $(T,V,N)$ (see [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] and [[thermodynamics/thermodynamic-system|thermodynamic system]]).
The **grand potential** $\Omega(T,V,\mu)$ is defined as the Legendre transform of $F$ with respect to the particle number $N$:
$$
\Omega(T,V,\mu) \;=\; \inf_{N\in\mathbb{N}} \bigl(F(T,V,N) - \mu N\bigr).
$$

At the minimizing $N=N^*(T,V,\mu)$ (when it exists), the stationarity condition is the familiar conjugacy relation
$$
\mu \;=\; \left(\frac{\partial F}{\partial N}\right)_{T,V}.
$$

Here $\mu$ is the [[thermodynamics/chemical-potential-thermo|chemical potential]], i.e. the intensive variable conjugate to $N$.

In the thermodynamic limit (see [[thermodynamics/thermodynamic-limit|thermodynamic limit]]), one often treats $N$ as effectively continuous, and the infimum can be interpreted as a minimum over $N\ge 0$.

## Statistical-mechanical counterpart

In statistical mechanics, the same transform is encoded by switching from the canonical normalization factor [[stat-mech/partition-function-canonical|canonical partition function]] to the [[stat-mech/grand-partition-function|grand partition function]]. Concretely, if the canonical free energy is defined by the construction [[stat-mech/construction-free-energy-from-partition|free energy from a partition function]], then the grand potential satisfies
$$
\Omega(T,V,\mu) \;=\; -\frac{1}{\beta}\,\log \Xi(\beta,\mu,V),
$$

where $\beta$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]] and $\Xi$ is constructed by [[stat-mech/construction-grand-canonical-partition-function|the grand-canonical partition-function construction]].

## Physical interpretation

- Passing from $F(T,V,N)$ to $\Omega(T,V,\mu)$ exchanges the constraint “fixed particle number” for “fixed chemical potential,” matching the physics of a system in particle exchange with a reservoir.
- The term $-\mu N$ represents the energetic/entropic bookkeeping associated with exchanging particles with that reservoir.
- In homogeneous equilibrium, $\Omega$ is extensive in $V$ and encodes the pressure $p$ via
$$
\Omega(T,V,\mu) \;=\; -p(T,\mu)\,V
$$
(up to boundary corrections), connecting directly to [[thermodynamics/grand-potential|the thermodynamic grand potential]].
