---
title: "Nonequilibrium steady state"
description: "A stationary state of driven dynamics with sustained probability/physical currents and positive entropy production; typically violates detailed balance."
---

A nonequilibrium steady state (NESS) is a *time-stationary* state of a system that is maintained away from thermal equilibrium by driving (external fields, boundary gradients, multiple reservoirs, etc.). Unlike equilibrium Gibbs states, a NESS typically carries nonzero currents and violates detailed balance.

This knowl is framed in the language of Markov dynamics (see {{< knowl id="markov-chain-discrete" text="Markov chains" >}} and {{< knowl id="markov-semigroup-continuous" text="Markov semigroups" >}}).

## Definition (Markov dynamics)

Consider a continuous-time Markov jump process on a discrete state space with transition rates $w_{i\to j}$ and time-dependent probabilities $p_i(t)$. The master equation (see {{< knowl id="master-equation" text="master equation" >}}) is
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

- If **detailed balance** holds (see {{< knowl id="detailed-balance" text="detailed balance" >}}), then $J_{i\to j}=0$ for every pair $(i,j)$.
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

Connections to information-theoretic quantities are often expressed using {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}.

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

Near equilibrium (weak driving), transport coefficients can often be expressed through equilibrium correlation functions via {{< knowl id="green-kubo-relations" text="Green–Kubo relations" >}} and the {{< knowl id="fluctuation-dissipation-theorem" text="fluctuation–dissipation theorem" >}}.

Far from equilibrium, work and current fluctuations satisfy exact identities and inequalities, including {{< knowl id="fluctuation-theorem-crooks" text="Crooks fluctuation theorem" >}} and {{< knowl id="jarzynski-equality" text="Jarzynski equality" >}}.

## Prerequisites

- {{< knowl id="probability-measure" section="probability" text="Probability measures" >}}
- {{< knowl id="markov-chain-discrete" text="Discrete Markov chains" >}}
- {{< knowl id="master-equation" text="Master equation" >}}
- {{< knowl id="detailed-balance" text="Detailed balance" >}}
- {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Relative entropy (KL divergence)" >}}
