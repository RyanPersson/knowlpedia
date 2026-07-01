+++
id = "stat-mech-lattice/random-cluster-model"
title = "Random-cluster model (Fortuin–Kasteleyn percolation)"
kind = "knowl"
summary = "A probability measure on open/closed edges with parameters p and q, interpolating between bond percolation (q=1) and the q-state Potts/Ising models via the Fortuin–Kasteleyn representation."
aliases = ["random-cluster-model", "Random-cluster model (Fortuin–Kasteleyn percolation)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/random-cluster-model.md"
+++

The **random-cluster model** (also called **FK percolation**) is a probability measure on bond configurations on a [[discrete-structures/finite-graph|finite graph]] $G=(V,E)$ (typically a finite region of a lattice such as a [[discrete-structures/finite-box-lattice|finite box in a lattice]] with [[discrete-structures/nearest-neighbor-zd|nearest-neighbor edges]]).

A configuration is
- either a subset of edges $\omega \subseteq E$ (the **open** edges), or equivalently
- an element of $\{0,1\}^E$ (edge “spins”), so it fits the general idea of a [[stat-mech-lattice/spin-configuration|spin configuration]] with [[stat-mech-lattice/spin-space|spin space]] $\{0,1\}$ per edge.

Let $|\omega|$ be the number of open edges, and let $k(\omega)$ be the number of connected components (**clusters**) in the spanning subgraph $(V,\omega)$, counting isolated vertices as single-vertex clusters.

For parameters $p\in[0,1]$ and $q>0$, the random-cluster measure on $G$ is the [[probability/probability-measure|probability measure]]
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
is the **random-cluster partition function**, the analogue of the [[stat-mech-lattice/partition-function-lattice|lattice partition function]].

## Boundary conditions (free vs wired)

On a finite subgraph cut out of an infinite lattice, one often specifies boundary conditions (compare [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]]). For random-cluster models the standard choices are:

- **Free boundary condition**: clusters are computed using only edges inside the region.
- **Wired boundary condition**: boundary vertices are identified (“wired together”) before counting clusters, which favors connections to the boundary.

These boundary conditions produce different finite-volume measures, and they are central when taking [[thermodynamics/thermodynamic-limit|thermodynamic limits]] and defining infinite-volume objects (compare [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]).

## Fortuin–Kasteleyn link to Potts and Ising

The model is designed so that, for **integer** $q\ge 2$, it is exactly the graphical expansion of the [[stat-mech-lattice/potts-model|q-state Potts model]] (and for $q=2$ the [[stat-mech-lattice/ising-model|Ising model]]).

On a graph with uniform ferromagnetic coupling $J>0$ at [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$, the FK parameter is
$$
p \;=\; 1-e^{-\beta J}.
$$

In this correspondence, the random-cluster partition function matches the Potts partition function up to an explicit factor, and the cluster-weight $q^{k(\omega)}$ has a clear meaning: after choosing $\omega$, each cluster can be assigned one of $q$ spin labels independently, giving $q^{k(\omega)}$ possible spin assignments.

A useful consequence (often phrased via the Edwards–Sokal coupling) is that **connectivity events encode Potts correlations**: the event “$x$ is connected to $y$ by open edges” controls the probability that Potts spins at $x$ and $y$ are equal under the corresponding Potts measure.

## Key properties

### Special cases
- **$q=1$**: the factor $q^{k(\omega)}$ is constant, so $\phi_{G,p,1}$ is **independent bond percolation** with edge-open probability $p$.
- **$q=2$**: corresponds to the [[stat-mech-lattice/ising-model|Ising model]] (FK representation).
- **Non-integer $q>0$**: still defines a perfectly good probability model on edges, even though there is no literal $q$-state spin interpretation.

### Positive association and monotonicity (for $q\ge 1$)
For $q\ge 1$, the random-cluster model satisfies strong correlation inequalities (FKG-type positive association). Informally:
- increasing events are positively correlated,
- the model is monotone in $p$,
- wired boundary conditions typically dominate free boundary conditions for increasing events.

These monotonicity properties are a major reason the model is a standard tool for proving existence and structure of phase transitions.

### Domain Markov / specification viewpoint
Although the weight involves the global quantity $k(\omega)$, the model still has a consistent “conditional distribution in a subregion given the outside configuration,” i.e. a specification in the sense of [[stat-mech-lattice/gibbs-specification|Gibbs specifications]]. This supports an infinite-volume formulation analogous to the [[stat-mech-lattice/dlr-equation|DLR equation]] approach used for lattice spin systems.

### Thermodynamic quantities
On boxes $\Lambda$ in $\mathbb{Z}^d$ with edge set $E_\Lambda$, one defines the finite-volume free-energy density / pressure via
$$
\frac{1}{|\Lambda|}\log Z_{G_\Lambda}(p,q),
$$
leading to the [[stat-mech-lattice/pressure-lattice|lattice pressure]] and its [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]] when the limit exists.

Non-analytic behavior of this limit as a function of $(p,q)$ corresponds to a [[stat-mech-lattice/phase-transition-gibbs|phase transition]].

## Physical interpretation

- The configuration $\omega$ describes which bonds are “active.” For Potts/Ising systems, open edges represent bonds that are compatible with (or reinforce) local alignment.
- **Clusters** in $(V,\omega)$ represent **domains** of aligned spins in the coupled Potts picture.
- The parameter $q$ controls the **entropic weight of forming new clusters**:
  - larger $q$ favors having many clusters (more internal label choices),
  - larger $p$ favors opening edges and merging clusters.
- Long-range order can be read as large-scale connectivity:
  - the emergence of macroscopic clusters is tied to an [[stat-mech-lattice/order-parameter|order parameter]],
  - in Potts/Ising language, this corresponds to [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] and [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]].

Because it translates spin ordering questions into geometric connectivity questions, the random-cluster model is a central bridge between lattice spin systems and percolation-style geometry, and it provides geometric access to quantities like [[stat-mech/correlation-function-two-point|two-point correlations]], [[stat-mech/correlation-length|correlation length]], and [[stat-mech/susceptibility-stat-mech|susceptibility]] through cluster connectivity and cluster-size statistics.
