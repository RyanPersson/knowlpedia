---
title: "Cluster expansion theorem (analyticity from convergent polymer expansions)"
description: "Abstract conditions ensuring convergence of cluster expansions for log-partition functions, yielding analyticity of pressure and decay of correlations at high temperature or low density."
---

## Context
Cluster expansions turn a partition function into a controlled series over *connected* objects (polymers/contours), yielding:
- analyticity of the {{< knowl id="pressure-log-partition-density" text="pressure (log-partition density)" >}},
- uniqueness of the {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="Gibbs state" >}} in appropriate regimes,
- quantitative bounds on {{< knowl id="correlation-function-two-point" section="stat-mech" text="correlations" >}} and a finite {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}.

In lattice spin systems these regimes typically correspond to **high temperature** (small $\beta$) or, in gas models, **low activity/density**.

## Definition (abstract polymer model)
Let $\mathcal{P}$ be a set of polymers with:
- a compatibility relation: $\gamma\sim\gamma'$ means polymers are compatible (can coexist),
- an activity (weight) $z(\gamma)\in\mathbb{C}$.

For a finite region $V$, the polymer partition function is
$$
Z_V = \sum_{\Gamma\ \text{compatible in }V}\ \prod_{\gamma\in\Gamma} z(\gamma),
$$

where the sum runs over finite compatible families $\Gamma$ (including the empty family).

The associated finite-volume pressure is
$$
p_V = \frac{1}{|V|}\log Z_V,
$$
which matches the usual canonical setup (see {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}}).

## Theorem (cluster expansion; typical Kotecký–Preiss-type criterion)
Assume there exists a function $a:\mathcal{P}\to(0,\infty)$ such that for every polymer $\gamma$,
$$
\sum_{\gamma'\not\sim \gamma} |z(\gamma')|\,e^{a(\gamma')} \le a(\gamma).
$$
Then:

1. **Convergent expansion for $\log Z_V$:**
   $$
   \log Z_V = \sum_{n\ge 1}\ \frac{1}{n!}\sum_{(\gamma_1,\dots,\gamma_n)}
   \phi(\gamma_1,\dots,\gamma_n)\prod_{i=1}^n z(\gamma_i),
   $$

   where $\phi$ vanishes unless the incompatibility graph on $\{\gamma_1,\dots,\gamma_n\}$ is connected (Ursell/connected cluster coefficients).

2. **Absolute convergence and analyticity:** the series converges absolutely and uniformly in $V$ in a polydisc of activities, implying that $p_V$ and the infinite-volume pressure are analytic functions of the parameters in that regime.

3. **Uniqueness and decay of correlations (in applications):** when the polymer representation encodes a Gibbs measure, convergence typically implies uniqueness of the infinite-volume Gibbs state and exponential decay of truncated correlations, hence a finite correlation length.

## Typical applications in statistical mechanics
- **High-temperature spin systems:** expansions around $\beta=0$ prove analyticity and uniqueness (useful for {{< knowl id="clt-high-temperature-gibbs" text="high-temperature CLT results" >}} and mixing estimates).
- **Low-density gases:** the expansion yields virial/cluster integral relations (compare {{< knowl id="cluster-integrals-mayer" text="Mayer cluster integrals" >}} and {{< knowl id="virial-coefficients" text="virial coefficients" >}}) and convergence criteria (see {{< knowl id="virial-expansion-convergence" text="virial expansion convergence" >}}).
- **Contours at low temperature:** contour expansions are a key input to {{< knowl id="pirogov-sinai-theory" text="Pirogov–Sinai theory" >}} for phase coexistence and surface tension.

## Prerequisites and connections (cross-links)
- Canonical thermodynamics link: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="free energy" >}}, {{< knowl id="pressure-log-partition-density" text="pressure as log-partition density" >}}.
- Gibbs formalism: {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}, {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equations" >}}.
- Phase transitions: {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions (Gibbs)" >}}, {{< knowl id="tfae-phase-transition-indicators" section="stat-mech-lattice" text="equivalent indicators of phase transitions" >}}.
