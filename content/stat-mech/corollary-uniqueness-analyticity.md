---
title: "Uniqueness implies analyticity (no phase transition in the uniqueness region)"
description: "In lattice systems, a uniqueness regime (e.g. Dobrushin uniqueness / convergent cluster expansion) yields a unique infinite-volume Gibbs state and analytic pressure and correlation functions."
---

## Statement (absence of nonanalyticity under uniqueness)
Let a finite-range lattice spin system (e.g. the {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}) be specified by a {{< knowl id="gibbs-specification" section="stat-mech-lattice" text="Gibbs specification" >}} and associated finite-volume {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="Gibbs measures" >}} with partition functions $Z_\Lambda(\beta,\mathbf{h})$.

Assume the system lies in a **uniqueness region**, for instance one covered by the {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness theorem" >}} (or any hypothesis implying a unique {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}} and exponential mixing).

Then:
1. There is a **unique** infinite-volume Gibbs measure $\mu_{\beta,\mathbf{h}}$ satisfying the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}.
2. The infinite-volume pressure (free energy density)
   $$
   p(\beta,\mathbf{h})=\lim_{\Lambda\uparrow \mathbb{Z}^d}\frac{1}{|\Lambda|}\log Z_\Lambda(\beta,\mathbf{h})
   $$
   exists and is **analytic** in parameters throughout that uniqueness region.
3. All finite-volume expectations of local observables converge to $\mu_{\beta,\mathbf{h}}$ uniformly in boundary conditions, and the resulting infinite-volume correlation functions are analytic in parameters.

## Key hypotheses
- Finite-range (or sufficiently fast decaying) interaction; well-defined specification.
- A criterion guaranteeing uniqueness and strong mixing, e.g. {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness" >}} or {{< knowl id="cluster-expansion-convergence" text="convergent cluster expansion" >}} in the parameter regime.
- Existence of the thermodynamic limit of the pressure (often proved independently, e.g. via subadditivity).

## Conclusions
- **No phase transition** (in the thermodynamic sense of nonanalyticity of $p$) can occur within the uniqueness region.
- In particular, nonuniqueness of Gibbs states (phase coexistence) cannot happen there:
  {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition as Gibbs nonuniqueness" >}} is excluded.

## Cross-links (definitions and supporting results)
- {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}}, {{< knowl id="extremal-gibbs-measure" section="stat-mech-lattice" text="extremal Gibbs measure" >}}
- {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="lattice pressure" >}}, {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="lattice partition function" >}}
- {{< knowl id="thermodynamic-limit-pressure-existence" section="thermodynamics" text="existence of thermodynamic limit of the pressure" >}}
- {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness theorem" >}}, {{< knowl id="corollary-high-temp-exponential-decay" text="high-temperature exponential decay" >}}
## significance
Uniqueness plus strong mixing yields uniform control of boundary-condition influence. In regimes covered by a convergent expansion (Dobrushin method or cluster expansion), one obtains absolutely convergent series for $\log Z_\Lambda$ and for expectations of local observables, uniform in $\Lambda$. Passing to the limit gives analyticity of $p(\beta,\mathbf{h})$ and of correlation functions.
This formalizes the slogan: **nonanalyticity requires nonuniqueness**.
