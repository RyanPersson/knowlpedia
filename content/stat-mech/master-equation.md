---
title: "Master equation"
description: "Forward equation for continuous-time Markov jump processes; describes probability flow between states via transition rates."
---

The master equation is the Kolmogorov forward equation for Markov jump processes. It is the standard starting point for stochastic models of relaxation, driven systems, and coarse-grained dynamics.

Prerequisites: {{< knowl id="probability-measure" section="probability" text="probability measure" >}}, {{< knowl id="markov-semigroup-continuous" text="Markov semigroup" >}}.

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

The family $P_t=e^{tQ}$ is the transition semigroup from {{< knowl id="markov-semigroup-continuous" text="Markov semigroups" >}}.

## Stationary distribution
A distribution $\pi$ is stationary if
$$
\pi Q=0,
$$

equivalently $\pi P_t=\pi$ for all $t\ge 0$.

## Detailed balance (equilibrium vs nonequilibrium)
A stationary $\pi$ satisfies {{< knowl id="detailed-balance" text="detailed balance" >}} when
$$
\pi_i q_{ij}=\pi_j q_{ji}\qquad (i\ne j).
$$
If detailed balance fails, the stationary state may still exist, but it typically carries nonzero steady currents (a hallmark of nonequilibrium steady states, compare {{< knowl id="nonequilibrium-steady-state" text="nonequilibrium steady state" >}}).

## Relative entropy decay (common Lyapunov function under detailed balance)
When detailed balance holds, {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} $D(p(t)\|\pi)$ is typically nonincreasing in time; this expresses relaxation toward equilibrium in an information-theoretic sense.
