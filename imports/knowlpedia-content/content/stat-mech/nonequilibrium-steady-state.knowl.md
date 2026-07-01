+++
id = "stat-mech/nonequilibrium-steady-state"
title = "Nonequilibrium steady state"
kind = "knowl"
summary = "A stationary state of driven dynamics with sustained probability/physical currents and positive entropy production; typically violates detailed balance."
aliases = ["nonequilibrium-steady-state", "Nonequilibrium steady state"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/nonequilibrium-steady-state.md"
+++

A nonequilibrium steady state (NESS) is a *time-stationary* state of a system that is maintained away from thermal equilibrium by driving (external fields, boundary gradients, multiple reservoirs, etc.). Unlike equilibrium Gibbs states, a NESS typically carries nonzero currents and violates detailed balance.

This knowl is framed in the language of Markov dynamics (see [[stat-mech/markov-chain-discrete|Markov chains]] and [[stat-mech/markov-semigroup-continuous|Markov semigroups]]).

## Definition (Markov dynamics)

Consider a continuous-time Markov jump process on a discrete state space with transition rates $w_{i\to j}$ and time-dependent probabilities $p_i(t)$. The master equation (see [[stat-mech/master-equation|master equation]]) is
$$
\dot p_i(t)
\;=\;
\sum_{j}\Bigl(p_j(t)\,w_{j\to i} - p_i(t)\,w_{i\to j}\Bigr).
$$

A probability vector $\pi$ is a **steady state** if it is stationary:
$$
0
\;=\;
\sum_{j}\Bigl(\pi_j\,w_{j\to i} - \pi_i\,w_{i\to j}\Bigr)
\quad \text{for all } i.
$$

A **nonequilibrium steady state (NESS)** is a steady state that is *not* an equilibrium state, typically characterized by:
- violation of detailed balance, and/or
- nonzero steady currents.

## Currents and detailed balance

Define the steady probability current along the oriented edge $i\to j$ by
$$
J_{i\to j}
\;=\;
\pi_i\,w_{i\to j} - \pi_j\,w_{j\to i}.
$$

- If **detailed balance** holds (see [[stat-mech/detailed-balance|detailed balance]]), then $J_{i\to j}=0$ for every pair $(i,j)$.
- A **NESS** typically has $J_{i\to j}\neq 0$ for some edges, producing persistent cycles of probability flow even though $\pi$ is time-independent.

## Entropy production rate

A standard quantitative measure of nonequilibrium is the steady-state entropy production rate:
$$
\sigma
\;=\;
\frac{1}{2}\sum_{i,j}
J_{i\to j}\,
\log\!\left(\frac{\pi_i\,w_{i\to j}}{\pi_j\,w_{j\to i}}\right),
\qquad
\sigma \ge 0.
$$

- In equilibrium (detailed balance), $\sigma=0$.
- In a genuine NESS with sustained currents, typically $\sigma>0$.

Connections to information-theoretic quantities are often expressed using [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]].

## Example: biased random walk on a ring

Take states $i\in\{1,\dots,N\}$ with rates
- $w_{i\to i+1}=p$ (clockwise),
- $w_{i\to i-1}=q$ (counterclockwise),
with indices modulo $N$.

Then:
- the stationary distribution is uniform, $\pi_i=1/N$,
- the steady current is constant,
$$
J_{i\to i+1} \;=\; \frac{p-q}{N},
$$

which is nonzero if $p\neq q$.

Thus the system is in a NESS whenever $p\neq q$: stationary but with persistent circulation and positive entropy production.

## Linear response and fluctuation relations (context)

Near equilibrium (weak driving), transport coefficients can often be expressed through equilibrium correlation functions via [[stat-mech/green-kubo-relations|Green–Kubo relations]] and the [[stat-mech/fluctuation-dissipation-theorem|fluctuation–dissipation theorem]].

Far from equilibrium, work and current fluctuations satisfy exact identities and inequalities, including [[stat-mech/fluctuation-theorem-crooks|Crooks fluctuation theorem]] and [[stat-mech/jarzynski-equality|Jarzynski equality]].

## Prerequisites

- [[probability/probability-measure|Probability measures]]
- [[stat-mech/markov-chain-discrete|Discrete Markov chains]]
- [[stat-mech/master-equation|Master equation]]
- [[stat-mech/detailed-balance|Detailed balance]]
- [[probability/relative-entropy-kl-divergence|Relative entropy (KL divergence)]]
