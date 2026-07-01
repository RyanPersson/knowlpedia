+++
id = "stat-mech/cluster-expansion-convergence"
title = "Convergence of the cluster expansion"
kind = "knowl"
summary = "Sufficient small-activity/high-temperature conditions guaranteeing absolute convergence of the cluster expansion for log partition functions, with analyticity of the pressure and control of correlations."
aliases = ["cluster-expansion-convergence", "Convergence of the cluster expansion"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/cluster-expansion-convergence.md"
+++

## Statement (cluster expansion convergence)

Many lattice and continuum models can be rewritten as a *polymer model* whose (finite-volume) partition function has the form
$$
Z = \sum_{\Gamma \ \text{compatible}} \ \prod_{\gamma \in \Gamma} w(\gamma),
$$
where:
- $\Gamma$ ranges over finite collections of mutually compatible polymers $\gamma$ (no hard-core conflicts),
- $w(\gamma)$ are (possibly complex) polymer weights/activities.

Assume there exists a nonnegative function $a(\gamma)\ge 0$ such that the **Kotecký–Preiss (KP) criterion** holds:
$$
\sum_{\gamma' \not\sim \gamma} |w(\gamma')|\,e^{a(\gamma')} \le a(\gamma)\qquad \text{for all polymers }\gamma,
$$

where $\gamma' \not\sim \gamma$ means $\gamma'$ is *incompatible* with $\gamma$.

Then:

1. The **cluster expansion** for $\log Z$ converges absolutely:
   $$
   \log Z = \sum_{n\ge 1} \frac{1}{n!}\sum_{\gamma_1,\dots,\gamma_n}
   \phi^T(\gamma_1,\dots,\gamma_n)\prod_{i=1}^n w(\gamma_i),
   $$

   where $\phi^T$ is the usual truncated/connected coefficient (Ursell function; a signed sum over connected graphs).

2. The expansion converges uniformly in volume whenever the KP bound is uniform, yielding existence of the infinite-volume pressure and analyticity in the parameters appearing in $w(\gamma)$.

3. In applications where correlation functions can be expanded similarly, the same convergence mechanism yields strong control of truncated correlations and, under standard geometric assumptions, exponential decay of correlations.

## Key hypotheses

- A polymer representation of the relevant finite-volume partition function (often obtained from a high-temperature expansion, Mayer expansion, or contour representation).
- Absolute summability/smallness encoded by the KP criterion:
  $$
  \sum_{\gamma' \not\sim \gamma} |w(\gamma')|e^{a(\gamma')}\le a(\gamma).
  $$
- (For thermodynamic-limit statements) uniformity of the KP constants with respect to the volume and boundary conditions.

## Key conclusions

- Absolute convergence of $\log Z$ as a sum over connected clusters.
- Analyticity of $\log Z$ (hence of the finite-volume pressure) in the parameters controlling $w(\gamma)$, within the KP domain.
- Under standard additional bookkeeping, existence of the thermodynamic limit of the pressure (often as in [[thermodynamics/thermodynamic-limit-pressure-existence|thermodynamic-limit pressure existence]]) and exponential decay of truncated correlations.

## Cross-links to relevant definitions

- Finite-volume partition functions in lattice systems: [[stat-mech-lattice/partition-function-lattice|partition function (lattice)]].
- Finite-volume and infinite-volume pressure: [[stat-mech-lattice/pressure-lattice|pressure (lattice)]].
- Gibbs measures used to interpret expectations/correlations: [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] and [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]].
- Correlations whose decay is often derived from convergent expansions: [[stat-mech/correlation-function-two-point|two-point correlation function]].
- Grand-canonical viewpoint (when polymers arise from activity/fugacity expansions): [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]].
