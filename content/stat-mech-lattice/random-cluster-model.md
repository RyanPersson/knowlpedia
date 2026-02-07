---
title: "Random-cluster model (Fortuin–Kasteleyn percolation)"
description: "A probability measure on open/closed edges with parameters p and q, interpolating between bond percolation (q=1) and the q-state Potts/Ising models via the Fortuin–Kasteleyn representation."
---


The **random-cluster model** (also called **FK percolation**) is a probability measure on bond configurations on a {{< knowl id="finite-graph" section="discrete-structures" text="finite graph" >}} $G=(V,E)$ (typically a finite region of a lattice such as a {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite box in a lattice" >}} with {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor edges" >}}).

A configuration is
- either a subset of edges $\omega \subseteq E$ (the **open** edges), or equivalently
- an element of $\{0,1\}^E$ (edge “spins”), so it fits the general idea of a {{< knowl id="spin-configuration" text="spin configuration" >}} with {{< knowl id="spin-space" text="spin space" >}} $\{0,1\}$ per edge.

Let $|\omega|$ be the number of open edges, and let $k(\omega)$ be the number of connected components (**clusters**) in the spanning subgraph $(V,\omega)$, counting isolated vertices as single-vertex clusters.

For parameters $p\in[0,1]$ and $q>0$, the random-cluster measure on $G$ is the {{< knowl id="probability-measure" section="probability" text="probability measure" >}}
$$
\phi_{G,p,q}(\omega)
\;=\;
\frac{1}{Z_{G}(p,q)}\,
p^{|\omega|}(1-p)^{|E|-|\omega|}\, q^{k(\omega)} ,
$$
where the normalizing constant
$$
Z_G(p,q)=\sum_{\omega\subseteq E} p^{|\omega|}(1-p)^{|E|-|\omega|}\, q^{k(\omega)}
$$
is the **random-cluster partition function**, the analogue of the {{< knowl id="partition-function-lattice" text="lattice partition function" >}}.

## Boundary conditions (free vs wired)

On a finite subgraph cut out of an infinite lattice, one often specifies boundary conditions (compare {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}}). For random-cluster models the standard choices are:

- **Free boundary condition**: clusters are computed using only edges inside the region.
- **Wired boundary condition**: boundary vertices are identified (“wired together”) before counting clusters, which favors connections to the boundary.

These boundary conditions produce different finite-volume measures, and they are central when taking {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limits" >}} and defining infinite-volume objects (compare {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}}).

## Fortuin–Kasteleyn link to Potts and Ising

The model is designed so that, for **integer** $q\ge 2$, it is exactly the graphical expansion of the {{< knowl id="potts-model" text="q-state Potts model" >}} (and for $q=2$ the {{< knowl id="ising-model" text="Ising model" >}}).

On a graph with uniform ferromagnetic coupling $J>0$ at {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta$, the FK parameter is
$$
p \;=\; 1-e^{-\beta J}.
$$

In this correspondence, the random-cluster partition function matches the Potts partition function up to an explicit factor, and the cluster-weight $q^{k(\omega)}$ has a clear meaning: after choosing $\omega$, each cluster can be assigned one of $q$ spin labels independently, giving $q^{k(\omega)}$ possible spin assignments.

A useful consequence (often phrased via the Edwards–Sokal coupling) is that **connectivity events encode Potts correlations**: the event “$x$ is connected to $y$ by open edges” controls the probability that Potts spins at $x$ and $y$ are equal under the corresponding Potts measure.

## Key properties

### Special cases
- **$q=1$**: the factor $q^{k(\omega)}$ is constant, so $\phi_{G,p,1}$ is **independent bond percolation** with edge-open probability $p$.
- **$q=2$**: corresponds to the {{< knowl id="ising-model" text="Ising model" >}} (FK representation).
- **Non-integer $q>0$**: still defines a perfectly good probability model on edges, even though there is no literal $q$-state spin interpretation.

### Positive association and monotonicity (for $q\ge 1$)
For $q\ge 1$, the random-cluster model satisfies strong correlation inequalities (FKG-type positive association). Informally:
- increasing events are positively correlated,
- the model is monotone in $p$,
- wired boundary conditions typically dominate free boundary conditions for increasing events.

These monotonicity properties are a major reason the model is a standard tool for proving existence and structure of phase transitions.

### Domain Markov / specification viewpoint
Although the weight involves the global quantity $k(\omega)$, the model still has a consistent “conditional distribution in a subregion given the outside configuration,” i.e. a specification in the sense of {{< knowl id="gibbs-specification" text="Gibbs specifications" >}}. This supports an infinite-volume formulation analogous to the {{< knowl id="dlr-equation" text="DLR equation" >}} approach used for lattice spin systems.

### Thermodynamic quantities
On boxes $\Lambda$ in $\mathbb{Z}^d$ with edge set $E_\Lambda$, one defines the finite-volume free-energy density / pressure via
$$
\frac{1}{|\Lambda|}\log Z_{G_\Lambda}(p,q),
$$
leading to the {{< knowl id="pressure-lattice" text="lattice pressure" >}} and its {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}} when the limit exists.

Non-analytic behavior of this limit as a function of $(p,q)$ corresponds to a {{< knowl id="phase-transition-gibbs" text="phase transition" >}}.

## Physical interpretation

- The configuration $\omega$ describes which bonds are “active.” For Potts/Ising systems, open edges represent bonds that are compatible with (or reinforce) local alignment.
- **Clusters** in $(V,\omega)$ represent **domains** of aligned spins in the coupled Potts picture.
- The parameter $q$ controls the **entropic weight of forming new clusters**:
  - larger $q$ favors having many clusters (more internal label choices),
  - larger $p$ favors opening edges and merging clusters.
- Long-range order can be read as large-scale connectivity:
  - the emergence of macroscopic clusters is tied to an {{< knowl id="order-parameter" text="order parameter" >}},
  - in Potts/Ising language, this corresponds to {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}} and {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}.

Because it translates spin ordering questions into geometric connectivity questions, the random-cluster model is a central bridge between lattice spin systems and percolation-style geometry, and it provides geometric access to quantities like {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}}, {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}, and {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}} through cluster connectivity and cluster-size statistics.
