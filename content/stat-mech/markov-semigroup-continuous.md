---
title: "Markov semigroup (continuous time)"
description: "One-parameter family of Markov operators describing continuous-time stochastic evolution; characterized by a generator and linked to the master equation."
---

A Markov semigroup is the continuous-time analogue of a Markov chain and is the natural language for equilibrium/non-equilibrium dynamics, including jump processes and diffusions.

Prerequisites: {{< knowl id="probability-measure" section="probability" text="probability measure" >}}, {{< knowl id="expectation" section="probability" text="expectation" >}}, {{< knowl id="master-equation" text="master equation" >}}.

## Definition (Markov semigroup)
A **Markov semigroup** is a family of linear operators $(P_t)_{t\ge 0}$ acting on bounded measurable functions $f$ on a state space $S$ such that:

1. (Semigroup) $P_0=\mathrm{Id}$ and $P_{t+s}=P_t P_s$ for all $t,s\ge 0$.
2. (Positivity) If $f\ge 0$ then $P_t f\ge 0$.
3. (Mass preservation) $P_t \mathbf{1}=\mathbf{1}$.

If $X_t$ is a time-homogeneous Markov process, then
$$
(P_t f)(x)=\mathbb{E}[f(X_t)\mid X_0=x].
$$

## Dual action on measures
For a probability measure $\mu$ on $S$, define $\mu_t=\mu P_t$ by
$$
\int f\,d\mu_t = \int (P_t f)\,d\mu.
$$

A measure $\pi$ is **stationary** if $\pi P_t=\pi$ for all $t\ge 0$.

## Generator
The (infinitesimal) **generator** $L$ is defined on a suitable domain by
$$
Lf=\lim_{t\downarrow 0}\frac{P_t f - f}{t},
$$
whenever the limit exists.

The semigroup then formally solves the backward equation
$$
\partial_t (P_t f) = L(P_t f), \qquad P_0 f=f.
$$

## Forward equation and the master equation
On measures (or densities), the evolution is governed by the adjoint generator $L^*$:
$$
\frac{d}{dt}\mu_t = \mu_t L^*.
$$

For pure jump processes on a countable state space, this becomes the {{< knowl id="master-equation" text="master equation" >}} with rate matrix $Q$.

## Detailed balance
A stationary $\pi$ satisfies {{< knowl id="detailed-balance" text="detailed balance" >}} (reversibility) when $L$ is self-adjoint in $L^2(\pi)$, equivalently when stationary probability currents vanish.
