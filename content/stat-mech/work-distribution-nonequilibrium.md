---
title: "Nonequilibrium work distribution"
description: "Definition of work as a trajectory functional under a driving protocol and the induced distribution P(W), central to Crooks and Jarzynski relations."
---

## Work as a trajectory functional
Consider a system with microstate $x$ (classical phase point or configuration) and a parameter-dependent Hamiltonian/energy $H(x,\lambda)$. A driving protocol $\lambda_t$ is applied over $t\in[0,\tau]$.

For a single realization with trajectory $t\mapsto x_t$, the (protocol) work done on the system is commonly defined as
$$
W[x_{0:\tau}]
={}
\int_0^\tau \dot{\lambda}_t\,\partial_\lambda H(x_t,\lambda_t)\,dt.
$$

For discrete-time driving $\lambda_{0},\lambda_{1},\dots,\lambda_{N}$ with microstates $x_0,\dots,x_N$,
$$
W
={}
\sum_{k=0}^{N-1}\bigl(H(x_k,\lambda_{k+1})-H(x_k,\lambda_k)\bigr),
$$
i.e. the energy change due purely to parameter updates.

Along a single realization, one can decompose the energy change as
$$
\Delta E \;=\; W + Q,
$$

where $\Delta E$ is the change in internal energy (compare {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}) and $Q$ is heat exchanged with the environment (first-law bookkeeping).

## The work distribution
Assume an initial distribution for $x_0$ (often equilibrium, e.g. the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at $\lambda_0$) and a dynamics generating a path measure on trajectories (Hamiltonian dynamics, Langevin, a {{< knowl id="markov-chain-discrete" text="Markov chain" >}}, or a {{< knowl id="markov-semigroup-continuous" text="Markov semigroup" >}}).

The **work distribution** $P(W)$ is the pushforward of the path measure under the map $\omega\mapsto W(\omega)$. Formally,
$$
P(W)
={}
\int \delta\!\bigl(W - W[\omega]\bigr)\,d\mathbb{P}(\omega),
$$

where $\mathbb{P}$ is the path probability measure and $\delta$ is the Dirac delta.

The mean work is $\langle W\rangle$, an {{< knowl id="expectation" section="probability" text="expectation" >}} under $P(W)$.

## Forward and reverse distributions
For a protocol $\lambda_t$ (forward) and its time reversal $\tilde\lambda_t=\lambda_{\tau-t}$ (reverse), denote the distributions by $P_F(W)$ and $P_R(W)$. Their relation is the content of the {{< knowl id="fluctuation-theorem-crooks" text="Crooks fluctuation theorem" >}} and implies {{< knowl id="jarzynski-equality" text="Jarzynski’s equality" >}}.

## Large-deviation viewpoint (optional)
In repeated driving of large systems, $W$ (or work per particle) often satisfies a {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}} with a {{< knowl id="rate-function" section="large-deviations" text="rate function" >}}, and fluctuation relations constrain that rate function via symmetry identities.
