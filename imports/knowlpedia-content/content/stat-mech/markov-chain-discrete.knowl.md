+++
id = "stat-mech/markov-chain-discrete"
title = "Markov chain (discrete time)"
kind = "knowl"
summary = "Stochastic process with the Markov property in discrete time; specified by a transition kernel/matrix and used to model relaxation and sampling."
aliases = ["markov-chain-discrete", "Markov chain (discrete time)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/markov-chain-discrete.md"
+++

A discrete-time Markov chain is a basic model for stochastic dynamics and is frequently used for equilibrium sampling (e.g. MCMC) and for coarse-grained dynamics in statistical mechanics.

Prerequisites: [[probability/probability-measure|probability measure]], [[probability/expectation|expectation]].

## Definition (Markov property)
Let $(X_n)_{n\ge 0}$ be a process on a state space $S$. It is a **Markov chain** if for all $n$ and measurable $A\subseteq S$,
$$
\mathbb{P}(X_{n+1}\in A \mid X_0,\dots,X_n)=\mathbb{P}(X_{n+1}\in A \mid X_n).
$$

The conditional law is determined by a **transition kernel** $P(x,A)$ (or by a matrix $P_{ij}$ when $S$ is countable).

## Transition operator and $n$-step transitions
For bounded functions $f$ on $S$ define
$$
(Pf)(x)=\int f(y)\,P(x,dy),
$$

and define $n$-step kernels by composition: $P^{n+m}=P^n P^m$ (Chapman–Kolmogorov).

If $\mu_0$ is the initial distribution, then the distribution after $n$ steps is
$$
\mu_n = \mu_0 P^n.
$$

## Stationary distribution
A probability measure $\pi$ on $S$ is **stationary** if
$$
\pi = \pi P,
\quad\text{i.e.}\quad
\pi(A)=\int \pi(dx)\,P(x,A).
$$

In statistical mechanics, $\pi$ is often chosen to be an equilibrium distribution such as a [[stat-mech/canonical-ensemble|canonical ensemble]] measure.

## Detailed balance and reversibility
If $\pi$ is stationary, the chain is **reversible** with respect to $\pi$ when it satisfies [[stat-mech/detailed-balance|detailed balance]]:
$$
\pi(dx)\,P(x,dy)=\pi(dy)\,P(y,dx)
$$

(in the discrete state case: $\pi_i P_{ij}=\pi_j P_{ji}$).

## Expectations along the chain
For an observable $f$ and initial law $\mu_0$,
$$
\mathbb{E}_{\mu_0}[f(X_n)] = \int \mu_0(dx)\,(P^n f)(x).
$$
Time averages and convergence to equilibrium depend on additional properties (irreducibility, aperiodicity, recurrence), but the operator viewpoint above is the main structural tool.
