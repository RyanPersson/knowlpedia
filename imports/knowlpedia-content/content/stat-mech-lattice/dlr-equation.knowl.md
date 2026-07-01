+++
id = "stat-mech-lattice/dlr-equation"
title = "DLR equation"
kind = "knowl"
summary = "Consistency condition defining infinite-volume Gibbs measures: finite-region conditional laws agree with the Gibbs specification almost surely."
aliases = ["dlr-equation", "DLR equation"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/dlr-equation.md"
+++

Let $\gamma = (\gamma_\Lambda)_{\Lambda\Subset\mathbb{Z}^d}$ be a [[stat-mech-lattice/gibbs-specification|Gibbs specification]] on the [[stat-mech-lattice/configuration-space-lattice|configuration space]] $\Omega$, and let $\mu$ be a [[probability/probability-measure|probability measure]] on $\Omega$.

The **DLR equation** (Dobrushin–Lanford–Ruelle) says that $\mu$ is an **infinite-volume Gibbs measure** for $\gamma$ if, for every finite region $\Lambda$ and every bounded measurable function $f:\Omega\to\mathbb{R}$,
$$
\int_\Omega f(\sigma)\,\mu(d\sigma)
={}
\int_\Omega
\left[
\int_\Omega f(\sigma)\,\gamma_\Lambda(d\sigma\mid\eta)
\right]
\mu(d\eta).
$$

Equivalently, in terms of conditional expectations (see [[probability/conditional-expectation|conditional expectation]]), $\mu$ satisfies that its conditional distribution in $\Lambda$ given the outside sigma-algebra coincides with $\gamma_\Lambda(\cdot\mid\eta)$ for $\mu$-almost every exterior configuration $\eta$.

A measure $\mu$ satisfying the DLR equation is precisely a [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]].

## Key properties

- **Convex set of solutions.** The collection of all DLR solutions for a fixed specification is convex: mixtures of solutions are solutions. This leads to the [[stat-mech-lattice/mixture-gibbs-measures|mixture decomposition]] viewpoint.

- **Extremal measures and pure phases.** Extreme points of the DLR solution set are [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]], which correspond to [[stat-mech-lattice/pure-phase|pure phases]] in the usual physical interpretation.

- **Phase transitions as non-uniqueness.** A common mathematical formulation of a [[stat-mech-lattice/phase-transition-gibbs|phase transition]] is the existence of more than one DLR solution (at the same parameters), often accompanied by phenomena such as [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] or [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]].

- **Local equilibrium principle.** The DLR equation enforces that every finite window of the infinite system, conditioned on its exterior, is distributed as the corresponding [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs law]] prescribed by the specification.

## Physical interpretation

The DLR equation is the rigorous form of the Gibbs postulate for infinite systems: even without a global finite-volume normalization, the system is in equilibrium if every finite region looks like a Gibbs-distributed subsystem when conditioned on its surroundings. Non-uniqueness of DLR solutions captures coexistence of macroscopic phases.
