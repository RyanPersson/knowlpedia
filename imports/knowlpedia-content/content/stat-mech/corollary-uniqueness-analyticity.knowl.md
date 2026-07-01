+++
id = "stat-mech/corollary-uniqueness-analyticity"
title = "Uniqueness implies analyticity (no phase transition in the uniqueness region)"
kind = "knowl"
summary = "In lattice systems, a uniqueness regime (e.g. Dobrushin uniqueness / convergent cluster expansion) yields a unique infinite-volume Gibbs state and analytic pressure and correlation functions."
aliases = ["corollary-uniqueness-analyticity", "Uniqueness implies analyticity (no phase transition in the uniqueness region)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-uniqueness-analyticity.md"
+++

## Statement (absence of nonanalyticity under uniqueness)
Let a finite-range lattice spin system (e.g. the [[stat-mech-lattice/ising-model|Ising model]]) be specified by a [[stat-mech-lattice/gibbs-specification|Gibbs specification]] and associated finite-volume [[stat-mech-lattice/finite-volume-gibbs-measure|Gibbs measures]] with partition functions $Z_\Lambda(\beta,\mathbf{h})$.

Assume the system lies in a **uniqueness region**, for instance one covered by the [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness theorem]] (or any hypothesis implying a unique [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] and exponential mixing).

Then:
1. There is a **unique** infinite-volume Gibbs measure $\mu_{\beta,\mathbf{h}}$ satisfying the [[stat-mech-lattice/dlr-equation|DLR equation]].
2. The infinite-volume pressure (free energy density)
   $$
   p(\beta,\mathbf{h})=\lim_{\Lambda\uparrow \mathbb{Z}^d}\frac{1}{|\Lambda|}\log Z_\Lambda(\beta,\mathbf{h})
   $$
   exists and is **analytic** in parameters throughout that uniqueness region.
3. All finite-volume expectations of local observables converge to $\mu_{\beta,\mathbf{h}}$ uniformly in boundary conditions, and the resulting infinite-volume correlation functions are analytic in parameters.

## Key hypotheses
- Finite-range (or sufficiently fast decaying) interaction; well-defined specification.
- A criterion guaranteeing uniqueness and strong mixing, e.g. [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness]] or [[stat-mech/cluster-expansion-convergence|convergent cluster expansion]] in the parameter regime.
- Existence of the thermodynamic limit of the pressure (often proved independently, e.g. via subadditivity).

## Conclusions
- **No phase transition** (in the thermodynamic sense of nonanalyticity of $p$) can occur within the uniqueness region.
- In particular, nonuniqueness of Gibbs states (phase coexistence) cannot happen there:
  [[stat-mech-lattice/phase-transition-gibbs|phase transition as Gibbs nonuniqueness]] is excluded.

## Cross-links (definitions and supporting results)
- [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]], [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measure]]
- [[stat-mech-lattice/pressure-lattice|lattice pressure]], [[stat-mech-lattice/partition-function-lattice|lattice partition function]]
- [[thermodynamics/thermodynamic-limit-pressure-existence|existence of thermodynamic limit of the pressure]]
- [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness theorem]], [[stat-mech/corollary-high-temp-exponential-decay|high-temperature exponential decay]]
## significance
Uniqueness plus strong mixing yields uniform control of boundary-condition influence. In regimes covered by a convergent expansion (Dobrushin method or cluster expansion), one obtains absolutely convergent series for $\log Z_\Lambda$ and for expectations of local observables, uniform in $\Lambda$. Passing to the limit gives analyticity of $p(\beta,\mathbf{h})$ and of correlation functions.
This formalizes the slogan: **nonanalyticity requires nonuniqueness**.
