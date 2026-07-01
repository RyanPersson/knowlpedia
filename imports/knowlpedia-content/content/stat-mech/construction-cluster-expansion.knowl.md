+++
id = "stat-mech/construction-cluster-expansion"
title = "Cluster expansion (construction)"
kind = "knowl"
summary = "Write log of the partition function as a convergent sum over connected clusters (polymers/graphs), typically in a high-temperature or low-activity regime."
aliases = ["construction-cluster-expansion", "Cluster expansion (construction)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-cluster-expansion.md"
+++

A **cluster expansion** is a systematic way to rewrite the logarithm of a finite-volume partition function as a sum of *connected* contributions. It is the workhorse behind rigorous high-temperature/low-density results: analyticity of the free energy, existence of the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], and decay of correlations.

## Polymer representation

In many lattice and continuum settings (e.g. models on a [[discrete-structures/finite-box-lattice|finite box]] inside a [[discrete-structures/lattice-zd|$\mathbb{Z}^d$ lattice]]), one first rewrites the finite-volume partition function—such as the [[stat-mech/partition-function-canonical|canonical partition function]] or the [[stat-mech/grand-partition-function|grand partition function]]—in **polymer-gas form**:
$$
Z_\Lambda \;=\; \sum_{\Gamma \,\text{compatible}} \;\prod_{\gamma\in\Gamma} w(\gamma).
$$
Here:
- $\Lambda$ is a finite region (volume).
- $\mathcal P_\Lambda$ is a collection of “polymers” $\gamma$ (typically localized objects: contours, connected sets, interaction blocks).
- $w(\gamma)$ is the polymer **activity** (weight).
- A set $\Gamma\subset \mathcal P_\Lambda$ is *compatible* if its polymers do not overlap (or otherwise satisfy a model-dependent compatibility rule).

This representation is the starting point for the general [[stat-mech/construction-canonical-partition-function|construction of partition functions]] in regimes where interactions can be treated perturbatively.

## Cluster expansion for $\log Z_\Lambda$

The cluster expansion is the identity
$$
\log Z_\Lambda
\;=\;
\sum_{n\ge 1}\frac{1}{n!}
\sum_{(\gamma_1,\dots,\gamma_n)\in\mathcal P_\Lambda^n}
\phi^T(\gamma_1,\dots,\gamma_n)\;
\prod_{i=1}^n w(\gamma_i),
$$

where $\phi^T(\gamma_1,\dots,\gamma_n)$ is the **truncated (connected) coefficient**. For a polymer gas with a hard incompatibility relation, define
$$
f(\gamma_i,\gamma_j)=
\begin{cases}
-1, & \gamma_i \text{ incompatible with } \gamma_j,\\
0, & \gamma_i \text{ compatible with } \gamma_j.
\end{cases}
$$
Then one convenient formula is
$$
\phi^T(\gamma_1,\dots,\gamma_n)
\;=\;
\sum_{\substack{G\ \text{connected graph}\\\text{on }\{1,\dots,n\}}}
\ \prod_{(i,j)\in E(G)} f(\gamma_i,\gamma_j).
$$

Only *connected* graphs contribute, which is why $\log Z_\Lambda$ is a sum over connected “clusters.”

This “connected vs disconnected” structure is the same reason derivatives of $\log Z$ produce cumulants and connected correlators (see [[stat-mech/construction-connected-correlations-cumulants|connected correlations from cumulants]] and [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from $\log Z$]]).

## Convergence and consequences

A cluster expansion becomes *useful* when the right-hand side converges absolutely and uniformly in $\Lambda$. A standard sufficient condition is of Kotecký–Preiss/Dobrushin type: there exists a size function $a(\gamma)\ge 0$ such that for every polymer $\gamma$,
$$
\sum_{\gamma' \not\sim \gamma} |w(\gamma')|\, e^{a(\gamma')} \;\le\; a(\gamma),
$$

where $\gamma'\not\sim \gamma$ means “incompatible.”

When such a condition holds:
- $(1/|\Lambda|)\log Z_\Lambda$ has a limit as $|\Lambda|\to\infty$, giving the free energy density via [[stat-mech/construction-free-energy-from-partition|free energy from the partition function]] and the pressure via [[stat-mech/pressure-from-partition-function|pressure from the partition function]].
- Connected correlations decay rapidly, implying a finite [[stat-mech/correlation-length|correlation length]] in that regime.
- One can often construct the infinite-volume Gibbs state by taking a [[stat-mech/construction-infinite-volume-gibbs-weak-limit|weak limit of finite-volume Gibbs measures]].

## Physical interpretation

The expansion organizes thermodynamics by *interaction clusters*: a cluster term represents a small group of degrees of freedom whose interactions cannot be factorized into independent pieces. Disconnected collections factorize in $Z_\Lambda$ but cancel in $\log Z_\Lambda$, leaving only genuinely collective contributions.

A canonical continuum example of the same connected-graph mechanism is the [[stat-mech/construction-mayer-expansion|Mayer expansion]] for gases.
