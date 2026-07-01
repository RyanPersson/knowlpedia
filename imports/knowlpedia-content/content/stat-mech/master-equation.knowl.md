+++
id = "stat-mech/master-equation"
title = "Master equation"
kind = "knowl"
summary = "Forward equation for continuous-time Markov jump processes; describes probability flow between states via transition rates."
aliases = ["master-equation", "Master equation"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/master-equation.md"
+++

The master equation is the Kolmogorov forward equation for Markov jump processes. It is the standard starting point for stochastic models of relaxation, driven systems, and coarse-grained dynamics.

Prerequisites: [[probability/probability-measure|probability measure]], [[stat-mech/markov-semigroup-continuous|Markov semigroup]].

## Setup: rates and generator
Let $S$ be a countable state space. Specify jump rates $q_{ij}\ge 0$ for $i\ne j$. Define the generator matrix $Q$ by
- $Q_{ij}=q_{ij}$ for $i\ne j$,
- $Q_{ii}=-\sum_{j\ne i} q_{ij}$ (so each row sums to $0$).

Let $p_i(t)=\mathbb{P}(X_t=i)$ and write $p(t)$ as a row vector.

## Master equation (component form)
For each state $i$,
$$
\frac{d}{dt}p_i(t)=\sum_{j\ne i}\Big(p_j(t)\,q_{ji}-p_i(t)\,q_{ij}\Big).
$$

The first term is inflow from other states into $i$, and the second is outflow from $i$.

## Master equation (matrix form) and semigroup solution
In row-vector convention,
$$
\frac{d}{dt}p(t)=p(t)\,Q,
\qquad
p(t)=p(0)\,e^{tQ}.
$$

The family $P_t=e^{tQ}$ is the transition semigroup from [[stat-mech/markov-semigroup-continuous|Markov semigroups]].

## Stationary distribution
A distribution $\pi$ is stationary if
$$
\pi Q=0,
$$

equivalently $\pi P_t=\pi$ for all $t\ge 0$.

## Detailed balance (equilibrium vs nonequilibrium)
A stationary $\pi$ satisfies [[stat-mech/detailed-balance|detailed balance]] when
$$
\pi_i q_{ij}=\pi_j q_{ji}\qquad (i\ne j).
$$
If detailed balance fails, the stationary state may still exist, but it typically carries nonzero steady currents (a hallmark of nonequilibrium steady states, compare [[stat-mech/nonequilibrium-steady-state|nonequilibrium steady state]]).

## Relative entropy decay (common Lyapunov function under detailed balance)
When detailed balance holds, [[probability/relative-entropy-kl-divergence|relative entropy]] $D(p(t)\|\pi)$ is typically nonincreasing in time; this expresses relaxation toward equilibrium in an information-theoretic sense.
