---
title: "Detailed balance"
description: "Reversibility condition for Markov dynamics: equilibrium has no net probability currents and path probabilities match under time-reversal."
---

Detailed balance is a *microscopic reversibility* condition for stochastic dynamics, central in equilibrium statistical mechanics and in Markov models of relaxation to equilibrium.

Prerequisites: {{< knowl id="probability-measure" section="probability" text="probability measure" >}}, {{< knowl id="expectation" section="probability" text="expectation" >}}, {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL)" >}}, {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}, {{< knowl id="markov-chain-discrete" text="Markov chain (discrete time)" >}}, {{< knowl id="markov-semigroup-continuous" text="Markov semigroup (continuous time)" >}}.

## Definition (discrete time)
Let $(X_n)_{n\ge 0}$ be a Markov chain on a countable state space with transition matrix $P=(P_{ij})$. A probability vector $\pi$ is *stationary* if $\pi=\pi P$.
We say **detailed balance holds** (or the chain is *reversible with respect to* $\pi$) if for all states $i,j$,
$$
\pi_i P_{ij}=\pi_j P_{ji}.
$$

Equivalently, the stationary *edge flow* $\pi_iP_{ij}$ is symmetric in $(i,j)$, so there are no steady probability currents.

## Definition (continuous time jump process)
For a continuous-time Markov chain with jump rates $q_{ij}\ge 0$ ($i\ne j$) and generator $Q$ (rows sum to $0$), detailed balance with stationary $\pi$ means
$$
\pi_i q_{ij}=\pi_j q_{ji}\qquad (i\ne j).
$$
This is the natural continuous-time analogue.

## TFAE (reversibility / detailed balance)
Assume $\pi$ is stationary.

The following are equivalent:

1. **(Detailed balance)** $\pi_i P_{ij}=\pi_j P_{ji}$ for all $i,j$ (discrete time), or $\pi_i q_{ij}=\pi_j q_{ji}$ for all $i\ne j$ (continuous time).

2. **(Time-reversal of paths)** For any finite path $i_0,i_1,\dots,i_n$,
   $$
   \pi_{i_0} P_{i_0 i_1}\cdots P_{i_{n-1} i_n}
   ={}
   \pi_{i_n} P_{i_n i_{n-1}}\cdots P_{i_1 i_0},
   $$
   i.e. the probability of a trajectory in stationarity equals that of its reversed trajectory.

3. **(Self-adjointness in $L^2(\pi)$)** The Markov operator $(Pf)(i)=\sum_j P_{ij} f(j)$ satisfies
   $$
   \langle f, Pg\rangle_\pi = \langle Pf, g\rangle_\pi,
   \quad
   \text{where }
   \langle f,g\rangle_\pi=\sum_i \pi_i f(i)g(i).
   $$
   (Similarly, the generator is self-adjoint for continuous time.)

4. **(No stationary currents)** The antisymmetric current $J_{ij}=\pi_iP_{ij}-\pi_jP_{ji}$ (or $J_{ij}=\pi_iq_{ij}-\pi_jq_{ji}$) vanishes for all pairs $(i,j)$.

## Global balance vs detailed balance
Stationarity $\pi=\pi P$ (or $\pi Q=0$) is sometimes called **global balance**; it only forces the *net* inflow at each state to match the outflow. Detailed balance is stronger: it matches inflow/outflow *pairwise* for each edge.

## Entropy production (interpretation)
Out of equilibrium, stationary currents typically lead to positive entropy production. Detailed balance is the stochastic analogue of equilibrium, connecting naturally to {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} and to monotone decay of {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} along dynamics defined by the {{< knowl id="master-equation" text="master equation" >}}.
