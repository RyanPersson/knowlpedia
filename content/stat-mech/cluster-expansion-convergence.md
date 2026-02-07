---
title: "Convergence of the cluster expansion"
description: "Sufficient small-activity/high-temperature conditions guaranteeing absolute convergence of the cluster expansion for log partition functions, with analyticity of the pressure and control of correlations."
---

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
- Under standard additional bookkeeping, existence of the thermodynamic limit of the pressure (often as in {{< knowl id="thermodynamic-limit-pressure-existence" section="thermodynamics" text="thermodynamic-limit pressure existence" >}}) and exponential decay of truncated correlations.

## Cross-links to relevant definitions

- Finite-volume partition functions in lattice systems: {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function (lattice)" >}}.
- Finite-volume and infinite-volume pressure: {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure (lattice)" >}}.
- Gibbs measures used to interpret expectations/correlations: {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}} and {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}}.
- Correlations whose decay is often derived from convergent expansions: {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}.
- Grand-canonical viewpoint (when polymers arise from activity/fugacity expansions): {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}}.

